// GET /api/keepalive: daily Vercel cron (vercel.json "crons") that runs one
// tiny write in Postgres so the free-plan Supabase project is never idle
// for 7 days and paused. Paused twice (July and Aug to Oct 2026), each time
// silently breaking the live signup form. Read-only ping still drew a pause
// warning on 2026-11-18, hence the write. Backed up every 6 h by
// .github/workflows/keepalive.yml.
//
// A Vercel Function, not an Astro page: the site is static output with no
// adapter. Uses the same publishable key the browser already has; the
// keepalive_ping() RPC (security definer) is its only way to touch the
// heartbeat row.
//
// If CRON_SECRET is set in the Vercel project, Vercel sends it as a bearer
// token and anything else is refused.

const json = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
  });

export async function GET(request) {
  const secret = process.env.CRON_SECRET;
  if (secret && request.headers.get('authorization') !== `Bearer ${secret}`) {
    return json(401, { ok: false });
  }

  const url = process.env.PUBLIC_SUPABASE_URL;
  const key = process.env.PUBLIC_SUPABASE_KEY;
  if (!url || !key) {
    console.error('keepalive: PUBLIC_SUPABASE_URL or PUBLIC_SUPABASE_KEY not set');
    return json(503, { ok: false, error: 'not configured' });
  }

  try {
    // A real write (scripts/keepalive.sql): one fixed row bumped by an RPC.
    // A read-only ping was judged "insufficient activity" (warning 2026-11-18).
    const headers = { apikey: key, Authorization: `Bearer ${key}` };
    let res = await fetch(`${url}/rest/v1/rpc/keepalive_ping`, {
      method: 'POST',
      headers: { ...headers, 'content-type': 'application/json' },
      body: '{}',
    });
    // RPC missing (scripts/keepalive.sql not applied, or dropped): still run the
    // old read so some activity lands, but report FAILURE. A read alone drew a
    // pause warning, so it must never look healthy.
    if (res.status === 404) {
      console.error('keepalive: FLAG keepalive_ping() missing, apply scripts/keepalive.sql; fell back to a read');
      res = await fetch(`${url}/rest/v1/subscribers?select=id&limit=1`, { headers });
      return json(502, { ok: false, status: res.status, error: 'heartbeat rpc missing' });
    }
    if (!res.ok) {
      console.error(`keepalive: FLAG Supabase returned ${res.status}`);
      return json(502, { ok: false, status: res.status });
    }
    // A 2xx is not proof of a write: the RPC returns the heartbeat timestamp,
    // which must be fresh (same check as .github/workflows/keepalive.yml).
    const ts = String(await res.json());
    const age = (Date.now() - Date.parse(ts)) / 1000;
    if (!(age >= -60 && age < 120)) {
      console.error(`keepalive: FLAG heartbeat timestamp ${ts} is ${age}s old`);
      return json(502, { ok: false, error: 'stale heartbeat', heartbeat: ts });
    }
    return json(200, { ok: true, heartbeat: ts });
  } catch (e) {
    console.error('keepalive: Supabase unreachable', e);
    return json(502, { ok: false, error: 'unreachable' });
  }
}

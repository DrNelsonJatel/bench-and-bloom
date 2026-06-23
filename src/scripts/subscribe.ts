// Client-side launch-list subscribe. Inserts an email into Supabase `subscribers`
// via the insert-only publishable key (the nelsonjatel pattern). No double opt-in
// in v0: a single insert is the subscription. RLS blocks reads with this key.
//
// Markup contract:
//   <form data-signup> with name="email", optional honeypot name="_gotcha",
//   and a [data-status] element for live messages.

const SUPABASE_URL = import.meta.env.PUBLIC_SUPABASE_URL as string | undefined;
const SUPABASE_KEY = import.meta.env.PUBLIC_SUPABASE_KEY as string | undefined;

function field(form: HTMLFormElement, name: string): string {
  const el = form.elements.namedItem(name) as HTMLInputElement | null;
  return el?.value?.trim() ?? '';
}

async function subscribe(form: HTMLFormElement) {
  const status = form.querySelector<HTMLElement>('[data-status]');
  const button = form.querySelector<HTMLButtonElement>('button[type="submit"]');
  const setStatus = (msg: string, kind: 'info' | 'error' | 'ok') => {
    if (status) { status.textContent = msg; status.dataset.kind = kind; }
  };

  // Honeypot: bots fill hidden fields. Pretend success, insert nothing.
  if (field(form, '_gotcha')) {
    form.innerHTML = '<p data-status data-kind="ok">Thank you. We will be in touch at launch.</p>';
    return;
  }

  const email = field(form, 'email').toLowerCase();
  if (!email || !email.includes('@') || !email.includes('.')) {
    setStatus('Please enter a valid email.', 'error');
    return;
  }
  if (!SUPABASE_URL || !SUPABASE_KEY) {
    setStatus('Sorry, sign-up is not available right now. Please email hello@benchandbloom.com.', 'error');
    return;
  }

  if (button) button.disabled = true;
  setStatus('Adding you to the list…', 'info');

  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/subscribers`, {
      method: 'POST',
      headers: {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json',
        Prefer: 'return=minimal',
      },
      body: JSON.stringify({
        email,
        source: window.location.pathname,
        referrer: document.referrer || null,
        user_agent: navigator.userAgent,
      }),
    });
    // 409 = already on the list (unique email). Treat as a soft success.
    if (res.status === 409) {
      form.innerHTML = '<p data-status data-kind="ok">You are already on the list. We will be in touch at launch.</p>';
      return;
    }
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    form.innerHTML = '<p data-status data-kind="ok">You are on the list. We will send the launch date and your lavender cocktail recipe card.</p>';
  } catch {
    if (button) button.disabled = false;
    setStatus('Something went wrong. Please try again, or email hello@benchandbloom.com.', 'error');
  }
}

export function initSignupForms() {
  document.querySelectorAll<HTMLFormElement>('form[data-signup]').forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      void subscribe(form);
    });
  });
}

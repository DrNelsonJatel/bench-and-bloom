# Bench & Bloom

Marketing site for **Bench & Bloom · Naramata Bench Botanicals** at
[benchandbloom.com](https://benchandbloom.com) — a half-acre Naramata Bench lavender farm and a
small-batch lavender simple syrup built for gin and cocktails. The syrup sells on **Amazon.ca**;
this site is the brand, story, recipes and launch email list.

Built with the **nelsonjatel.com method**: Astro static site → Vercel → (Supabase email capture,
pending). Domains registered at Squarespace's registrar; DNS repoints to Vercel at launch.

## Develop

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output to dist/
npm run preview
```

## Status (v0 — single-page launch teaser)

- Home: hero, positioning pillars, the syrup, recipe preview, our-farm story, launch email section.
- Brand system in `src/styles/global.css` (tokens from `build/BRAND_TOKENS.md`).
- LocalBusiness JSON-LD in `src/layouts/Base.astro`.

### Pending (do not ship placeholders; flip flags in `src/consts.ts` when ready)

- `AMAZON_URL` — empty until the Amazon.ca listing (2-case test) is live.
- `EMAIL_CAPTURE.enabled` — flip to true once Supabase email capture is wired.
- `SOCIAL` handles — empty until claimed (@benchandbloom is taken; using a variant).
- Photography — golden-hour field/bottle/cocktail shots (see `build/SHOT_LIST.md`).
- OG share image, real `og-default` once a hero photo exists.
- Multi-page Phase 1: /syrup, /recipes (hub), /farm, /visit.

Planning docs live in `build/` (BUILD_BRIEF, SHOT_LIST, BRAND_TOKENS) and stay out of the deploy.

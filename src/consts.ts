// Central site configuration. Edit these in one place.
// Items marked PENDING need a real value before launch; do not ship placeholders.

export const SITE = {
  title: 'Bench & Bloom',
  wordmark: 'Bench & Bloom',
  // Provenance descriptor; the place/line under the brand. Swaps in one place.
  descriptor: 'Naramata Bench Botanicals',
  url: 'https://benchandbloom.com',
  email: 'hello@benchandbloom.com',
  author: 'Bench & Bloom',
  locale: 'en_CA',
  description:
    'Small-batch lavender simple syrup, grown and made on the Naramata Bench. ' +
    'Real lavender buds steeped and strained, no essential oils, built to stand ' +
    'up to gin, citrus and sparkling wine.',
  ogImage: '/images/og-default.jpg',
} as const;

export const CLOSER = 'Made on the Naramata Bench.';

// The Amazon.ca product link. EMPTY until the listing is live (a 2-case test
// batch). While empty the "Buy" button renders a "coming soon" state instead of
// a broken link, so nothing ships half-finished.
export const AMAZON_URL = '';

// Primary navigation (real routes, Phase 1).
export const NAV = [
  { href: '/syrup', label: 'The Syrup' },
  { href: '/recipes', label: 'Recipes' },
  { href: '/farm', label: 'Our Farm' },
  { href: '/visit', label: 'Visit' },
] as const;

// Social handles. EMPTY until claimed (the exact @benchandbloom is taken; a
// variant such as @benchandbloomfarm will be grabbed). Footer hides empty ones.
export const SOCIAL = {
  instagram: '',
  facebook: '',
} as const;

// Visit / Find Us. Production-only for now. Flip standOpen to true and fill the
// fields when the roadside stand opens, and the Visit page switches itself on.
export const VISIT = {
  standOpen: false,
  hours: '', // e.g. 'Fridays to Sundays, 10am to 4pm, July to August'
  note:
    'A small roadside lavender stand is planned for the bloom season. Dates will be ' +
    'posted here and sent to the launch list first.',
} as const;

// Launch email capture (the cocktail recipe-card lead magnet + launch list).
// Gated: the form only renders once the Supabase backend is wired (nelsonjatel
// pattern). Until then the section shows a "sign-up opens soon" note, never a
// dead input.
export const EMAIL_CAPTURE = {
  enabled: true,
  heading: 'Be first to pour it.',
  prompt:
    'We are launching a small first batch on Amazon.ca this season. Leave your ' +
    'email for the launch date and a free lavender cocktail recipe card.',
} as const;

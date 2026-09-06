// Bench & Bloom bilingual site.
//
// HOW SYNC WORKS: every page lives once, in src/pagebody/, and takes a `lang`
// prop. src/pages/x.astro renders it with lang="en"; src/pages/fr/x.astro
// renders the SAME component with lang="fr". Structure, layout and any new
// section therefore appear in both languages automatically. Only the STRINGS
// differ, and they live in src/i18n/ui.ts.
//
// FALLBACK: t() returns the English string when a French key is missing, so an
// untranslated addition ships as English rather than as a blank or a crash.
export const LANGS = ['en', 'fr'] as const;
export type Lang = (typeof LANGS)[number];
export const DEFAULT_LANG: Lang = 'en';

export const LANG_NAME: Record<Lang, string> = { en: 'English', fr: 'Français' };

// The French translation is a DRAFT and has not been professionally verified.
// While this is true, /fr/ pages carry noindex so an unverified translation is
// never indexed or cited. Flip to true once a francophone reviewer has signed
// off, and the noindex disappears.
export const FR_VERIFIED = false;

/** 'fr' for any /fr/... URL, else 'en'. */
export function langFromUrl(url: URL): Lang {
  const [, first] = url.pathname.split('/');
  return (LANGS as readonly string[]).includes(first) && first !== 'en' ? (first as Lang) : 'en';
}

/** Map a path to its equivalent in the other language. '/syrup' <-> '/fr/syrup'. */
export function localizePath(path: string, lang: Lang): string {
  const bare = path.replace(/^\/fr(?=\/|$)/, '') || '/';
  return lang === 'en' ? bare : `/fr${bare === '/' ? '' : bare}`;
}

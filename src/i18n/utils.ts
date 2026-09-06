import { ui } from './ui';
import { DEFAULT_LANG, type Lang } from './config';

/**
 * Returns a lookup that resolves a dotted key against the requested language and
 * FALLS BACK TO ENGLISH when the key is missing. That fallback is what lets new
 * English copy ship before it is translated without breaking the French site.
 */
export function useTranslations(lang: Lang) {
  return function t(key: string): string {
    const get = (l: Lang) =>
      key.split('.').reduce<any>((o, k) => (o == null ? undefined : o[k]), ui[l]);
    const v = get(lang);
    if (typeof v === 'string') return v;
    const fallback = get(DEFAULT_LANG);
    return typeof fallback === 'string' ? fallback : key;
  };
}

/** Same, for keys whose value is a string[] (bullet lists, pillars). */
export function useList(lang: Lang) {
  return function tl(key: string): string[] {
    const get = (l: Lang) =>
      key.split('.').reduce<any>((o, k) => (o == null ? undefined : o[k]), ui[l]);
    const v = get(lang);
    if (Array.isArray(v)) return v;
    const fallback = get(DEFAULT_LANG);
    return Array.isArray(fallback) ? fallback : [];
  };
}

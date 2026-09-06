// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build
export default defineConfig({
  site: 'https://benchandbloom.com',
  // The French translation is an unverified draft and carries noindex, so keep it
  // out of the sitemap too. Both come off together when FR_VERIFIED flips.
  integrations: [sitemap({ filter: (page) => !/\/fr(\/|$)/.test(new URL(page).pathname) })],
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
  // Static output; deploys to Vercel unchanged (same as nelsonjatel).
  output: 'static',
});

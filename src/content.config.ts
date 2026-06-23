import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Recipe hub: one anchor post ("how to make lavender simple syrup") plus spoke
// posts (gin fizz, French 75, lemonade, latte) that link back to it. Structured
// ingredients/steps in frontmatter drive both the page render and the Recipe
// JSON-LD; the markdown body holds intro prose, tips and cross-links.
const recipes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/recipes' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    // anchor = the base-syrup how-to; cocktail / mocktail = the drinks.
    kind: z.enum(['anchor', 'cocktail', 'mocktail']).default('cocktail'),
    spirit: z.string().optional(),
    servings: z.string().optional(),
    prepTime: z.string().optional(), // ISO 8601 duration, e.g. PT5M
    totalTime: z.string().optional(),
    ingredients: z.array(z.string()),
    steps: z.array(z.string()),
    order: z.number().default(100),
    related: z.array(z.string()).optional(), // slugs
  }),
});

export const collections = { recipes };

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Recipe hub: one anchor post ("how to make lavender simple syrup") plus spoke
// posts (gin fizz, French 75, lemonade, latte) that link back to it. Structured
// ingredients/steps in frontmatter drive both the page render and the Recipe
// JSON-LD; the markdown body holds intro prose, tips and cross-links.
const recipeSchema = z.object({
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
    // Bench & Bloom original / signature serve (Okanagan-named), featured on the hub.
    signature: z.boolean().default(false),
    related: z.array(z.string()).optional(), // slugs
});

const recipes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/recipes' }),
  schema: recipeSchema,
});

// French recipes. Same schema, same slugs. A slug present here is served at
// /fr/recipes/<slug>; a slug ABSENT here still gets a French URL that renders the
// English entry, so a new English recipe never 404s in French and never silently
// disappears from the French hub.
const recipesFr = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/recipes-fr' }),
  schema: recipeSchema,
});

export const collections = { recipes, 'recipes-fr': recipesFr };

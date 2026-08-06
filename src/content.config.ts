import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    category: z.enum(['evidence', 'resources']),
    tags: z.array(z.string()).default([]),
    author: z.string().default('MUJO Panacea'),
    heroImage: z.string().optional(),
    archived: z.boolean().default(false),
    legacyId: z.number().optional(),
    legacyUrl: z.string().url().optional(),
  }),
});

const team = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/team' }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      role: z.string(),
      order: z.number(),
      photo: image().optional(),
      linkedin: z.string().url().optional(),
    }),
});

const partners = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/partners' }),
  schema: ({ image }) =>
    z.object({
      name: z.string(),
      logo: image(),
      url: z.string().url().optional(),
      order: z.number().default(999),
      active: z.boolean().default(true),
    }),
});

export const collections = { posts, team, partners };

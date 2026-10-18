# feat(zod): support JSON schema registries

Brings the v1 `JSON_SCHEMA_REGISTRY`, `JSON_SCHEMA_INPUT_REGISTRY`, and `JSON_SCHEMA_OUTPUT_REGISTRY` to `@orpc/zod` v2, so users can customize the generated JSON schema per Zod schema.

```ts
import { JSON_SCHEMA_REGISTRY } from '@orpc/zod'

const user = z.object({
  name: z.string(),
  age: z.number(),
})

JSON_SCHEMA_REGISTRY.add(user, {
  examples: [{ name: 'John', age: 20 }],
})
```

- Registry entries are merged over the generated schema at any nesting level; direction-specific registries take precedence over the general one, matching v1 behavior.
- Registries are typed with `$input`/`$output`, so `examples`, `default`, etc. are checked against the schema's input/output types.

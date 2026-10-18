# feat(openapi): accept optional path params in the input schema

The OpenAPI generator no longer throws when a dynamic path param is optional in the input schema. The router only reaches a procedure after the path matched, so the param is always present at runtime, and OpenAPI mandates `required: true` on path parameters anyway. The generator now emits that unconditionally instead of refusing to produce a document.

This also removes an inconsistency: detailed mode already tolerated an optional `params` section, and union inputs where only some branches carried the param were rejected even though the route physically requires the segment.

## Behavior

- Contracts with an optional path param field now generate, with the parameter documented as `required: true`.
- Params missing from the input schema still throw.
- Backward compatible: only contracts that previously threw are affected.

## Testing

- Unit tests cover compact and detailed inputs with an optional param.
- An e2e test with zod `.optional()` verifies the generated parameter.
- The routing docs no longer state that path param fields must be required.


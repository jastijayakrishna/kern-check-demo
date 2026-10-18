# feat(tanstack-query,pinia-colada): support back option in key utils

## Summary

Key utils now accept a `back` option that drops trailing path segments, making it easy to target a parent path from a nested util:

```ts
orpc.planet.find.key({ back: 1 }) // equals orpc.planet.key()

queryClient.invalidateQueries({
  queryKey: orpc.planet.find.key({ back: 1 }),
})
```

- Supported in both `@orpc/tanstack-query` and `@orpc/pinia-colada`, including `generateOperationKey`
- `back` only shapes the key path — like `prefix`, it never appears inside the generated key
- A `back` larger than the path depth resolves to the root key

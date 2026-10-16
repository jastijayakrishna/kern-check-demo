# fix: generate `number` type for number fields root-cms.d.ts

`number` fields were missing from the type-mapping switch in `generate-types.ts`, so they fell through to `unknown` in generated `.d.ts` files instead of TypeScript `number`.

### Changes

- **`packages/root-cms/cli/generate-types.ts`**: Add a `field.type === 'number'` branch in `fieldType()` returning `dom.type.number`.

```ts
if (field.type === 'number') {
  return dom.type.number;
}
```

### Audit of other `field.type` call sites

Verified `number` is already handled correctly elsewhere; no other changes needed:

- `core/validation.ts` — validates `typeof value === 'number'` and rejects `NaN`
- `ui/utils/test-field-empty.ts` — explicit `case 'number'`
- `ui/components/DocEditor/DocEditor.tsx` — renders `<NumberField>`
- `ui/utils/extract.ts`, `core/checks-translations.ts` — correctly skip number fields (not translatable)

# fix(igx-ts): resolve lint errors in Angular project templates

- [x] Fix `no-useless-assignment` in `fintech-grid/data/financialData.ts`
- [x] Fix `no-useless-assignment` in `fintech-tree-grid/assets/financialData.ts`
- [x] Fix `no-useless-assignment` in `fintech-grid/__filePrefix__.ts`
- [x] Fix `no-useless-assignment` in `fintech-tree-grid/__filePrefix__.ts`
- [x] Fix `@typescript-eslint/no-empty-function` + `@typescript-eslint/no-unused-vars` in `local-storage.ts`
- [x] Fix `@typescript-eslint/no-unused-vars` in `jwt-util.ts` (bare catch) and `@typescript-eslint/no-empty-object-type` (reverted `object` → `{}` with eslint-disable comment to keep spec compatibility)
- [x] Fix `@typescript-eslint/consistent-generic-constructors` in `external-auth.ts`
- [x] Fix `@typescript-eslint/no-unused-vars` + `@typescript-eslint/no-empty-function` in `facebook-provider.ts`
- [x] Fix `@angular-eslint/component-selector` in `generate/__filePrefix__.ts`
- [x] Update `eslint.config.js` with `argsIgnorePattern: '^_'` for unused vars, and a spec file override disabling `@typescript-eslint/no-empty-function` and `@typescript-eslint/class-literal-property-style` for test files
- [x] Fix `prefer-const` in `services.spec.ts` - consolidate `mockLocalStorage` declaration and assignment

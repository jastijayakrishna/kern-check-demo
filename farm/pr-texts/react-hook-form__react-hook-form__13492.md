# update type dirtyFields typing for field arrays with undefined entries

# Pull Request Template

## Proposed Changes

`dirtyFields` for field arrays can contain sparse entries at runtime (e.g. `undefined` for untouched/default array slots), but the type previously implied every array element was defined. This updates the type mapping so array items in `dirtyFields` can be `undefined`, matching actual behavior.

- **Type mapping update**
  - Updated `DeepMap` array handling to preserve per-item `undefined`:
    - from object-only recursion to explicit array mapping with `| undefined` element support.
- **Type coverage**
  - Added a typetest assertion for `UseFormStateReturn<FormType>['dirtyFields']['items']` to ensure array elements are typed as object-or-undefined.

```ts
type DirtyItems =
  | (
      | { myField?: boolean | undefined; myOtherField?: boolean | undefined }
      | undefined
    )[]
  | undefined;
```

## Type of change

Please delete options that are not relevant.

- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## Checklist:

- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing tests pass locally with my changes

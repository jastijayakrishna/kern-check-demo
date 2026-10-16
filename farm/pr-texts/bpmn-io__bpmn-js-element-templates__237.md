# Fix validation messages showing "undefined" when property label is missing

When a template property has no `label`, constraint validation messages render as `"undefined must be at least 3 characters."` instead of a meaningful message.

Related to https://github.com/camunda/camunda-modeler/issues/5859

## Changes

- **`src/cloud-element-templates/util/propertyUtil.js`** — In `validateProperty`, when `label` is present messages are prefixed with it (e.g. `"My Field must not be empty."`). When `label` is absent, a standalone capitalized message is produced instead (e.g. `"Must not be empty."`), consistent with the style used elsewhere in the Modeler. All `translate` calls use replacement variables rather than string concatenation.

- **`test/spec/cloud-element-templates/linting/LinterPlugin.json`** — Added three fixture templates (minLength, maxLength, notEmpty) without a `label` field.

- **`test/spec/cloud-element-templates/linting/LinterPlugin.spec.js`** — Added corresponding invalid-cases asserting label-free messages (e.g. `"Must be at least 5 characters."`) are produced when no label is defined.

# Add Date type support with string format date-time

## What does this PR do?

- Add support for Date type in schema-forge, mapping it to JSON Schema string type with format "date-time"
- Add class-validator decorator inference support (ArrayMaxSize, ArrayMinSize, Max, Min, IsInt, MinLength, MaxLength, IsUrl, IsPositive)
- Add validation constraint properties to ToolProp options (minimum, maximum, minLength, maxLength, minItems, maxItems, format)

## Type of change

This pull request is a
- [x] Feature
- [ ] Bugfix
- [ ] Enhancement

Which introduces
- [ ] Breaking changes
- [x] Non-breaking changes

## How should this be manually tested?

1. Create a class with a Date property using the @ToolProp decorator
2. Call classToJsonSchema on the class
3. Verify the Date property has type "string" and format "date-time"
4. Create a class with validation constraints (minimum, maximum, minLength, etc.) in @ToolProp
5. Verify the constraints are included in the generated JSON Schema

## Any background context you want to provide beyond Shortcut?

[Devin session link](https://app.devin.ai/sessions/5bfd33a0171946f0a30639b10347784b)

[Shortcut story](https://app.shortcut.com/fireflies/story/93154)

Requested by: Greg Teixeira (greg@fireflies.ai) @greguintow


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Date support: Date properties emitted as string with date-time format.
  * Class-validator integration: infer common validation constraints (integer, min/max, lengths, item counts, formats) while preserving explicit options.

* **Tests**
  * End-to-end tests added for date handling and validator-derived constraints across output formats.

* **Documentation**
  * Added docs and examples for class-validator integration and precedence rules.

* **Chores**
  * Package version bumped to 2.0.0.

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

# Nest Checkout element configuration types

## Summary

Nest the Checkout Payment Element and Currency Selector helper types under their owning configurations. This changes their TypeScript paths while keeping the configuration object shapes and native mapping the same. Mark the configuration namespaces and nested types with `@CheckoutSessionPrivatePreview`.

## Motivation

Checkout Elements API review feedback.

## Testing

- [ ] I tested this manually
- [ ] I added automated tests
- `yarn typescript`
- `yarn api-extractor:check`
- ESLint passes for the changed TypeScript files.
- The standalone Android Gradle project uses the same 2 GiB heap as the example project. This prevents the CI daemon from exhausting its default 512 MiB heap after detekt completes.

## Documentation

- [x] I have added relevant documentation for my changes.
- [ ] This PR does not result in any developer-facing changes.

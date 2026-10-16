# Fix POU rename file extension mismatch

# Pull request info

## References

This PR resolves #463.

### Link to Devin run

[Devin session](https://app.devin.ai/sessions/e9685b47d0f24efb9c58ba3b691b8c56)

Requested by: joao.pereira@autonomylogic.com (@JoaoGSP)

## Description of the changes proposed

- Fixed the POU rename operation which was failing due to a mismatch between virtual file paths (`.json`) and actual file paths (language-specific extensions like `.st`, `.ld`, `.fbd`, etc.)
- Modified `PouService.renamePouFile()` to convert `.json` virtual paths to actual language extensions using `getExtensionFromLanguage()` when POU data is provided
- Updated `SharedSlice.rename()` to pass the POU data as `fileContent` so the main process can determine the correct file extension

**Root cause:** The renderer uses `.json` as a virtual path identifier internally, but actual files are stored with language-specific extensions. The save operation in `ProjectService.saveFile()` already handled this correctly, but the rename operation did not.

**Key areas for review:**
- The `isPou` type guard logic at lines 80-81 in `pou-service/index.ts`
- The extension conversion logic follows the same pattern as `ProjectService.saveFile()`
- Edge case: if `fileContent` is not provided, the code falls back to original behavior (though the renderer now always provides it)

## DOD checklist

- [x] The code is complete and according to developers' standards.
- [x] I have performed a self-review of my code.
- [x] Meet the acceptance criteria.
- [ ] Unit tests are written and green.
- [ ] Test coverage: __ %.
- [ ] Integration tests are written and green.
- [ ] Changes were communicated and updated in the ticket description.
- [ ] Reviewed and accepted by the Product Owner.
- [ ] End-to-end test are successful.

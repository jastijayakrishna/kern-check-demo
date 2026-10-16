# Add ACHCreditPaymentInitiation Implementation

# Add ACHCreditPaymentInitiation Implementation

This PR implements ACH Credit Payment Initiation functionality for the iso20022.js library, addressing [Issue #8](https://github.com/svapnil/iso20022.js/issues/8).

## Changes

- Added ACH-related types and enums in `src/lib/types.ts`
  - ACHLocalInstrumentCode (CCD, PPD, WEB, etc.)
  - ACHServiceLevelCode (NURG, URGP, SDVA)
  - ACHInstructionPriorityCode (NORM, HIGH)
  - ACHCreditPaymentInstruction interface

- Implemented `ACHCreditPaymentInitiation` class in `src/pain/001/ach-credit-payment-initiation.ts`
  - Follows ISO20022 pain.001.001.03 XML standards for ACH credit transfers
  - Uses NORM and NURG as defaults for instruction priority and service level codes
  - Includes validation for USD currency requirement
  - Supports XML serialization and parsing

- Updated ISO20022 class with `createACHCreditPaymentInitiation` method
- Added exports in `index.ts`
- Added comprehensive tests in `test/pain/001/ach-credit-payment-initiation.test.ts`

## Testing

All tests are passing. The implementation includes tests for:
- XML serialization and validation against XSD schema
- XML parsing and reconstruction
- Error handling for invalid inputs
- Integration with the ISO20022 class

Link to Devin run: https://app.devin.ai/sessions/531a9bd3fee74ec0bb9cb7699a8d4637
Requested by: Svapnil

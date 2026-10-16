# Implement fiat payment support using Request Network's ANY_DECLARATIVE payment feature

# Implement fiat payment support using Request Network's ANY_DECLARATIVE payment feature

Resolves #24

This PR implements fiat payment support through Request Network's ANY_DECLARATIVE payment network. It adds the ability to create invoices with EUR, USD, and GBP currencies using traditional banking details (IBAN/BIC).

## Changes include:
- Added payment type selection (crypto/fiat) in the invoice form
- Added bank details input fields for fiat payments
- Updated the invoice creation process to handle both payment types
- Updated the invoice view to properly display fiat payment information
- Ensured existing crypto payment functionality remains intact

Link to Devin run: https://app.devin.ai/sessions/98ee646fb3f8471daa4a57ab2b2729e3

Requested by: ben (ben@prologe.io)

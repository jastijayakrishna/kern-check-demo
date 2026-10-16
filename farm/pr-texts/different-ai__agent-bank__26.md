# Fix: Dynamic Currency Display in Invoice View Page

Fixes #25

This PR fixes the hardcoded currency issue in the invoice-container.tsx component, replacing it with dynamic currency extraction from the invoice data. Now the component correctly displays EURe for Gnosis Chain invoices and USDC for Ethereum Mainnet invoices.

Link to Devin run: https://app.devin.ai/sessions/d6f034dbe4ea4658a68209bd8de8f076
Requested by: ben (ben@prologe.io)

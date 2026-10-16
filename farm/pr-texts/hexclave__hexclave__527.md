# [DEVIN: Konsti] Update OpenAPI schema generator to support multiple status codes

# [DEVIN: Zai] Update OpenAPI schema generator to support multiple status codes

## Description
This PR updates the OpenAPI schema generator to support multiple return status codes. Previously, the generator was limited to zero or one status code and would throw an error: "Expected status code to have zero or one values".

## Changes
- Modified the `parseOverload` function to handle multiple status codes
- Replaced the single status code restriction with a more flexible approach using `reduce` to build responses for multiple status codes
- Maintained backward compatibility with existing route handlers
- Preserved the default 200 status code when no status codes are specified

## Testing
- Verified changes pass lint checks
- Ensured type safety by properly casting `options.statusCodeDesc.oneOf` to `number[]`

Link to Devin run: https://app.devin.ai/sessions/9aa3c8523d7d497796d2f5cac430ceba

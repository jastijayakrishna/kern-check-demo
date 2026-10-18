# feat(api-reference): render `$dynamicRef` in schemas

OpenAPI 3.1 schemas using JSON Schema 2020-12 `$dynamicRef` / `$dynamicAnchor` loaded fine but rendered as empty shapes, so a generic `PaginatedResponse<T>` showed nothing for its item type. Now `@scalar/api-reference` resolves the binding and renders the concrete type: `PaginatedUserResponse.items` shows `User`, and the same template bound to `Group` shows `Group`.

Two small pieces:

- **Rendering (`@scalar/api-reference`)** — carry the JSON Schema dynamic scope down the schema tree and bind each `$dynamicRef` to whatever the resource bound it to.
- **Ingestion (`@scalar/workspace-store`)** — the keywords were being dropped on ingestion, so I added `$id` / `$anchor` / `$dynamicAnchor` / `$dynamicRef` to the Schema Object to let them survive.

## Before

<img width="430" height="365" alt="Screenshot 2026-06-23 at 11 08 40" src="https://github.com/user-attachments/assets/aa6823d6-d345-485a-938e-037e12eb9ce9" />

## After

<img width="498" height="472" alt="Screenshot 2026-06-23 at 11 09 08" src="https://github.com/user-attachments/assets/e976b6d4-795e-4570-8b3d-e77ebc277fd5" />

## Example

```yaml
openapi: 3.1.0
info:
  title: DynamicRef demo
  version: 0.1.0
paths:
  /users:
    get:
      responses:
        '200':
          description: User page
          content:
            application/json:
              schema: { $ref: '#/components/schemas/PaginatedUserResponse' }
  /groups:
    get:
      responses:
        '200':
          description: Group page
          content:
            application/json:
              schema: { $ref: '#/components/schemas/PaginatedGroupResponse' }
components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id: { type: string }
        email: { type: string, format: email }
    Group:
      type: object
      required: [id, groupName]
      properties:
        id: { type: string }
        groupName: { type: string }
    # Generic, reusable pagination template. Its item type is an unbound $dynamicRef.
    PaginatedTemplate:
      $id: https://example.com/schemas/PaginatedTemplate
      $defs:
        itemType: { $dynamicAnchor: itemType, not: {} }
      type: object
      required: [items, total]
      properties:
        items:
          type: array
          items: { $dynamicRef: '#itemType' }
        total: { type: integer }
    # Binds the template's itemType to User via a sibling $defs + root $ref.
    PaginatedUserResponse:
      $id: https://example.com/schemas/PaginatedUserResponse
      $defs:
        itemType: { $dynamicAnchor: itemType, $ref: '#/components/schemas/User' }
      $ref: '#/components/schemas/PaginatedTemplate'
    # Same template, bound to Group instead.
    PaginatedGroupResponse:
      $id: https://example.com/schemas/PaginatedGroupResponse
      $defs:
        itemType: { $dynamicAnchor: itemType, $ref: '#/components/schemas/Group' }
      $ref: '#/components/schemas/PaginatedTemplate'
```

`PaginatedUserResponse.items` renders the `User` shape (`id`, `email`); `PaginatedGroupResponse.items` renders `Group` (`id`, `groupName`) from the same template.

## Ticket

Part of #9414

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Touches core schema rendering and document coercion across api-reference and workspace-store; behavior is guarded by tests but changes how many schemas display and what survives ingestion.
> 
> **Overview**
> Fixes **empty schema shapes** for OpenAPI 3.1 documents that use JSON Schema 2020-12 **`$dynamicRef` / `$dynamicAnchor`** (e.g. shared `PaginatedTemplate` with `items: { $dynamicRef: '#itemType' }` bound per response).
> 
> **Ingestion** adds `$id`, `$anchor`, `$dynamicAnchor`, and `$dynamicRef` to the OpenAPI 3.1 Schema Object in `@scalar/schemas`, `@scalar/types`, and `@scalar/workspace-store` so coercion no longer strips those keywords from operation-reachable schemas.
> 
> **Resolution** adds `resolv

# Restrict notebook mutation and execution from sandboxed AppKernel

## Summary

- limit the sandbox bridge to inspection and collaboration capabilities
- block general-purpose notebook mutation, storage-write, restoration, and execution methods in both default and code-mode sandboxes
- update agent guidance and documentation for the reduced capability boundary
- add regression coverage proving rejected calls never reach the host bridge

## Problem

Sandboxed AppKernel code could invoke host bridge methods beyond its intended capability boundary. This let sandbox-originated workflows ask trusted host handlers to mutate or execute notebook content.

## Fix

Remove notebook mutation and execution methods, including equivalent run/rerun, raw storage-write, embedding, and restoration helpers, from the sandbox allowlists. Rejected calls now fail at the sandbox boundary before the host bridge is invoked. Trusted browser AppKernel cells and normal UI execution remain unchanged.

## User impact

WebMCP and sandboxed AppKernel workflows remain able to inspect notebooks and use supported collaboration helpers. Intentional notebook mutation and execution must use a trusted browser AppKernel cell or the normal Runme UI.

## Validation

- `runme run build test`
- focused sandbox and instruction tests: 26 passed
- full app test suite: 799 passed
- `git diff --check origin/main...HEAD`


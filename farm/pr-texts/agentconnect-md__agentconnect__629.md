# feat(daemon): link sessions to integration sources

## Summary

- add a generic ingress-to-session `threadUrl` path with first-write persistence
- populate native source links for GitHub hooks, Discord messages, and addressable Telegram messages/topics
- keep Slack permalink derivation behind a daemon platform strategy, so session readers and the console stay platform-agnostic
- document how the capability fits the integration plugin architecture

## Why

The session title integration label could navigate back to Slack, but other integrations lost their original platform location even when the provider exposed one.

## Behavior

GitHub links use the event's repository-scoped source URL, Discord uses the provider message URL, and Telegram emits documented public/private message links when its event has enough coordinates. A GitHub event anchored into another integration keeps the target conversation's link semantics, so the displayed mark, label, and destination stay aligned. Feishu/Lark remains unset because its receive event does not include the opaque token required for a native message share link.

## Validation

- daemon focused suite: 235 passed
- protocol suite: 278 passed
- daemon, message, and protocol typechecks
- ESLint, Prettier, diff checks, and the full pre-push lint hook

Created by Codex . gpt-5.6-sol


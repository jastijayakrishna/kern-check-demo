# chore(deps-dev): bump the dev-dependencies-minor-patch group across 1 directory with 39 updates

Bumps the dev-dependencies-minor-patch group with 39 updates in the / directory:

| Package | From | To |
| --- | --- | --- |
| [@hono/node-server](https://github.com/honojs/node-server) | `2.1.4` | `2.1.5` |
| [@tanstack/ai](https://github.com/TanStack/ai/tree/HEAD/packages/ai) | `0.66.0` | `0.69.0` |
| [@tanstack/ai-client](https://github.com/TanStack/ai/tree/HEAD/packages/ai-client) | `0.39.0` | `0.39.3` |
| [@types/node](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/node) | `26.6.4` | `26.6.5` |
| [react](https://github.com/react/react/tree/HEAD/packages/react) | `19.3.0` | `19.3.1` |
| [vite](https://github.com/vitejs/vite/tree/HEAD/packages/vite) | `8.3.3` | `8.3.4` |
| [zod](https://github.com/colinhacks/zod) | `4.6.5` | `4.6.7` |
| [@tanstack/react-query](https://github.com/TanStack/query/tree/HEAD/packages/react-query) | `5.104.1` | `5.104.3` |
| [@tanstack/solid-query](https://github.com/TanStack/query/tree/HEAD/packages/solid-query) | `5.104.1` | `5.104.3` |
| [@tanstack/svelte-query](https://github.com/TanStack/query/tree/HEAD/packages/svelte-query) | `6.3.1` | `6.3.3` |
| [@tanstack/vue-query](https://github.com/TanStack/query/tree/HEAD/packages/vue-query) | `5.104.1` | `5.104.3` |
| [blume](https://github.com/haydenbleasel/blume/tree/HEAD/packages/blume) | `2.2.2` | `2.2.3` |
| [effect](https://github.com/Effect-TS/effect/tree/HEAD/packages/effect) | `4.0.2` | `4.0.5` |
| [ai](https://github.com/vercel/ai/tree/HEAD/packages/ai) | `7.0.130` | `7.0.141` |
| [@types/bun](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/bun) | `1.4.2` | `1.4.3` |
| [wrangler](https://github.com/cloudflare/workers-sdk/tree/HEAD/packages/wrangler) | `4.149.0` | `4.151.0` |
| [evlog](https://github.com/evloghq/evlog) | `2.30.1` | `2.32.0` |
| [@nestjs/common](https://github.com/nestjs/nest/tree/HEAD/packages/common) | `12.1.2` | `12.1.3` |
| [@nestjs/core](https://github.com/nestjs/nest/tree/HEAD/packages/core) | `12.1.2` | `12.1.3` |
| [@nestjs/platform-express](https://github.com/nestjs/nest/tree/HEAD/packages/platform-express) | `12.1.2` | `12.1.3` |
| [@nestjs/platform-fastify](https://github.com/nestjs/nest/tree/HEAD/packages/platform-fastify) | `12.1.2` | `12.1.3` |
| [@nestjs/testing](https://github.com/nestjs/nest/tree/HEAD/packages/testing) | `12.1.2` | `12.1.3` |
| [express](https://github.com/expressjs/express) | `5.2.1` | `5.3.0` |
| [fastify](https://github.com/fastify/fastify) | `5.12.5` | `5.12.7` |
| [next](https://github.com/vercel/next.js) | `16.4.0` | `16.4.1` |
| [@scalar/api-reference](https://github.com/scalar/scalar/tree/HEAD/packages/api-reference) | `1.73.1` | `1.74.0` |
| [swagger-ui](https://github.com/swagger-api/swagger-ui) | `5.33.1` | `5.33.2` |
| [pinia](https://github.com/vuejs/pinia) | `4.0.3` | `4.1.0` |
| [vue](https://github.com/vuejs/core) | `3.5.43` | `3.5.44` |
| [@angular/core](https://github.com/angular/angular/tree/HEAD/packages/core) | `22.2.2` | `22.2.3` |
| [@tanstack/angular-query-experimental](https://github.com/TanStack/query/tree/HEAD/packages/angular-query-experimental) | `5.104.1` | `5.104.3` |
| [@tanstack/query-core](https://github.com/TanStack/query/tree/HEAD/packages/query-core) | `5.104.1` | `5.104.3` |
| [react-dom](https://github.com/react/react/tree/HEAD/packages/react-dom) | `19.3.0` | `19.3.1` |
| [ts-pattern](https://github.com/gvergnaud/ts-pattern) | `5.9.0` | `5.9.2` |
| [@cloudflare/vite-plugin](https://github.com/cloudflare/workers-sdk/tree/HEAD/packages/vite-plugin-cloudflare) | `1.63.1` | `1.64.0` |
| [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/tree/HEAD/packages/plugin-react) | `6.1.1` | `6.1.2` |
| [@nestjs/schematics](https://github.com/nestjs/schematics) | `12.0.6` | `12.0.7` |
| [@swc/core](https://github.com/swc-project/swc/tree/HEAD/packages/core) | `1.16.13` | `1.16.18` |
| [@tanstack/react-query-next-experimental](https://github.com/TanStack/query/tree/HEAD/packages/react-query-next-experimental) | `5.104.1` | `5.104.3` |


Updates `@hono/node-server` from 2.1.4 to 2.1.5
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/honojs/node-server/releases">@​hono/node-server's releases</a>.</em></p>
<blockquote>
<h2>v2.1.5</h2>
<h2>What's Changed</h2>
<ul>
<li>fix(listener): abort the request signal when an HTTP/2 client resets the stream by <a href="https://github.com/affanmomin"><code>@​affanmomin</code></a> in <a href="https://redirect.github.com/honojs/node-server/pull/404">honojs/node-server#404</a></li>
<li>fix(serve-static): only serve GET and HEAD requests by <a href="https://github.com/usualoma"><code>@​usualoma</code></a> in <a href="https://redirect.github.com/honojs/node-server/pull/405">honojs/node-server#405</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/affanmomin"><code>@​affanmomin</code></a> made their first contribution in <a href="https://redirect.github.com/honojs/node-server/pull/404">honojs/node-server#404</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/honojs/node-server/compare/v2.1.4...v2.1.5">https://github.com/honojs/node-server/compare/v2.1.4...v2.1.5</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/honojs/node-server/commit/4b47a0d8a5c12ed69a9f8493df69918f62fb61c0"><code>4b47a0d</code></a> 2.1.5</li>
<li><a href="https://github.com/honojs/node-server/commit/e77824a912c7f12d26f8f200b0b2e9c2b0d72a97"><code>e77824a</code></a> fix(serve-static): only serve GET and HEAD requests (<a href="https://redirect.github.com/honojs/node-server/issues/405">#405</a>)</li>
<li><a href="https://github.com/honojs/node-server/commit/1b6e6bfc21f0f018d5725b8bd8f5a230680e2134"><code>1b6e6bf</code></a> fix(listener): abort the request signal when an HTTP/2 client resets the stre...</li>
<li>See full diff in <a href="https://github.com/honojs/node-server/compare/v2.1.4...v2.1.5">compare view</a></li>
</ul>
</details>
<br />

Updates `@tanstack/ai` from 0.66.0 to 0.69.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/ai/releases">@​tanstack/ai's releases</a>.</em></p>
<blockquote>
<h2><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.69.0</h2>
<h3>Minor Changes</h3>
<ul>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1698">#1698</a> <a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a> - Keep the order of Claude's thinking, text, and tool calls in one answer.</p>
<ul>
<li>Claude can answer with thinking, a tool call, more thinking, and another tool call. The stream, the stored messages, the client wire, and the next request to Claude keep that order.</li>
<li><code>ModelMessage</code> has a new optional <code>blockOrder</code> field. The library writes it only when the order is not the default (thinking, then text, then tool calls), so a message in the default order does not change. <code>orderedAssistantBlocks(message)</code> gives adapter authors the blocks in order.</li>
<li>Each Claude thinking block ends with its own <code>REASONING_MESSAGE_END</code> and <code>REASONING_END</code>.</li>
<li>Text after a second thinking block starts a new text part.</li>
<li>On the client wire, an answer in another order goes out as ordered rows. A row that exists only for the order has <code>metadata.tanstack.continues</code>, and the server joins it back into one message. A <code>UIMessage</code> that holds two model calls with a tool result between them reaches the server as assistant, tool, assistant, for every adapter.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1686">#1686</a> <a href="https://github.com/TanStack/ai/commit/412b0fea4f4bb569998c3d253d174efd7b501e3c"><code>412b0fe</code></a> - <code>chat()</code> can now retry a rate-limited model call by itself. Pass <code>retry: { maxRetries, maxWaitMs? }</code>. When the provider sends a wait time (<code>retryAfterMs</code>) with an error, <code>chat()</code> waits that long, then calls the model again.</p>
<ul>
<li>It retries only when the provider sent a wait time.</li>
<li>It does not retry when the wait is longer than <code>maxWaitMs</code> (default 60 000).</li>
<li>It does not retry a call that already streamed output, so no output repeats.</li>
<li>An abort stops the wait. You then get the <code>RUN_ERROR</code>.</li>
<li>It does not retry the structured-output call.</li>
<li>A <code>maxRetries</code> or <code>maxWaitMs</code> that is not valid throws a <code>TypeError</code>.</li>
</ul>
<p><code>retry</code> is off by default.</p>
<p><code>chat()</code> now also sends <code>RUN_STARTED</code> before a <code>RUN_ERROR</code> when the adapter failed before it sent a start.</p>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1739">#1739</a> <a href="https://github.com/TanStack/ai/commit/a0150c26b9e2b6050663450171e36a9dfa80915b"><code>a0150c2</code></a> - Text adapters now set one stable code on <code>RUN_ERROR</code> when the input does not fit in the model's context window: <code>code: 'context_overflow'</code>. <code>@tanstack/ai</code> exports it as <code>CONTEXT_OVERFLOW_CODE</code>. The provider's own text stays in <code>message</code>.</p>
<pre lang="ts"><code>if (chunk.type === 'RUN_ERROR' &amp;&amp; chunk.code === CONTEXT_OVERFLOW_CODE) {
  // shorten the messages, then call chat() again
}
</code></pre>
<p>These adapters set it: OpenAI and the other OpenAI-compatible adapters (from <code>code: 'context_length_exceeded'</code>), Anthropic, Gemini, Bedrock (Converse, Chat Completions, and Responses), OpenRouter, Grok, Cloudflare Workers AI, and BytePlus.</p>
<p>Changes to code that reads the old values:</p>
<ul>
<li>OpenAI-compatible adapters gave <code>code: 'context_length_exceeded'</code>. They now give <code>'context_overflow'</code>. <code>rawEvent</code> still has the provider's code.</li>
<li>Anthropic, Grok, OpenRouter, and BytePlus gave the HTTP status or a general bad-request code for this error. Gemini and Bedrock Converse gave no code.</li>
<li>The Anthropic adapter now sends <code>RUN_ERROR</code> with this code when the model stops with <code>stop_reason: 'model_context_window_exceeded'</code>. Before, it sent <code>RUN_FINISHED</code> with <code>finishReason: 'stop'</code>, so a cut-off answer looked complete.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1715">#1715</a> <a href="https://github.com/TanStack/ai/commit/fac055559de98eb0fa23a0bc725808033ba3c2fc"><code>fac0555</code></a> - New hooks for hosts that run <code>chat()</code> for a long session.</p>
<ul>
<li><code>@tanstack/ai</code> exports <code>runAgentStream</code> (runs a <code>defineAgent</code> agent outside a parent chat turn), <code>createSubagentId</code>, <code>createSubagentSink</code>, <code>CapabilityRegistry</code>, and the <code>SubagentsBag</code> and <code>SubagentSink</code> types. Pass the sink to keep interrupt objects and token usage. The finished event has <code>interruptIds</code> only.</li>
<li><code>MetadataStore</code> has optional <code>getVersioned</code> and <code>setIf</code> for compare-and-set writes. The memory store of <code>@tanstack/ai-persistence</code> has both, and the conformance testkit checks them.</li>
<li><code>toolDefinition({ replay: 'safe' | 'never' })</code> tells a host if it can run the tool again after a crash.</li>
<li>The tool context has an optional <code>detach</code> field. A host sets it when it can move the call to the background. A tool passes its work to <code>detach</code> and races the two promises.</li>
<li>A tool that throws the MCP input-required shape can set the interrupt <code>reason</code>. The default is <code>'mcp_input'</code>. The interrupt id stays <code>mcp_input_&lt;toolCallId&gt;</code>.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1713">#1713</a> <a href="https://github.com/TanStack/ai/commit/5bd27f2fc94ebfb6d11bfb28d46d5d858310805e"><code>5bd27f2</code></a> - <code>toJsonResponse</code> now accepts the object from <code>chat({ outputSchema })</code>. It sends the object as a complete structured output, so <code>useChat</code> with <code>fetchJson</code> shows it as a <code>structured-output</code> part. Before this change, the call failed with <code>Cannot read properties of undefined (reading 'map')</code>. <code>toJsonResponse</code> also awaits a Promise input, so <code>toJsonResponse(chat({ ... }))</code> works.</p>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1714">#1714</a> <a href="https://github.com/TanStack/ai/commit/c20f7b021aa618fbfcc114b3f0bef5e888ff6b84"><code>c20f7b0</code></a> - Add <code>LogRecordsCapability</code> and the <code>LogRecord</code> and <code>LogRecordsWriter</code> types. A chat middleware can append records to a session log when a host middleware provides one. Read the writer with <code>getLogRecords(ctx, { optional: true })</code>. It is <code>undefined</code> when no host provides the log, and <code>getLogRecords(ctx)</code> throws. A host provides the writer in <code>setup</code> with <code>provideLogRecords(ctx, writer)</code>. <code>@tanstack/ai</code> does not provide the log.</p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/ai/blob/main/packages/ai/CHANGELOG.md">@​tanstack/ai's changelog</a>.</em></p>
<blockquote>
<h2>0.69.0</h2>
<h3>Minor Changes</h3>
<ul>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1698">#1698</a> <a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a> - Keep the order of Claude's thinking, text, and tool calls in one answer.</p>
<ul>
<li>Claude can answer with thinking, a tool call, more thinking, and another tool call. The stream, the stored messages, the client wire, and the next request to Claude keep that order.</li>
<li><code>ModelMessage</code> has a new optional <code>blockOrder</code> field. The library writes it only when the order is not the default (thinking, then text, then tool calls), so a message in the default order does not change. <code>orderedAssistantBlocks(message)</code> gives adapter authors the blocks in order.</li>
<li>Each Claude thinking block ends with its own <code>REASONING_MESSAGE_END</code> and <code>REASONING_END</code>.</li>
<li>Text after a second thinking block starts a new text part.</li>
<li>On the client wire, an answer in another order goes out as ordered rows. A row that exists only for the order has <code>metadata.tanstack.continues</code>, and the server joins it back into one message. A <code>UIMessage</code> that holds two model calls with a tool result between them reaches the server as assistant, tool, assistant, for every adapter.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1686">#1686</a> <a href="https://github.com/TanStack/ai/commit/412b0fea4f4bb569998c3d253d174efd7b501e3c"><code>412b0fe</code></a> - <code>chat()</code> can now retry a rate-limited model call by itself. Pass <code>retry: { maxRetries, maxWaitMs? }</code>. When the provider sends a wait time (<code>retryAfterMs</code>) with an error, <code>chat()</code> waits that long, then calls the model again.</p>
<ul>
<li>It retries only when the provider sent a wait time.</li>
<li>It does not retry when the wait is longer than <code>maxWaitMs</code> (default 60 000).</li>
<li>It does not retry a call that already streamed output, so no output repeats.</li>
<li>An abort stops the wait. You then get the <code>RUN_ERROR</code>.</li>
<li>It does not retry the structured-output call.</li>
<li>A <code>maxRetries</code> or <code>maxWaitMs</code> that is not valid throws a <code>TypeError</code>.</li>
</ul>
<p><code>retry</code> is off by default.</p>
<p><code>chat()</code> now also sends <code>RUN_STARTED</code> before a <code>RUN_ERROR</code> when the adapter failed before it sent a start.</p>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1739">#1739</a> <a href="https://github.com/TanStack/ai/commit/a0150c26b9e2b6050663450171e36a9dfa80915b"><code>a0150c2</code></a> - Text adapters now set one stable code on <code>RUN_ERROR</code> when the input does not fit in the model's context window: <code>code: 'context_overflow'</code>. <code>@tanstack/ai</code> exports it as <code>CONTEXT_OVERFLOW_CODE</code>. The provider's own text stays in <code>message</code>.</p>
<pre lang="ts"><code>if (chunk.type === 'RUN_ERROR' &amp;&amp; chunk.code === CONTEXT_OVERFLOW_CODE) {
  // shorten the messages, then call chat() again
}
</code></pre>
<p>These adapters set it: OpenAI and the other OpenAI-compatible adapters (from <code>code: 'context_length_exceeded'</code>), Anthropic, Gemini, Bedrock (Converse, Chat Completions, and Responses), OpenRouter, Grok, Cloudflare Workers AI, and BytePlus.</p>
<p>Changes to code that reads the old values:</p>
<ul>
<li>OpenAI-compatible adapters gave <code>code: 'context_length_exceeded'</code>. They now give <code>'context_overflow'</code>. <code>rawEvent</code> still has the provider's code.</li>
<li>Anthropic, Grok, OpenRouter, and BytePlus gave the HTTP status or a general bad-request code for this error. Gemini and Bedrock Converse gave no code.</li>
<li>The Anthropic adapter now sends <code>RUN_ERROR</code> with this code when the model stops with <code>stop_reason: 'model_context_window_exceeded'</code>. Before, it sent <code>RUN_FINISHED</code> with <code>finishReason: 'stop'</code>, so a cut-off answer looked complete.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1715">#1715</a> <a href="https://github.com/TanStack/ai/commit/fac055559de98eb0fa23a0bc725808033ba3c2fc"><code>fac0555</code></a> - New hooks for hosts that run <code>chat()</code> for a long session.</p>
<ul>
<li><code>@tanstack/ai</code> exports <code>runAgentStream</code> (runs a <code>defineAgent</code> agent outside a parent chat turn), <code>createSubagentId</code>, <code>createSubagentSink</code>, <code>CapabilityRegistry</code>, and the <code>SubagentsBag</code> and <code>SubagentSink</code> types. Pass the sink to keep interrupt objects and token usage. The finished event has <code>interruptIds</code> only.</li>
<li><code>MetadataStore</code> has optional <code>getVersioned</code> and <code>setIf</code> for compare-and-set writes. The memory store of <code>@tanstack/ai-persistence</code> has both, and the conformance testkit checks them.</li>
<li><code>toolDefinition({ replay: 'safe' | 'never' })</code> tells a host if it can run the tool again after a crash.</li>
<li>The tool context has an optional <code>detach</code> field. A host sets it when it can move the call to the background. A tool passes its work to <code>detach</code> and races the two promises.</li>
<li>A tool that throws the MCP input-required shape can set the interrupt <code>reason</code>. The default is <code>'mcp_input'</code>. The interrupt id stays <code>mcp_input_&lt;toolCallId&gt;</code>.</li>
</ul>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1713">#1713</a> <a href="https://github.com/TanStack/ai/commit/5bd27f2fc94ebfb6d11bfb28d46d5d858310805e"><code>5bd27f2</code></a> - <code>toJsonResponse</code> now accepts the object from <code>chat({ outputSchema })</code>. It sends the object as a complete structured output, so <code>useChat</code> with <code>fetchJson</code> shows it as a <code>structured-output</code> part. Before this change, the call failed with <code>Cannot read properties of undefined (reading 'map')</code>. <code>toJsonResponse</code> also awaits a Promise input, so <code>toJsonResponse(chat({ ... }))</code> works.</p>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1714">#1714</a> <a href="https://github.com/TanStack/ai/commit/c20f7b021aa618fbfcc114b3f0bef5e888ff6b84"><code>c20f7b0</code></a> - Add <code>LogRecordsCapability</code> and the <code>LogRecord</code> and <code>LogRecordsWriter</code> types. A chat middleware can append records to a session log when a host middleware provides one. Read the writer with <code>getLogRecords(ctx, { optional: true })</code>. It is <code>undefined</code> when no host provides the log, and <code>getLogRecords(ctx)</code> throws. A host provides the writer in <code>setup</code> with <code>provideLogRecords(ctx, writer)</code>. <code>@tanstack/ai</code> does not provide the log.</p>
</li>
<li>
<p><a href="https://redirect.github.com/TanStack/ai/pull/1697">#1697</a> <a href="https://github.com/TanStack/ai/commit/cef19119c76fc5f618d6c971efbc486323b213c3"><code>cef1911</code></a> - Keep the prompt cache when tools or system prompts are added during a conversation.</p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/TanStack/ai/commit/293aea91a187ccce331c99c3b936d8cf4d4a72e2"><code>293aea9</code></a> ci: Version Packages (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai/issues/1699">#1699</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/6f1e55934fe95ddf2bf3fb3031488a713e48c7af"><code>6f1e559</code></a> fix(ai): do not log when the client skips a tool call of a cut answer (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai/issues/1746">#1746</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/7a5c0d6fc1541187a7f01b444bc07a0478274bcb"><code>7a5c0d6</code></a> feat(ai): never run a tool call cut at the output limit, retry it through age...</li>
<li><a href="https://github.com/TanStack/ai/commit/51f72fbf60e201f9c8d014aefa6406e777c05d6a"><code>51f72fb</code></a> feat(ai, ai-compaction, openai-base): native provider compaction (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai/issues/1729">#1729</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/78edeb20a5ba89f2513c3f46f1267a7ed7185045"><code>78edeb2</code></a> feat(ai, openai-base): keep Responses answer item ids and phases for a same-m...</li>
<li><a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a> fix(ai, openai-base, adapters): a watching ChatClient ends each run, a chunk ...</li>
<li><a href="https://github.com/TanStack/ai/commit/44e3a0a89c86defebd38b2221dd3b7725a12839a"><code>44e3a0a</code></a> feat(ai): a subagents router pick can give an agent its input (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai/issues/1722">#1722</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/b8c68a867fcb59b323b98e3ee8fd41ff00a828a8"><code>b8c68a8</code></a> fix(ai-anthropic): send output_config.effort for chat({ reasoning }) on Claud...</li>
<li><a href="https://github.com/TanStack/ai/commit/a0150c26b9e2b6050663450171e36a9dfa80915b"><code>a0150c2</code></a> feat(ai, openai-base, adapters): a stable context_overflow code on RUN_ERROR ...</li>
<li><a href="https://github.com/TanStack/ai/commit/fac055559de98eb0fa23a0bc725808033ba3c2fc"><code>fac0555</code></a> feat(ai, ai-persistence): host hooks for long-running sessions (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai/issues/1715">#1715</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/TanStack/ai/commits/@tanstack/ai@0.69.0/packages/ai">compare view</a></li>
</ul>
</details>
<br />

Updates `@tanstack/ai-client` from 0.39.0 to 0.39.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/ai/releases">@​tanstack/ai-client's releases</a>.</em></p>
<blockquote>
<h2><code>@​tanstack/ai-client</code><a href="https://github.com/0"><code>@​0</code></a>.39.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a>, <a href="https://github.com/TanStack/ai/commit/412b0fea4f4bb569998c3d253d174efd7b501e3c"><code>412b0fe</code></a>, <a href="https://github.com/TanStack/ai/commit/a0150c26b9e2b6050663450171e36a9dfa80915b"><code>a0150c2</code></a>, <a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a>, <a href="https://github.com/TanStack/ai/commit/fac055559de98eb0fa23a0bc725808033ba3c2fc"><code>fac0555</code></a>, <a href="https://github.com/TanStack/ai/commit/6774e803da3205101613ab2857c9ed4fbf975681"><code>6774e80</code></a>, <a href="https://github.com/TanStack/ai/commit/5bd27f2fc94ebfb6d11bfb28d46d5d858310805e"><code>5bd27f2</code></a>, <a href="https://github.com/TanStack/ai/commit/c20f7b021aa618fbfcc114b3f0bef5e888ff6b84"><code>c20f7b0</code></a>, <a href="https://github.com/TanStack/ai/commit/cef19119c76fc5f618d6c971efbc486323b213c3"><code>cef1911</code></a>, <a href="https://github.com/TanStack/ai/commit/51f72fbf60e201f9c8d014aefa6406e777c05d6a"><code>51f72fb</code></a>, <a href="https://github.com/TanStack/ai/commit/6f1e55934fe95ddf2bf3fb3031488a713e48c7af"><code>6f1e559</code></a>, <a href="https://github.com/TanStack/ai/commit/eb4eea05b6c53b748bba5fd414b04ce387ead05d"><code>eb4eea0</code></a>, <a href="https://github.com/TanStack/ai/commit/cef19119c76fc5f618d6c971efbc486323b213c3"><code>cef1911</code></a>, <a href="https://github.com/TanStack/ai/commit/7532b2b09188ebd1095a60a7c5df6ef08b06916c"><code>7532b2b</code></a>, <a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a>, <a href="https://github.com/TanStack/ai/commit/78edeb20a5ba89f2513c3f46f1267a7ed7185045"><code>78edeb2</code></a>, <a href="https://github.com/TanStack/ai/commit/44e3a0a89c86defebd38b2221dd3b7725a12839a"><code>44e3a0a</code></a>, <a href="https://github.com/TanStack/ai/commit/7532b2b09188ebd1095a60a7c5df6ef08b06916c"><code>7532b2b</code></a>, <a href="https://github.com/TanStack/ai/commit/7a5c0d6fc1541187a7f01b444bc07a0478274bcb"><code>7a5c0d6</code></a>, <a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a>]:
<ul>
<li><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.69.0</li>
<li><code>@​tanstack/ai-utils</code><a href="https://github.com/0"><code>@​0</code></a>.4.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/ai-client</code><a href="https://github.com/0"><code>@​0</code></a>.39.1</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/ai/commit/7dbfaf6c37a3d97de3b1f5bdb87be8bbbe2b0164"><code>7dbfaf6</code></a>, <a href="https://github.com/TanStack/ai/commit/88fd67cd7ddfbe2b154173d2395b2c0338e97644"><code>88fd67c</code></a>, <a href="https://github.com/TanStack/ai/commit/3aa2e3d95e2dcb1c14b4fda3bcdbdf3152582092"><code>3aa2e3d</code></a>, <a href="https://github.com/TanStack/ai/commit/c5ae4152d0a040bb6ce7321e16b7ee66d3c36f96"><code>c5ae415</code></a>, <a href="https://github.com/TanStack/ai/commit/13ba1b0e47dc822f10f6c5133184f92c2eb0a013"><code>13ba1b0</code></a>, <a href="https://github.com/TanStack/ai/commit/377262c0b4e5f59f8fd467a831b9341cc705077e"><code>377262c</code></a>]:
<ul>
<li><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.67.0</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/ai/blob/main/packages/ai-client/CHANGELOG.md">@​tanstack/ai-client's changelog</a>.</em></p>
<blockquote>
<h2>0.39.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a>, <a href="https://github.com/TanStack/ai/commit/412b0fea4f4bb569998c3d253d174efd7b501e3c"><code>412b0fe</code></a>, <a href="https://github.com/TanStack/ai/commit/a0150c26b9e2b6050663450171e36a9dfa80915b"><code>a0150c2</code></a>, <a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a>, <a href="https://github.com/TanStack/ai/commit/fac055559de98eb0fa23a0bc725808033ba3c2fc"><code>fac0555</code></a>, <a href="https://github.com/TanStack/ai/commit/6774e803da3205101613ab2857c9ed4fbf975681"><code>6774e80</code></a>, <a href="https://github.com/TanStack/ai/commit/5bd27f2fc94ebfb6d11bfb28d46d5d858310805e"><code>5bd27f2</code></a>, <a href="https://github.com/TanStack/ai/commit/c20f7b021aa618fbfcc114b3f0bef5e888ff6b84"><code>c20f7b0</code></a>, <a href="https://github.com/TanStack/ai/commit/cef19119c76fc5f618d6c971efbc486323b213c3"><code>cef1911</code></a>, <a href="https://github.com/TanStack/ai/commit/51f72fbf60e201f9c8d014aefa6406e777c05d6a"><code>51f72fb</code></a>, <a href="https://github.com/TanStack/ai/commit/6f1e55934fe95ddf2bf3fb3031488a713e48c7af"><code>6f1e559</code></a>, <a href="https://github.com/TanStack/ai/commit/eb4eea05b6c53b748bba5fd414b04ce387ead05d"><code>eb4eea0</code></a>, <a href="https://github.com/TanStack/ai/commit/cef19119c76fc5f618d6c971efbc486323b213c3"><code>cef1911</code></a>, <a href="https://github.com/TanStack/ai/commit/7532b2b09188ebd1095a60a7c5df6ef08b06916c"><code>7532b2b</code></a>, <a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a>, <a href="https://github.com/TanStack/ai/commit/78edeb20a5ba89f2513c3f46f1267a7ed7185045"><code>78edeb2</code></a>, <a href="https://github.com/TanStack/ai/commit/44e3a0a89c86defebd38b2221dd3b7725a12839a"><code>44e3a0a</code></a>, <a href="https://github.com/TanStack/ai/commit/7532b2b09188ebd1095a60a7c5df6ef08b06916c"><code>7532b2b</code></a>, <a href="https://github.com/TanStack/ai/commit/7a5c0d6fc1541187a7f01b444bc07a0478274bcb"><code>7a5c0d6</code></a>, <a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a>]:
<ul>
<li><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.69.0</li>
<li><code>@​tanstack/ai-utils</code><a href="https://github.com/0"><code>@​0</code></a>.4.2</li>
</ul>
</li>
</ul>
<h2>0.39.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/ai/commit/723b4a4e8432825374d4980cc74c5f66dc7d1122"><code>723b4a4</code></a>, <a href="https://github.com/TanStack/ai/commit/d84a49e5fef03499b10f63255880d056a55767a3"><code>d84a49e</code></a>]:
<ul>
<li><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.68.0</li>
</ul>
</li>
</ul>
<h2>0.39.1</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/ai/commit/7dbfaf6c37a3d97de3b1f5bdb87be8bbbe2b0164"><code>7dbfaf6</code></a>, <a href="https://github.com/TanStack/ai/commit/88fd67cd7ddfbe2b154173d2395b2c0338e97644"><code>88fd67c</code></a>, <a href="https://github.com/TanStack/ai/commit/3aa2e3d95e2dcb1c14b4fda3bcdbdf3152582092"><code>3aa2e3d</code></a>, <a href="https://github.com/TanStack/ai/commit/c5ae4152d0a040bb6ce7321e16b7ee66d3c36f96"><code>c5ae415</code></a>, <a href="https://github.com/TanStack/ai/commit/13ba1b0e47dc822f10f6c5133184f92c2eb0a013"><code>13ba1b0</code></a>, <a href="https://github.com/TanStack/ai/commit/377262c0b4e5f59f8fd467a831b9341cc705077e"><code>377262c</code></a>]:
<ul>
<li><code>@​tanstack/ai</code><a href="https://github.com/0"><code>@​0</code></a>.67.0</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/TanStack/ai/commit/293aea91a187ccce331c99c3b936d8cf4d4a72e2"><code>293aea9</code></a> ci: Version Packages (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai-client/issues/1699">#1699</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/b881627d51076dcc1af031ac951046e2fb7d84c4"><code>b881627</code></a> fix(ai, openai-base, adapters): a watching ChatClient ends each run, a chunk ...</li>
<li><a href="https://github.com/TanStack/ai/commit/1bfcee35bb3cf0ff3aac005440c842e66c3d687d"><code>1bfcee3</code></a> feat(ai, adapters): keep block order and replay history across models (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai-client/issues/1698">#1698</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/3920a883361c983577f977abb77404f907788ec2"><code>3920a88</code></a> ci: Version Packages (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai-client/issues/1693">#1693</a>)</li>
<li><a href="https://github.com/TanStack/ai/commit/9614cc7682c902580eca83774768feae78982324"><code>9614cc7</code></a> ci: Version Packages (<a href="https://github.com/TanStack/ai/tree/HEAD/packages/ai-client/issues/1687">#1687</a>)</li>
<li>See full diff in <a href="https://github.com/TanStack/ai/commits/@tanstack/ai-client@0.39.3/packages/ai-client">compare view</a></li>
</ul>
</details>
<br />

Updates `@types/node` from 26.6.4 to 26.6.5
<details>
<summary>Commits</summary>
<ul>
<li>See full diff in <a href="https://github.com/DefinitelyTyped/DefinitelyTyped/commits/HEAD/types/node">compare view</a></li>
</ul>
</details>
<br />

Updates `react` from 19.3.0 to 19.3.1
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/react/react/releases">react's releases</a>.</em></p>
<blockquote>
<h2>19.3.1 (October 14th, 2026)</h2>
<h2>React Server Components</h2>
<ul>
<li>Improve transport protocol (<a href="https://redirect.github.com/facebook/react/pull/37845">#37845</a> by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> and <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/react/react/commit/61aa00df822d0eb76d0362eb8b6fdd3527693efe"><code>61aa00d</code></a> [19.3.x][Flight] Improve transport protocol (<a href="https://github.com/react/react/tree/HEAD/packages/react/issues/37845">#37845</a>)</li>
<li>See full diff in <a href="https://github.com/react/react/commits/v19.3.1/packages/react">compare view</a></li>
</ul>
</details>
<br />

Updates `vite` from 8.3.3 to 8.3.4
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vitejs/vite/releases">vite's releases</a>.</em></p>
<blockquote>
<h2>v8.3.4</h2>
<h3>Features</h3>
<ul>
<li><strong>bundled-dev:</strong> support <code>import.meta.hot.acceptExports</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23463">#23463</a>) (<a href="https://github.com/vitejs/vite/commit/bc0f21c56a2e003a4d2dd23ccb9da3ec8c706c4e">bc0f21c</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>avoid mutating hmr defaults (fix <a href="https://redirect.github.com/vitejs/vite/issues/23575">#23575</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23576">#23576</a>) (<a href="https://github.com/vitejs/vite/commit/574d5e351905fe99891364d03c2440531378f7fd">574d5e3</a>)</li>
<li><strong>build:</strong> correct preloads when chunkImportMap is enabled with non-root base (<a href="https://redirect.github.com/vitejs/vite/issues/23698">#23698</a>) (<a href="https://github.com/vitejs/vite/commit/2a8c0f05c76e35c43ab3560984a5103c8db8dbcd">2a8c0f0</a>)</li>
<li><strong>build:</strong> wait for in-flight stylesheets in preload helper (fix <a href="https://redirect.github.com/vitejs/vite/issues/23652">#23652</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23662">#23662</a>) (<a href="https://github.com/vitejs/vite/commit/036b74599b2fe1d8c61475371b856ceb88d26963">036b745</a>)</li>
<li><strong>bundled-dev:</strong> serve <code>/@vite/client</code> and stub <code>@vite/env</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23664">#23664</a>) (<a href="https://github.com/vitejs/vite/commit/5afc5a8876624888fc1e8f43fed1c85c4b0e830b">5afc5a8</a>)</li>
<li><strong>client:</strong> skip rewriting unchanged adopted styles (<a href="https://redirect.github.com/vitejs/vite/issues/23697">#23697</a>) (<a href="https://github.com/vitejs/vite/commit/fa7146938b0ca703653c90c20907191a01c032ba">fa71469</a>)</li>
<li><strong>css:</strong> resolve imported preprocessors from their file path with lightningcss (<a href="https://redirect.github.com/vitejs/vite/issues/23688">#23688</a>) (<a href="https://github.com/vitejs/vite/commit/cf52011c46409a4a45f3d74bba631b8f005c4bc9">cf52011</a>)</li>
<li><strong>deps:</strong> update all non-major dependencies (<a href="https://redirect.github.com/vitejs/vite/issues/23648">#23648</a>) (<a href="https://github.com/vitejs/vite/commit/8a4c19cfc035f2dd203f2fa6d00ab9256a5e77c9">8a4c19c</a>)</li>
<li><strong>deps:</strong> update rolldown-related dependencies (<a href="https://redirect.github.com/vitejs/vite/issues/23649">#23649</a>) (<a href="https://github.com/vitejs/vite/commit/794516d50cff80e405bc9b3e5faac1c82987566c">794516d</a>)</li>
<li><strong>dev:</strong> a restart requested during a restart used to be dropped (fix <a href="https://redirect.github.com/vitejs/vite/issues/23392">#23392</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23484">#23484</a>) (<a href="https://github.com/vitejs/vite/commit/70d56ea1848909edab416934f3f68ce14343eb73">70d56ea</a>)</li>
<li>don't treat modules ending with js-like query as js (<a href="https://redirect.github.com/vitejs/vite/issues/23687">#23687</a>) (<a href="https://github.com/vitejs/vite/commit/fcb6f1252a95857823d935f98554b938888d41a0">fcb6f12</a>)</li>
<li><strong>html:</strong> avoid adding filesystem root to watcher (<a href="https://redirect.github.com/vitejs/vite/issues/23689">#23689</a>) (<a href="https://github.com/vitejs/vite/commit/3a7f2aea757d59bae66ad6edf6b321d26a7e6778">3a7f2ae</a>)</li>
<li><strong>html:</strong> skip caching CSS of chunks in a cycle (fix <a href="https://redirect.github.com/vitejs/vite/issues/23628">#23628</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23636">#23636</a>) (<a href="https://github.com/vitejs/vite/commit/15d82f7dc679ab9c18d5ce2c3711157c2365ddd1">15d82f7</a>)</li>
<li><strong>optimizer:</strong> scan deep imports with custom extensions (<a href="https://redirect.github.com/vitejs/vite/issues/23678">#23678</a>) (<a href="https://github.com/vitejs/vite/commit/8579189bae8626b6ddab55a09325e209d62e027e">8579189</a>)</li>
<li>remove input option unescaping for now (<a href="https://redirect.github.com/vitejs/vite/issues/23694">#23694</a>) (<a href="https://github.com/vitejs/vite/commit/facc2fb1fffce03d9e2dd7011d0bd0eeddc7d0f6">facc2fb</a>)</li>
<li><strong>server:</strong> match static aliases on path boundaries (<a href="https://redirect.github.com/vitejs/vite/issues/23643">#23643</a>) (<a href="https://github.com/vitejs/vite/commit/b28db28e9e62d9866a9a0f1b22e74589cc180577">b28db28</a>)</li>
<li><strong>watcher:</strong> normalize file before root check in <code>ensureWatchedFile</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23673">#23673</a>) (<a href="https://github.com/vitejs/vite/commit/12bb28c22379c8d2fe90088fa0eefbfa2ab3fb80">12bb28c</a>)</li>
</ul>
<h3>Performance Improvements</h3>
<ul>
<li><strong>module-runner:</strong> skip cloning call sites that have no source map (<a href="https://redirect.github.com/vitejs/vite/issues/23646">#23646</a>) (<a href="https://github.com/vitejs/vite/commit/3d674869a50a0bca84a8cc8dc55bd35d57100e37">3d67486</a>)</li>
</ul>
<h3>Code Refactoring</h3>
<ul>
<li><strong>bundled-dev:</strong> import CSS HMR helpers from <code>/@vite/client</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23674">#23674</a>) (<a href="https://github.com/vitejs/vite/commit/182f5b2a65391da5bee05f9c3df1aeb3794e98d9">182f5b2</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md">vite's changelog</a>.</em></p>
<blockquote>
<h2><!-- raw HTML omitted --><a href="https://github.com/vitejs/vite/compare/v8.3.3...v8.3.4">8.3.4</a> (2026-10-08)<!-- raw HTML omitted --></h2>
<h3>Features</h3>
<ul>
<li><strong>bundled-dev:</strong> support <code>import.meta.hot.acceptExports</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23463">#23463</a>) (<a href="https://github.com/vitejs/vite/commit/bc0f21c56a2e003a4d2dd23ccb9da3ec8c706c4e">bc0f21c</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>avoid mutating hmr defaults (fix <a href="https://redirect.github.com/vitejs/vite/issues/23575">#23575</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23576">#23576</a>) (<a href="https://github.com/vitejs/vite/commit/574d5e351905fe99891364d03c2440531378f7fd">574d5e3</a>)</li>
<li><strong>build:</strong> correct preloads when chunkImportMap is enabled with non-root base (<a href="https://redirect.github.com/vitejs/vite/issues/23698">#23698</a>) (<a href="https://github.com/vitejs/vite/commit/2a8c0f05c76e35c43ab3560984a5103c8db8dbcd">2a8c0f0</a>)</li>
<li><strong>build:</strong> wait for in-flight stylesheets in preload helper (fix <a href="https://redirect.github.com/vitejs/vite/issues/23652">#23652</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23662">#23662</a>) (<a href="https://github.com/vitejs/vite/commit/036b74599b2fe1d8c61475371b856ceb88d26963">036b745</a>)</li>
<li><strong>bundled-dev:</strong> serve <code>/@vite/client</code> and stub <code>@vite/env</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23664">#23664</a>) (<a href="https://github.com/vitejs/vite/commit/5afc5a8876624888fc1e8f43fed1c85c4b0e830b">5afc5a8</a>)</li>
<li><strong>client:</strong> skip rewriting unchanged adopted styles (<a href="https://redirect.github.com/vitejs/vite/issues/23697">#23697</a>) (<a href="https://github.com/vitejs/vite/commit/fa7146938b0ca703653c90c20907191a01c032ba">fa71469</a>)</li>
<li><strong>css:</strong> resolve imported preprocessors from their file path with lightningcss (<a href="https://redirect.github.com/vitejs/vite/issues/23688">#23688</a>) (<a href="https://github.com/vitejs/vite/commit/cf52011c46409a4a45f3d74bba631b8f005c4bc9">cf52011</a>)</li>
<li><strong>deps:</strong> update all non-major dependencies (<a href="https://redirect.github.com/vitejs/vite/issues/23648">#23648</a>) (<a href="https://github.com/vitejs/vite/commit/8a4c19cfc035f2dd203f2fa6d00ab9256a5e77c9">8a4c19c</a>)</li>
<li><strong>deps:</strong> update rolldown-related dependencies (<a href="https://redirect.github.com/vitejs/vite/issues/23649">#23649</a>) (<a href="https://github.com/vitejs/vite/commit/794516d50cff80e405bc9b3e5faac1c82987566c">794516d</a>)</li>
<li><strong>dev:</strong> a restart requested during a restart used to be dropped (fix <a href="https://redirect.github.com/vitejs/vite/issues/23392">#23392</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23484">#23484</a>) (<a href="https://github.com/vitejs/vite/commit/70d56ea1848909edab416934f3f68ce14343eb73">70d56ea</a>)</li>
<li>don't treat modules ending with js-like query as js (<a href="https://redirect.github.com/vitejs/vite/issues/23687">#23687</a>) (<a href="https://github.com/vitejs/vite/commit/fcb6f1252a95857823d935f98554b938888d41a0">fcb6f12</a>)</li>
<li><strong>html:</strong> avoid adding filesystem root to watcher (<a href="https://redirect.github.com/vitejs/vite/issues/23689">#23689</a>) (<a href="https://github.com/vitejs/vite/commit/3a7f2aea757d59bae66ad6edf6b321d26a7e6778">3a7f2ae</a>)</li>
<li><strong>html:</strong> skip caching CSS of chunks in a cycle (fix <a href="https://redirect.github.com/vitejs/vite/issues/23628">#23628</a>) (<a href="https://redirect.github.com/vitejs/vite/issues/23636">#23636</a>) (<a href="https://github.com/vitejs/vite/commit/15d82f7dc679ab9c18d5ce2c3711157c2365ddd1">15d82f7</a>)</li>
<li><strong>optimizer:</strong> scan deep imports with custom extensions (<a href="https://redirect.github.com/vitejs/vite/issues/23678">#23678</a>) (<a href="https://github.com/vitejs/vite/commit/8579189bae8626b6ddab55a09325e209d62e027e">8579189</a>)</li>
<li>remove input option unescaping for now (<a href="https://redirect.github.com/vitejs/vite/issues/23694">#23694</a>) (<a href="https://github.com/vitejs/vite/commit/facc2fb1fffce03d9e2dd7011d0bd0eeddc7d0f6">facc2fb</a>)</li>
<li><strong>server:</strong> match static aliases on path boundaries (<a href="https://redirect.github.com/vitejs/vite/issues/23643">#23643</a>) (<a href="https://github.com/vitejs/vite/commit/b28db28e9e62d9866a9a0f1b22e74589cc180577">b28db28</a>)</li>
<li><strong>watcher:</strong> normalize file before root check in <code>ensureWatchedFile</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23673">#23673</a>) (<a href="https://github.com/vitejs/vite/commit/12bb28c22379c8d2fe90088fa0eefbfa2ab3fb80">12bb28c</a>)</li>
</ul>
<h3>Performance Improvements</h3>
<ul>
<li><strong>module-runner:</strong> skip cloning call sites that have no source map (<a href="https://redirect.github.com/vitejs/vite/issues/23646">#23646</a>) (<a href="https://github.com/vitejs/vite/commit/3d674869a50a0bca84a8cc8dc55bd35d57100e37">3d67486</a>)</li>
</ul>
<h3>Code Refactoring</h3>
<ul>
<li><strong>bundled-dev:</strong> import CSS HMR helpers from <code>/@vite/client</code> (<a href="https://redirect.github.com/vitejs/vite/issues/23674">#23674</a>) (<a href="https://github.com/vitejs/vite/commit/182f5b2a65391da5bee05f9c3df1aeb3794e98d9">182f5b2</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vitejs/vite/commit/b6c20f6a8126d8561891e5fb9368e8fc9da37538"><code>b6c20f6</code></a> release: v8.3.4 (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23702">#23702</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/b28db28e9e62d9866a9a0f1b22e74589cc180577"><code>b28db28</code></a> fix(server): match static aliases on path boundaries (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23643">#23643</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/bc0f21c56a2e003a4d2dd23ccb9da3ec8c706c4e"><code>bc0f21c</code></a> feat(bundled-dev): support <code>import.meta.hot.acceptExports</code> (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23463">#23463</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/fa7146938b0ca703653c90c20907191a01c032ba"><code>fa71469</code></a> fix(client): skip rewriting unchanged adopted styles (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23697">#23697</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/2a8c0f05c76e35c43ab3560984a5103c8db8dbcd"><code>2a8c0f0</code></a> fix(build): correct preloads when chunkImportMap is enabled with non-root bas...</li>
<li><a href="https://github.com/vitejs/vite/commit/3a7f2aea757d59bae66ad6edf6b321d26a7e6778"><code>3a7f2ae</code></a> fix(html): avoid adding filesystem root to watcher (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23689">#23689</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/facc2fb1fffce03d9e2dd7011d0bd0eeddc7d0f6"><code>facc2fb</code></a> fix: remove input option unescaping for now (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23694">#23694</a>)</li>
<li><a href="https://github.com/vitejs/vite/commit/70d56ea1848909edab416934f3f68ce14343eb73"><code>70d56ea</code></a> fix(dev): a restart requested during a restart used to be dropped (fix <a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23392">#23392</a>...</li>
<li><a href="https://github.com/vitejs/vite/commit/cf52011c46409a4a45f3d74bba631b8f005c4bc9"><code>cf52011</code></a> fix(css): resolve imported preprocessors from their file path with lightningc...</li>
<li><a href="https://github.com/vitejs/vite/commit/fcb6f1252a95857823d935f98554b938888d41a0"><code>fcb6f12</code></a> fix: don't treat modules ending with js-like query as js (<a href="https://github.com/vitejs/vite/tree/HEAD/packages/vite/issues/23687">#23687</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vitejs/vite/commits/v8.3.4/packages/vite">compare view</a></li>
</ul>
</details>
<br />

Updates `zod` from 4.6.5 to 4.6.7
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/colinhacks/zod/releases">zod's releases</a>.</em></p>
<blockquote>
<h2>v4.6.7</h2>
<h2>Commits:</h2>
<ul>
<li>b500a2ee95134f81d74da7911d7378dd2853d042 4.6.7</li>
</ul>
<h2>v4.6.6</h2>
<blockquote>
<p>Six malicious commits pushed to <code>main</code> on September 21 with a compromised git credential were reverted the same day in <a href="https://redirect.github.com/colinhacks/zod/issues/6620">#6620</a> and have since been removed from the history of <code>main</code>. None were ever published to npm. The npm provenance for 4.6.6 names 284243fb, the pre-rewrite copy of 9c219833 with identical contents.</p>
</blockquote>
<h2>Commits:</h2>
<ul>
<li>0cd3af5e9f50ad11bbcd4407a46a21b8848ba574 docs: load the en locale directly in Zod Mini</li>
<li>9d5e60f162997b764b40d45aa02481888db50dea docs: import locales from zod/locales, not z.locales</li>
<li>34a626f307871ecbb0123947559328dc52ed5e3e docs: tighten the z.locales tree-shaking note</li>
<li>74304ce5b5796b5edb9a88ceb8e170b6ea3e82df release: stage npm versions instead of publishing them (<a href="https://redirect.github.com/colinhacks/zod/issues/6622">#6622</a>)</li>
<li>b2ef983e0711ff6517d6020b021071e2e5653efa docs: add Code for Japan to bronze sponsors</li>
<li>8fb2faf0584828a6a027d8279db36f6f52784462 docs: crop the Code for Japan logo and list it first in bronze</li>
<li>bacad518c41610d654658172d325874bf0ee6290 docs: square the Code for Japan logo to match the other bronze tiles</li>
<li>c42596bd1c87e941d7241d10e012c5c196adcc10 release: hold the run on the release-approval environment until the staged versions are approved (<a href="https://redirect.github.com/colinhacks/zod/issues/6638">#6638</a>)</li>
<li>a2ba4a67986a3e6b2b131be30084a2f460d9ea67 fix(types): declare record output and input as members, not base type arguments (<a href="https://redirect.github.com/colinhacks/zod/issues/6645">#6645</a>)</li>
<li>a0ebf970f2d752e5f58527cd2942ff48be4f46bd fix(v4): check array, set and map size bounds before parsing elements (<a href="https://redirect.github.com/colinhacks/zod/issues/6652">#6652</a>)</li>
<li>529f78dd9431b07f49647fee3aa0819b3f8b66b7 4.6.6</li>
<li>9c219833c3a3764fa1f1ea9c5ecec8254a63c0b1 ci: stage at verbose so a failed OIDC token exchange says why</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/colinhacks/zod/commit/b500a2ee95134f81d74da7911d7378dd2853d042"><code>b500a2e</code></a> 4.6.7</li>
<li><a href="https://github.com/colinhacks/zod/commit/9c219833c3a3764fa1f1ea9c5ecec8254a63c0b1"><code>9c21983</code></a> ci: stage at verbose so a failed OIDC token exchange says why</li>
<li><a href="https://github.com/colinhacks/zod/commit/529f78dd9431b07f49647fee3aa0819b3f8b66b7"><code>529f78d</code></a> 4.6.6</li>
<li><a href="https://github.com/colinhacks/zod/commit/a0ebf970f2d752e5f58527cd2942ff48be4f46bd"><code>a0ebf97</code></a> fix(v4): check array, set and map size bounds before parsing elements (<a href="https://redirect.github.com/colinhacks/zod/issues/6652">#6652</a>)</li>
<li><a href="https://github.com/colinhacks/zod/commit/a2ba4a67986a3e6b2b131be30084a2f460d9ea67"><code>a2ba4a6</code></a> fix(types): declare record output and input as members, not base type argumen...</li>
<li><a href="https://github.com/colinhacks/zod/commit/c42596bd1c87e941d7241d10e012c5c196adcc10"><code>c42596b</code></a> release: hold the run on the release-approval environment until the staged ve...</li>
<li><a href="https://github.com/colinhacks/zod/commit/bacad518c41610d654658172d325874bf0ee6290"><code>bacad51</code></a> docs: square the Code for Japan logo to match the other bronze tiles</li>
<li><a href="https://github.com/colinhacks/zod/commit/8fb2faf0584828a6a027d8279db36f6f52784462"><code>8fb2faf</code></a> docs: crop the Code for Japan logo and list it first in bronze</li>
<li><a href="https://github.com/colinhacks/zod/commit/b2ef983e0711ff6517d6020b021071e2e5653efa"><code>b2ef983</code></a> docs: add Code for Japan to bronze sponsors</li>
<li><a href="https://github.com/colinhacks/zod/commit/74304ce5b5796b5edb9a88ceb8e170b6ea3e82df"><code>74304ce</code></a> release: stage npm versions instead of publishing them (<a href="https://redirect.github.com/colinhacks/zod/issues/6622">#6622</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/colinhacks/zod/compare/v4.6.5...v4.6.7">compare view</a></li>
</ul>
</details>
<br />

Updates `@tanstack/react-query` from 5.104.1 to 5.104.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/query/releases">@​tanstack/react-query's releases</a>.</em></p>
<blockquote>
<h2><code>@​tanstack/react-query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
<li><code>@​tanstack/query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query-next-experimental</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query-persist-client</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/ed4d849731bfe6404be9d40aec84eda54f958d7f"><code>ed4d849</code></a>]:
<ul>
<li><code>@​tanstack/query-persist-client-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/0f15bc925db5813be6a17527988ec7d7b3c8cfc0"><code>0f15bc9</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query-next-experimental</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query-persist-client</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/query-persist-client-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
<li><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/react-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/03e8c3955ddbf20f0a07b79982b52dfad8df5323"><code>03e8c39</code></a>]:</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/query/blob/main/packages/react-query/CHANGELOG.md">@​tanstack/react-query's changelog</a>.</em></p>
<blockquote>
<h2>5.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/0f15bc925db5813be6a17527988ec7d7b3c8cfc0"><code>0f15bc9</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2>5.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/03e8c3955ddbf20f0a07b79982b52dfad8df5323"><code>03e8c39</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/TanStack/query/commit/ee47993724e5b71e65d9f38ae416367d2dd18395"><code>ee47993</code></a> ci: Version Packages (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11998">#11998</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/0f15bc925db5813be6a17527988ec7d7b3c8cfc0"><code>0f15bc9</code></a> fix(query-core): preserve union narrowing in setQueryData updaters (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11935">#11935</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/b699b52d60e10220403673a407d95bcebeba3e81"><code>b699b52</code></a> ci: Version Packages (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11849">#11849</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/e22e7c4a27129457636a2a800f8ce19fc0c7b0e3"><code>e22e7c4</code></a> chore: test TypeScript 7.1 preview and drop 5.6 (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11947">#11947</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/df78a9d137993546a6d7407b3fd68c1b5429888a"><code>df78a9d</code></a> chore(*): pass the root 'settings' to the package oxlint configs, which 'exte...</li>
<li><a href="https://github.com/TanStack/query/commit/833062c2fcf3720f6e0201adb832aa7bd90e3770"><code>833062c</code></a> chore: replace prettier with oxfmt (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11939">#11939</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/d0cfa6a4a8ee7ad9895ae196910a8718e9308a74"><code>d0cfa6a</code></a> chore: replace eslint with oxlint (<a href="https://github.com/TanStack/query/tree/HEAD/packages/react-query/issues/11938">#11938</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/0012ec14c3679f4a441acf6fdc1f928cd602ed5d"><code>0012ec1</code></a> docs(react-query): add JSDoc to the properties of the exported interfaces and...</li>
<li><a href="https://github.com/TanStack/query/commit/b5e8e7b697b9a4a104c7c1a550280a9e03e33048"><code>b5e8e7b</code></a> docs(react-query): add JSDoc to the exported classes, methods, and arrow func...</li>
<li><a href="https://github.com/TanStack/query/commit/01abab33f866299afa2aeebfd4e00fd0c2bbc4c8"><code>01abab3</code></a> docs(*): note that 'throwOnError' makes the hook rethrow the errors of 'mutat...</li>
<li>Additional commits viewable in <a href="https://github.com/TanStack/query/commits/@tanstack/react-query@5.104.3/packages/react-query">compare view</a></li>
</ul>
</details>
<br />

Updates `@tanstack/solid-query` from 5.104.1 to 5.104.3
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/query/releases">@​tanstack/solid-query's releases</a>.</em></p>
<blockquote>
<h2><code>@​tanstack/solid-query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
<li><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/solid-query-persist-client</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/ed4d849731bfe6404be9d40aec84eda54f958d7f"><code>ed4d849</code></a>]:
<ul>
<li><code>@​tanstack/query-persist-client-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
<li><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/0f15bc925db5813be6a17527988ec7d7b3c8cfc0"><code>0f15bc9</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/solid-query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/query-devtools</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
<li><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/solid-query-persist-client</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies []:
<ul>
<li><code>@​tanstack/query-persist-client-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
<li><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
<h2><code>@​tanstack/solid-query</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/03e8c3955ddbf20f0a07b79982b52dfad8df5323"><code>03e8c39</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/TanStack/query/blob/main/packages/solid-query/CHANGELOG.md">@​tanstack/solid-query's changelog</a>.</em></p>
<blockquote>
<h2>5.104.3</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/0f15bc925db5813be6a17527988ec7d7b3c8cfc0"><code>0f15bc9</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.3</li>
</ul>
</li>
</ul>
<h2>5.104.2</h2>
<h3>Patch Changes</h3>
<ul>
<li>Updated dependencies [<a href="https://github.com/TanStack/query/commit/03e8c3955ddbf20f0a07b79982b52dfad8df5323"><code>03e8c39</code></a>]:
<ul>
<li><code>@​tanstack/query-core</code><a href="https://github.com/5"><code>@​5</code></a>.104.2</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/TanStack/query/commit/ee47993724e5b71e65d9f38ae416367d2dd18395"><code>ee47993</code></a> ci: Version Packages (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11998">#11998</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/b699b52d60e10220403673a407d95bcebeba3e81"><code>b699b52</code></a> ci: Version Packages (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11849">#11849</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/e22e7c4a27129457636a2a800f8ce19fc0c7b0e3"><code>e22e7c4</code></a> chore: test TypeScript 7.1 preview and drop 5.6 (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11947">#11947</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/df78a9d137993546a6d7407b3fd68c1b5429888a"><code>df78a9d</code></a> chore(*): pass the root 'settings' to the package oxlint configs, which 'exte...</li>
<li><a href="https://github.com/TanStack/query/commit/833062c2fcf3720f6e0201adb832aa7bd90e3770"><code>833062c</code></a> chore: replace prettier with oxfmt (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11939">#11939</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/d0cfa6a4a8ee7ad9895ae196910a8718e9308a74"><code>d0cfa6a</code></a> chore: replace eslint with oxlint (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11938">#11938</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/aab352876a01f76fd0e00b0b500a85907ec7c8b4"><code>aab3528</code></a> chore(solid-query*): add 'eslint-plugin-solid' (<a href="https://github.com/TanStack/query/tree/HEAD/packages/solid-query/issues/11929">#11929</a>)</li>
<li><a href="https://github.com/TanStack/query/commit/4e1476cb691e879bd61169553ad18037b8841b52"><code>4e1476c</code></a> test(solid-query): add the 'override' modifier to test classes that override ...</li>
<li><a href="https://github.com/TanStack/query/commit/b18e7ab6f4a3b00449ba351ba4311bf13f6a0d2f"><code>b18e7ab</code></a> docs(solid-query): add JSDoc to the pro...

_Description has been truncated_

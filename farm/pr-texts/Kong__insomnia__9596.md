# Fix Socket.io JSON requests and responses handling - [INS-1993]

- [x] Understand the issue: Socket.io JSON messages are sent as strings instead of parsed objects, and received JSON objects are displayed as `[object Object]`
- [x] Analyze the codebase: Identified locations requiring fixes
- [x] Fix sending issue in `body-tab-pane.tsx`: Parse JSON content type args before sending to socket
- [x] Fix receiving issue in `event-view.tsx`: Handle objects properly when stringifying for display (detail view)
- [x] Fix receiving issue in `event-log-view.tsx`: Add stringifyEventData helper to display JSON objects in list view
- [x] Request code review - addressed feedback
- [x] Run security checks - No security vulnerabilities found
- [x] Fix potential runtime errors in handleSend when renderedArgs is undefined

## Summary

This PR fixes Socket.io JSON handling in three places:

1. **Sending JSON messages**: When users send JSON payloads, the content is now properly parsed into JavaScript objects before being sent via socket.emit()

2. **Receiving JSON responses (detail view)**: Incoming JSON objects from Socket.io servers are now properly stringified for display in the event detail view

3. **Receiving JSON responses (list view)**: Added `stringifyEventData()` helper function to properly display JSON objects in the event list instead of showing `[object Object]`

4. **Error handling**: Added null checks and early return for potential runtime errors when `tryToInterpolateRequestOrShowRenderErrorModal` returns undefined

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Socket.io JSON requests and responses issue</issue_title>
> <issue_description>Hello,
> 
> not sure if this is a bug or if its just not implemented but when I send a JSON message to my NestJS backend it is received as a string and when I return a JSON object from my NestJS backend Insomnia is rendering it as `[object Object]`.
> 
> If I use Postman my NestJS app receives the payload and successfully (automatically) converts it into a Javascript object but when using Insomnia my backend receives it as a string and does not convert it into an object.
> 
> Likewise when returning an object from my backend Postman renders the JSON correctly. However with Insomnia it is rendered like `[object Object]`, which tells me it is at least receiving a JSON object. I can only see the data if I stringify the response. Then Insomnia receives and renders the string.
> 
> <img width="934" height="380" alt="Image" src="https://github.com/user-attachments/assets/f9d52c3f-6d15-4e0a-91ec-755978e114f5" />
> 
> I switched on verbose logging from socket.io in Nest and tested a connection and message with Postman and Insomnia. Here are two images.
> 
> The logs when using Postman. Highlighted is the line where the parser decodes the data. It looks to be an object:
> 
> <img width="1911" height="745" alt="Image" src="https://github.com/user-attachments/assets/89bb8c11-d900-4000-a032-abad1bf7f85e" />
> 
> The logs when using Insomnia. Highlighted is the line where the parser decodes the data. It looks to be a string:
> 
> <img width="1911" height="745" alt="Image" src="https://github.com/user-attachments/assets/c3c1a2c9-fe13-4554-adfe-e2fe83f9bbed" />
> 
> Handshake data from Postman:
> 
> ```
> handshake: {
>     headers: {
>       'sec-websocket-version': '13',
>       'sec-websocket-key': 'oGX1NHrDrqpxQkpXUY00tQ==',
>       connection: 'Upgrade',
>       upgrade: 'websocket',
>       'auth-token': 'u1111',
>       'sec-websocket-extensions': 'permessage-deflate; client_max_window_bits',
>       host: 'localhost:3000'
>     },
>     time: 'Fri Jan 16 2026 10:44:31 GMT+0100 (Central European Standard Time)',
>     address: '::ffff:127.0.0.1',
>     xdomain: false,
>     secure: false,
>     issued: 1768556671959,
>     url: '/socket.io/?EIO=4&transport=websocket',
>     query: { EIO: '4', transport: 'websocket' },
>     auth: {}
>   }
> ```
> Handshake data from Insomnia;
> 
> ```
>   handshake: {
>     headers: {
>       'user-agent': 'insomnia/12.3.0',
>       accept: '*/*',
>       'auth-token': 'u1111',
>       host: 'localhost:3000',
>       connection: 'close'
>     },
>     time: 'Fri Jan 16 2026 10:44:25 GMT+0100 (Central European Standard Time)',
>     address: '::ffff:127.0.0.1',
>     xdomain: false,
>     secure: false,
>     issued: 1768556665630,
>     url: '/socket.io/?EIO=4&transport=polling&t=oz4ssm1a',
>     query: { EIO: '4', transport: 'polling', t: 'oz4ssm1a' },
>     auth: {}
>   }
> ```
> 
> I don't know the internals enough to know exactly whats going on but thought it would be useful context.
> 
> Version: Insomnia 12.3.0
> Build date: 1/15/2026
> OS: Linux x64 6.14.0-37-generic
> Electron: 38.4.0
> Node: 22.20.0
> Node ABI: 139
> V8: 14.0.365.10-electron.0
> Architecture: x64</issue_description>
> 
> <agent_instructions>Socket.io logic path:
> insomnia/src/main/network/socket-io.ts</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> <comment_new><author>@CurryYangxx</author><body>
> @ThriceGood Thanks for your feedback. I will take a look at this issue.</body></comment_new>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes Kong/insomnia#9577

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.

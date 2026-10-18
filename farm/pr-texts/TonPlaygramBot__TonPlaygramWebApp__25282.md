# Fix Murlan Royale crashes in Android WebView

### Motivation
- Constrained mobile runtimes (especially Android WebView) were triggering large transient WebGL / glTF decoding memory spikes that lead to crashes during Murlan Royale scene setup. 
- The goal is to detect these environments and apply a memory-safe rendering and asset-loading profile to avoid out-of-memory conditions on low-memory or embedded browser runtimes.

### Description
- Add runtime detection helpers `isAndroidWebViewRuntime()` and `isConstrainedMobileRuntime()` and use them from `resolveDefaultPixelRatioCap()` to detect mobile / WebView contexts. 
- Enforce a mobile-safe graphics profile in the frame quality path by capping FPS, forcing `renderScale = 1`, and lowering the `pixelRatioCap` when `isConstrainedMobileRuntime()` is true. 
- Limit texture/HDR resolution for constrained devices by returning a 1k HDRI and a `MOBILE_PREFERRED_TEXTURE_SIZES` order, and ensure `activeTextureResolutionOrder` respects the mobile fallback. 
- Reduce renderer memory usage on constrained devices by disabling antialiasing, turning off dynamic shadows, and capping anisotropy, and set `powerPreference` to a safe default. 
- Avoid concurrent glTF decoding spikes by loading character models sequentially and, on constrained devices, loading only the selected/safe template instead of all roster themes concurrently.

### Testing
- Ran lint with `npm --prefix webapp run lint -- src/pages/Games/MurlanRoyaleArena.jsx` and it completed successfully. 
- Performed a production build with `npm --prefix webapp run build`, which completed successfully (the build reported existing chunk-size warnings but no errors). 
- Verified no outstanding whitespace or syntax issues with `git diff --check` which reported no problems.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a71646672a88329881e24cb4489ce15)

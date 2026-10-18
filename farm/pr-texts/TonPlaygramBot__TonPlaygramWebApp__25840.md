# Add installable app controls on Home and signed Android APK release

Home currently offers asset caching as a download, but does not expose an installable APK. Android and iOS Capacitor projects already exist, and the repository currently has no published releases.

This change adds a portrait-friendly app installation card immediately after the theme picker on Home. It supports configured HTTPS Android APK and App Store/TestFlight links, browser installation, Safari/menu guidance, Telegram external-browser opening and installed-native status. Missing release links are not invented. Existing asset caching remains available below.

The Android download workflow now builds the complete webapp, syncs Capacitor from the correct directory, signs a release APK using the existing mobile-store-release environment, verifies its signature, and prepares a draft release with a checksum. It no longer distributes a debug launcher as the release app. Documentation explains signing, version upgrades, physical-device checks, publishing and setting the public download URLs. Browser prompt handling now consumes prompts once and waits for appinstalled before claiming completion.

Validation: 3 Node download-link tests passed; workflow YAML parsed successfully. Full web/native build and portrait browser preview were not run: this environment could read and edit via the GitHub connector, but repository cloning/network access was blocked and project dependencies are not installed locally.

Before release: run the web build, test install/cancel and Safari/Telegram flows, supply the existing Android signing and production API configuration, run the signed APK workflow and test the artifact on a physical device. Publish the reviewed draft and configure VITE_ANDROID_APK_URL, then rebuild/deploy the website. iOS requires a separately signed Apple distribution and VITE_IOS_APP_URL. No binaries were built or published and main has not been merged.

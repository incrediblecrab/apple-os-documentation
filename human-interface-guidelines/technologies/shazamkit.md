# ShazamKit

ShazamKit supports audio recognition by matching an audio sample against the Shazam catalog or a custom audio catalog.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

You can use ShazamKit to provide features like:

- Enhancing experiences with graphics that correspond with the genre of currently playing music
- Making media content accessible to people with hearing disabilities by providing closed captions or sign language that syncs with the audio
- Synchronizing in-app experiences with virtual content in contexts like online learning and retail

If you need the device microphone to get audio samples for your app to recognize, you must request access to it. As with all types of permission requests, it's important to help people understand why you're asking for access.

Check recognition status and controls over the artwork or video your app displays. Preserve readable contrast and [accessible feedback](../foundations/accessibility.md) when people change display preferences.

## Topics

### Best Practices

After you receive permission to access the microphone for features that use ShazamKit, follow these guidelines:

- **Stop recording as soon as possible** - When people allow your app to record audio for recognition, they don't expect the microphone to stay on. To help preserve privacy, only record for as long as it takes to get the sample you need.

- **Ask before saving recognized-song results** - Let people opt in before adding results to their synced Shazam library. The Music Recognition control and Shazam app identify your app as the source, but that attribution doesn't replace consent to save items. See [SHLibrary](https://developer.apple.com/documentation/shazamkit/shlibrary).

### Developer Documentation

- [ShazamKit](https://developer.apple.com/documentation/shazamkit) - ShazamKit framework

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/shazamkit)*

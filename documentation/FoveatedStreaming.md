# Foveated Streaming

Display remotely rendered immersive content on Apple Vision Pro while retaining native visionOS interactions.

**Platforms:** visionOS 26.4+ — Apple Vision Pro

**Status:** Available before OS 27. The OS 27 notes below are not the framework's introduction date.

**Provider-extension availability:** `FoveatedStreamingProviderContext` and `FoveatedStreamingProviderEndpoint` require **visionOS 27.0+**, unlike the core session/client workflow available in 26.4.

## Overview

Foveated Streaming connects a visionOS app to a local or cloud rendering endpoint. The endpoint concentrates streamed image quality around the approximate region where the person is looking. A native immersive space can combine that stream with RealityKit content and SwiftUI controls.

This is a paired client-and-renderer system, not a player for an arbitrary video URL. Apple's integration guides use NVIDIA CloudXR for the rendering endpoint and describe the required session-management protocol.

## Topics

### Build both sides

- [Creating a foveated streaming client on visionOS](https://developer.apple.com/documentation/foveatedstreaming/creating-a-foveated-streaming-client-on-visionos) — Client sample covering connection, presentation, pause, resume, and disconnect.
- [Streaming a CloudXR application to Apple Vision Pro with foveation](https://developer.apple.com/documentation/foveatedstreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation) — Connect the desktop or cloud renderer to the streaming system.
- [Establishing foveated streaming sessions with Apple Vision Pro](https://developer.apple.com/documentation/foveatedstreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro) — Discovery, pairing, and endpoint session management.
- [FoveatedStreamingSession](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession) — Owns connection state and bidirectional data channels.
- [FoveatedStreamingSpaceContent](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspacecontent) — Represents immersive streamed content.

### Performance and extensions

- [Analyzing the performance of a foveated streaming session](https://developer.apple.com/documentation/foveatedstreaming/analyzing-the-performance-of-a-foveated-streaming-session) — Use the dedicated Instruments statistics rather than evaluating only the renderer's frame rate.
- [FoveatedStreamingProviderContext](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext) — Connection context for a streaming provider.
- [FoveatedStreamingProviderEndpoint](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint) — Endpoint supplied to a provider extension.

## Requirements and consent

- Add the [Foveated Streaming Session entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.foveated-streaming-session).
- Test the end-to-end stream on a physical Apple Vision Pro running visionOS 26.4 or later. Apple's client sample does **not** stream in Simulator; its mocked SwiftUI previews test UI behavior only.
- For cloud connections, declare the server mapping in [ApprovedStreamingEndpoints](https://developer.apple.com/documentation/bundleresources/information-property-list/approvedstreamingendpoints). A remote endpoint name must resolve through that configuration.
- Local/system-discovered endpoints use pairing, including a QR-code step for an initial connection. The system also asks permission to share approximate viewing-region information. Treat refusal as a normal canceled connection, not a reason to bypass consent.

## Session and failure handling

Keep an explicit connection state in the UI, allow cancellation during connection, and provide pause, resume, and disconnect controls. Opening the immersive space and establishing the network session are related but separate lifecycle operations.

Test pairing failures, unreachable endpoints, interruptions, and reconnects against the real endpoint. Profile both the network and the renderer; a fast desktop frame rate alone does not establish acceptable headset latency.

The **visionOS 27** release notes mark the microphone-access failure in `FoveatedStreamingProvider` extensions as **resolved** (175954012). Do not describe provider microphone access as categorically unavailable on OS 27; ordinary authorization and application requirements still need validation.

## Sources

- [Foveated Streaming reference](https://developer.apple.com/documentation/foveatedstreaming)
- [visionOS 27 release notes — Foveated Streaming](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#Foveated-Streaming)

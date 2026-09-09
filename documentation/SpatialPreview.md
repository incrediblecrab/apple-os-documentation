# Spatial Preview

Preview documents and editable 3D scenes from a Mac app on Apple Vision Pro.

**Platforms:** macOS 27.0+ | visionOS 27.0+

**Status:** OS 27 beta APIs, reviewed September 8, 2026. The authoring app runs on the Mac; the connected visionOS device presents the preview. This is not an iOS or iPadOS preview API.

## Overview

Spatial Preview connects an existing Mac workflow to a spatial display. Use it to review spatial photographs, inspect a model at an appropriate scale, or synchronize scene edits without building a separate document editor on Apple Vision Pro. It complements local rendering rather than replacing your app's document storage.

## Topics

### Essentials

- [Working with content from your Mac app using Spatial Preview](https://developer.apple.com/documentation/spatialpreview/working-with-content-from-your-mac-app-using-spatial-preview) — Apple's sample covers stereo HEIC documents, furniture-layout changes, and annotations.
- [SpatialPreviewEndpoint](https://developer.apple.com/documentation/spatialpreview/spatialpreviewendpoint) — Identifies the device your session will use.
- [SpatialPreviewDevicePicker](https://developer.apple.com/documentation/spatialpreview/spatialpreviewdevicepicker) — Lets the person select a nearby device from the Mac app; this picker is a macOS API.
- [ConnectedSpatialEndpointObserver](https://developer.apple.com/documentation/spatialpreview/connectedspatialendpointobserver) — Finds the endpoint associated with Mac Virtual Display. Handle the absence of an available connection rather than assuming one exists.

### Choose a session

- [DocumentPreviewSession](https://developer.apple.com/documentation/spatialpreview/documentpreviewsession) — Use for file-oriented previews, such as spatial photos.
- [USDPreviewSession](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession) — Use for a composed USD stage whose edits need to stay synchronized.
- [SpatialPreviewSessionState](https://developer.apple.com/documentation/spatialpreview/spatialpreviewsessionstate) — Distinguishes waiting, connected, interrupted, and invalidated sessions.
- [USDKit](USDKit.md) — The system USD API integrates directly with preview synchronization.

## Integration essentials

1. Obtain a compatible endpoint through the picker or the Mac Virtual Display observer. Keep the Mac document usable when no headset is connected.
2. Choose document preview for a file workflow or USD preview for incremental scene editing. Retain the session for the lifetime of the preview.
3. Check session state before sending edits. Queue changes during an interruption; create a new session after invalidation rather than trying to revive the ended connection.
4. For a private OpenUSD runtime, follow [Bridging an external USD runtime to Spatial Preview](https://developer.apple.com/documentation/spatialpreview/bridging-an-external-usd-runtime-to-spatial-preview). Writing a file alone does not notify USDKit. Exchange a thin override layer, apply USDKit edits on the main actor, and avoid echoing device-originated changes back as new edits.

## Compatibility and failure checks

Test on a compatible Mac and Apple Vision Pro, not only in a document editor or SwiftUI preview. Validate reconnects, large scene updates, and asset dependencies. Framework availability is separate from whether a particular USD renderer supports an asset's materials or geometry; see [USD feature validation](USD.md).

The **macOS 27 Beta 8** notes mark discovery of incompatible older visionOS devices, failures with certain large poorly connected meshes, and synchronization failures for USDZ assets over 75 MB as **resolved**. The visionOS notes also mark the mesh-preview problem as resolved. These are regression-test cases, not documented current file-size or triangle-count limits.

## Sources

- [Spatial Preview reference](https://developer.apple.com/documentation/spatialpreview)
- [macOS 27 release notes — Spatial Preview](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#Spatial-Preview)
- [visionOS 27 release notes — Spatial Preview](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#Spatial-Preview)

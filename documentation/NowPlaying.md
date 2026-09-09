# Now Playing

Publish media metadata and supported playback commands to system playback surfaces.

**Local-session platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

**RemoteMediaSession platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+

**Status:** OS 27 beta APIs, reviewed September 8, 2026. The framework-wide platform list does not make every remote-session API available on every platform.

## Overview

Now Playing observes an application's playback model and publishes its metadata, timing, and commands to the system. Available surfaces depend on the platform and accessory, such as the Lock Screen, Control Center, or CarPlay. The framework publishes playback information; your player or remote device still performs playback.

Choose between a local session for media on the current device and a remote session backed by an extension for media playing elsewhere.

## Topics

### Local playback

- [Publishing media sessions](https://developer.apple.com/documentation/nowplaying/publishing-media-sessions) — Model, artwork, audio setup, and primary-session lifecycle.
- [MediaSessionRepresentable](https://developer.apple.com/documentation/nowplaying/mediasessionrepresentable) — Supplies an observable session's identity, content, timing, and commands.
- [MediaSession](https://developer.apple.com/documentation/nowplaying/mediasession) — Registers the application's local playback model with the system.
- [MediaPlaybackSnapshot](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot) — Associates playback state and elapsed time with a timestamp.
- [Content types and metadata](https://developer.apple.com/documentation/nowplaying/content-types-and-metadata) and [Playback commands](https://developer.apple.com/documentation/nowplaying/playback-commands) — Describe the content and only the operations your player can perform.

### Remote playback

- [Publishing remote media sessions](https://developer.apple.com/documentation/nowplaying/publishing-remote-media-sessions) — Extension setup, device controls, and APNs start/update/end events.
- [RemoteMediaSession](https://developer.apple.com/documentation/nowplaying/remotemediasession) — App-side remote-session lifecycle; implement the extension through the separate extension protocol below.
- [RemoteMediaSessionExtension](https://developer.apple.com/documentation/nowplaying/remotemediasessionextension) — Supplies remote sessions and forwards commands.
- [RemoteMediaSessionRepresentable](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable) — Observable remote content, state, commands, and devices.

## Implementation essentials

For local playback, retain a `MediaSession` for the active model and request application-primary status when publishing it. Release the session when playback ends. Where your platform uses `AVAudioSession`, configure and activate the audio session appropriately before publishing audio playback.

Use a timestamped snapshot so the system can advance the progress display between updates. Disable commands that cannot currently succeed, such as next-track at the end of a queue.

Requesting **system-primary** status is a foreground operation. Apple's guides say the request has no effect when the app is in the background; creating a session does not override that rule.

For remote playback, keep stable session identifiers across attribute updates and end sessions when the receiver stops. The extension needs the `com.apple.nowplaying.remote-media` extension point. APNs delivery uses dedicated Now Playing push tokens and the documented `nowplaying` push type; handle token changes rather than retaining an obsolete token indefinitely.

## Migration and failure boundaries

**Do not mix the new framework with `MPNowPlayingInfoCenter` and `MPRemoteCommandCenter` for local playback.** Apple documents undefined behavior when they are combined. Maintain a separate legacy [Media Player](MediaPlayer.md) path for older OS versions instead of publishing the same local player through both systems.

Handle publication and command errors without displaying a playback state the receiver has not confirmed. Publishing a remote session does not itself discover a receiver, authorize a stream, or guarantee device connectivity; [AVSystemRouting](AVSystemRouting.md) and [Media Device](MediaDevice.md) serve different routing/provider roles.

## Sources

- [Now Playing reference](https://developer.apple.com/documentation/nowplaying)
- [MediaSession availability](https://developer.apple.com/documentation/nowplaying/mediasession)
- [RemoteMediaSession availability](https://developer.apple.com/documentation/nowplaying/remotemediasession)
- [Publishing media sessions](https://developer.apple.com/documentation/nowplaying/publishing-media-sessions)
- [Publishing remote media sessions](https://developer.apple.com/documentation/nowplaying/publishing-remote-media-sessions)

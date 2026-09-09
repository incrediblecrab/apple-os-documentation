# AVSystemRouting

Route media from a playback app to hardware supported by a media device extension.

**Platforms:** iOS 27.0+ | iPadOS 27.0+

**Status:** OS 27 beta APIs, reviewed September 8, 2026. A TV or speaker can be the receiving device without being an SDK deployment platform for this framework.

**Mac Catalyst discrepancy:** The framework reference annotates Mac Catalyst 27.0, but [Routing and streaming media to remote devices](https://developer.apple.com/documentation/avsystemrouting/routing-and-streaming-media-to-remote-devices) explicitly says AVSystemRouting and MediaDevice are unavailable on Mac Catalyst and visionOS. Do not promise Catalyst support from the catalog annotation alone; verify the target SDK and current deployment guidance.

## Overview

AVSystemRouting is the playback-app side of system media routing. Protocol providers supply [Media Device](MediaDevice.md) extensions, and the system connects those extensions to apps when a person selects a receiver. A playback app does not need to embed every provider's device SDK.

Use this framework to react to the selected route, launch URL playback or a companion app on the receiver, and observe remote playback. It does not make every network device a compatible receiver: discovery, supported protocols, and device capabilities still matter.

## Topics

### Essentials

- [Routing media to third-party devices](https://developer.apple.com/documentation/avsystemrouting/routing-media-to-third-party-devices) — Observer, session creation, playback control, and companion-app communication.
- [Routing and streaming media to remote devices](https://developer.apple.com/documentation/avsystemrouting/routing-and-streaming-media-to-remote-devices) — End-to-end app routing and streaming guidance.
- [AVSystemRouteController](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-18ns8) — Coordinates system routes.
- [AVSystemRouteControllerObserver](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-5syvg) — Receives activation and deactivation events.

### Sessions and control

- [AVSystemRoute](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um) — The selected route and its sessions.
- [AVSystemRouteSession](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-gp78) — Starts playback using a URL and supported launch mode.
- [AVSystemRouteMediaSession](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-98ioq) — Provides playback control and, where supported, a data channel.
- [AVSystemRoutingError](https://developer.apple.com/documentation/avsystemrouting/avsystemroutingerror-7miya) — Errors from routing operations.

## Integration essentials

1. Declare [MDESupportedProtocols](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportedprotocols) and, for applicable URL playback, [MDESupportsUniversalURLPlayback](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportsuniversalurlplayback).
2. Register an observer with the shared route controller. Report whether your app handled each event, including events it does not recognize.
3. On activation, create a session in a launch mode the receiver supports, add it to the route, and start it. Handle both failure to add the session and an error while starting it.
4. Drive your UI from the returned media session's playback state. Do not assume that optional playback controls or a companion-app data channel are present.
5. On failure, remove the unsuccessful session; on deactivation, stop the app's corresponding remote-playback activity and update its UI.

## Choosing the right API

- Use **AVSystemRouting** in a media app consuming provider-supported routes.
- Use **Media Device** when implementing the discovery and hardware protocol itself. Its extension/container entitlement requirements are distinct from the playback app's protocol declarations.
- Keep [AVRouting](AVRouting.md) for its existing custom-route and playback-arbitration APIs; this new framework does not retroactively change their minimum availability.
- Use a coherent [Now Playing](NowPlaying.md) or legacy Media Player metadata strategy. Do not mix Now Playing's local-playback APIs with `MPNowPlayingInfoCenter` and `MPRemoteCommandCenter` in your app; Apple documents undefined behavior.

## Sources

- [AVSystemRouting reference](https://developer.apple.com/documentation/avsystemrouting)
- [Routing media to third-party devices](https://developer.apple.com/documentation/avsystemrouting/routing-media-to-third-party-devices)
- [Creating a media device extension](https://developer.apple.com/documentation/mediadevice/creating-a-media-device-extension)

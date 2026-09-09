# HTTP Live Streaming

Send audio and video to iOS, tvOS, and macOS devices.

## Overview

HTTP Live Streaming (HLS) sends audio and video over HTTP from an ordinary web server for playback on iOS-based devices—including iPhone, iPad, iPod touch, and Apple TV—and on desktop computers (macOS). Using the same protocol that powers the web, HLS deploys content using ordinary web servers and content delivery networks. HLS is designed for reliability and dynamically adapts to network conditions by optimizing playback for the available speed of wired and wireless connections.

HLS supports the following:

- Live broadcasts and prerecorded content (video on demand, or VOD)
- Multiple alternate streams at different bit rates
- Intelligent switching of streams in response to network bandwidth changes
- Media encryption and user authentication

### Encode and deliver streaming media

An HTTP Live Stream has three main parts: encoding and packaging, HTTP distribution, and client playback.

An encoder produces compressed audio and video, and a packager creates compatible media segments and playlists. Codec and container choices are not interchangeable: Apple's [authoring specification](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices) requires fragmented MP4 for HEVC video. The playlist and segments are published on a web server. A client reads the playlist, requests the media, and buffers and decodes it for continuous playback; network or device limitations can still cause stalls.

### Prepare media with the server component

The server component is responsible for taking input streams of media and encoding them digitally. It encapsulates them in a format suitable for delivery and prepares the encapsulated media for distribution.

For live events, the server requires a media encoder, which can be off-the-shelf hardware, and a way to break the encoded media into segments and save them as files, which can either be software such as the media stream segmenter provided by Apple or part of an integrated third-party solution.

### Deliver files with the distribution component

Baseline HLS distribution serves playlists and media segments over HTTP through web servers and caches; it does not require a specialized streaming-protocol server. Configure delivery for the playlists and media your encoder produces, using codec/container combinations supported by the target clients. Low-Latency HLS adds server behavior beyond ordinary static-file delivery, so follow its separate guide rather than assuming every HLS deployment needs only default web-server settings.

### Access media through client software

Client software is responsible for determining the appropriate media to request, downloading those resources, and then reassembling them so that the media can be presented to the user in a continuous stream. For the rules governing the interaction between an HLS player and its server, see HTTP Live Streaming 2nd Edition.

Apple provides several frameworks that support HTTP Live Streaming, including AVKit, AVFoundation, and WebKit. HLS playback support itself dates to iOS 3.0 and Safari 4.0; the individual framework APIs have separate availability. Prefer the system playback stack when it meets your requirements rather than implementing a new HLS client.

However, if you do develop your own client software, begin by fetching the index file using a URL that identifies the stream. The index file, in turn, specifies the location of the available media files, decryption keys, and any alternate streams available. For the selected stream, download each available media file in sequence. Each file contains a consecutive segment of the stream. Once it has a sufficient amount of data downloaded, present the reassembled stream to the user.

> **Important:** Your client is responsible for fetching any decryption keys, authenticating or presenting a user interface to allow authentication, and decrypting media files as needed.

`EXT-X-ENDLIST` signals that no more media segments will be added to that media playlist; the client still plays the available queued media. Reload mutable playlists according to the playlist type and protocol-defined rules rather than polling every playlist indiscriminately: a VOD playlist is static. An open-ended playlist is not a guarantee that the source is currently producing new media.

## Topics

### Essentials
- [Deploying a Basic HTTP Live Streaming (HLS) Stream](https://developer.apple.com/documentation/http-live-streaming/deploying-a-basic-http-live-streaming-hls-stream) - Create a basic webpage to deliver HLS.
- [Preparing Audio for HTTP Live Streaming](https://developer.apple.com/documentation/http-live-streaming/preparing-audio-for-http-live-streaming) - Encode your media properly to ensure synchronized audio and video playback.

### Stream creation
- Learn to create a stream for ingestion by apps enabled with HTTP Live Streaming. Ensure correct playlist formatting and adherence to guidelines.
- [Example playlists for HTTP Live Streaming](https://developer.apple.com/documentation/http-live-streaming/example-playlists-for-http-live-streaming) - View and compare playlists for different HLS applications.
- [About the EXT-X-VERSION tag](https://developer.apple.com/documentation/http-live-streaming/about-the-ext-x-version-tag) - Find the protocol version that corresponds with the HLS features your app supports.

### Tool usage and validation
- Use the provided tools to segment your stream, create multivariant playlists, and verify the output of your own tools.
- [Using Apple's HTTP Live Streaming (HLS) Tools](https://developer.apple.com/documentation/http-live-streaming/using-apple-s-http-live-streaming-hls-tools) - Segment your video stream and create media playlists for successful transmission with Apple's provided tools.

### Specifications and other documents
- [HTTP Live Streaming (HLS) authoring specification for Apple devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices) - Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](https://developer.apple.com/documentation/http-live-streaming/using-content-protection-systems-with-hls) - Add encryption keys to media playlists.
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](https://developer.apple.com/documentation/http-live-streaming/about-the-common-media-application-format-with-http-live-streaming-hls) - Learn the Common Media Application Format as it applies to HLS.
- [Enabling Low-Latency HTTP Live Streaming (HLS)](https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls) - Add Low-Latency HLS to your content streams to maintain scalability.
- [Links to additional specifications and videos](https://developer.apple.com/documentation/http-live-streaming/links-to-additional-specifications-and-videos) - Review additional specifications and documents.
- [Videos about HLS](https://developer.apple.com/documentation/http-live-streaming/videos-about-hls) - Review informational videos about HTTP Live Streaming.
- [Providing metadata for xHE-AAC video soundtracks](https://developer.apple.com/documentation/http-live-streaming/providing-metadata-for-xhe-aac-video-soundtracks) - Ensure volume normalization by including metadata for loudness and dynamic range control.
- [Adjusting anchor loudness](https://developer.apple.com/documentation/http-live-streaming/adjusting-anchor-loudness) - Adjust anchor loudness when measurements of speech-gated loudness for a full mix may be inaccurate, such as when speech activity is low.
- [Providing JavaScript Object Notation (JSON) chapters](https://developer.apple.com/documentation/http-live-streaming/providing-javascript-object-notation-json-chapters) - Prepare JSON chapters for HTTP Live Streaming.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HTTP-Live-Streaming)*

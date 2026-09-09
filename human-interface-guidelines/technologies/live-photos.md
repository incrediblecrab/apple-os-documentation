# Live Photos

Live Photos lets people capture favorite memories in a sound- and motion-rich interactive experience that adds vitality to traditional still photos.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

When Live Photos is available, the Camera app captures additional content — including audio and extra frames — before and after people take a photo. People press a Live Photo to see it spring to life.

## Topics

### Best Practices

- **Apply adjustments to all frames** - If your app lets people apply effects or adjustments to a Live Photo, make sure those changes are applied to the entire photo. If you don't support this, give people the option of converting it to a still photo.

- **Keep Live Photo content intact** - It's important for people to experience Live Photos in a consistent way that uses the same visual treatment and interaction model across all apps. Don't disassemble a Live Photo and present its frames or audio separately.

- **Implement a great photo sharing experience** - If your app supports photo sharing, let people preview the entire contents of Live Photos before deciding to share. Always offer the option to share Live Photos as traditional photos.

- **Clearly indicate when a Live Photo is downloading and when the photo is playable** - Show a progress indicator during the download process and provide some indication when the download is complete.

- **Display Live Photos as traditional photos in environments that don't support Live Photos** - Don't attempt to replicate the Live Photos experience provided in a supported environment. Instead, show a traditional, still representation of the photo.

- **Make Live Photos easily distinguishable from still photos** - A brief motion hint helps people recognize Live Photo content. Although the HIG says there are no built-in motion effects like the Photos browsing transition, [PHLivePhotoView](https://developer.apple.com/documentation/photosui/phlivephotoview) explicitly supports `startPlayback(with: .hint)` for brief, silent motion. Distinguish that built-in playback hint from a custom browsing transition. When movement isn't appropriate, show the system-provided badge in a consistent position. The badge supports overlay and solid appearances, including a variant for a Live Photo shown as a still. Don't substitute a video-style playback button.

- **Keep badge placement consistent** - If you show a badge, put it in the same location on every photo. Typically, a badge looks best in a corner of a photo.

### Platform Considerations

**visionOS**  
- In visionOS, people can view a Live Photo, but they can't capture one.

**watchOS**  
- Live Photos are not supported in watchOS.

### Developer Documentation

- [PHLivePhoto](https://developer.apple.com/documentation/photos/phlivephoto) - Photos
- [LivePhotosKit JS](https://developer.apple.com/documentation/livephotoskitjs) - LivePhotosKit JS

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/live-photos)*

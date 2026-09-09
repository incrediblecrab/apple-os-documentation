# LivePhotosKit JS

Play Live Photos on the web.

**Platforms:** LivePhotosKit JS 1.0+

## Overview
Use the LivePhotosKit JS library to play Live Photos on your web pages.

The JavaScript API presents the player in the form of a DOM element, much like an image or video tag, which can be configured with photo and video resources and other options, and have its playback controlled either programmatically by the consuming developer, or via pre-provided controls by the browsing end-user.

## Before You Begin

### Embed LivePhotosKit JS in your webpage

Use the script tag and link to Apple’s hosted version of LivePhotosKit JS at https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js.

```html
<script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
```

The `/lpk/1/` URL selects the version-1 library line, not an exact 1.0.0 build. The hosted script captured for this review identifies itself as 1.5.8; the NPM package metadata separately reports 1.5.6. Do not assume the hosted and packaged builds are identical.

### Enable JavaScript strict mode

To enable strict mode for an entire script, put `'use strict'` before any other statements.

```javascript
'use strict';
```

LivePhotosKit JS is also available through NPM at https://www.npmjs.com/package/livephotoskit.

The install command is:

```shell
npm install --save livephotoskit
```

## Declarative HTML

By including the LivePhotosKit JS script on your page, you can create players by simply adding declarative markup to your HTML. As the page loads, LivePhotosKit JS will determine what player instances are on the page and initialize them. You can use any HTML tag that supports child nodes.

At minimum, each tag requires the data-live-photo attribute as well as a non-zero height and width. Doing this allows LivePhotosKit JS to find the DOM elements to be initialized as players.

Then you can specify the locations of the photo and video components by setting the data-photo-src and data-video-src attributes, respectively.

Optionally, you can use the following additional data attributes:

data-photo-time: The timestamp from the beginning of the provided video component, at which the still photo was captured.

data-proactively-loads-video: Whether or not the Player will download the bytes at the provided data-video-src prior to the user or developer attempting to begin playback.

data-shows-native-controls: Whether or not the playback controls are enabled for the user.

Each DOM element assigned to be a Player will be decorated with a playback control.

This declarative example needs real, paired photo and video URLs in place of the placeholders.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
    </head>
    <body>
        <div
            data-live-photo
            data-photo-src="https://..."
            data-video-src="https://..."
            style="width: 320px; height: 320px">
        </div>
    </body>
</html>
```

## JavaScript API

Create a new LivePhotosKit.Player by invoking it either as a wrapper around a pre-existing DOM element, or by calling it without an argument, which will create a new DOM element.

These are alternative construction examples. A player created in JavaScript still needs nonzero dimensions and media sources before it can display a Live Photo.

```javascript
// A Player built from a new DIV:
const myNewPlayer = LivePhotosKit.Player();
myNewPlayer.style.width = '320px';
myNewPlayer.style.height = '320px';
document.body.appendChild(myNewPlayer);
// A Player built from a pre-existing element:
LivePhotosKit.Player(document.getElementById('myExistingElement'));
```

After a Player is created, use the properties and methods to set it up and use it, just as you would with a native image or video element.

The player will emit these events:

canplay when the Player has obtained just enough video frames and is obtaining them quickly enough for smooth playback.

error when loading of either the photo or video components of the Live Photo has failed.

ended when playback of the Live Photo has completed.

videoload when the video component of the Live Photo has finished loading.

photoload when the photo component of the Live Photo has finished loading.

The next example assumes a sized element with the indicated ID already exists. Replace both asset URL placeholders. The playback and seek calls demonstrate separate operations, not an initialization sequence; wait until the media is ready before using them.

```javascript
// Create the player using a pre-existing DOM element.
const player = LivePhotosKit.Player(document.getElementById('my-live-photo-target-element'));
player.photoSrc = 'https://...';
player.videoSrc = 'https://...';
// Listen to events the player emits.
player.addEventListener('canplay', evt => console.log('player ready', evt));
player.addEventListener('error', evt => console.log('player load error', evt));
player.addEventListener('ended', evt => console.log('player finished playing through', evt));
// Use the playback controls.
player.playbackStyle = LivePhotosKit.PlaybackStyle.HINT;
player.playbackStyle = LivePhotosKit.PlaybackStyle.FULL;
player.play();
player.pause();
player.toggle();
player.stop();
// Seek the animation to one quarter through.
player.currentTime = 0.25 * player.duration;
// Seek the animation to 0.1 seconds into the Live Photo.
player.currentTime = 0.1;
```

## Error Handling

A Player will emit error events, if and when errors occur while attempting to load or play. If a Player does experience an error, it will also publish the error to its public property errors as a way to convey whether or not it is in an error state, and, if so, what the errors were.

The error states can be seen here LivePhotosKit.Errors.

This handler uses the `player` created in the previous example.

```javascript
player.addEventListener('error', (ev) => {
    if (typeof ev.detail.errorCode === 'number') {
        switch (ev.detail.errorCode) {
        case LivePhotosKit.Errors.IMAGE_FAILED_TO_LOAD:
            // Do something
            break;
        case LivePhotosKit.Errors.VIDEO_FAILED_TO_LOAD:
            // Do something
            break;
        }
    } else {
        // Extract error.
        console.error(ev.detail.error);
    }
});
```

## Browser Compatibility

Apple's version-1 reference publishes the following compatibility matrix. It includes legacy browser entries and is not a record of testing against current browser versions. Validate your target versions and media formats; the JavaScript examples above use modern syntax.

| Device | Browser |
|--------|--------|
| iOS | Safari, Chrome |
| macOS | Safari, Chrome, Firefox |
| Android (performance depends on device) | Chrome (beta) |
| Windows | Chrome, Firefox, Edge, Internet Explorer 11 |

## How to obtain Live Photo assets

Live Photos consist of a still image and a paired video of the moments around capture. Preserve both components when exporting. [Photos exports unmodified originals in their original formats](https://support.apple.com/guide/photos/export-photos-videos-and-slideshows-pht6e157c5f/mac), so the still image is not guaranteed to be JPEG; it may be HEIC. Prepare a browser-compatible still image and video for web playback rather than assuming the original files will decode on every target browser.

Important

Keep download and decode costs within the target browser's budget. Give the player explicit dimensions before its photo loads so loading UI has a visible area. Test appropriately sized assets and encodings instead of assuming that every original Live Photo is suitable for web delivery.

### Using macOS Photos

Connect your iOS device to your Mac.

Import your photos into the Photos application.

Select the Live Photo you wish to export.

Use File > Export > Export Unmodified Original to export to your file system.

### Using macOS Image Capture

Connect your iOS device to your Mac.

Select the Live Photo you wish to import from your device to your local file system.

Choose the destination folder and click on Import.

### Using Windows 10 File Explorer

This is the legacy File Explorer workflow retained in the version-1 reference, not a current Windows-version requirement. Apple's [current transfer guide](https://support.apple.com/en-us/120267) uses the Apple Devices app rather than requiring iTunes: connect the device by USB, unlock it, and approve the trust prompt. If iCloud Photos is enabled, download the original full-resolution assets to the device before a PC import.

Open File Explorer. This can be opened by pressing the Windows Key and E at the same time.

Connect your iOS device to your PC.

You should see your iOS device in the “This PC” folder.

Navigate to the following folder: (your device) > Internal Storage > DCIM and look for the Live Photo you wish to import.

Find the matching still-image and video files. Their formats depend on the original asset and transfer settings; do not assume that every pair is JPG plus MOV.

Drag the pair of files to your local file system.

## Topics

### Classes
- **LivePhotosKit** - The namespace for the LivePhotosKit library.
- **LivePhotosKit.Player** - A player for Live Photos.

### Enumerations
- **LivePhotosKit.Errors** - The errors that can occur when playing a LivePhoto.
- **LivePhotosKit.PlaybackStyle** - Possible playback styles.
- **LivePhotosKit.EffectType**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LivePhotosKitJS)*

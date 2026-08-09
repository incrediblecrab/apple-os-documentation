# MusicKit for Web

JavaScript library for integrating Apple Music into web applications.

**Platforms:** Web

## Overview

MusicKit on the Web uses JSON Web Tokens (JWTs) to interact with the Apple Music API. You must have a signed developer token in order to initialize MusicKit on the Web.

**Important:** You use a developer token to authenticate yourself as a trusted developer and member of the Apple Developer Program and to use MusicKit on the Web. You can find more information about creating an Apple Music developer token in Getting Keys and Creating Tokens.

Token validity is checked up-front by MusicKit on the Web and it must be valid and not expired in order to continue with any further functionality.

### Embedding MusicKit on the Web

Use the script tags and link to Apple's hosted version of MusicKit on the Web:

```html
<script src="https://js-cdn.music.apple.com/musickit/v3/musickit.js" data-web-components async></script>
```

The `data-web-components` attribute instructs MusicKit to also load the Web Components for playback controls. The `async` attribute is recommended for non-blocking page rendering.

### Configuration

You can configure MusicKit on the Web with markup or JavaScript:

**Using meta tags:**
```html
<head>
  <meta name="apple-music-developer-token" content="DEVELOPER-TOKEN" />
  <meta name="apple-music-app-name" content="My Cool Web App" />
  <meta name="apple-music-app-build" content="1978.4.1" />
</head>
```

**Using JavaScript:**
```javascript
document.addEventListener('musickitloaded', async function () {
  try {
    await MusicKit.configure({
      developerToken: 'DEVELOPER-TOKEN',
      app: {
        name: 'My Cool Web App',
        build: '1978.4.1',
      },
    });
  } catch (err) {
    // Handle configuration error
  }

  const music = MusicKit.getInstance();
});
```

### The musickitloaded Event

MusicKit on the web is initialized asynchronously, which means the MusicKit global is not available immediately after the JavaScript file is evaluated. Instead a `musickitloaded` event is fired on the document when the MusicKit global is available.

```javascript
document.addEventListener('musickitloaded', async function () {
  // MusicKit global is now defined.
});
```

**Important:** You won't see this event listener wrapper in all examples within this documentation, but you may need to add it in your code if you see an error in console similar to: `ReferenceError: Can't find variable: MusicKit`

## Topics

### Getting Started
- Basic setup and configuration for MusicKit on the Web
- Developer token authentication and initialization
- Embedding the library in web applications

### Configuration
- Markup-based configuration using meta tags
- JavaScript-based configuration for advanced customization
- Handling the asynchronous initialization process

### Web Components
- Optional playback controls for quick implementation
- Ready-to-use UI components for music playback

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://js-cdn.music.apple.com/musickit/v3/docs/index.html?path=/story/introduction--page)*
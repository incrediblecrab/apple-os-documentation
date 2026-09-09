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
<script src="https://js-cdn.music.apple.com/musickit/v3/musickit.js" async></script>
```

The `async` attribute avoids blocking page rendering. Register the initialization listener before this asynchronous script is added.

### Configuration

The current v3 introduction configures the library using JavaScript. The [v3 migration guide](https://js-cdn.music.apple.com/musickit/v3/docs/index.html?path=/docs/tech-notes-migrating-to-v3--page) removes declarative HTML support and the `declarativeMarkup` option. Do not treat older meta-tag or web-component bootstrap examples as the setup contract for this version.

Register the listener before asynchronously loading the library, and replace the developer-token placeholder with a valid signed token. This is a setup excerpt, not a complete playback or authorization flow.

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
    console.error('MusicKit configuration failed', err);
    return;
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

A listener added after the event has already fired does not replay that event. Establish the listener before adding the asynchronous script; acquire the MusicKit instance only after configuration succeeds.

## Topics

### Getting Started
- Basic setup and configuration for MusicKit on the Web
- Developer token authentication and initialization
- Embedding the library in web applications

### Configuration
- JavaScript configuration with `MusicKit.configure`
- Handling rejected or expired developer tokens
- Handling the asynchronous initialization process

### Version migration
- [Migrating to v3](https://js-cdn.music.apple.com/musickit/v3/docs/index.html?path=/docs/tech-notes-migrating-to-v3--page) - Review removed declarative markup and changed instance APIs before adapting v1 examples.
- [Apple Music API](AppleMusicAPI.md) - Keep catalog requests, developer credentials, and user-library authorization requirements distinct.

---

*Source: [Apple Developer Documentation](https://js-cdn.music.apple.com/musickit/v3/docs/index.html?path=/story/introduction--page)*

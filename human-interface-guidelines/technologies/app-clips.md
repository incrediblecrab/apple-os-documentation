# App Clips

An App Clip is a lightweight version of your app or game that provides an on-the-go or demo experience that's instantly available.

**Platforms:** iOS | iPadOS

## Overview

App Clips deliver an experience from your app or game without requiring people to download the full app from the App Store. App Clips focus on a fast solution to a task or contain a demo that showcases the full app or game, and they remain on the device for a limited amount of time while preserving people's privacy.

People discover and launch App Clips in a variety of situations and contexts. At a physical location, people launch an App Clip by scanning an App Clip Code, NFC tag, or a QR code. An App Clip Code tends to be the best way for people to discover and launch your App Clip because its distinct design is immediately recognizable, and people trust it to offer a fast, secure way to launch an App Clip.

On their device, people launch an App Clip from location-based suggestions they permit in Siri Suggestions, the Maps app, Smart App Banners on websites, App Clip cards in Safari, and by tapping links others share with them in the Messages app. Starting with iOS 17, an app can include links and App Clip previews that people tap to launch another app's App Clip.

Consider creating an App Clip if your app provides an in-the-moment experience that helps people perform a task over a finite amount of time. For example:

- A rental bike could come with an App Clip Code that people tap or scan to launch an App Clip that lets them rent the bike.
- A coffee shop could offer an App Clip for fast advance orders that customers launch from a Smart App Banner or an App Clip card on the shop's website. Customers could share a link to the website from the Messages app, which recipients then tap to launch the App Clip from within Messages.
- A food truck could create marketing material (for example, a poster to promote a seasonal dish) that includes an App Clip Code. People can scan the App Clip Code with the Camera app on their device and instantly launch the App Clip to order the seasonal dish.
- A restaurant could let diners pay for a meal by launching an App Clip from the Maps app or a suggestion from Siri Suggestions, or by holding their device close to an App Clip Code or NFC tag at their table.
- A museum could have visitors scan App Clip Codes or QR codes on labels next to displayed works to launch an App Clip that reveals augmented reality content or provides audio commentary.

Consider creating an App Clip to let people experience your app or game before committing to a purchase or subscription. Focus on providing people with an opportunity to experience and understand your app or game. For example:

- A game might offer an App Clip that lets people play a demo version of the game, including a tutorial and the first level of the game.
- A fitness app might offer an App Clip with a free workout and a guided meditation.
- A text editor might allow people to create and save a document using the demo App Clip.

For developer guidance, see [App Clips](https://developer.apple.com/documentation/app_clips).

## Topics

### Best Practices

- **Allow people to complete a task or demo** - Don't require people to install the full app to experience the entire demo, complete a task, or finish a level in a game.
- **Focus on essential features** - Interactions with App Clips are quick and focused. Limit features to what's necessary to accomplish the task at hand. Reserve advanced or complex features for the app.
- **Provide real value** - Don't use App Clips solely for marketing purposes. App Clips need to provide real value and help people accomplish tasks. Don't use them to advertise services or products, and don't display ads.
- **Use native components** - Avoid using web views in your App Clip. App Clips use native components and frameworks to offer an app-quality experience.
- **Design a linear, focused interface** - App Clips don't need tab bars, complex navigation, or settings. Keep the number of screens and entry forms to a minimum.
- **Show relevant content immediately** - On launch, show the most relevant part of your App Clip. Skip unnecessary steps and take people immediately to the part that best fits their context.
- **Ensure immediate usability** - App Clips need to include all required assets, omit splash screens, and never make people wait on launch.
- **Keep it small** - The smaller your App Clip, the faster it will launch. Reduce unnecessary code and remove unused assets. Avoid downloading additional data.
- **Make it shareable** - When someone shares a link to an App Clip in Messages, recipients can launch it from within Messages. Offer the ability to share links to specific points.
- **Simplify payments** - Consider supporting [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) to offer express checkout and let people enter shipping information with no typing.
- **Minimize account requirements** - Avoid requiring people to create an account before they can benefit from your App Clip. If an account is required, consider offering [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple).
- **Provide a familiar app experience** - When people install the full app, ensure it provides a focused, familiar experience to people who previously used the App Clip.

### Privacy Considerations

- **Follow system limitations** - The system imposes limits on App Clips to ensure people's privacy. For example, App Clips can't perform background operations.
- **Limit data storage** - If you need to store people's data, store it securely. Don't rely on the availability of data previously stored on the device.
- **Use secure authentication** - Consider offering [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple) to securely retain login information off people's devices.
- **Provide secure payments** - Offer a secure way to pay for services or goods that respects people's privacy, such as [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay).

### App Promotion

- **Don't compromise user experience** - Avoid asking people to install the full app if it compromises the experience. Let people fully experience demos before recommending installation.
- **Choose the right timing** - When someone completes a task or reaches a natural pause, display an overlay that allows people to download your full app.
- **Be respectful** - Don't ask people to install the full app repeatedly or interrupt them during a task. Push notifications aren't appropriate for app promotion.
- **Communicate value** - Clearly communicate your app's additional features when recommending installation.

### Notifications

- **Use sparingly** - App Clips can schedule and receive notifications for up to 8 hours after launch. Only request extended permission if really needed.
- **Keep focused** - Don't send purely promotional notifications. Only use notifications in response to explicit user actions.
- **Help complete tasks** - Notifications should relate directly to the task the App Clip helps accomplish, such as delivery updates for food orders.

### App Clip Cards

- **Be informative** - Make sure the image clearly communicates the features offered by your App Clip, supported tasks, or content.
- **Use photography and graphics** - Avoid screenshots of your app's user interface. Use images that help people understand the App Clip's value.
- **Avoid text in images** - Text in header images isn't localizable and can be difficult to read.
- **Follow image requirements** - Use 1800x1200 px PNG or JPEG images without transparency.
- **Write concise copy** - Create titles with no more than 30 characters and subtitles with no more than 56 characters.
- **Choose appropriate action verbs** - Use "View" for media or informational content, "Play" for games, and "Open" for all other App Clips.

### App Clip Codes

App Clip Codes are the best way for people to discover your App Clip. Their distinct design is immediately recognizable, and they offer a fast, secure way to launch your App Clip.

- **Use Apple-provided designs** - App Clip Codes always use the designs Apple provides. Choose between the badge design with the App Clip logo or a design without it when space is limited.
- **Choose the right variant** - Use NFC-integrated codes when people can physically access them, and scan-only codes for inaccessible or digital placements.
- **Follow size requirements** - Minimum 3/4 inch (1.9 cm) diameter for printed materials, 256×256 px for digital, and consider viewing distance ratios.
- **Ensure proper placement** - Place on flat or cylindrical surfaces only, keep unobstructed, display upright, and provide adequate clear space.
- **Use clear messaging** - Add call-to-action text that explains how to use the code, especially for designs without the App Clip logo.
- **Follow printing guidelines** - Use high-quality materials, proper resolution settings, and test codes before distribution.

### Platform Considerations

**iOS**
- App Clips are available on iOS devices and can be launched through various methods including App Clip Codes, NFC tags, QR codes, Safari, Maps, and Siri Suggestions
- Support for location-based suggestions and Smart App Banners

**iPadOS**
- Full App Clip functionality available on iPad devices
- Optimized for larger screen experiences while maintaining the lightweight nature

### Related Components

- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) - Streamlined payment solution for App Clips
- [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple) - Privacy-focused authentication
- [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc) - Near field communication for App Clip Codes

### Developer Documentation

- [App Clips](https://developer.apple.com/documentation/app_clips) - App Clips framework
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App Clip configuration and management
- [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) - Legal requirements for App Clip Codes

## Changelog

### June 9, 2025
- Updated guidance to include demo App Clips

### May 2, 2023
- Consolidated guidance into one page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/app-clips)*
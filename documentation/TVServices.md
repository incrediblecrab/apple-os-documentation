# TV Services

Display content and descriptions, provide channel guides, and support multiple users on Apple TV.

**Platforms:** tvOS 9.0+

## Overview

Use the **TVServices** framework to display content prominently on the screen and to speed up user login. You can highlight media and other information from your app in the top shelf area. For example, a video playback app might show the user's most recently viewed videos. The system displays your media items when the user selects your app on the tvOS Home Screen; your app doesn't need to be running. You provide top shelf content using a **Top Shelf app extension**, which you include in the bundle of your tvOS app.

Apps that manage multiple user profiles can accelerate the login process by retaining the profile for each Apple TV user. Apple TV supports multiple user accounts, and these accounts are separate from the profiles your app manages. Mapping the system accounts to your own profiles lets users skip profile selection screens and go straight to their content, which provides a better user experience.

[`TVUserManager`](https://developer.apple.com/documentation/tvservices/tvusermanager) requires the User Management entitlement and the documented Runs as Current User configuration. On tvOS 16 and later, check [`shouldStorePreferencesForCurrentUser`](https://developer.apple.com/documentation/tvservices/tvusermanager/shouldstorepreferencesforcurrentuser): if false, ask for a profile for the current session but do not save that selection. On tvOS 15 and earlier, Apple's guidance is to show the profile picker at each session start. A system account is not automatic authorization to a media-service account.

**Important**

Don't perform memory-intensive operations from your **TVServices** app extension. The memory limits for app extensions are significantly lower than for apps, and using too much memory might cause the system to terminate your extension. Instead, generate top shelf content and perform other memory-intensive operations on your server.

## Topics

### Top Shelf App Extensions
- [Building a Full Screen Top Shelf Extension](https://developer.apple.com/documentation/tvservices/building-a-full-screen-top-shelf-extension) - Highlight content from your Apple TV application by building a full screen Top Shelf extension.
- **TVTopShelfContentProvider** - The main interface for your Top Shelf app extension, which you use to provide content for the top shelf area of the tvOS Home Screen.
- [Legacy Extension](https://developer.apple.com/documentation/tvservices/legacy-extension) - Help users discover your app by providing top shelf content and a description of your tvOS app.

### Carousel Content
- **TVTopShelfCarouselItem** - An item containing images, video, and other information that you want to display using a carousel-based interface.
- **TVTopShelfCarouselContent** - A set of items you present using a carousel-style interface in the top shelf.

### Sectioned and Inset Content
- **TVTopShelfSectionedItem** - An item to display in a section-based interface.
- **TVTopShelfItemCollection** - A group of items that you display together in a sectioned interface in the top shelf.
- **TVTopShelfSectionedContent** - The set of items you want to present using a section-based interface in the top shelf.
- **TVTopShelfInsetContent** - A set of items to present using an inset-style interface in the top shelf.

### Multiple Users
- [Personalizing Your App for Each User on Apple TV](https://developer.apple.com/documentation/tvservices/personalizing-your-app-for-each-user-on-apple-tv) - Use account-specific storage to segregate data on a multiuser system.
- [Supporting Multiple Users in Your tvOS App](https://developer.apple.com/documentation/tvservices/supporting-multiple-users-in-your-tvos-app) - Store separate data for each user with the Runs as Current User capability.
- [Mapping Apple TV users to app profiles](https://developer.apple.com/documentation/tvservices/mapping-apple-tv-users-to-app-profiles) - Adapt the content of your app for the current viewer by using an entitlement and simplifying sign-in flows.
- **TVUserManager** - An object that indicates how to store preferences for multiple people on a shared device; available from tvOS 13.0.

### Channel Guide
- [Providing Channel Navigation](https://developer.apple.com/documentation/tvservices/providing-channel-navigation) - Support browsing an electronic program guide (EPG) and changing channels with specialized remote buttons.
- **TVUserActivityTypeBrowsingChannelGuide** - An activity for viewing your app's channel guide.

### Common Types
- **TVTopShelfItem** - An item that uses an image to represent a movie, show, or other content in the top shelf.
- **TVTopShelfAction** - An action to perform in response to user interactions with an item in the top shelf.
- **TVTopShelfContent** - The protocol that objects adopt to provide content for the top shelf.
- **TVTopShelfObject** - An abstract base class for describing top shelf items and item collections.

### Variables
- [`TVUserActivityTypeBrowsingEntertainmentContent`](https://developer.apple.com/documentation/tvservices/tvuseractivitytypebrowsingentertainmentcontent) - The activity type used to open the TV Provider app's main screen; available from tvOS 18.1.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVServices)*

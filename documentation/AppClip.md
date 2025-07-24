# App Clips

Create a lightweight, in-the-moment experience or demo version for your app that's instantly available.

**Platforms:** iOS 14.0+ | iPadOS 14.0+

## Overview

An App Clip is a lightweight version of your app that offers access to some of the app's functionality. For example, a donut shop's app a person downloads and installs from the App Store may allow them to order donuts, save favorites, collect rewards, get special offers, and so on. The donut shop's App Clip is instantly available – for example, when someone searches for "donuts" near the shop – without the need to install the full app. To ensure a fast launch experience and a fast order experience, the App Clip offers only the functionality to order donuts.

App Clips that conform to a set of constraints can be larger in size, making it possible to offer an App Clip that's a demo version of your app. The larger demo size allows people to experience your app's functionality without a purchase or subscription. For example, a game might offer an App Clip to play the first level, a fitness app might offer an App Clip with a free workout, and so on. When a person has finished the game's first level or completed the free workout, the App Clip displays a prompt to install the full app.

### Offer a great user experience

App Clips provide a polished user experience that helps users solve a real-world task as quickly as possible or effortlessly try out a new app. Additionally, App Clips don't appear on the Home screen, and users don't manage them the way they manage full apps. Instead, the system removes an App Clip from a device after a period of inactivity, emphasizing the importance of a polished user experience.

For design guidance, see Human Interface Guidelines > App Clips.

### Review App Clip creation

Limit the function of an App Clip to ensure a fast launch experience, protect user privacy, and preserve resources for in-the-moment experiences and demo versions of your app. Before you create an App Clip:

- Review technology available to App Clips and constraints that ensure a good user experience.
- Identify which of your app's functionalities might make a great App Clip.
- Learn how people discover and launch App Clips with invocations and how you configure App Clip experiences and use invocation URLs to offer a great launch experience.

For more information, refer to Choosing the right functionality for your App Clip and Configuring App Clip experiences.

When you've identified functionality for your App Clip and identified invocations:

- Make changes to your app's Xcode project and your code; for example, add an App Clip target and share code between your App Clip and full app.
- Add code to respond to invocations and to handle invocation URLs.
- Create App Clip experiences in App Store Connect.
- Optionally, associate your App Clip with your website to support additional invocations and advanced App Clip experiences.
- Optionally, create App Clip Codes that offer the best experience for people to discover and launch your App Clip.

## Topics

### Essentials
- [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/app_clips/choosing_the_right_functionality_for_your_app_clip) - Review frameworks available to App Clips and identify functionality that makes a great App Clip.
- [Configuring App Clip experiences](https://developer.apple.com/documentation/app_clips/configuring_app_clip_experiences) - Review how people launch your App Clip with invocation URLs, default and demo links, and advanced App Clip experiences.
- [App Clips updates](https://developer.apple.com/documentation/app_clips/app_clips_updates) - Learn about important changes in App Clips.

### Creation
- [Creating an App Clip with Xcode](https://developer.apple.com/documentation/app_clips/creating_an_app_clip_with_xcode) - Add an App Clip target to your Xcode project and share code between the App Clip and its corresponding full app.
- [Fruta: Building a Feature-Rich App with SwiftUI](https://developer.apple.com/documentation/swiftui/fruta_building_a_feature-rich_app_with_swiftui) - Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- **Parent Application Identifiers Entitlement** - A list of parent application identifiers for an App Clip with exactly one entry.
- **com.apple.developer.associated-appclip-app-identifiers** - A list of App Clip identifiers for an app with exactly one entry.
- **com.apple.developer.on-demand-install-capable** - A Boolean value that indicates whether a bundle represents an App Clip.

### Launch
- [Responding to invocations](https://developer.apple.com/documentation/app_clips/responding_to_invocations) - Add code to respond to invocations and offer a focused launch experience.
- [Associating your App Clip with your website](https://developer.apple.com/documentation/app_clips/associating_your_app_clip_with_your_website) - Enable the system to verify your App Clip to support invocations from your website and devices running iOS 16.3 or earlier.
- [Supporting invocations from your website and the Messages app](https://developer.apple.com/documentation/app_clips/supporting_invocations_from_your_website_and_the_messages_app) - Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.
- [Confirming a person's physical location](https://developer.apple.com/documentation/app_clips/confirming_a_person_s_physical_location) - Add code to quickly confirm a person's physical location while respecting their privacy.
- [Launching another app's App Clip from your app](https://developer.apple.com/documentation/app_clips/launching_another_app_s_app_clip_from_your_app) - Enable people to launch another app's App Clip from your app with App Clip links and offer a rich preview of it with the Link Presentation framework.
- **APActivationPayload** - Information that's passed to an App Clip on launch.
- **NSAppClip** - A collection of keys that an App Clip uses to get additional capabilities.

### App Clip Codes
- [Creating App Clip Codes](https://developer.apple.com/documentation/app_clips/creating_app_clip_codes) - Help users discover your App Clip by using an NFC-integrated or scan-only App Clip Code.
- [Encoding a URL in an App Clip Code](https://developer.apple.com/documentation/app_clips/encoding_a_url_in_an_app_clip_code) - Choose an invocation URL for your App Clip Code that you can encode efficiently.
- [Preparing multiple App Clip Codes for production](https://developer.apple.com/documentation/app_clips/preparing_multiple_app_clip_codes_for_production) - Prepare your App Clip Codes to send to a professional printing service.
- [Interacting with App Clip Codes in AR](https://developer.apple.com/documentation/app_clips/interacting_with_app_clip_codes_in_ar) - Display content and provide services in an AR experience with App Clip Codes.

### App Clip to full app transition
- [Recommending your app to App Clip users](https://developer.apple.com/documentation/app_clips/recommending_your_app_to_app_clip_users) - Display an overlay in your App Clip to recommend your app to users.
- [Sharing data between your App Clip and your full app](https://developer.apple.com/documentation/app_clips/sharing_data_between_your_app_clip_and_your_full_app) - Use CloudKit, Sign in with Apple, shared user defaults or containers, and the keychain to offer a smooth transition from your App Clip to your app.

### Notifications
- [Enabling notifications in App Clips](https://developer.apple.com/documentation/app_clips/enabling_notifications_in_app_clips) - Enable your App Clip to schedule and receive notifications for a short or extended time period.

### Live Activities
- [Offering Live Activities with your App Clip](https://developer.apple.com/documentation/app_clips/offering_live_activities_with_your_app_clip) - Add a widget extension to your App Clip target and use ActivityKit to display Live Activities on the Lock Screen and in the Dynamic Island.

### Testing
- [Testing the launch experience of your App Clip](https://developer.apple.com/documentation/app_clips/testing_the_launch_experience_of_your_app_clip) - Debug App Clip invocations, test the launch experience, and verify the configuration of your released App Clip.

### Distribution
- [Distributing your App Clip](https://developer.apple.com/documentation/app_clips/distributing_your_app_clip) - Archive the full app for your App Clip, upload it to App Store Connect, and distribute it to testers or publish it on the App Store.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppClip)*
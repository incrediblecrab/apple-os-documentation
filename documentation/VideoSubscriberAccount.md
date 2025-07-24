# Video Subscriber Account

Support TV provider and Apple TV app functionality.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | macOS 10.14+ | tvOS 10.0+ | visionOS 1.0+

## Overview

VideoSubscriberAccount provides APIs to help you create apps that require secure communication with a TV provider's authentication service. The framework also informs the Apple TV app about whether someone has a subscription and the details of that subscription.

## Topics

### Essentials
- [Video Subscriber Account updates](https://developer.apple.com/documentation/videosubscriberaccount/video_subscriber_account_updates) - Learn about important changes in Video Subscriber Account.

### TV provider authentication
- **VSAccountManager** - The object that coordinates your app's authentication requests with a TV provider's authentication service.

### TV app integration
- **VSAppleSubscription** - An Apple streaming service customer and their subscriptions.
- **VSSubscriptionRegistrationCenter** - An object that stores subscription information that the system provides to the Apple TV app.
- **VSAccountApplicationProvider** - An object to display app-specific providers in your app.

### User account management
- [Signing people in to their media accounts automatically](https://developer.apple.com/documentation/videosubscriberaccount/signing_people_in_to_their_media_accounts_automatically) - Implement single sign-on for media-streaming apps by managing a sign-in token on a person's Apple Account.
- **VSUserAccountManager** - The object that coordinates your app's user account actions.
- **VSUserAccount** - An object that represents a user's account.

### Errors
- **VSErrorDomain** - The domain for all errors in the framework.
- **VSErrorInfoKeySAMLResponse** - The subscription provider's SAML error response.
- **VSErrorInfoKeySAMLResponseStatus** - The subscription provider's SAML error-response status code.
- **VSErrorInfoKeyAccountProviderResponse** - The account provider's error-response object.
- **VSErrorInfoKeyUnsupportedProviderIdentifier** - The identifier of the unsupported subscription provider.
- **VSError** - Error information in the framework error domain.
- **VSError.Code** - Error codes in the framework error domain.

### Deprecated
- **VSSubscription** - An object that describes a subscriber's access to content. (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/VideoSubscriberAccount)*
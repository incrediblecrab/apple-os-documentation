# AdAttributionKit

Present, process, and register postbacks for in-app ads in the App Store and alternative app marketplaces.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 17.4+

## Overview

AdAttributionKit helps advertisers measure the success of ad campaigns while helping maintain user privacy.

The API involves three participants:

- Ad networks that sign ads and receive postbacks after ads result in conversions
- Publisher apps that display ads from the ad networks
- Advertised apps that update conversion values as people engage with the app

Ad networks register with Apple to get an ad network ID and to use the API. Developers configure their apps to accept attributable ads from ad networks and receive copies of winning postbacks. For information about setup, see Registering an ad network, Configuring a publisher app, and Configuring an advertised app.

### Ad Attribution Flow

Below is the path of an ad impression that wins ad attribution. The ad network serves an ad that an app displays. A person taps the ad and downloads or reengages with the advertised app.

Apple determines a postback data tier for the conversion, and the device uses the tier later to determine the level of detail the postback can contain to help ensure crowd anonymity. For more information about the postback contents and the data tiers, see Receiving postbacks in multiple conversion windows.

If a person launches the app within an attribution time-window, the ad impression is eligible for postbacks. As that person engages with the app, the app updates the conversion value. The system provides three conversion windows if the ad network meets the criteria for conversion. The system sends the postbacks to the ad network, and to the app's developer if they opt in to receive postbacks.

Devices send postbacks to multiple ad networks that sign their ads.

- One ad network receives postbacks, as part of multiple conversion windows, with a did-win parameter value of true for the ad impression that wins the ad attribution.
- For install conversions, up to five other ad networks receive a postback with a did-win parameter value of false if their ad impressions qualify for the attribution, but don't win.
- For reengagement conversions, a single ad network may receive winning postbacks in multiple conversion windows. The framework doesn't generate runner-up postbacks for reengagements.

For more information about receiving ad attributions, including time-window details, information about install and reengagement conversions, and other constraints, see Receiving ad attributions and postbacks. The information in the postback that Apple cryptographically signs doesn't include user- or device-specific data. It can include values from the ad network and the advertised app if providing those values meets the privacy threshold that Apple sets. For more information about postback values and postback data tiers, see Receiving postbacks in multiple conversion windows. For more information about the contents of postbacks, see Verifying a postback.

### Present ads, update conversion values, and receive attribution

Each participant has specific responsibilities when using the APIs to present ads and receive attribution.

**The ad network's responsibilities are to:**
- Register and provide its ad network identifier to developers. See Registering an ad network.
- Serve signed ads to the publisher app. See Presenting ads in your app.
- Receive postbacks at the URL it establishes during registration.
- Verify the postbacks. See Verifying a postback.

**The publisher app's responsibilities are to:**
- Add the ad network identifiers to its Info.plist file. See Configuring a publisher app.
- Display ads that the ad network signs. See Presenting ads in your app.

**The advertised app's responsibilities are to:**
- Register a conversion by updating the conversion value when a person first launches the app by calling one of the conversion updating methods, such as updateConversionValue(_:lockPostback:).
- Optionally, continue to update the conversion value as the person engages with the app by calling one of the conversion updating methods, such as updateConversionValue(_:coarseConversionValue:lockPostback:).
- Optionally, specify a server URL in its Info.plist file to receive a copy of the winning postback. See Configuring an advertised app.

Apple designs ad attribution APIs to help maintain user privacy. Apps don't need to use App Tracking Transparency before calling ad attribution APIs, and can call these APIs regardless of their tracking authorization status. For more information about privacy, see User privacy and data use.

## Topics

### Essentials
- [Understanding AdAttributionKit and SKAdNetwork interoperability](https://developer.apple.com/documentation/adattributionkit/understanding_adattributionkit_and_skadnetwork_interoperability) - Learn how attribution APIs interact to deliver ad impressions.
- [Presenting ads in your app](https://developer.apple.com/documentation/adattributionkit/presenting_ads_in_your_app) - Render different ad styles in your app.
- [Receiving ad attributions and postbacks](https://developer.apple.com/documentation/adattributionkit/receiving_ad_attributions_and_postbacks) - Understand timeframes and priorities for ad impressions that result in ad attributions, and how impressions qualify for postbacks.
- [Identifying conversion values with conversion tags](https://developer.apple.com/documentation/adattributionkit/identifying_conversion_values_with_conversion_tags) - Use conversion tags to identify and update specific postbacks when you have overlapping conversion windows.

### Ad network registration and configuration
- [Registering an ad network](https://developer.apple.com/documentation/adattributionkit/registering_an_ad_network) - Use the AdAttributionKit APIs for your ad campaigns after registering your ad network with Apple.
- [Configuring a publisher app](https://developer.apple.com/documentation/adattributionkit/configuring_a_publisher_app) - Set up a publisher app to participate in ad campaigns.
- [Configuring an advertised app](https://developer.apple.com/documentation/adattributionkit/configuring_an_advertised_app) - Prepare an advertised app to participate in ad campaigns.
- [Configuring attribution rules for your app](https://developer.apple.com/documentation/adattributionkit/configuring_attribution_rules_for_your_app) - Tune aspects of attribution flow, including the time available to register impressions and the minimum time your app is willing to accept conversions.

### Ad attribution testing
- [Testing ad attributions with Developer Mode](https://developer.apple.com/documentation/adattributionkit/testing_ad_attributions_with_developer_mode) - Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.
- [Creating postbacks in developer settings](https://developer.apple.com/documentation/adattributionkit/creating_postbacks_in_developer_settings) - Test development postbacks for your advertised app without interacting with ads from a publisher app.
- [Testing ad attributions with a downloaded profile](https://developer.apple.com/documentation/adattributionkit/testing_ad_attributions_with_a_downloaded_profile) - Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.

### Signatures
- [Generating JWS impressions](https://developer.apple.com/documentation/adattributionkit/generating_jws_impressions) - Create a JSON Web Signature (JWS) for use with app impressions in AdAttributionKit.

### App impressions
- **AppImpression** - A structure that represents an attributable impression the developer generates in response to a person's interaction with an ad in an app.

### Postbacks
- **Postback** - A structure that provides methods you use to update conversion values for ad attributions.
- **PostbackUpdate** - Values you use to update properties in a postback, such as the conversion value.
- **CoarseConversionValue** - Values that describe developer-defined, relative-attribution conversion values.

### Postback verification and parameter identification
- [Verifying a postback](https://developer.apple.com/documentation/adattributionkit/verifying_a_postback) - Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.
- [Identifying the parameters in a postback](https://developer.apple.com/documentation/adattributionkit/identifying_the_parameters_in_a_postback) - Interpret postback properties to understand the attribution report.

### Errors
- **AdAttributionKitError** - Values that describe ad attribution error conditions.

### Articles
- [Receiving postbacks in multiple conversion windows](https://developer.apple.com/documentation/adattributionkit/receiving_postbacks_in_multiple_conversion_windows) - Learn about the data that postbacks can contain in each conversion window.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdAttributionKit)*
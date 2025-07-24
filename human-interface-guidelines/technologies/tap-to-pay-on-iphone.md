# Tap to Pay on iPhone

Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware.

**Platforms:** iOS

## Overview

When you support Tap to Pay on iPhone in your iOS payment app, you help merchants present a consistent and trusted payment experience to their customers.

**Note:** Tap to Pay on iPhone works alongside your existing payment-acceptance hardware and accessories.

Before you can integrate Tap to Pay on iPhone into your iOS app, you need to work with a supported payment service provider (PSP), request the Tap to Pay on iPhone entitlement, and use ProximityReader APIs, either through the PSP's SDK or by adopting the framework. For high-level guidance — including marketing recommendations for letting people know about your app's new capabilities — see Tap to Pay on iPhone; for developer guidance, see Setting up Tap to Pay on iPhone.

## Topics

### Best Practices

**Enabling Tap to Pay on iPhone**

- **Help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with their customers** - Merchants must accept the terms and conditions before you perform the initial device configuration, so it works well when they can do so before they begin a checkout or other customer-facing flow.
- **Present Tap to Pay on iPhone terms and conditions only to an administrative user** - If a nonadministrator tries to activate the feature, present a message explaining that administrator access is required.
- **If necessary, help merchants make sure their device is up to date** - If your PSP requires specific versions of iOS, be sure to present the terms and conditions only after the merchant updates their device.

**Educating Merchants**

- **Provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone** - You can offer this tutorial in your in-app messaging, after merchants accept terms and conditions, to new users, or in help content.
- **Use Apple-approved assets or the ProximityReaderDiscovery API** - You can build your tutorial using Apple-approved assets from the Tap to Pay on iPhone marketing guidelines, or use the API to provide a pre-built merchant education experience.
- **Make sure your tutorial shows how to launch checkout flows, help customers position their payment methods, handle PIN entry, and provide opportunities to accept terms and conditions** - Cover all essential aspects of the payment flow.

**Checking Out**

- **Provide Tap to Pay on iPhone as a checkout option whether the feature is enabled or not** - Including a Tap to Pay on iPhone button gives merchants flexibility to use the feature without exiting the checkout flow.
- **Avoid making merchants wait to use Tap to Pay on iPhone** - Prepare the feature as soon as your app starts and immediately after each transition to the foreground to minimize potential wait times.
- **Make the checkout option available even if configuration is continuing in the background** - Display a progress indicator during configuration, but let merchants select the checkout option immediately.
- **Make the Tap to Pay on iPhone button easy to find** - Avoid making merchants scroll to access the feature. If your app doesn't support other payment acceptance options, open Tap to Pay on iPhone automatically when checkout begins.
- **Use "Tap to Pay on iPhone" or "Tap to Pay" for button labels** - If Tap to Pay on iPhone is the only payment-acceptance method you support, you can reuse existing Charge or Checkout buttons.
- **Design your button to match other buttons in your app** - Use the button color and shape that coordinate best with your interface, while using the required labels.
- **Determine the final amount before initiating the Tap to Pay on iPhone experience** - Make sure merchants offer interactions that can affect the total before displaying the Tap to Pay on iPhone screen.

**Displaying Results**

- **Start processing a transaction as soon as possible** - The system provides API you can use to request the result of a successful tap before the Tap to Pay on iPhone screen finishes displaying the checkmark animation.
- **Display a progress indicator while payment is authorizing** - Transaction authorization can take several seconds to complete, depending on factors like connectivity.
- **Clearly display the result of a transaction, whether it's declined or successful** - Also give merchants ways to offer customers digital receipts, such as through QR codes or text messages.
- **Help merchants complete the checkout flow when a payment can't complete** - Present options for alternate payment forms, different methods, or relaunching Tap to Pay on iPhone if customers have another card.
- **Display clear descriptions and appropriate resolutions for system errors** - For example, if the device's iOS version doesn't support Tap to Pay on iPhone, recommend updating to the latest version.
- **Make it easy for merchants to get help with issues they can't resolve** - Direct merchants to help content in your app or website, and provide actions to contact your support team.

### Additional Interactions

- **Use generic labels for buttons that read payment cards without transaction amounts** - Don't include "Tap to Pay on iPhone" or "Tap to Pay" in such labels; instead, use generic labels like "Look Up," "Store Card," "Verify," or "Refund."
- **Distinguish loyalty card transactions from payment-acceptance flows** - Give merchants separate, clearly labeled buttons to initiate loyalty card transactions, avoiding payment-related terms in the labels.

### Platform Considerations

**iOS**  
Tap to Pay on iPhone is available only on supported iPhone models with iOS versions that meet PSP requirements.

Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) - Apple Pay integration
- [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc) - Near Field Communication

### Developer Documentation

- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding_support_for_tap_to_pay_on_iphone_to_your_app) - ProximityReader
- [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting_up_tap_to_pay_on_iphone) - Implementation guidance

### Related Resources

- [Tap to Pay on iPhone Marketing guidelines](https://developer.apple.com/tap-to-pay-on-iphone/marketing-guidelines/) - Marketing resources

## Changelog

### January 17, 2024
- Updated merchant education guidance

### May 7, 2024
- Updated to include guidance on enabling the feature and educating merchants

### March 3, 2023
- Enhanced guidance for educating merchants and improving their experience

### September 14, 2022
- Refined guidance on preparing Tap to Pay on iPhone and helping merchants learn how to use the feature

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone)*
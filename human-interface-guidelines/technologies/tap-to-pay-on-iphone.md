# Tap to Pay on iPhone

Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware.

**Platforms:** iOS

## Overview

When you support Tap to Pay on iPhone in your iOS payment app, you help merchants present a consistent and trusted payment experience to their customers.

**Note:** Tap to Pay on iPhone works alongside your existing payment-acceptance hardware and accessories.

Integration requires a supported payment service provider (PSP), an approved Tap to Pay on iPhone entitlement, and ProximityReader integration, directly or through the PSP's SDK. Confirm [supported regions and PSPs](https://developer.apple.com/tap-to-pay/#regions), compatible hardware, and the provider's OS requirements. TestFlight and App Store distribution require distribution entitlement approval, not just a development entitlement. See [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone), and follow your PSP's documentation when its SDK supplies the payment UI.

## Topics

### Best Practices

#### Enabling Tap to Pay on iPhone

Check the merchant's current account-link status and present terms acceptance only when needed. Acceptance is associated with the merchant identifier, not something every employee must repeat on every device.

- **Help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with their customers** - Merchants must accept the terms and conditions before you perform the initial device configuration, so it works well when they can do so before they begin a checkout or other customer-facing flow.
- **Present Tap to Pay on iPhone terms and conditions only to an administrative user** - If a nonadministrator tries to activate the feature, explain that an administrator must complete acceptance. With PSP support, that administrator can use a separate app or web flow, including on a device other than iPhone.
- **If necessary, help merchants make sure their device is up to date** - If your PSP requires specific versions of iOS, be sure to present the terms and conditions only after the merchant updates their device.

#### Educating Merchants

- **Provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone** - You can offer this tutorial in your in-app messaging, after merchants accept terms and conditions, to new users, or in help content.
- **Use Apple-approved assets or the ProximityReaderDiscovery API** - Follow the marketing guidelines' asset-use requirements, or use [ProximityReaderDiscovery](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery) for system-provided education on supported versions. This API starts in iOS 18; don't assume every OS capable of payment acceptance includes it.
- **Teach the complete interaction** - Cover checkout, positioning a contactless card or wallet, and required PIN entry including accessibility mode. At the end, offer terms acceptance to eligible merchants who haven't completed it.

#### Checking Out

- **Offer checkout access before setup finishes on eligible devices** - Merchants shouldn't have to leave checkout to enable the feature. Handle necessary administrator acceptance and configuration before opening the reader; this isn't an instruction to offer an unusable option on unsupported hardware or in unsupported regions.
- **Avoid unnecessary preparation delays** - Once prerequisites are satisfied, prepare the reader at launch and on each return to the foreground. A reader session ends when the app goes into the background; discard that session and prepare again. Preparation doesn't replace merchant acceptance or PSP authorization.
- **Keep checkout selectable while configuration continues** - After selection, show progress until the reader is ready. Use determinate progress when the framework reports update progress, and indeterminate progress when no useful completion fraction is available.
- **Make the Tap to Pay on iPhone button easy to find** - Avoid making merchants scroll to access the feature. If your app doesn't support other payment acceptance options, open Tap to Pay on iPhone automatically when checkout begins.
- **Use "Tap to Pay on iPhone," shortened to "Tap to Pay" when space is constrained** - If this is the only payment-acceptance method, existing Charge or Checkout buttons can activate it. If your payment-method buttons use icons, the HIG specifies `wave.3.right.circle` or `wave.3.right.circle.fill`; don't use the Apple logo.
- **Design your button to match other buttons in your app** - Use the button color and shape that coordinate best with your interface, while using the required labels.
- **Determine the final amount before initiating the Tap to Pay on iPhone experience** - Make sure merchants offer interactions that can affect the total before displaying the Tap to Pay on iPhone screen.

#### Displaying Results

A successful tap and system checkmark mean the reader obtained payment information, not that the financial transaction is authorized. Send the encrypted result to your PSP for processing, then communicate its authorization outcome separately.

- **Start processing promptly** - [returnReadResultImmediately](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/returnreadresultimmediately) can return card-read data before the system UI closes. It defaults to false and is available from iOS 16.4. Early data delivery isn't early payment approval.
- **Display a progress indicator while payment is authorizing** - Transaction authorization can take several seconds to complete, depending on factors like connectivity.
- **Clearly display the result of a transaction, whether it's declined or successful** - Also give merchants ways to offer customers digital receipts, such as through QR codes or text messages.
- **Help merchants complete the checkout flow when a payment can't complete** - Present options for alternate payment forms, different methods, or relaunching Tap to Pay on iPhone if customers have another card.
- **Match error recovery to the actual cause** - Recommend an OS update for a resolvable version requirement, but don't imply that updating can fix an unsupported device model or region. Follow PSP guidance for issues such as additional authentication, PIN fallback, or alternate payment methods.
- **Make it easy for merchants to get help with issues they can't resolve** - Direct merchants to help content in your app or website, and provide actions to contact your support team.

### Additional Interactions

- **Use generic labels for buttons that read payment cards without transaction amounts** - Don't include "Tap to Pay on iPhone" or "Tap to Pay" in such labels; instead, use generic labels like "Look Up," "Store Card," "Verify," or "Refund."
- **Distinguish loyalty card transactions from payment-acceptance flows** - Give merchants separate, clearly labeled buttons to initiate loyalty card transactions, avoiding payment-related terms in the labels.

### Platform Considerations

**iOS**  
Tap to Pay on iPhone requires a supported iPhone, starting with iPhone XS, and an OS version accepted for the region and PSP. `PaymentCardReader.isSupported` checks the device model, not the OS version; passing that check alone doesn't establish eligibility.

The physical card-reading experience is an iPhone feature. Some API types exist for other SDK targets, and a separate administrator terms-acceptance flow can run elsewhere with PSP support; neither makes those devices Tap to Pay readers.

### Related Components

- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) - Apple Pay integration
- [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc) - Near Field Communication

### Developer Documentation

- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) - ProximityReader
- [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone) - Implementation guidance
- [PaymentCardReader.prepare(using:)](https://developer.apple.com/documentation/proximityreader/paymentcardreader/prepare(using:)) - Reader configuration and foreground session lifecycle
- [PaymentCardReader.isSupported](https://developer.apple.com/documentation/proximityreader/paymentcardreader/issupported) - Hardware-only support check
- [PaymentCardReader.Event.updateProgress(_:)](https://developer.apple.com/documentation/proximityreader/paymentcardreader/event/updateprogress(_:)) - Configuration progress

### Related Resources

- [Tap to Pay on iPhone Marketing guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/) - Marketing resources

## Changelog

These are Apple's displayed HIG change-log entries. There is a source-year discrepancy: the article's update metadata dates the merchant-education alert January 17, 2025, while its change-log row below says January 17, 2024. Neither field is presented here as an independently established API release date.

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

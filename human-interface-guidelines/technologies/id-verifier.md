# ID Verifier

ID Verifier lets your iPhone app read mobile IDs in person without requiring external hardware.

**Platforms:** iOS

## Overview

Beginning in iOS 17, you can integrate ID Verifier into your app, letting a compatible iPhone read ISO 18013-5 compliant mobile IDs for in-person verification. For example, personnel at a concert venue can use your app to verify customers' ages. Check `MobileDocumentReader.isSupported`, enable the Verifier API capability, and confirm the current region and credential requirements; an OS version alone doesn't establish support.

Using ID Verifier has advantages for both customers and organizations.

- Customers can approve sharing just the necessary age or identity information without handing over a physical ID card. Design each request to minimize disclosure.
- Apple provides the key components of the certificate issuance, management, and validation process, simplifying app development and enabling a consistent and trusted ID verification experience.

Depending on the needs of your app, you can use ID Verifier to make the following types of requests:

**Display Only request** - Display requested information, such as a name or age and portrait, in system UI for visual inspection. The app doesn't read or store those personal ID fields. It can receive a validation or configured confirmation outcome, which is different from receiving the underlying identity data. For developer guidance, see [MobileDriversLicenseDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest).

**Data Transfer request** - Use this separately entitled capability only for an approved legal verification need that requires processing or retaining identity fields. Apple's eligibility conditions include an equivalent verification process for the same in-person goods or services, and a legal requirement that Display Only or Verify with Wallet can't satisfy. Entitlement approval is per bundle ID, not a blanket authorization for every app from an organization. See [Get started with ID Verifier](https://developer.apple.com/wallet/id-verifier/) for the current requirements and application process.

> **Online age assurance is separate from in-person ID verification.** [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) **1.2.1(a)** applies to creator apps; **4.7.5** applies to software offered under section 4.7. These clauses require identifying content or software above the app's age rating and restricting underage access using verified or declared age. They don't by themselves require government-ID collection or ID Verifier. The separate [Declared Age Range framework](https://developer.apple.com/documentation/declaredagerange) shares an age range and declaration information. For children in a Family Sharing group, a parent, guardian, or Family Organizer can configure whether and how that age information is shared.

## Topics

### Best Practices

- **Ask only for the data you need** - People may lose trust in the experience if you ask for more data than you need to complete the current verification. For example, if you need to ensure that a customer is at least a minimum age, use a request that specifies an age threshold; avoid requesting the customer's current age or birth date.
- **Identify your organization in the verification experience** - If eligible, register for ID Verifier with Apple Business Register and configure a reader token for your organization. The token supplied when preparing the reader lets the system show your organization's name and logo; registration alone doesn't configure the app's reader session.
- **Provide a button that initiates the verification process** - Use a label like Verify Age in a button that performs a simple age check or Verify Identity for a more detailed identity data request. Avoid including a symbol that specifies a particular type of communication, like NFC or QR codes. Never include the Apple logo in any button label.
- **In a Display Only request, help the person using your app provide feedback on the visual confirmation they perform** - For example, when the reader displays the customer's portrait, you might provide buttons labeled Matches Person and Doesn't Match Person so your app can receive an approved or rejected value as part of the response.

### Button Types

| Button type | Example usage |
|-------------|---------------|
| Verify Age | An app that checks whether people are old enough to attend an event or access a venue, like a concert hall. |
| Verify Identity | An app that verifies whether specific identity information matches expected values, such as name and birth date when picking up a rental car. |

### Platform Considerations

No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Apple Business Register — ID Verifier registration](https://register.apple.com/services/login?returnTo=/signin/tap-to-present-id-on-iphone)
- [IDs in Wallet](https://learn.wallet.apple/id)
- [Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet)

### Developer Documentation

- [Adopting the Verifier API in your iPhone app — ProximityReader](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) - ProximityReader
- [MobileDriversLicenseDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest) - ProximityReader
- [MobileDriversLicenseDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest) - ProximityReader
- [MobileDriversLicenseRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest) - Raw response data for processing
- [ageAtLeast(_:)](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/element/ageatleast(_:)) - ProximityReader

## Changelog

These dates describe Apple's HIG article history.

### September 12, 2023
- New page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/id-verifier)*

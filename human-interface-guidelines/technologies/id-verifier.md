# ID Verifier

ID Verifier lets your iPhone app read mobile IDs in person without requiring external hardware.

**Platforms:** iOS

## Overview

Beginning in iOS 17, you can integrate ID Verifier into your app, letting iPhone read ISO18013-5 compliant mobile IDs and helping you support in-person ID verification. For example, personnel at a concert venue can use your app on iPhone to verify customers' ages.

Using ID Verifier has advantages for both customers and organizations.

- Customers only present the minimum data needed to prove their age or identity, without handing over their ID card or showing their device.
- Apple provides the key components of the certificate issuance, management, and validation process, simplifying app development and enabling a consistent and trusted ID verification experience.

Depending on the needs of your app, you can use ID Verifier to make the following types of requests:

**Display Only request** - Use a Display Only request to display data — such as a person's name or age alongside their photo portrait — within system-provided UI on the requester's iPhone, so the requester can visually confirm the person's identity. When you make a Display Only request, the customer's data remains within the system-provided UI and isn't transmitted to your app. For developer guidance, see MobileDriversLicenseDisplayRequest.

**Data Transfer request** - Use a Data Transfer request only when you have a legal verification requirement and you need to store or process information like a person's address or date of birth. You must request an additional entitlement to make a Data Transfer request. To learn more, see Get started with ID Verifier; for developer guidance, see MobileDriversLicenseDataRequest and MobileDriversLicenseRawDataRequest.

## Topics

### Best Practices

- **Ask only for the data you need** - People may lose trust in the experience if you ask for more data than you need to complete the current verification. For example, if you need to ensure that a customer is at least a minimum age, use a request that specifies an age threshold; avoid requesting the customer's current age or birth date.
- **If your app qualifies for Apple Business Register, register for ID Verifier to ensure that people can view essential information about your organization when you make a request** - Registering for ID Verifier with Apple Business Register lets you provide your official organization name and logo for the system to display on customers' devices as part of the ID verification UI.
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

- [Apple Business Register](https://developer.apple.com/documentation/proximityreader/apple-business-register)
- [IDs in Wallet](https://developer.apple.com/design/human-interface-guidelines/ids-in-wallet)
- [Identity verification](https://developer.apple.com/design/human-interface-guidelines/identity-verification)

### Developer Documentation

- [Adopting the Verifier API in your iPhone app — ProximityReader](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) - ProximityReader
- [MobileDriversLicenseDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest) - ProximityReader
- [MobileDriversLicenseDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest) - ProximityReader
- [ageAtLeast(_:)](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserequest/ageatleast(_:)) - ProximityReader

## Changelog

### September 12, 2023
- New page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/id-verifier)*
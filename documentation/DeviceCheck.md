# DeviceCheck

Reduce fraudulent use of your services by managing device state and asserting app integrity.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 11.0+ | macOS 10.15+ | tvOS 11.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

The DeviceCheck services consist of both a framework interface that you access from your app and an Apple server interface that you access from your own server.

Using the DCDevice class in your app, you can get a token that you use on your server to set and query two binary digits of data per device, while maintaining user privacy. For example, you might use this data to identify devices that have already taken advantage of a promotional offer that you provide, or to flag a device that you've determined to be fraudulent. The server-to-server APIs also let you verify that the token you receive comes from your app on an Apple device.

Someone who modifies your app and distributes it outside the App Store can add unauthorized features like game cheats, ad removal, or access to premium content. The App Attest service gives your app a way to assert its validity so that your server can more confidently provide access to sensitive resources. You use the DCAppAttestService class to generate a special cryptographic key on the device, and have Apple attest to the validity of that key. You then use that key to assert the validity of your app whenever you request sensitive data from your server.

No single policy can eliminate all fraud. For example, App Attest can't definitively pinpoint a device with a compromised operating system. Instead, the DeviceCheck services provide information that you can integrate into an overall risk assessment for a given device.

## Topics

### Device Identification
- [Accessing and modifying per-device data](https://developer.apple.com/documentation/devicecheck/accessing_and_modifying_per-device_data) - Use a token from your app to query and modify two per-device binary digits stored on an Apple server.
- **DCDevice** - A representation of a device that provides a unique, authenticated token.

### App Attest
- [Establishing your app's integrity](https://developer.apple.com/documentation/devicecheck/establishing_your_app_s_integrity) - Ensure that requests your server receives come from legitimate instances of your app.
- [Validating apps that connect to your server](https://developer.apple.com/documentation/devicecheck/validating_apps_that_connect_to_your_server) - Verify that connections to your server come from legitimate instances of your app.
- [Assessing fraud risk](https://developer.apple.com/documentation/devicecheck/assessing_fraud_risk) - Request and analyze risk data using server-to-server calls.
- [Preparing to use the app attest service](https://developer.apple.com/documentation/devicecheck/preparing_to_use_the_app_attest_service) - Test your implementation in a development environment and onboard users gradually.
- **DCAppAttestService** - A service that you use to validate the instance of your app running on a device.
- **App Attest Environment** - The environment for an app that uses the App Attest service to validate itself.

### Errors
- **DCError** - A type that indicates when DeviceCheck encounters an error.
- **Code** - DeviceCheck error codes.
- **DCErrorDomain** - The error domain for errors associated with DeviceCheck APIs.

### Articles
- [Attestation Object Validation Guide](https://developer.apple.com/documentation/devicecheck/attestation_object_validation_guide) - Use this guide to validate your implementation of verifying the attestation object verification process.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceCheck)*
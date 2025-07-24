# Apple Pay on the Web

Support Apple Pay on your website with JavaScript-based APIs.

**Platforms:** Safari Desktop 10.0+ | Safari Mobile 10.0+

## Overview

Safari supports two JavaScript APIs that let you accept Apple Pay payments from customers on your website:

- Payment Request API, a W3C candidate API
- Apple Pay JS API, analogous to the PassKit (Apple Pay and Wallet) framework for Apple Pay in apps.

Tip: You can try out Apple Pay transactions on the demo page. See Apple Pay on the Web Interactive Demo.

Apple Pay is available on all iOS devices with a Secure Element — an industry-standard, certified chip designed to store payment information safely. In macOS, users must have an Apple Pay-capable iPhone or Apple Watch to authorize the payment, or a Mac with Touch ID.

### Apple Pay availability by region and platform

Apple Pay is available in supported regions.

The Apple Pay APIs are available in Safari on the following platforms:

| API | Worldwide (except China) | China |
|-----|-------------------------|--------|
| Apple Pay JS | iOS 10 and later<br>macOS 10.12 and later | iOS 11.2 and later<br>(Not available in macOS) |
| Payment Request API | iOS 11.3 and later<br>macOS 10.12.6 and later, in Safari 11.1 and later | iOS 11.3 and later<br>(Not available in macOS) |

In iOS, Safari and SFSafariViewController objects support Apple Pay.

See Checking for Apple Pay availability to ensure your implementation only displays the Apple Pay button on supported devices.

Note: Regulations in some regions may require specific configurations in your implementation. For more information, see Complying with regional regulations.

### Apple Pay requirements

The requirements for using Apple Pay on your website are:

- Your website must comply with the Apple Pay guidelines. For more information, see Acceptable Use Guidelines for Apple Pay on the Web.
- You must have an Apple Developer Account and complete the registration. For more information, see Configuring Your Environment.
- All pages that include Apple Pay must be served over HTTPS. For more information, see Setting Up Your Server.

For design guidance, see Human Interface Guidelines > Apple Pay.

## Topics

### Essentials
- [Loading the latest version of the Apple Pay JS SDK](https://developer.apple.com/documentation/ApplePayontheWeb/loading_the_latest_version_of_the_apple_pay_js_sdk) - Link to the most recent autoupdating version of the Apple Pay JS SDK or a version of your choice.

### Apple Pay setup
- [Setting Up Your Server](https://developer.apple.com/documentation/ApplePayontheWeb/setting_up_your_server) - Set up your server for secure communications with Apple Pay.
- [Configuring Your Environment](https://developer.apple.com/documentation/ApplePayontheWeb/configuring_your_environment) - Create your Apple Pay merchant ID and certificates, and verify your domain.
- [Maintaining Your Environment](https://developer.apple.com/documentation/ApplePayontheWeb/maintaining_your_environment) - Prevent interruptions in your Apple Pay service by keeping certificates and domain verification current.

### Apple Pay Later visual merchandising widget
- [Adding an Apple Pay Later visual merchandising widget](https://developer.apple.com/documentation/ApplePayontheWeb/adding_an_apple_pay_later_visual_merchandising_widget) - Configure and style Apple Pay Later visual merchandising widgets to match your website.

### Apple order tracking button
- [Adding a Track with Apple Wallet button](https://developer.apple.com/documentation/ApplePayontheWeb/adding_a_track_with_apple_wallet_button) - Configure and style an Apple Wallet Button to match your website.

### Apple Pay buttons
- [Displaying Apple Pay Buttons Using JavaScript](https://developer.apple.com/documentation/ApplePayontheWeb/displaying_apple_pay_buttons_using_javascript) - Load and configure the JavaScript Apple Pay button.
- **ApplePayButton** - An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [Displaying Apple Pay Buttons Using CSS](https://developer.apple.com/documentation/ApplePayontheWeb/displaying_apple_pay_buttons_using_css) - Use CSS templates to display Apple Pay buttons in Safari.

### Apple Pay JavaScript APIs
- [Choosing an API for Implementing Apple Pay on Your Website](https://developer.apple.com/documentation/ApplePayontheWeb/choosing_an_api_for_implementing_apple_pay_on_your_website) - Compare Apple Pay JS and Payment Request API to choose the right implementation for your website.
- [Apple Pay on the Web version history](https://developer.apple.com/documentation/ApplePayontheWeb/apple_pay_on_the_web_version_history) - Learn about features in each version of Apple Pay on the Web.
- **Apple Pay JS API** - Implement Apple Pay on the web using Apple's JavaScript API.
- **Payment Request API** - Accept payments on your website with Apple Pay using the Payment Request API.

### Apple Pay JS SDK change log
- [Apple Pay JS change log](https://developer.apple.com/documentation/ApplePayontheWeb/apple_pay_js_change_log) - Learn about new features and updates in the Apple Pay JS SDK.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ApplePayontheWeb)*
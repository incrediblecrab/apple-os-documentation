# Apple Pay

Apple Pay is a secure, easy way to make payments for physical goods and services — as well as donations and subscriptions — in apps running on iPhone, iPad, Mac, and Apple Watch, and on websites.

**Platforms:** iOS | iPadOS | macOS | watchOS

## Overview

People authorize payments and provide shipping and contact information, using credentials that are securely stored on the device.

**Note:** It's important to understand the difference between Apple Pay and In-app purchase. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and tickets for events; and for donations. Use [In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase) in your app to sell virtual goods, such as premium content for your app, and subscriptions for digital content.

Apps that accept Apple Pay display an Apple Pay mark wherever available payment options are shown and an Apple Pay button that people tap to bring up a payment sheet. During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments and then authorize payment and complete the purchase.

Websites that accept Apple Pay incorporate it into the purchasing flow. An Apple Pay mark needs to be shown wherever available payment options are shown and an Apple Pay button lets people view a payment sheet. During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments, authorize payment, and complete the purchase using securely stored credentials on iPhone, iPad, and Macs that include Touch ID or a Magic Keyboard with Touch ID. On other Macs, people confirm the purchase with their nearby iPhone or Apple Watch on which Apple Pay is set up.

All websites that offer Apple Pay must include a privacy statement and adhere to the [Acceptable use guidelines for Apple Pay on the web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/). For a hands-on demo of Apple Pay on the web, see [Apple Pay on the web interactive demo](https://applepaydemo.apple.com/).

## Topics

### Best Practices

- **Offer Apple Pay on all supported devices** - If the device doesn't support Apple Pay, don't present Apple Pay as a payment option.

- **Make Apple Pay the primary payment option when possible** - If you use Apple Pay APIs to find out whether someone has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs.

- **Feature Apple Pay prominently** - If you also offer other payment methods, offer Apple Pay at the same time and feature it at least as prominently as other options on every page or screen that offers or accepts payment methods.

- **Use Apple-provided APIs for buttons** - If you use an Apple Pay button to start the Apple Pay payment process, you must use the Apple-provided API to display it. Unlike a button graphic, the buttons produced by the API always have the correct appearance and are localized automatically.

- **Don't misuse Apple Pay branding on custom buttons** - If you use a custom button to start the Apple Pay payment process, make sure your custom button doesn't display "Apple Pay" or the Apple Pay logo. In this scenario, you must let people know that you accept Apple Pay by displaying the Apple Pay mark or referencing Apple Pay in text on the same page.

- **Use Apple Pay buttons only for their intended purpose** - Use Apple Pay buttons only to start the Apple Pay payment process and, when appropriate, the Apple Pay set-up process. Don't use Apple Pay buttons in any other ways.

- **Don't hide Apple Pay buttons** - Don't hide an Apple Pay button or make it appear unavailable. If an Apple Pay button can't be used yet, such as when a product size or color hasn't been selected, gracefully point out the problem after someone taps or clicks the button.

- **Use the Apple Pay mark correctly** - Use the Apple Pay mark only to communicate that Apple Pay is accepted. The Apple Pay mark doesn't facilitate payment. Never use it as a payment button or position it as a button.

- **Optimize for search engines** - Inform search engines that Apple Pay is accepted on your website. If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.

- **Provide a cohesive checkout experience** - The entire checkout flow should feel tightly integrated with your app or website. Use your branding throughout the checkout experience and avoid opening different pages or windows.

- **Present Apple Pay as the preferred option** - If Apple Pay is available, assume the person wants to use it. Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.

- **Accelerate single-item purchases** - In addition to offering a shopping cart, consider putting Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated this way should be for an individual item only, excluding any items already in the shopping cart.

- **Offer express checkout for multiple items** - Consider providing an express checkout feature that immediately displays the payment sheet, allowing people to purchase multiple items quickly using a single shipping method and destination.

- **Collect necessary information before checkout** - Collect required information like color and size options before people reach the Apple Pay button. When additional information is needed at checkout time, gracefully point out the problem and help them correct it.

- **Collect optional information separately** - There's no way to input optional data like gift messages or delivery instructions on the payment sheet, so collect this information ahead of time or after the purchase is complete.

- **Handle complex shipping scenarios upfront** - If customers can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay checkout begins, not on the payment sheet.

- **Prepare pickup locations in advance** - For in-store pickup, help people choose a pickup location before displaying the payment sheet. Display the location's address in read-only format on the payment sheet.

- **Trust Apple Pay information** - Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout.

- **Avoid requiring account creation** - If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate registration fields using information from the payment sheet.

- **Report transaction results** - Report the result of the transaction so that people can view it in the payment sheet. In failure cases, the payment sheet can display the errors you provide.

- **Display order confirmation** - After the payment sheet shows the transaction result, display an order confirmation page to thank people for their purchase and provide shipping details.

- **Present only essential information** - People may get confused or have privacy concerns if the payment sheet includes extraneous information. Only request information that's relevant to the specific purchase.

- **Display active coupons and promotional codes** - If people can enter a code before the payment sheet appears, displaying it on the sheet can reassure them that the code works as expected. Alternatively, allowing code entry on the payment sheet can be particularly beneficial in an express checkout flow.

- **Provide clear shipping method options** - Show a clear description, cost, and optionally an estimated delivery or pickup date for each available option. Take advantage of the shipping method's calendar and time-zone support to provide accurate delivery information.

- **Offer pickup time windows** - For in-store pickup, consider letting people choose a pickup window that works for them using the shipping method to supply a range of dates and times.

- **Use line items effectively** - Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring, and future payments. Don't use line items to show an itemized list of products that make up the purchase.

- **Keep line items concise** - Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.

- **Provide clear business identification** - Provide a business name after the word "Pay" on the same line as the total. Use the same business name people will see when they look for the charge on their bank or credit card statement.

- **Clarify intermediary relationships** - If you're not the end merchant, specify both your business name and the end merchant's name in the payment sheet. Clearly describe the relationship, such as "Pay [End_Merchant_Business_Name (via Your_Business_Name)]".

- **Disclose variable costs** - Clearly disclose when additional costs may be incurred after payment authorization. When the total cost may be unknown at checkout time, provide a clear explanation and a subtotal marked as "Amount Pending".

- **Handle errors gracefully** - If an error occurs during checkout, help people resolve it quickly so they can complete their transaction.

### Website Icons

Websites that support Apple Pay can display an icon in the payment sheet of the connected device that's used to authorize payment. The icon provides visual reassurance that payment is going to the right place.

If your website supports Apple Pay, provide an icon in the following sizes:
- **@2x:** 60x60 pt (120x120 px @2x)
- **@3x:** 60x60 pt (180x180 px @3x)

### Error Handling

Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve problems quickly and complete their transaction.

Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the transaction. Use these opportunities to check for data entry problems and to provide clear and consistent messaging.

When data is invalid, system-provided error messaging calls attention to relevant fields on the payment sheet. People can choose a field to view additional details and resolve the problem. Provide customized error messages for the detail view that appears when people choose a problematic field.

**Note:** For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction. Prior to authorization, only the card type and a redacted shipping address are accessible. It's critical to display errors when authorization fails, but to the extent possible, you also need to attempt to validate available information and report problems before authorization.

- **Design intelligent validation** - Design a data validation process that's intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction.

- **Provide accurate status reporting** - When a problem occurs, it's essential that your app or website accurately indicate the type of problem so the system can show the most relevant error message on the payment sheet.

- **Use specific error messages** - Succinctly and specifically describe the problem when data is invalid or incorrectly formatted. Reference the relevant field and indicate exactly what's expected. For example, instead of showing "Address is invalid," show "Zip code doesn't match city."

**Payment Processing**

Handle interruptions correctly. A user-driven event like a cancellation or a system-driven event like a timeout could cause an interruption in the payment flow, resulting in the payment sheet being dismissed. When such an event occurs, you must cancel any in-progress payment.

### Subscriptions

Your app or website can use Apple Pay to request authorization for recurring fees. A recurring fee can be a fixed amount, such as a monthly movie ticket subscription, or — when local regulations allow — a variable amount like a weekly grocery order.

- **Clarify subscription details beforehand** - Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can reiterate the billing frequency on the payment sheet.

- **Include detailed line items** - Include line items that reiterate billing frequency, discounts, and additional upfront fees. Use these line items to remind people what they're authorizing.

- **Clarify current payment amounts** - Make sure people know the amount they're being billed at the time of authorization.

- **Only request authorization when necessary** - Only show the payment sheet when a subscription change results in additional fees. When someone changes a subscription, authorization isn't necessary if the cost decreases or remains the same.

### Donations

Approved nonprofits can use Apple Pay to accept donations.

- **Use clear donation line items** - Display a line item on the payment sheet that reminds people they're authorizing a donation; for example, display "Donation $50.00".

- **Offer predefined amounts** - You can reduce steps in the donation process by offering one-step recommended donations, like $25, $50, $100. Be sure to include an "Other Amount" option too, so people can customize the donation if they prefer.

### Apple Pay Buttons

The system provides several Apple Pay button types and styles you can use in your app or website. In contrast to the Apple Pay buttons, you use the Apple Pay mark to communicate the availability of Apple Pay as a payment option.

Don't create your own Apple Pay button design or attempt to mimic the system-provided button designs.

**Button Types**

Apple provides several types of buttons so you can choose the button type that fits best with the terminology and flow of your purchase or payment experience.

Use the Apple-provided APIs to create Apple Pay buttons. When you use the system-provided APIs, you get:

- A button that is guaranteed to use an Apple-approved caption, font, color, and style
- Assurance that the button's contents maintain ideal proportions as you change its size
- Automatic translation of the button's caption into the language that's set for the device
- Support for configuring the button's corner radius to match the style of your UI
- A system-provided alternative text label that lets VoiceOver describe the button

**Available Button Types:**

- **Buy with Apple Pay** - An area in an app or website where people can make a purchase, such as a product detail page or shopping cart page.
- **Pay with Apple Pay** - An app or website that lets people pay bills or invoices, such as those for a utility or service.
- **Check out with Apple Pay** - An app or website offering a shopping cart or purchase experience that includes other payment buttons starting with "Check out".
- **Continue with Apple Pay** - An app or website offering a shopping cart or purchase experience that includes other payment buttons starting with "Continue with".
- **Book with Apple Pay** - An app or website that helps people book flights, trips, or other experiences.
- **Donate with Apple Pay** - An app or website for an approved nonprofit that lets people make donations.
- **Subscribe with Apple Pay** - An app or website that lets people purchase a subscription, such as a gym membership or meal-kit delivery service.
- **Reload with Apple Pay** - An app or website that uses the term "reload" to help people add money to a card, account, or payment system.
- **Add Money with Apple Pay** - An app or website that uses the term "add money" to help people add money to a card, account, or payment system.
- **Top Up with Apple Pay** - An app or website that uses the term "top up" to help people add money to a card, account, or payment system.
- **Order with Apple Pay** - An app or website that lets people place orders for items like meals or flowers.
- **Rent with Apple Pay** - An app or website that lets people rent items like cars or scooters.
- **Support with Apple Pay** - An app or website that uses the term "support" to help people give money to projects, causes, or organizations.
- **Contribute with Apple Pay** - An app or website that uses the term "contribute" to help people give money to projects, causes, or organizations.
- **Tip with Apple Pay** - An app or website that lets people tip for goods or services.
- **Apple Pay** - An app or website that has stylistic reasons to use a button that can have a smaller minimum width or that doesn't specify a call to action.
- **Set up Apple Pay** - When a device supports Apple Pay, but it hasn't been set up yet, you can use this button to show that Apple Pay is accepted and give people an explicit opportunity to set it up.

**Button Styles**

You can use the automatic style to let the current system appearance determine the appearance of the Apple Pay buttons in your app. If you want to control the button appearance yourself, you can use one of the following options:

- **Black** - Use on white or light-color backgrounds that provide sufficient contrast. Don't use on black or dark backgrounds.
- **White with outline** - Use on white or light-color backgrounds that don't provide sufficient contrast. Don't place on dark or saturated backgrounds.
- **White** - Use on dark-color backgrounds that provide sufficient contrast.

**Button Size and Position**

- **Display prominently** - Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.
- **Position correctly with Add to Cart buttons** - In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button. In a stacked layout, place the Apple Pay button above an Add to Cart button.
- **Match corner radius** - Adjust the corner radius to match the appearance of other buttons. By default, an Apple Pay button has rounded corners, but you can change this to produce square corners or capsule-shaped buttons.
- **Maintain minimum sizing** - Be mindful that the button title may vary in length depending on the locale.

**Note:** If the size you specify doesn't accommodate the translated title for the type of payment button you're using, the system automatically replaces it with the plain Apple Pay button.

**Minimum Button Specifications:**
- **Apple Pay button:** 100pt minimum width, 30pt minimum height, 1/10 button height margins
- **All other Apple Pay buttons:** 140pt minimum width, 30pt minimum height, 1/10 button height margins

### Apple Pay Mark

Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other payment options in a similar manner. The Apple Pay mark isn't a button; if you need an Apple Pay button, choose one of the buttons described above.

- **Use only Apple-provided artwork** - Use only the artwork provided by Apple, with no alterations other than height. Make sure the height you use is equal to or larger than other payment brand marks in your payment flow.
- **Maintain proper spacing** - Maintain a minimum clear space around the mark of 1/10 of its height. Don't let the Apple Pay mark share its surrounding border with another graphic or button.
- **Download official artwork** - [Download the Apple Pay mark graphic and full usage guidelines](https://developer.apple.com/apple-pay/marketing/).

### Referring to Apple Pay

As with all Apple product names, use Apple Pay exactly as shown in [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) — never make it plural or possessive — and adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

- **Use proper capitalization** - Use two words with an uppercase A, an uppercase P, and lowercase for all other letters. Display Apple Pay entirely in uppercase only when necessary for conforming to an established typographic interface style.
- **Include trademark symbol when appropriate** - In the United States, use the registered trademark symbol (®) the first time Apple Pay appears in body text. Don't include it when Apple Pay appears as a selection option during checkout.
- **Coordinate with your app's typography** - Don't mimic Apple typography. Instead, use text attributes that are consistent with the rest of your app or website.
- **Don't translate the trademark** - Always use Apple trademarks in English, even when they appear within non-English text.
- **Follow App Store guidelines** - When promoting your app's use of Apple Pay, refer to the [App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/).

## Platform Considerations

No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS. Not supported in tvOS.

### Related Components

- [In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase) - For selling virtual goods and digital content

### Developer Documentation

- [Apple Pay — PassKit](https://developer.apple.com/documentation/passkit/apple_pay) - PassKit
- [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web) - Web
- [WKInterfacePaymentButton — WatchKit](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) - WatchKit

## Changelog

### June 10, 2024
- Updated links to developer guidance for offering Apple Pay on the web.

### September 12, 2023
- Updated artwork.

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-pay)*
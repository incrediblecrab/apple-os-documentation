# Wallet

Wallet helps people securely store their credit and debit cards, driver's license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

**Platforms:** iOS | iPadOS | macOS | visionOS | watchOS

## Overview

People use their cards and passes in Wallet to make Apple Pay purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.

When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual's identity so they can access personal content, and offer detailed receipts and tracking information where it's most convenient. For developer guidance, see Wallet.

Use Pass Designer to author and preview passes, and consider the poster generic style when a full-background-image layout suits a pass that does not fit another category. Check the tools and APIs for their individual system requirements.

## Topics

### Best Practices

#### Passes

- **Offer to add new passes to Wallet** - When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap.
- **Check authorization for background additions** - For frequent, predictable additions, the HIG describes background pass delivery after one-time authorization. Check the [background-add capability](https://developer.apple.com/documentation/passkit/pkpasslibrary/capability/backgroundaddpasses) and API availability; provide a review-and-add interface when someone needs to inspect the pass first.
- **Help people add a pass that they created outside of your app** - If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app.
- **Add related passes as a group** - If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don't have to add each one individually.
- **Display an Add to Apple Wallet button to let people add an existing pass that isn't already in Wallet** - You can display this button wherever the corresponding pass information appears in your app.
- **Let people jump from your app to their pass in Wallet** - Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly.
- **Tell the system when your pass expires** - Wallet automatically hides expired passes to reduce crowding, while also providing a button that lets people revisit them.
- **Always get people's permission before deleting a pass from Wallet** - For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or have them removed automatically.
- **Help the system suggest a pass when it's contextually relevant** - When you supply information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it.
- **Update passes as needed** - Physical passes don't typically change, but a digital pass can reflect updates to events.
- **Use change messages only for updates to time-critical information** - A change message interrupts people's current workflow, so it's essential to send one only when you make an update they need to know about.

#### Designing passes

- **Preview with Pass Designer** - Use templates or a blank design to build and inspect the pass layout. The authoring app requires macOS 27 or later; that host requirement is separate from a pass feature's availability on the recipient's device. See [Creating a pass with Pass Designer](https://developer.apple.com/documentation/walletpasses/creating-a-pass-with-pass-designer).
- **Keep essential information as text** - Use pass fields and semantic tags rather than embedding labels or other important text in images. Add barcodes through Pass Designer or the corresponding APIs, not as part of a background image.

- **Design a pass that looks great and works well on all devices** - Passes can look different on different devices. Don't put essential information in elements that might be unavailable on certain devices.
- **Avoid using device-specific language** - You can't predict the device people will use to view your pass, so don't write text that might not make sense on a particular device.
- **Make your pass instantly identifiable** - Using color — especially a color that's linked to your brand — can help people recognize your pass as soon as they see it.
- **Keep the front of a pass uncluttered** - Put essential information in the header so it remains visible when the pass is collapsed. Do not assume every pass style or layout direction places that information at the top right.
- **Consider contactless use when supported** - An NFC-enabled pass lets people hold their device near a compatible reader. Adding NFC to a pass requires a special entitlement from Apple; see [Pass.NFC](https://developer.apple.com/documentation/walletpasses/pass/nfc-data.dictionary). Do not assume every pass or reader supports NFC.
- **Reduce image sizes for optimal performance** - To make downloads as fast as possible, use the smallest image files that still look great.
- **Provide an icon that represents your company or brand** - The system includes your icon when displaying information about a relevant pass on the Lock Screen.

### Pass Styles

Choose the style that matches the pass's purpose, then consult its schema for supported fields and images.

| Style | Appropriate use |
|-------|-----------------|
| Boarding pass | Travel credentials such as airline or train tickets. |
| Coupon | Discounts and special offers. |
| Store card | Loyalty, points, and gift-card experiences. |
| Event ticket | Admission to an event, including the poster event presentation where supported. |
| Poster generic | A flexible, full-background-image presentation when another category does not fit. |
| Generic | Other credentials, such as a membership or claim ticket. |

For poster backgrounds, keep important artwork within the safe area and account for the material strip and any barcode near the bottom. Preview the finished pass instead of assuming that artwork remains unobscured.

### Order Tracking

When you support order tracking, Wallet can display information about an order a customer placed through your app or website, updating the information whenever the status of the order changes.

- **Make it easy for people to add an order to Wallet** - For example, when a customer completes an Apple Pay transaction in your app or website, automatically add the order to Wallet.
- **Make information about an order available immediately after people place it** - People need to confirm that their order was received, even when payment, processing, and fulfillment are still pending.
- **Provide fulfillment information as soon as it's available, and keep the status up to date** - When you supply fulfillment data or change the status of an order, the system updates the order information and can automatically send a notification to customers.
- **Supply high-resolution logo and product images** - Use images that measure 300x300 pixels with nontransparent backgrounds.
- **Keep text brief and use clear, approachable language** - People appreciate being able to read text at a glance, and the system can truncate text that's too long.

### Identity Verification

On iPhone running iOS 16 and later, people can store an ID card in Wallet, and later allow an app or App Clip to access information on the card to verify their identity without leaving their current context.

- **Present a Wallet verification option only when the device supports it** - If the current device can't return the identity information you request, don't display a Verify with Apple Wallet button.
- **Ask for identity information only at the precise moment you need it** - People can be suspicious of a request for personal information if it doesn't seem to be related to their current action.
- **Clearly and succinctly describe the reason you need the information you're requesting** - You must write text that explains why people need to share identity information with your app.
- **Ask only for the data you actually need** - People may lose trust in your app if you ask for more data than you need to complete the current task or action.
- **Clearly indicate whether you will keep the data and how long** - To help people trust your app, it's essential to explain how long you might need to keep the personal information they agree to share with you.

### Platform Considerations

The HIG gives no additional platform considerations for iOS, iPadOS, macOS, or visionOS. This does not mean every Wallet feature is available on every device: check the relevant PassKit, Wallet, and identity-verification capability before offering it. The HIG does not support Wallet in tvOS.

On watchOS, a pass can show fewer fields and images than on iPhone. Keep essential information in elements the watch can present, use device-neutral language, and do not rely on image padding or embedded text for layout and accessibility.

### Related Components

- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) - Apple Pay integration
- [ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier) - Identity verification guidance

### Developer Documentation

- [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/passkit) - Framework
- [Wallet Passes](https://developer.apple.com/documentation/walletpasses) - Pass creation
- [Wallet Orders](https://developer.apple.com/documentation/walletorders) - Order tracking
- [FinanceKit](https://developer.apple.com/documentation/financekit) - Financial data
- [FinanceKitUI](https://developer.apple.com/documentation/financekitui) - Financial UI components

### Videos

- [What's new in Wallet](https://developer.apple.com/videos/play/wwdc2026/209)
- [What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2022/10041/)

## Changelog

### June 8, 2026
- Apple updated the HIG for iOS 27 and Pass Designer.

### January 17, 2025
- Added specifications for pass image dimensions

### December 18, 2024
- Added guidance for the poster event ticket style

### September 12, 2023
- Added guidance for helping people add orders to Wallet

### February 20, 2023
- Enhanced guidance for presenting order-tracking information and added artwork

### November 30, 2022
- Added guidance to include a carrier name in status information for a shipping fulfillment

### September 14, 2022
- Added guidelines for using Verify with Wallet, updated guidance on providing shipping status values and descriptions, and consolidated guidance into one page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/wallet)*

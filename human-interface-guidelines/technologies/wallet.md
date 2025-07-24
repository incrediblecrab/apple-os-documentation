# Wallet

Wallet helps people securely store their credit and debit cards, driver's license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

**Platforms:** iOS | iPadOS | macOS | visionOS | watchOS

## Overview

People use their cards and passes in Wallet to make Apple Pay purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.

When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual's identity so they can access personal content, and offer detailed receipts and tracking information where it's most convenient. For developer guidance, see Wallet.

## Topics

### Best Practices

**Passes**

- **Offer to add new passes to Wallet** - When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap.
- **Help people add a pass that they created outside of your app** - If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app.
- **Add related passes as a group** - If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don't have to add each one individually.
- **Display an Add to Apple Wallet button to let people add an existing pass that isn't already in Wallet** - You can display this button wherever the corresponding pass information appears in your app.
- **Let people jump from your app to their pass in Wallet** - Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly.
- **Tell the system when your pass expires** - Wallet automatically hides expired passes to reduce crowding, while also providing a button that lets people revisit them.
- **Always get people's permission before deleting a pass from Wallet** - For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or have them removed automatically.
- **Help the system suggest a pass when it's contextually relevant** - When you supply information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it.
- **Update passes as needed** - Physical passes don't typically change, but a digital pass can reflect updates to events.
- **Use change messages only for updates to time-critical information** - A change message interrupts people's current workflow, so it's essential to send one only when you make an update they need to know about.

**Designing Passes**

- **Design a pass that looks great and works well on all devices** - Passes can look different on different devices. Don't put essential information in elements that might be unavailable on certain devices.
- **Avoid using device-specific language** - You can't predict the device people will use to view your pass, so don't write text that might not make sense on a particular device.
- **Make your pass instantly identifiable** - Using color — especially a color that's linked to your brand — can help people recognize your pass as soon as they see it.
- **Keep the front of a pass uncluttered** - Show essential information in the top-right area of the pass so people can still see it when the pass is collapsed in Wallet.
- **Prefer an NFC-compatible pass** - People appreciate having a contactless pass, because it means that they can just hold their device near a reader.
- **Reduce image sizes for optimal performance** - To make downloads as fast as possible, use the smallest image files that still look great.
- **Provide an icon that represents your company or brand** - The system includes your icon when displaying information about a relevant pass on the Lock Screen.

### Pass Styles

The system defines several pass styles for categories like boarding pass, coupon, store card, and event ticket. Pass styles specify the appearance and layout of content in your pass, and the information that the system needs to suggest your pass when it's relevant.

**Boarding Passes**  
Use the boarding pass style for train tickets, airline boarding passes, and other types of transit passes. A boarding pass can display logo and footer images, and it can have up to two primary fields and up to five auxiliary fields.

**Coupons**  
Use the coupon style for coupons, special offers, and other discounts. A coupon can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.

**Store Cards**  
Use the store card style for store loyalty cards, discount cards, points cards, and gift cards. A store card can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.

**Event Tickets**  
Use the event ticket pass style to give people entry into events like concerts, movies, plays, and sporting events. An event ticket can display logo, strip, background, or thumbnail images. In iOS 18 and later, the system defines an additional style for contactless event tickets called poster event ticket.

**Generic Passes**  
Use the generic style for a type of pass that doesn't fit into the other categories, such as a gym membership card or coat-check claim ticket. A generic pass can display logo and thumbnail images, and it can have up to four secondary and auxiliary fields.

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

**iOS**  
Full support for all Wallet features including passes, order tracking, and identity verification.

**iPadOS, macOS, visionOS**  
Basic Wallet support available. Some features may have limitations compared to iOS.

**watchOS**  
Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don't create a watch-specific app.

Not supported in tvOS.

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

- [What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2024/10081/)
- [What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2023/10056/)
- [What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2022/10041/)

## Changelog

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
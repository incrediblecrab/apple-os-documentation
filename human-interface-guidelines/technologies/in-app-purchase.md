# Apple In-App Purchase

People can use Apple In-App Purchase to pay for digital goods and services, like premium content and subscriptions, securely within your app.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

You can also promote and offer your Apple In-App Purchase items directly through the App Store.

**Tip:** Apple In-App Purchase and Apple Pay are different technologies for different use cases. Use Apple In-App Purchase to sell virtual goods in your app, such as premium content and subscriptions to digital content. Use Apple Pay for physical goods, for services such as club memberships, hotel reservations and event tickets, and for donations. Donations have additional conditions: App Review Guideline 3.2.1(vi) covers approved nonprofits, requires Apple Pay support, and sets disclosure and legal-compliance requirements.

Apple In-App Purchase supports four types of content:

- Consumable content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.
- Non-consumable content like premium features in an app. Purchased non-consumable content doesn't expire.
- Auto-renewable subscriptions to virtual content, services, and premium features in your app on an ongoing basis. An auto-renewable subscription renews at the end of each subscription period until people cancel it. A billing issue can still cause a subscription to expire, so check subscription status rather than assuming every renewal succeeds.
- Non-renewing subscriptions to a service or content that lasts for a limited time, like access to an in-game battle pass. People purchase a non-renewing subscription each time they want to extend their access to the service or content.

For marketing and business guidance, see Apple In-App Purchase and Auto-renewable subscriptions. For information about what you can and can't sell in your app, including usage requirements and restrictions for Apple In-App Purchase, see App Review Guidelines. For developer guidance, see Apple In-App Purchase in the StoreKit documentation.

**Note:** For apps with exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or apps that provide subscriptions with optional add-on content as a single purchase within the app, the Advanced Commerce API allows you to manage your catalog of Apple In-App Purchase items directly. See the Advanced Commerce API App Store support page for an overview, and see Advanced Commerce API for developer guidance.

> **Storefront-specific payment rules:** App Review Guideline [3.1.1(a)](https://developer.apple.com/app-store/review/guidelines/#link-to-other-purchase-methods) states that entitlements for external purchase links and buttons aren't required in United States storefront apps. This isn't a global exemption from in-app purchase rules; check the requirements for the storefront and service you support.

## Topics

### Best Practices

- **Let people experience your app before making a purchase** - People may be more inclined to invest in paid items or features after they've enjoyed your app and discovered its value. If you offer auto-renewable subscriptions, consider supporting limited free access to your content.
- **Design an integrated shopping experience** - You don't want people to think they've entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.
- **Use simple, succinct product names and descriptions** - Titles that don't truncate or wrap and plain, direct language can help people find products quickly.
- **Display the total billing price for each in-app purchase you offer, regardless of type** - People need to know the total billing amount for every purchase they consider.
- **Display your store only when people can make payments** - If someone can't make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isn't available.
- **Use the default confirmation sheet** - When someone makes a purchase using Apple In-App Purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don't modify or replicate this sheet.

### Supporting Family Sharing

People can use Family Sharing to share access to their purchased content — such as auto-renewable subscriptions and non-consumable in-app purchases — with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.

- **Prominently mention Family Sharing in places where people learn about the content you offer** - For example, including "Family" or "Shareable" in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.
- **Help people understand the benefits of Family Sharing and how to participate** - When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings.
- **Aim to customize your in-app messaging so that it makes sense to both purchasers and family members** - For example, when a family member views shared content for the first time, you might welcome them with wording like "Your family subscription includes…".

### Providing Help

Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow.

- **Provide help that customers can view before they request a refund** - In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app.
- **Use a simple title for the refund action, like "Refund" or "Request a Refund"** - The system-provided refund flow makes it clear that people request a refund from Apple, so there's no need to reiterate this information.
- **Help people find the problematic purchase** - For each recent purchase you display, include contextual information that helps people identify the one they want.
- **Consider offering alternative solutions** - For example, if the customer didn't receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.
- **Make it easy for people to request a refund** - Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn't create a barrier to requesting a refund.
- **Avoid characterizing or providing guidance on Apple's refund policies** - For example, don't speculate about whether customers will receive the refund they request. To explain the process, you can link to Apple's support article [Request a refund for apps or content that you bought from Apple](https://support.apple.com/en-us/HT204084).

### Auto-renewable Subscriptions

- **Call attention to subscription benefits during onboarding** - By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they'll gain by subscribing.
- **Offer a range of content choices, service levels, and durations** - People appreciate the flexibility to choose the subscription that best meets their needs.
- **Consider letting people try your content for free before signing up** - Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.
- **Prompt people to subscribe at relevant times, like when they near their monthly limit of free content** - Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.
- **Encourage a new subscription only when someone isn't already a subscriber** - Otherwise, people may believe their existing subscription has lapsed when that's not actually the case. If you sell the same subscription in several apps or on your website, offer a way to sign in so people don't think they have to pay twice for the same service.

#### Making Signup Effortless

- **Provide clear, distinguishable subscription options** - Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.
- **Simplify initial signup by asking only for necessary information** - A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.
- **In your tvOS app, help people sign up or authenticate using another device** - Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.
- **Give people more information in your app's sign-up screen** - In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include the subscription name, duration, and the content or services provided in each period; the billing amount, localized for the territories and currencies where the subscription is sold; and a way for existing subscribers to sign in or restore purchases.
- **Clearly describe how a free trial works** - It's particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period.
- **Include a sign-up opportunity in your app's settings** - App and account settings are common places for people to look for a way to subscribe.

#### Supporting Offer Codes

In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content.

There are two types of offer code. A one-time use code is a unique code you generate in App Store Connect; people can redeem it through a redemption URL, in your app if you support redemption, or by entering it in the App Store, which prompts them to install your app if they haven't already. It suits small distributions and codes whose access you need to restrict. A custom code is one you create, such as NEWYEAR or SPRINGSALE; people can redeem it through a redemption URL or in your app if you support redemption. It suits large campaigns that distribute codes widely.

- **Clearly explain offer details** - To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.
- **Follow guidelines for creating a custom code** - A custom code can contain only alphanumeric ASCII characters. Don't use special characters, including Chinese and Arabic characters.
- **Tell people how to redeem a custom code** - Because people can't redeem a custom code by entering it in their App Store account settings, explain how to use its redemption URL or your app's supported redemption flow.
- **Consider supporting offer redemption within your app** - The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store. The only custom UI you need is a control that starts the system flow, such as a "Redeem Code" button in your paywall, onboarding screens or settings. For developer guidance, see [presentOfferCodeRedeemSheet(from:options:)](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc) and [offerCodeRedemption(options:isPresented:onCompletion:)](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:)).
- **Supply an engaging and informative promotional image** - Creating this optional image can help people understand the value of your content. If you don't supply a promotional image, the code redemption screens use your app icon by default.
- **Help people benefit from unlocked content as soon as they complete the redemption flow** - Think about ways to align the post-redemption experience in your app with the subscriber's new status.

#### Helping People Manage Their Subscriptions

Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.

- **Provide summaries of the customer's subscriptions** - In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option.
- **Consider using the system-provided subscription-management UI** - Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app.
- **Encourage a subscriber to keep their subscription or resubscribe later** - When someone tries to cancel, consider reminding them what they'd lose access to, suggesting a different plan, or offering a discount. If they still cancel, consider a personalized, discounted offer to resubscribe later. For developer guidance, see [Retention Messaging API](https://developer.apple.com/documentation/retentionmessaging) and [Win-back offers](https://developer.apple.com/app-store/subscriptions/#win-back-offers). To check whether a subscription is set to renew in the next period, read [`willAutoRenew`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew).
- **Always make it easy for customers to cancel an auto-renewable subscription** - If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they're being discouraged or prevented from canceling.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.

**watchOS**  
The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.

- **Clearly describe the differences between versions of your app that run on different devices** - If your watchOS app supports different functionality or provides a subset of the content that's available on other devices, be sure to clarify these differences in your description.
- **Consider using a modal sheet to display the required information** - After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view.
- **Make subscription options easy to compare on a small screen** - People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that's easy to scan and compare.

### Related Components

- [Apple In-App Purchase](https://developer.apple.com/in-app-purchase/)
- [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/)
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Developer Documentation

- [Apple In-App Purchase — StoreKit](https://developer.apple.com/documentation/storekit/in-app-purchase) - StoreKit
- [canMakePayments](https://developer.apple.com/documentation/storekit/appstore/canmakepayments) - StoreKit
- [beginRefundRequest(for:in:)](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph) - StoreKit
- [Product.SubscriptionInfo](https://developer.apple.com/documentation/storekit/product/subscriptioninfo) - StoreKit
- [showManageSubscriptions(in:)](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)) - StoreKit
- [presentOfferCodeRedeemSheet(from:options:)](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc) - StoreKit; iOS, iPadOS, Mac Catalyst and visionOS 27.0
- [offerCodeRedemption(options:isPresented:onCompletion:)](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:)) - SwiftUI; iOS, iPadOS, Mac Catalyst, macOS and visionOS 27.0
- [presentOfferCodeRedeemSheet(in:)](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(in:)) - StoreKit; iOS, iPadOS and Mac Catalyst 16.0, visionOS 1.0. Deprecated in 27.0 on all four; Apple points to presentOfferCodeRedeemSheet(from:options:)
- [Retention Messaging API](https://developer.apple.com/documentation/retentionmessaging) - Server-to-server web service; Apple labels it pre-release, with access by request

### Videos

- [What's new in Apple In-App Purchase](https://developer.apple.com/videos/play/wwdc2026/210/)

## Changelog

### September 17, 2026
- Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices.

### September 12, 2023
- Updated artwork and guidance for redeeming offer codes.

### November 3, 2022
- Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase)*

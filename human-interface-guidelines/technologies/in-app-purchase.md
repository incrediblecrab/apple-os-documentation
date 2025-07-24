# In-app purchase

People can use in-app purchase to pay for virtual goods — like premium content, digital goods, and subscriptions — securely within your app.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

You can also promote and offer in-app purchases directly through the App Store. For developer guidance, see In-App Purchase.

**Tip:** In-app purchase and Apple Pay are different technologies that support different use cases. Use in-app purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.

Using in-app purchase, there are four types of content you can offer:

- Consumable content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.
- Non-consumable content like premium features in an app. Purchased non-consumable content doesn't expire.
- Auto-renewable subscriptions to virtual content, services, and premium features in your app on an ongoing basis. An auto-renewable subscription continues to automatically renew at the end of each subscription period until people choose to cancel it.
- Non-renewing subscriptions to a service or content that lasts for a limited time, like access to an in-game battle pass. People purchase a non-renewing subscription each time they want to extend their access to the service or content.

For marketing and business guidance, see In-app purchase and Auto-renewable subscriptions. For information about what you can and can't sell in your app, including in-app purchase usage requirements and restrictions, see App Review Guidelines.

**Note:** For apps with exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or apps that provide subscriptions with optional add-on content as a single purchase within the app, the Advanced Commerce API allows you to manage your In-App Purchase catalog directly. See the Advanced Commerce API App Store support page for an overview, and see Advanced Commerce API for developer guidance.

## Topics

### Best Practices

- **Let people experience your app before making a purchase** - People may be more inclined to invest in paid items or features after they've enjoyed your app and discovered its value. If you offer auto-renewable subscriptions, consider supporting limited free access to your content.
- **Design an integrated shopping experience** - You don't want people to think they've entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.
- **Use simple, succinct product names and descriptions** - Titles that don't truncate or wrap and plain, direct language can help people find products quickly.
- **Display the total billing price for each in-app purchase you offer, regardless of type** - People need to know the total billing amount for every purchase they consider.
- **Display your store only when people can make payments** - If someone can't make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isn't available.
- **Use the default confirmation sheet** - When someone initiates an in-app purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don't modify or replicate this sheet.

### Supporting Family Sharing

People can use Family Sharing to share access to their purchased content — such as auto-renewable subscriptions and non-consumable in-app purchases — with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.

- **Prominently mention Family Sharing in places where people learn about the content you offer** - For example, including "Family" or "Shareable" in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.
- **Help people understand the benefits of Family Sharing and how to participate** - When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings.
- **Aim to customize your in-app messaging so that it makes sense to both purchasers and family members** - For example, when a family member views shared content for the first time, you might welcome them with wording like "Your family subscription includes…".

### Providing Help with In-app Purchases

Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow.

- **Provide help that customers can view before they request a refund** - In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app.
- **Use a simple title for the refund action, like "Refund" or "Request a Refund"** - The system-provided refund flow makes it clear that people request a refund from Apple, so there's no need to reiterate this information.
- **Help people find the problematic purchase** - For each recent purchase you display, include contextual information that helps people identify the one they want.
- **Consider offering alternative solutions** - For example, if the customer didn't receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.
- **Make it easy for people to request a refund** - Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn't create a barrier to requesting a refund.
- **Avoid characterizing or providing guidance on Apple's refund policies** - For example, don't speculate about whether customers will receive the refund they request.

### Auto-renewable Subscriptions

- **Call attention to subscription benefits during onboarding** - By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they'll gain by subscribing.
- **Offer a range of content choices, service levels, and durations** - People appreciate the flexibility to choose the subscription that best meets their needs.
- **Consider letting people try your content for free before signing up** - Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.
- **Prompt people to subscribe at relevant times, like when they near their monthly limit of free content** - Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.
- **Encourage a new subscription only when someone isn't already a subscriber** - Otherwise, people may believe their existing subscription has lapsed when that's not actually the case.

#### Making Signup Effortless

- **Provide clear, distinguishable subscription options** - Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.
- **Simplify initial signup by asking only for necessary information** - A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.
- **In your tvOS app, help people sign up or authenticate using another device** - Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.
- **Give people more information in your app's sign-up screen** - In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include the subscription name, duration, content or services provided, billing amount, and a way for existing subscribers to sign in or restore purchases.
- **Clearly describe how a free trial works** - It's particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period.
- **Include a sign-up opportunity in your app's settings** - App and account settings are common places for people to look for a way to subscribe.

#### Supporting Offer Codes

In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content.

- **Clearly explain offer details** - To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.
- **Follow guidelines for creating a custom code** - A custom code can contain only alphanumeric ASCII characters. Don't use special characters, including Chinese and Arabic characters.
- **Tell people how to redeem a custom code** - Because people can't redeem a custom code by entering it in their App Store account settings, it's important to let them know that they can redeem it on your website or within your app.
- **Consider supporting offer redemption within your app** - The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store.
- **Supply an engaging and informative promotional image** - Creating this optional image can help people understand the value of your content. If you don't supply a promotional image, the code redemption screens use your app icon by default.
- **Help people benefit from unlocked content as soon as they complete the redemption flow** - Think about ways to align the post-redemption experience in your app with the subscriber's new status.

#### Helping People Manage Their Subscriptions

Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.

- **Provide summaries of the customer's subscriptions** - In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option.
- **Consider using the system-provided subscription-management UI** - Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app.
- **Consider ways to encourage a subscriber to keep their subscription or resubscribe later** - When you use StoreKit APIs, your app is notified when someone chooses to cancel their subscription. In this scenario, you might want to extend a personalized offer as an alternative to cancellation or invite people to describe their reasons for canceling in an exit survey.
- **Always make it easy for customers to cancel an auto-renewable subscription** - If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they're being discouraged or prevented from canceling.
- **Consider creating a branded, contextual experience to complement the system-provided management UI** - Within your custom UI, you might offer a popular premium tier or provide personalized suggestions for alternative plans based on what you know about the customer's preferences or how they use your app.

### Platform Considerations

**watchOS**  
The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.

- **Clearly describe the differences between versions of your app that run on different devices** - If your watchOS app supports different functionality or provides a subset of the content that's available on other devices, be sure to clarify these differences in your description.
- **Consider using a modal sheet to display the required information** - After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view.
- **Make subscription options easy to compare on a small screen** - People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that's easy to scan and compare.

### Related Components

- [In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase)
- [Offering Subscriptions](https://developer.apple.com/design/human-interface-guidelines/offering-subscriptions)
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Developer Documentation

- [In-App Purchase — StoreKit](https://developer.apple.com/documentation/storekit/in-app-purchase) - StoreKit
- [canMakePayments](https://developer.apple.com/documentation/storekit/skpaymentqueue/canmakepayments()) - StoreKit
- [beginRefundRequest(for:in:)](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)) - StoreKit
- [Product.SubscriptionInfo](https://developer.apple.com/documentation/storekit/product/subscriptioninfo) - StoreKit
- [showManageSubscriptions(in:)](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)) - StoreKit
- [presentOfferCodeRedeemSheet(in:)](https://developer.apple.com/documentation/storekit/appstore/presentoffercodeoffersheet(in:)) - StoreKit

## Changelog

### September 12, 2023
- Updated artwork and guidance for redeeming offer codes.

### November 3, 2022
- Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase)*
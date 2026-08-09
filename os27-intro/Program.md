# Apple Developer Program — OS 27 Generation

Membership in the Apple Developer Program provides access to beta software, advanced capabilities, testing tools, and worldwide distribution. This page covers what changes for the OS 27 generation: beta access, SDK requirements, and the 2026 App Store and regulatory landscape.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

The Apple Developer Program costs **$99 USD per year** for individuals and organizations; the Apple Developer Enterprise Program costs **$299 USD per year** for in-house distribution. Standard App Store commission is 30%, reduced to 15% under the App Store Small Business Program.

## Beta Access

Membership includes access to pre-release builds of every platform.

### OS 27 Betas

- **Developer beta 1** — June 8, 2026, immediately following the WWDC 2026 keynote
- **Public beta 1** — July 13, 2026
- **Current developer beta** — beta 5 for iOS and iPadOS as of early August 2026; Apple moved to a weekly cadence during the summer. Beta numbering diverges across platforms, so check each platform's release notes rather than assuming parity.
- **Expected public release** — September 2026 for iOS and iPadOS, fall 2026 for the remaining platforms. **Apple has not announced a release date.**

### Current Shipping Releases

| Platform | Version | Released |
|----------|---------|----------|
| iOS, iPadOS, tvOS, watchOS, visionOS | 26.6 | July 27, 2026 |
| macOS Tahoe | 26.6.1 | August 6, 2026 |
| Xcode | 26.6 (`17F113`) | June 25, 2026 |

## SDK Requirements

**In force since April 28, 2026:** uploads to App Store Connect must be built with the iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26 SDK or later — that is, Xcode 26 or newer. Deployment targets may remain lower; this requirement governs the SDK you build against, not the OS versions you support.

**No Xcode 27 / OS 27 SDK deadline has been announced.** Apple has historically set this requirement in the spring following a release, but no date has been published. Monitor [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) rather than planning against an assumed date.

> **Xcode 27 requires macOS 27 Golden Gate on Apple silicon.** Because macOS 27 drops all Intel Macs, adopting the OS 27 SDK requires an Apple silicon build machine and CI fleet. Treat this as the long-lead item in your migration plan.

## App Store Review Guidelines — 2026 Changes

- **5.1.2(i)** — You must clearly disclose where personal data is shared with third parties, **including third-party AI services**, and obtain explicit permission first.
- **1.2.1(a)** — Apps with user-generated content need a way to flag content exceeding the app's age rating, plus an age restriction mechanism based on verified or declared age.
- **4.7** — HTML5/JavaScript mini apps and mini games are explicitly in scope. **4.7.2** — such software may not extend or expose native platform APIs without Apple's prior permission. **4.7.5** — the same age restriction requirement as 1.2.1(a) applies.
- **2.5.10 deleted** — the rule on empty ad banners and test ads has been removed.
- **3.2.2(ix)** — Loan apps are capped at **36% APR** with a minimum repayment term over 60 days.
- **4.1(c)** — You may not use another developer's icon, brand, or product name without their approval.
- **5.1.1(ix)** — Crypto exchanges are added to the highly-regulated-fields category.

### DeclaredAgeRange

The DeclaredAgeRange framework (iOS 26.0+, Xcode 26.2+) provides age-appropriate experiences without collecting birthdates. It requires the `com.apple.developer.declared-age-range` entitlement, returns age **ranges** only, and is parent-controlled for children in Family Sharing. See [DeclaredAgeRange](../documentation/DeclaredAgeRange.md).

## Distribution and Regulation

### Alternative Distribution

Alternative app marketplaces and web distribution are available in the **European Union, Brazil, and Japan**. These require iOS 17.4+ for marketplaces, iOS 17.5+ for web distribution, and Xcode 15.3+ for MarketplaceKit. Notarization is the mandatory baseline review for all alternatively distributed apps.

### Japan MSCA

Enforcement of Japan's Mobile Software Competition Act began December 18, 2025. **iOS 26.2** enabled alternative marketplaces, marketplace operation, and non-IAP payment methods in Japan. The developer agreement acceptance deadline was March 17, 2026. The JFTC enforces compliance.

### European Union DMA

Apple remains a designated gatekeeper. Active obligations include alternative marketplaces, third-party browser engines, web distribution, interoperability requests, and anti-self-preferencing rules. A Core Technology Fee of €0.50 per first annual install above one million applies to some distribution paths — verify current terms directly with Apple, as fee structures have been revised repeatedly.

### United States

External purchase links and buttons are permitted in US storefront apps **without an entitlement** under guideline 3.1.1, following the Epic injunction. The Supreme Court granted certiorari in *Apple v. Epic Games* (No. 25-1311) in June 2026; the outcome is pending and could change this position.

### United Kingdom

The CMA designated Apple with Strategic Market Status in October 2025. Remedies remain under consultation.

## Testing and Tools

- **TestFlight** — up to 10,000 external testers and 100 internal testers. TestFlight 4.3 released July 21, 2026.
- **App Store Connect API** — version 4.4.1, released July 15, 2026. See [App Store Connect API](../documentation/AppStoreConnectAPI.md).
- **App Store Connect** — version 3.2, released April 1, 2026.

## Pricing and Tax Updates

Effective August 21, 2026: Brazil IOF changes, Canada DST removal, Estonia VAT 22% → 24%, Romania VAT 19% → 21%, and Philippines VAT at 12%, along with Vietnam changes. Philippines and Vietnam price equalization takes effect September 8, 2026. Review your pricing in App Store Connect.

## Membership Types

### Individual Membership
For solo developers publishing under a personal name. $99 USD per year.

### Organization Membership
For companies and institutions publishing under a legal entity name. Requires a D-U-N-S Number and legal authority to bind the organization. $99 USD per year.

### Apple Developer Enterprise Program
For large organizations distributing proprietary in-house apps to employees. $299 USD per year. Not for App Store distribution.

## Getting Started

1. Sign in with an Apple Account at [developer.apple.com](https://developer.apple.com/)
2. Choose Individual or Organization enrollment
3. Provide legal entity details and a D-U-N-S Number for organizations
4. Complete payment and await verification
5. Accept the current Program License Agreement in App Store Connect

## Resources

- [Apple Developer Program](https://developer.apple.com/programs/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/)
- [Developer Forums](https://developer.apple.com/forums/)
- [TestFlight](https://developer.apple.com/testflight/)

### Platform Coverage
- [iOS](iOS.md) · [iPadOS](iPadOS.md) · [macOS](macOS.md) · [tvOS](tvOS.md) · [visionOS](visionOS.md) · [watchOS](watchOS.md)

### Previous Generation
- [Apple Developer Program — OS 26 Generation](../os26-intro/Program.md)

---

*Reviewed 2026-08-09. Program terms, fees, guidelines, and regulatory positions change frequently and vary by region. Always verify against Apple's official pages before making business decisions.*

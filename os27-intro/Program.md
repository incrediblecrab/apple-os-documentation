# Apple Developer Program — OS 27 Generation

Use this overview to plan OS27 testing and distribution without confusing beta SDK availability with submission deadlines, entitlement approval, or regional eligibility. Policy statements are checked through **September 8, 2026**.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Apple lists annual membership fees of **$99 USD** for the Developer Program and **$299 USD** for the Enterprise Program, with local pricing where available. Enterprise membership is for eligible proprietary in-house distribution, not a general substitute for App Store distribution. Membership fees are not a universal App Store commission schedule. See [enrollment](https://developer.apple.com/support/enrollment/) and [Enterprise eligibility](https://developer.apple.com/programs/enterprise/).

Eligible nonprofit, accredited educational, and government organizations may request a [Developer Program membership fee waiver](https://developer.apple.com/help/account/membership/fee-waivers/); qualifying and continuing conditions apply.

## Beta Access

An Apple developer account provides developer beta access without paid Program enrollment. Use version-specific release notes and download eligibility for your Apple Account. A listed beta is a testing baseline, not permission to submit a beta-built app to production or an announced public release date.

### OS 27 Betas

- **iOS, iPadOS, macOS, tvOS, watchOS, and visionOS 27 beta 8:** August 31, 2026.
- **Xcode 27 beta 6 (`27A5252f`):** August 24, 2026; Swift 6.4 and the OS27 SDKs.
- These are the releases listed at the cutoff, not an assumption that every future beta number will match. The listings do not establish general-availability dates or a visionOS public-beta program.

### Current Shipping Releases

| Platform | Version | Released |
|----------|---------|----------|
| iOS and iPadOS | 26.6.2 (`23G90`) | September 8, 2026 |
| macOS Tahoe | 26.6.2 (`25G83`) | August 17, 2026 |
| visionOS | 26.6.1 (`23O780`) | August 17, 2026 |
| tvOS | 26.6 (`23L773`) | July 27, 2026 |
| watchOS | 26.6 (`23U67`) | July 27, 2026 |
| Xcode | 26.6 (`17F113`) | June 25, 2026 |

Sources: [Apple Developer releases](https://developer.apple.com/news/releases/) and [Apple security releases](https://support.apple.com/en-us/100100). Security-update scope is not a list of newly added APIs.

## SDK Requirements

**In force since April 28, 2026:** the [requirements notice](https://developer.apple.com/news/upcoming-requirements/) requires Xcode 26 or later and the corresponding iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26 SDK or later for uploads on those platforms. Deployment targets can remain lower. The notice does not set a macOS SDK minimum.

**No OS27 SDK deadline appears in the checked notice.** Do not infer one from past annual schedules. Separately, responses to the updated age-rating questionnaire for **each app** were due **January 31, 2026** to avoid interruptions when submitting updates.

> **Xcode 27 beta 6 requires an Apple silicon Mac running macOS Tahoe 26.4 or later—not macOS 27.** Intel Macs cannot host Xcode 27. Its macOS SDK can still build universal apps for macOS 12 or later, and Rosetta can run Intel apps on eligible Apple silicon systems; neither makes Intel hardware an eligible Xcode 27 host. Source: [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

## Review Requirements for OS26 and OS27 Apps

- **5.1.2(i):** disclose third-party personal-data sharing, including third-party AI, and obtain explicit permission before sharing. A failed or declined AI request must not silently switch providers.
- **1.2:** general UGC apps need moderation, reporting with timely responses, blocking, and published contact information.
- **1.2.1(a):** specifically **creator apps** must let people identify content exceeding the app's rating and restrict underage access using verified or declared age. This is not a blanket rule newly imposed on all UGC by that clause.
- **4.7:** the host is responsible for qualifying mini apps/games, streaming games, chatbots, plug-ins, and retro-console/PC emulator apps offering downloadable games. Additional rules include Apple's prior permission for native API exposure, per-instance user consent for sharing data/permissions with individual software, an index with universal links, and age restrictions.
- **2.1 and 5.1.1(v):** provide a complete, reviewable app and working services; apps supporting account creation must offer in-app account deletion.

These are current obligations, not a claim that every rule was introduced in 2026. See the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [App Store readiness checklist](../guides/app-store-readiness.md) for exact scope and failure handling.

### DeclaredAgeRange

Use [DeclaredAgeRange](https://developer.apple.com/documentation/declaredagerange) where available to request an age range rather than collecting a full birthdate. Check its entitlement and platform requirements, and handle declined or unavailable results without assuming adulthood. An SDK version associated with a bug fix is not the framework's introduction version; the API alone does not satisfy every age-assurance obligation.

## Distribution and Regulation

### Alternative Distribution

Apple's [alternative-distribution guidance](https://support.apple.com/en-us/118110) distinguishes:

- **European Union:** iPhone **and iPad** marketplaces and direct developer Web Distribution.
- **Brazil and Japan:** **iPhone** marketplaces and apps offered through them. The cited guidance does not establish iPad marketplaces or direct developer Web Distribution in these countries.

Account region and physical presence both matter. Notarization is a baseline review, not full App Store approval. See [regional distribution](../guides/regional-distribution.md) for route-specific OS minima, unverified prerequisites, travel behavior, support responsibilities, and the announced EU terms transition.

### Payments and Regional Terms

For **US storefront apps**, guideline **3.1.1(a)** says entitlements are not required for buttons, links, or other calls to action to other purchase methods. Do not extend this to every storefront or infer a universal fee exemption. Use the current [guideline](https://developer.apple.com/app-store/review/guidelines/#link-to-other-purchase-methods), not an unverified litigation timeline, as the policy reference.

## Testing and Tools

- **[TestFlight](https://developer.apple.com/testflight/):** up to 10,000 external testers and 100 eligible internal team members. External testing requires the applicable beta review; a beta approval is not App Store release approval.
- **App Store Connect/API:** check [release history](https://developer.apple.com/news/releases/) and [API documentation](https://developer.apple.com/documentation/appstoreconnectapi) for the particular workflow rather than treating a mobile client version as a service-wide compatibility requirement.
- **[Private Cloud Compute](../guides/private-cloud-compute.md):** managed entitlement and developer eligibility are separate from Program membership. Test unavailable models, quota, network failure, and permission refusal.

## Pricing and Tax Updates

Check current notices and accepted agreements in [App Store Connect](https://appstoreconnect.apple.com/) before changing prices or estimating proceeds. This overview does not carry forward unverified tax dates, a historical EU per-install fee as a universal rule, or a global commission table. Effective dates, reporting obligations, and tax responsibility depend on the applicable region and agreement.

## Membership Types

### Individual Membership
For individuals and sole proprietors publishing under their personal legal name. $99 USD per year, with regional pricing where available.

### Organization Membership
For legal entities publishing under the organization's name. Enrollment requires verification and legal authority; check Apple's [D-U-N-S requirements and exceptions](https://developer.apple.com/help/account/membership/D-U-N-S/). $99 USD per year, with regional pricing where available.

### Apple Developer Enterprise Program
For eligible organizations distributing proprietary in-house apps securely to employees, where other distribution options do not meet their needs. Apple requires at least 100 employees and additional verification. $299 USD per year; not for App Store distribution.

## Getting Started

1. Sign in with an Apple Account with two-factor authentication at [developer.apple.com](https://developer.apple.com/); meet your region's legal age requirement.
2. Choose individual or organization enrollment and provide legal identity details, including a D-U-N-S Number where required.
3. Complete the applicable verification. Organizations wait for Apple's review and next-steps email.
4. Accept the associated program license agreement and purchase membership when offered; individuals may do this during initial enrollment.
5. Wait for membership confirmation, then request any separately managed capabilities or distribution permissions.

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

## Sources

[Apple Developer Program](https://developer.apple.com/programs/), [enrollment](https://developer.apple.com/support/enrollment/), [release listings](https://developer.apple.com/news/releases/), [submission requirements](https://developer.apple.com/news/upcoming-requirements/), and [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) support the corresponding sections; the inline sources cover narrower eligibility and regional questions.

*Reviewed September 8, 2026 against the linked primary sources. Account-specific approval, pricing, taxes, and legal obligations require verification in the applicable current terms.*

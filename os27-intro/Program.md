# Apple Developer Program — OS 27 Generation

Use this overview to plan OS27 testing and distribution without confusing SDK availability with submission deadlines, entitlement approval, or regional eligibility. Policy statements were checked through **September 8, 2026**; dated **October 29, 2026** and **November 1, 2026** updates are included below.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Apple lists annual membership fees of **$99 USD** for the Developer Program and **$299 USD** for the Enterprise Program, with local pricing where available. Enterprise membership is for eligible proprietary in-house distribution, not a general substitute for App Store distribution. Membership fees are not a universal App Store commission schedule. See [enrollment](https://developer.apple.com/help/account/membership/program-enrollment/) and [Enterprise eligibility](https://developer.apple.com/programs/enterprise/).

Eligible nonprofit, accredited educational, and government organizations may request a [Developer Program membership fee waiver](https://developer.apple.com/help/account/membership/fee-waivers/); qualifying and continuing conditions apply.

## Beta Access

An [Apple developer account](https://developer.apple.com/programs/) provides developer beta access without paid Program enrollment. Use version-specific release notes and download eligibility for your Apple Account. OS 27 has shipped; a listed beta remains a testing baseline, not permission to submit a beta-built app to production.

### OS 27 Betas

- **iOS, iPadOS, macOS, tvOS, watchOS, and visionOS 27.0:** shipped September 14, 2026, with builds `24A437`, `24A437`, `26A428`, `24J361`, `24R364`, and `24M362`, respectively.
- **Xcode 27 (`27A266a`):** shipped September 14, 2026; Swift 6.4 and the OS27 SDKs.
- These general-availability releases superseded the August 31 beta listings as the September 14, 2026 OS 27 baseline. The release listings do not establish a visionOS public-beta program.

### Current Shipping Releases

**Checked November 1, 2026:** the point releases below follow the September general-availability releases recorded above.

| Platform | Version | Released |
|----------|---------|----------|
| iOS | 27.2 (`24B119`, `24B91020`) | October 26, 2026 |
| iPadOS | 27.2 (`24B119`) | October 26, 2026 |
| macOS 27 Golden Gate | 27.2 (`26B123`) | October 26, 2026 |
| tvOS | 27.2 (`24K122`) | October 26, 2026 |
| visionOS | 27.2 (`24N120`) | October 26, 2026 |
| watchOS | 27.2 (`24S118`) | October 26, 2026 |
| Xcode | 27.2 (`27B52`) | October 29, 2026 |
| Safari | 27.2 (`20625.2.8`) | October 26, 2026 |

The release feed does not identify the device scope of the two iOS 27.2 builds. The feed checked November 1, 2026 lists the final Xcode 27.2 build `27B52`, dated October 29, 2026, the date Apple's security list also gives; the October 19, 2026 RC (`27B48`) recorded in the October 29 check no longer appears in the feed. Xcode 27.1 (`27A9275`) was released October 15, 2026.

The feed lists September 28, 2026 updates to 27.0.1 for iOS and iPadOS (`24A446`), macOS (`26A434`), watchOS (`24R365`), and visionOS (`24M372`).

The feed has no iOS 27.1 software-update entry, but the security list separately dates iOS 27.1 for iPhone Duo to October 23, 2026. [Safari 27.1](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes) (`20625.1.29`) was released October 23, 2026 for iOS 27.1. [Safari 27.2](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) supports iOS, iPadOS, visionOS, and macOS 27.2, plus macOS 26 and macOS Sequoia.

For 26-generation testing, the feed lists iPadOS 26.7.2 (`23H128`) on October 26, 2026; the security list also records iOS 26.7.2 that day, while the feed's latest iOS 26 entry remains 26.6.2. The security list dates macOS Tahoe 26.7, 26.7.1, and 26.7.2 to September 14, 2026, September 28, 2026, and October 26, 2026, respectively, and tvOS 26.6.1 to October 26, 2026 for Apple TV HD and Apple TV 4K 1st generation; it supplies no build numbers for these macOS or tvOS entries.

Sources: [Apple Developer releases](https://developer.apple.com/news/releases/), the [release feed](https://developer.apple.com/news/releases/rss/releases.rss), [Apple security releases](https://support.apple.com/en-us/100100), and the linked Safari notes. Security-update scope is not a list of newly added APIs.

## SDK Requirements

**In force since April 28, 2026:** the [requirements notice](https://developer.apple.com/news/upcoming-requirements/) requires Xcode 26 or later and the corresponding iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26 SDK or later for uploads on those platforms. Deployment targets can remain lower. The notice does not set a macOS SDK minimum.

**October 29, 2026 update:** a separate entry in that notice requires iOS and iPadOS uploads to target iOS 13 or later, effective **September 9, 2026**.

**No OS27 SDK deadline appears in the notice checked November 1, 2026.** Do not infer one from past annual schedules. Separately, responses to the updated age-rating questionnaire for **each app** were due **January 31, 2026** to avoid interruptions when submitting updates.

> **Xcode 27 requires an Apple silicon Mac running macOS Tahoe 26.6 or later—not macOS 27.** Intel Macs cannot host Xcode 27. Its macOS SDK can still build universal apps for macOS 12 or later, and Rosetta can run Intel apps on eligible Apple silicon systems; neither makes Intel hardware an eligible Xcode 27 host. Source: [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

**Point-release SDKs:** [Xcode 27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) includes an iOS 27.1 SDK, with iPadOS, tvOS, watchOS, macOS, and visionOS SDKs still at 27. [Xcode 27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) includes SDKs for all six 27.2 platforms. Both bundle Swift 6.4 and require macOS Tahoe 26.6 or later.

Both point releases document Mac Catalyst compilation failures when code uses iOS 27.1-specific APIs; use the documented build-time guards for affected code. Xcode 27.2 also incorrectly offers 27.1 deployment targets for macOS, watchOS, tvOS, and visionOS; its notes warn that Mac Catalyst targets of 27.1 or 27.2 may not expose newly introduced APIs.

## Review Requirements for OS26 and OS27 Apps

- **5.1.2(i):** disclose third-party personal-data sharing, including third-party AI, and obtain explicit permission before sharing. A failed or declined AI request must not silently switch providers.
- **1.2:** UGC and AI content-creation apps need content filtering, reporting with timely responses, blocking, and published contact information.
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

[Apple Developer Program](https://developer.apple.com/programs/), [enrollment](https://developer.apple.com/help/account/membership/program-enrollment/), [release listings](https://developer.apple.com/news/releases/), [submission requirements](https://developer.apple.com/news/upcoming-requirements/), and [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) support the corresponding sections; the inline sources cover narrower eligibility and regional questions.

Point-release details were checked against the [release feed](https://developer.apple.com/news/releases/rss/releases.rss), [Xcode 27.1 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes), [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes), [iOS and iPadOS 27.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes), [macOS 27.2 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes), [Safari 27.1 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes), and [Safari 27.2 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes).

*Reviewed September 8, 2026 against the linked primary sources. Account-specific approval, pricing, taxes, and legal obligations require verification in the applicable current terms.*

*Reviewed again October 29, 2026 against the captured primary sources.*

*Reviewed again November 1, 2026: Xcode 27.2 final build, enrollment link, and the captured requirements, guidelines, and release sources.*

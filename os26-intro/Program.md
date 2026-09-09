# Apple Developer Program

Use the Apple Developer Program for supported app services, testing, analytics, and distribution across Apple platforms. Membership, a build SDK, an entitlement, and approval to use a particular distribution channel are separate requirements.

**Standard annual membership:** $99 USD, with local pricing where available and conditional fee waivers.

> **Status checked September 8, 2026:** this page retains OS26 Program context. Shipping releases are iOS/iPadOS **26.6.2** (September 8), macOS **26.6.2** and visionOS **26.6.1** (August 17), and tvOS/watchOS **26.6** (July 27). All six OS27 beta 8 releases are dated August 31. See the [OS27 Program overview](../os27-intro/Program.md) for the separate Xcode baseline and current policy scope.

## Overview

Choose the enrollment and distribution route that fits your app and legal entity. Some capabilities need additional approval, and neither membership nor passing a build proves compliance with App Review or regional terms.

## Current Submission Requirements

- **Since April 28, 2026:** uploads for iOS, iPadOS, tvOS, visionOS, and watchOS require Xcode 26 or later and the corresponding 26 SDK or later. Deployment targets may remain older; this notice does not set a macOS SDK minimum.
- **Since January 31, 2026:** complete the updated age-rating questionnaire for each app to avoid interruptions when submitting updates. Automatic conversion to new ratings did not remove the questionnaire requirement.
- The checked [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) page announces no OS27 SDK deadline. Beta listings do not establish general-availability dates or production upload acceptance.
- **AI and privacy:** [5.1.2(i)](https://developer.apple.com/app-store/review/guidelines/#data-use-and-sharing) requires clear disclosure and explicit permission before third-party personal-data sharing, including third-party AI.
- **Content scope:** general UGC moderation is governed by 1.2; the exceed-rating identification and age restriction rule in **1.2.1(a) applies to creator apps**. Software offered under **4.7** has additional host, permission, index, and age requirements.

Use [App Store readiness](../guides/app-store-readiness.md) for permission refusal, unavailable age information, review access, and account-deletion checks. Use [regional distribution](../guides/regional-distribution.md) for EU iPhone/iPad marketplace and web routes versus Brazil/Japan iPhone marketplace routes; their OS minima and terms are not interchangeable.

## Program Benefits

### Get the Latest Betas

**Be ready for what's coming next**  
Apple customers adopt new software rapidly, so you can keep innovating. Integrate the latest Apple technologies in your apps to deliver incredible experiences on Apple platforms as soon as they're released.

**Early Access Includes:**
- iOS 27 and iPadOS 27 beta releases and developer previews
- macOS Golden Gate 27 beta software
- watchOS 27, tvOS 27, and visionOS 27 beta releases
- Xcode 27 pre-release toolchains

An Apple developer account provides access to developer beta software without paid Program enrollment. Distribution, managed capabilities, and particular testing services have separate membership or approval requirements; check the account's available downloads.

> **Toolchain planning:** Xcode 27 beta 6 was released August 24 and needs **an Apple silicon Mac running macOS Tahoe 26.4 or later**, not macOS 27. Intel Macs cannot host it; support for running Intel apps through Rosetta on Apple silicon is a separate question. See the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

### Access Comprehensive Services and Capabilities

**Leverage Apple's integrated ecosystem**  
Create useful and engaging experiences with Apple's tightly integrated hardware, software, services, and capabilities.

**Key Services:**
- **In-App Purchase**: Offer special content and services with secure payment processing
- **Apple Intelligence**: Integrate on-device machine learning and AI capabilities
- **Apple Pay**: Offer supported payment flows for goods and services; digital-content purchases must separately follow App Review's payment rules
- **Spatial Computing**: Create immersive experiences for Apple Vision Pro
- **HealthKit**: Access health and fitness data with user permission
- **MapKit**: Integrate maps and location services
- **Core ML**: Deploy machine learning models with optimized performance

These are technology choices, not capabilities that membership automatically enables. Check each framework's device, OS, authorization, and entitlement requirements.

### Test Your Apps

**Collect valuable feedback before release**  
With TestFlight, you can invite up to 10,000 external users to try out your beta builds using just their email address or by sharing a public link.

**TestFlight Features:**
- Beta testing for supported iOS, iPadOS, macOS, watchOS, tvOS, and visionOS apps
- Crash reporting and user feedback collection
- Optional automatic distribution of new builds to internal testers
- Internal testing for up to 100 eligible App Store Connect users with access to the app
- External testing for up to 10,000 users
- Each uploaded build is testable for up to 90 days

### Distribute Apps Worldwide

**Reach customers in 175 regions**  
The App Store makes it easy for users worldwide to discover and download your apps, games, and extensions across Apple platforms.

**Distribution Benefits:**
- **Global Reach**: 175 regions and territories worldwide
- **Payment Processing**: Apple processes App Store transactions in supported storefronts; configure availability and pricing for your app
- **Hosting and Bandwidth**: App Store app distribution includes hosting and bandwidth, including free apps; this is not unlimited hosting for your own backend services
- **App Review**: App Store distribution includes review requirements; developers remain responsible for their own account and data-security flows
- **Organizational Distribution**: Volume purchasing through Apple School Manager and Apple Business
- **Mac App Store Alternative**: Distribute Mac apps outside the App Store using Developer ID

### Analytics and Insights

**Dive deep into app performance**  
Use [App Store Connect Analytics](https://developer.apple.com/app-store-connect/analytics/) to review discovery, engagement, and monetization. Usage metrics include only people who opt to share diagnostics and usage information; privacy thresholds and platform/feature coverage can limit what appears.

**Analytics Include:**
- App Store impression and download metrics
- User engagement and retention data
- Revenue and financial reporting
- Crash-rate metrics
- Custom product page performance
- Product page optimization results

## Membership Types

Eligible nonprofit, accredited educational, and government organizations may request a [membership fee waiver](https://developer.apple.com/help/account/membership/fee-waivers/). Eligibility and continuing requirements apply; organization status alone does not guarantee a waiver.

### Individual Membership
- **Cost**: $99 USD annually
- **Best for**: Individual developers and sole proprietors
- **Identity**: Verified individual using an Apple Account
- **App Store Listing**: Personal legal name, not a DBA

### Organization Membership
- **Cost**: $99 USD annually
- **Best for**: Companies, educational institutions, and organizations
- **Legal Entity**: Requires verification; [D-U-N-S requirements](https://developer.apple.com/help/account/membership/D-U-N-S/) depend on the organization type, with government organizations exempt from the number requirement
- **App Store Listing**: Organization name
- **Team Management**: Add multiple team members with different roles

### Apple Developer Enterprise Program
- **Cost**: $299 USD annually
- **Best for**: Large organizations distributing proprietary apps internally
- **Requirements**: At least 100 employees and Apple's organization verification, including a D-U-N-S Number where required
- **Distribution**: Internal distribution only (not on App Store)

## Getting Started

### Enrollment Process
1. **Apple Account**: Use an Apple Account with two-factor authentication and meet your region's legal age requirement
2. **Enrollment details**: Choose individual or organization enrollment and provide legal identity details, including a D-U-N-S Number where required
3. **Verification**: Complete the applicable identity and authority checks; organizations wait for Apple's verification and next-steps email
4. **Agreement and payment**: Accept the associated program license agreement and purchase membership when offered; individuals may do this during initial enrollment
5. **Activation**: Wait for membership confirmation; request separately managed capabilities and distribution permissions as needed

### Essential Resources
- **Xcode**: Get a shipping release from the Mac App Store; use Apple's developer downloads for beta releases and version-specific toolchains
- **Documentation**: Access comprehensive developer documentation
- **Sample Code**: Explore code examples and project templates
- **WWDC Sessions**: Watch technical sessions and presentations
- **Forums**: Connect with the developer community and Apple engineers

## Support and Community

### Meet with Apple
Check [Meet with Apple](https://developer.apple.com/events/) for scheduled in-person and online activities. Depending on the event and eligibility, offerings include:
- Technical presentations
- One-to-one appointments
- Hands-on labs
- Interactive workshops

### Developer Forums
Access Apple Developer Forums to:
- Discuss technical questions with developers and participating Apple engineers
- Share knowledge with the developer community
- Discuss beta behavior; submit formal bug reports through [Feedback Assistant](https://developer.apple.com/bug-reporting/)
- Discuss best practices and implementation strategies

## Platform Coverage

Build apps for all Apple platforms with a single membership:
- [iOS](iOS.md) - iPhone applications
- [iPadOS](iPadOS.md) - iPad-optimized experiences
- [macOS](macOS.md) - Desktop and laptop applications
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing experiences
- [watchOS](watchOS.md) - Wearable applications

---

*Membership fees and availability may vary by region. Some program benefits may require additional verification or approval.*

## Sources

[Apple Developer Program](https://developer.apple.com/programs/), [Apple Developer releases](https://developer.apple.com/news/releases/), [enrollment and fees](https://developer.apple.com/support/enrollment/), [Enterprise eligibility](https://developer.apple.com/programs/enterprise/), [TestFlight](https://developer.apple.com/testflight/), [requirements](https://developer.apple.com/news/upcoming-requirements/), and [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) support the checked Program and policy guidance as of September 8, 2026. The inline Analytics, fee-waiver, events, and feedback sources provide their specific qualifications. Regional fees, taxes, and account-specific terms need their own verification.

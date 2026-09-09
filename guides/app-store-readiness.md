# App Store Readiness

**Scope:** App Store submissions across Apple platforms. **Research cutoff:** September 8, 2026.

## Overview

Use this policy checklist alongside platform migration testing. Compiling against a new SDK does not establish App Review compliance, entitlement approval, or regional distribution eligibility.

## Submission Gates

| Check | Required action |
|---|---|
| Build SDK | Since **April 28, 2026**, uploads for iOS, iPadOS, tvOS, visionOS, and watchOS must use Xcode 26 or later and the corresponding 26 SDK or later. The notice does not set a macOS SDK minimum. |
| Mac upload contents | Since **February 18, 2025**, macOS apps uploaded to App Store Connect for TestFlight or the Mac App Store must have the `com.apple.quarantine` **extended file attribute removed from all files within the app**. This is an artifact check, not an `Info.plist` key or entitlement. |
| Deployment target | Choose supported older OS versions separately from the SDK used to build. Do not raise the target merely to meet the upload requirement. |
| OS27 planning | The checked requirements page gives no OS27 SDK deadline. Beta availability also does not prove that App Store Connect accepts a particular beta-built submission. |
| Age questionnaire | Updated questions for **each app** were due **January 31, 2026** to avoid interruptions to update submissions. Confirm the responses in App Store Connect; automatic rating conversion did not remove this task. |
| DSA trader status | Complete App Store Connect's trader/non-trader declaration, even if you do not distribute in the EU. Traders distributing on the EU App Store must complete the applicable contact-information verification. The **February 17, 2025** EU availability enforcement is already in effect; see [regional compliance guidance](regional-distribution.md). |

Sources: [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) and [DSA compliance instructions](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/). These are existing obligations, not new OS27 requirements. Older SDK-minimum notices retained in the index do not override the current SDK row above.

For iOS/iPadOS apps built with SDK 27, the [release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) also require a launch-screen declaration: `UILaunchStoryboardName`, `UILaunchStoryboards`, `UILaunchScreen`, or `UILaunchScreens`. Apps without one will be rejected when the App Store starts accepting SDK 27 builds. This conditional acceptance rule is not an announced SDK 27 upload deadline. See [UIKit](../documentation/UIKit.md) for scene-lifecycle launch requirements.

Before submitting, follow [guideline 2.1](https://developer.apple.com/app-store/review/guidelines/#app-completeness): remove temporary content, provide working metadata and URLs, test on-device, keep required services available, and supply reviewer access. If a demo account cannot be provided for legal/security reasons, a substitute demo mode needs Apple's prior approval. Make purchases reviewable and explain any unavailable items.

## Manifests and Product-Page Declarations

| Surface | Release check |
|---|---|
| Privacy manifests | Inventory your app and bundled SDKs. Include the applicable collection, tracking, and required-reason API entries in target resources named `PrivacyInfo.xcprivacy`; select reasons that match actual use. Apple's [manifest reference](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) scopes required-reason API declarations to iOS, iPadOS, tvOS, visionOS, and watchOS. Review the separately listed [third-party SDK manifest and signature requirements](https://developer.apple.com/support/third-party-SDK-requirements/); do not assume every SDK has the same requirements. |
| App privacy details | Reconcile the archive's privacy report with actual app and third-party data practices, then update the [App Store privacy responses](https://developer.apple.com/app-store/app-privacy-details/). A bundled manifest does not replace product-page disclosures, a privacy policy, or permission to collect/share data. |
| Accessibility Nutrition Labels | Reporting remains voluntary in the checked [Apple guidance](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels/). When reporting, evaluate each supported device separately and indicate support only when common tasks can be completed with the feature, including onboarding, login, purchases, and settings where applicable. An automated audit alone is not this evaluation. |

For third-party or user-generated content, Apple's label criteria distinguish your app's common-task interface from each contributed item. Where that content is part of common tasks, provide creators a reasonable, discoverable way to make it accessible; the guidance does not require every contributed item to be accessible before you can report support.

## Privacy, Permission, and Age Handling

- **Personal data and AI — 5.1.2(i):** explain where and how personal data is used. Clearly disclose third-party recipients, including third-party AI, and obtain explicit permission **before** sharing. A system permission to read Photos or Contacts is not blanket permission to transmit the data elsewhere. ATT permission, where applicable, is a separate requirement.
- **Failure or refusal:** cancellation, unavailable AI, or declined sharing permission must not trigger an undisclosed provider fallback. Keep unrelated functionality usable and minimize sensitive content in logs and crash reports.
- **Accounts — 5.1.1(v):** an app that supports account creation must offer account deletion within the app. Test deletion and credential revocation, not only sign-out.
- **Age range:** if using [DeclaredAgeRange](https://developer.apple.com/documentation/declaredagerange), handle declined, unavailable, or insufficient information without assuming the person is an adult. Restrict the affected content appropriately rather than collecting a full birthdate merely to fill a missing API result. An age-range API does not by itself satisfy every legal or review obligation.

Sources: [Privacy guidelines](https://developer.apple.com/app-store/review/guidelines/#privacy), especially 5.1.1 and 5.1.2. Health and children's data can have additional restrictions even when someone gives permission.

## Content Rules Have Different Scopes

| App/content type | Review scope and operational check |
|---|---|
| General user-generated content | **1.2:** provide filtering, reporting with timely responses, blocking of abusive users, and published contact information. Test moderation escalation, not just the presence of a report button. |
| Creator apps | **1.2.1(a):** provide a way to identify content exceeding the app's rating and an age restriction mechanism based on verified or declared age. This clause is specifically about **creator apps**, not a blanket extension to all UGC apps. |
| Software offered under 4.7 | The scope includes HTML5/JavaScript mini apps and mini games, streaming games, chatbots, and plug-ins; retro console and PC emulators may offer downloadable games. The host developer remains responsible for the offered software. |

For [4.7 software](https://developer.apple.com/app-store/review/guidelines/#third-party-software), review all of 4.7.1–4.7.5: privacy, moderation, and payment compliance; **Apple's prior permission** before exposing native APIs/technologies; **explicit user consent in each instance** before sharing data or permissions with individual software; an index with metadata and universal links; and identification/age restriction of software exceeding the host app's rating. Do not turn one host-level consent into authorization for every mini app.

Sources: [User-generated content](https://developer.apple.com/app-store/review/guidelines/#user-generated-content), [creator content](https://developer.apple.com/app-store/review/guidelines/#1.2.1), and [the full App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

## Purchases, Signing, and Delivery

For paid features, verify transactions before granting access and test restores, expiration, refunds, revocation, and interrupted purchases. Use the [StoreKit verification guidance](../documentation/StoreKit.md#verification-and-entitlement-handling), [App Store Server API](../documentation/AppStoreServerAPI.md), and [server notifications](../documentation/AppStoreServerNotifications.md) for the actual contracts. Exercise sandbox delivery and missed or duplicate notifications; a locally successful StoreKit test is not evidence that the production receiver works.

[StoreKit Testing in Xcode](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode) uses local `.storekit` data, even with a configuration synced from App Store Connect. Disable that configuration when testing real App Store product data in [sandbox](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox). [TestFlight purchases](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight) also use sandbox; they do not prove production product availability or server routing.

Apple's account instructions distinguish these iOS/iPadOS testing modes:

- **Development-signed app:** Sandbox Apple Account appears under Settings > Developer after a purchase attempt. There is no need to sign out of the non-Sandbox Apple Account.
- **TestFlight sandbox controls:** purchases already use sandbox, but accessing Sandbox account controls requires signing out of **Media & Purchases** and signing in with a Sandbox Apple Account under Developer. This is not signing out of iCloud. Apple warns that the Media & Purchases change can affect access to purchased content and suggests a dedicated testing device for this workflow.

Use the source's separate macOS instructions for Mac testing; neither “always sign out” nor “never sign out” is a universal rule.

Archive the intended target with its distribution configuration. Check signing identity, provisioning, capabilities, and entitlements for the selected channel; keep private signing material out of source control. Follow [Xcode's distribution workflow](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases) to validate the archive and deliver the selected build through TestFlight or App Store Connect. Xcode's automated validation is limited and does not constitute App Review approval. Record which archive was tested and submitted, not just the latest successful debug build.

**Mac notarization is a separate workflow.** Mac App Store software does not require a separate notarization submission. For Developer ID distribution outside the Mac App Store, follow [Apple's notarization instructions](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution). Since **November 1, 2023**, the notary service no longer accepts uploads from `altool` or Xcode 13 or earlier. Use the documented `notarytool` or supported Xcode workflow. That historical tool cutoff is not an OS27 SDK minimum or a rule governing every App Store Connect upload tool.

Inspect the archived app and the actual exported or distributed build using [Apple's preparation guidance](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution):

- **Identity and resources:** compare the localized display name and icons with the store listing. [Guideline 2.3.8](https://developer.apple.com/app-store/review/guidelines/#accurate-metadata) requires similar metadata to avoid confusion, not identical text in every context. Check the built `Info.plist`, selected icon assets, launch resources, and usage descriptions; a file's presence in the project does not prove it was included or selected.
- **Shipped bundles:** inspect `CFBundleShortVersionString`, `CFBundleVersion`, and capabilities/entitlements in the app and its distributed embedded apps/extensions. Check each bundle's platform and containing-app requirements rather than assuming every test target must match. Reconcile distribution-time build-number changes: Xcode can update archive contents, and **Mac build strings must increase across all app versions**, not reset universally for each marketing version.
- **Native Mac interaction:** exercise the delivered Mac app with the [pointer and trackpad interactions](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#macOS) it supports, including hover, dragging, secondary clicks, scrolling, and applicable gestures. Keyboard and primary-click tests alone do not cover those paths; retain accessibility testing too.

## Release Evidence

Record the tested OS/SDK builds, reviewer instructions, permission-denial results, age-content behavior, purchase verification results, and moderation contact. Recheck region-specific payment and distribution terms immediately before launch; don't substitute a remembered fee schedule or litigation outcome for the current agreement.

- [Regional distribution](regional-distribution.md) — storefront, device, and channel eligibility
- [Private Cloud Compute](private-cloud-compute.md) — approved access, privacy boundary, and failure handling
- [OS27 Program overview](../os27-intro/Program.md) — release baseline and membership context

## Sources

- [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) and [iOS/iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files), [third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/), and [App privacy details](https://developer.apple.com/app-store/app-privacy-details/)
- [Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels/)
- [StoreKit verification](https://developer.apple.com/documentation/storekit/verificationresult) and [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi)
- [Local StoreKit testing](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode), [sandbox testing](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox), and [TestFlight purchases](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight)
- [Preparing an app](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution), [distributing an app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases), and [Mac pointing-device guidance](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#macOS)
- [DSA trader compliance](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/) and [Mac notarization](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)

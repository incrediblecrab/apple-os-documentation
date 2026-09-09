# Regional App Distribution

**Scope:** alternative iPhone/iPad distribution and related storefront checks. **Research cutoff:** September 8, 2026.

## Overview

Treat the distribution channel, device platform, Apple Account region, physical presence, and accepted developer agreement as separate eligibility checks. Downloading a **marketplace app** from its operator's website is not the same as **Web Distribution** of your own app.

## Verified Channel Matrix

| Region | Channels confirmed by Apple | OS minimum established by the cited sources |
|---|---|---|
| European Union | Alternative marketplaces on **iPhone and iPad**; direct developer **Web Distribution** on iPhone and iPad | Marketplaces: **iOS 17.4 / iPadOS 18**. Web Distribution: **iOS 17.5 / iPadOS 18**. |
| Brazil | Alternative marketplaces and their apps on **iPhone** | Fixed minimum **not verified here**. Apple's user guidance recommends updating to the latest iOS; do not reuse the EU minimum. |
| Japan | Alternative marketplaces and their apps on **iPhone** | Fixed minimum **not verified here**. Confirm the current Japan-specific prerequisites; do not reuse EU marketplace or web-distribution minima. |

[Apple's alternative-distribution support article](https://support.apple.com/en-us/118110) establishes the country/device/channel scope. It does **not** establish iPad marketplaces or direct app Web Distribution in Brazil or Japan. The EU minima come from [alternative app marketplaces in the EU](https://developer.apple.com/support/alternative-app-marketplace-in-the-eu/) and [Web Distribution in the EU](https://developer.apple.com/support/web-distribution-eu/), not from MarketplaceKit's API availability annotation.

## Eligibility and Failure Handling

1. **Check the intended route.** Having a Developer Program membership or a compilable MarketplaceKit integration does not establish approval to operate a marketplace or distribute from a website. Verify the capability, applicable agreement, and account status.
2. **Respect user eligibility.** Apple requires the account country/region and physical location to match the eligible region. Use system eligibility results; do not invent a location test or ask people to bypass restrictions.
3. **Handle unavailable installation.** Explain whether the required OS, channel, account eligibility, approval, or parental-control setting is missing. Offer an eligible alternative where available; don't keep retrying an installation the person declined.
4. **Plan travel behavior.** Apple says previously installed apps can still be opened after leaving the eligible region, and updates may continue for up to **90 days**. New marketplace/app installations require presence in the eligible region. Do not promise indefinite updates while abroad.
5. **Plan distributor failure.** Apps can stop functioning if their marketplace closes or is deleted. Explain support, data export, restoration, and any limitations on moving purchases between distribution channels.

Source for user eligibility, travel, and marketplace-failure behavior: [Apple Support 118110](https://support.apple.com/en-us/118110).

## Review and Support Responsibilities

**Notarization is a baseline integrity review, not full App Store approval.** Alternative distributors have their own content review and support processes. Make responsibility for payments, refunds, subscriptions, privacy questions, and account recovery clear. App Store features such as Ask to Buy and purchase sharing are not automatically provided for alternative-channel purchases. See [Apple's support comparison](https://support.apple.com/en-us/118110) and the [Notarization Review Guidelines within App Review](https://developer.apple.com/app-store/review/guidelines/).

EU Web Distribution requires an authorized developer and a website domain registered in App Store Connect. Provide signed assets through the approved process; do not describe any arbitrary website download as an eligible installation.

## Agreements, Payments, and Effective Dates

- **DSA trader compliance is already enforced:** [App Store Connect requires a trader/non-trader declaration](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/), even without EU App Store distribution. Traders distributing on the EU App Store must provide verified contact details for their product pages. Apple's [historical notices](https://developer.apple.com/news/upcoming-requirements/) set the update-submission gate at **October 16, 2024** and EU removal of noncompliant apps at **February 17, 2025**, until compliance is resolved. Assess trader status rather than assuming membership determines it. This App Store compliance process is not an OS27 API requirement or approval for alternative marketplace/Web Distribution.
- **EU transition announced, not yet effective at this cutoff:** Apple's [Web Distribution page](https://developer.apple.com/support/web-distribution-eu/) describes an **October 1, 2026** transition to unified EU terms and capability issuance for that route. Earlier access has different conditions. Check which agreement is accepted and when it takes effect; old accrued obligations are not erased by switching agreements.
- **United States storefront:** [guideline 3.1.1(a)](https://developer.apple.com/app-store/review/guidelines/#link-to-other-purchase-methods) says an entitlement is not required for buttons, external links, or other calls to action to other purchase methods in US storefront apps. This is not a worldwide exception, permission for every payment implementation, or a statement that all fees disappear.
- **Fees, taxes, and legal proceedings:** this guide does not reproduce a global commission table or unverified litigation/tax dates. Confirm the current regional terms, transaction reporting, tax responsibilities, and App Store Connect notices for your account before launch. Do not apply historical EU per-install fees or one country's terms to every route.

See [App Store readiness](app-store-readiness.md) for content and permission requirements. Policy eligibility is separate from an API's deployment availability.

*Sources: [Apple Support](https://support.apple.com/en-us/118110), [EU marketplaces](https://developer.apple.com/support/alternative-app-marketplace-in-the-eu/), [EU Web Distribution](https://developer.apple.com/support/web-distribution-eu/), [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [DSA compliance](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/), and [historical requirements](https://developer.apple.com/news/upcoming-requirements/). Checked September 8, 2026; each source's scope is identified above.*

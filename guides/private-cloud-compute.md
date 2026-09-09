# Private Cloud Compute Security Guide

**Scope:** an original developer summary of PCC's privacy boundary and approved app access. **Research cutoff:** September 8, 2026.

## Overview

Private Cloud Compute (PCC) is Apple's infrastructure for server-side Apple Intelligence processing. It is not ordinary on-device inference, an arbitrary cloud endpoint for your server, or a promise that every AI feature in your app uses PCC.

The [OS27 Foundation Models API](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel) exposes `PrivateCloudComputeLanguageModel` for iOS, iPadOS, Mac Catalyst, macOS, visionOS, and watchOS 27 or later; tvOS is not listed. API availability does not establish device, region, account, or developer eligibility.

## What the Security Architecture Covers

Apple's [PCC Security Guide](https://security.apple.com/documentation/private-cloud-compute/) describes a narrower trust boundary than a conventional application server:

- **Request-limited processing:** personal data is used to fulfill the request, with statelessness and restrictions on retention. The guide also discusses possible encrypted caches controlled by keys from the user's device; avoid an overbroad claim about every future storage mechanism. See [core requirements](https://security.apple.com/documentation/private-cloud-compute/corerequirements).
- **No privileged bypass:** the design excludes privileged runtime access that would let an operator bypass the stated privacy protections. This is a PCC design property, not a security assessment of your own code or dependencies.
- **Client validation:** the device validates node attestations before making request-decryption keys available to trusted PCC nodes. Requests pass through privacy-preserving transport rather than giving an ordinary application proxy plaintext access. See [request flow](https://security.apple.com/documentation/private-cloud-compute/requestflow).
- **Inspectable releases:** clients check software measurements against an append-only transparency log, and researchers can inspect published builds. See [release transparency](https://security.apple.com/documentation/private-cloud-compute/releasetransparency).

These protections do not cover sensitive text your app separately puts in analytics, crash reports, a third-party AI prompt, or your own backend logs.

## Approval and Eligibility

The checked [Accessing Private Cloud Compute](https://developer.apple.com/private-cloud-compute/) page requires:

1. Enrollment in the **App Store Small Business Program**.
2. Fewer than **two million first-time App Store downloads for any of the developer's apps**, as defined by Apple.
3. The managed **PCC entitlement assigned to the developer account**.

Approved access is for App Store apps where Apple Intelligence is available, with TestFlight or ad hoc distribution for testing. Testing installs do not count toward first-time downloads. Apple's no-cloud-API-cost offer is conditional on these eligibility rules, not a free service available to every developer.

If an app exceeds the threshold or Small Business Program enrollment ends, Apple says the developer will be notified and must migrate to an alternative within **six months**. Plan that transition without silently changing who receives personal data. [Request the entitlement](https://developer.apple.com/contact/request/private-cloud-compute/) and verify approval before advertising availability.

## Permissions and Failure Handling

| State | Recommended behavior |
|---|---|
| Missing developer approval or unsupported OS | Keep the feature unavailable or offer a non-PCC path; installing the SDK is not approval. |
| Model unavailable | Check `availability`/`isAvailable`. Distinguish an ineligible device from a system that is not ready; keep unrelated app features usable. |
| Quota reached | Inspect the reported quota state, explain the limit, and defer/retry appropriately. Do not promise unlimited requests because API access has no cloud charge. |
| Network or service failure | Preserve the person's work, allow cancellation, and use bounded retries. Never silently transmit the same prompt to another provider. |
| Permission declined or sensitive content excluded | Respect the decision. Obtain any required permission before data leaves its authorized context, and minimize what enters prompts or diagnostics. |

The API documents [availability reasons](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/availability-swift.enum/unavailablereason) and distinct [quota, network, and service errors](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error). They are not a fixed hardware whitelist or an assurance that a request will succeed after an availability check.

[App Review 5.1.2(i)](https://developer.apple.com/app-store/review/guidelines/#data-use-and-sharing) still governs personal-data use and sharing. In particular, clearly disclose and obtain explicit permission before a fallback shares personal data with third-party AI. PCC's architecture does not supply consent for your app or remove additional restrictions on health or children's data.

## Verification Before Release

Test absent entitlement, unavailable model, quota exhaustion, interrupted requests, and an explicit refusal to share. Record OS and SDK builds, minimize test data, and document your fallback without implying equivalent privacy guarantees across providers. The iOS/visionOS beta 8 notes mark earlier PCC simulator failures as resolved; do not treat those old beta failures as permanent restrictions.

- [iOS & iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [visionOS 27 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes)
- [App Store readiness](app-store-readiness.md)

## Sources

[PCC Security Guide](https://security.apple.com/documentation/private-cloud-compute/), [PCC access requirements](https://developer.apple.com/private-cloud-compute/), [Foundation Models API](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel), and [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). Checked September 8, 2026; chapter-level and error references are linked above.

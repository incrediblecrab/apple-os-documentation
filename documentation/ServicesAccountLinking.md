# ServicesAccountLinking

Associate an authorized reseller account with a person's Apple Media & Purchases account.

**Platforms:** iOS 16.4+ | iPadOS 16.4+ | Mac Catalyst 16.4+. This existing partner-integration framework is not an OS 27 introduction.

## Overview

ServicesAccountLinking lets participating content providers and channel partners register a reseller account identifier or signed entitlement token with Apple's media-services account system. It is not a general-purpose login framework, an account-directory API, or a substitute for Sign in with Apple.

The user's reseller account, the partner's entitlement data, and the Apple Media & Purchases account are distinct. Complete your own account authentication before attempting to link the intended reseller account.

## Prerequisites and authorization

- Enroll the application in Apple's channel partnership program.
- Obtain the partner credentials needed to produce the required identifier or signed token.
- Target a supported platform and use the token format supplied through the partner integration. Public documentation does not define a universal reseller-token schema.
- Keep partner signing credentials on the appropriate trusted backend; do not embed them in the application or log entitlement tokens.

## Topics

- [`ResellerAccount`](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount) — Entry point for account registration.
- [`registerToken(_:)`](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registertoken(_:)) — Asynchronously register a signed entitlement token; the method throws on failure.
- [`registerIdentifier(_:)`](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registeridentifier(_:)) — Asynchronously register the partner's entitlement identifier as a UUID string, not an arbitrary username; the method throws on failure.
- [`RegistrationError`](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror) and [`RegistrationErrorDomain`](https://developer.apple.com/documentation/servicesaccountlinking/registrationerrordomain) — Inspect registration failures. The framework catalog labels the domain `SALRegistrationErrorDomain`; the Swift declaration is `RegistrationErrorDomain`.

The current Swift declaration of `registerToken(_:)` uses `@backDeployed(before: iOS 26.2)`. That declaration is not evidence that the framework requires iOS 26.2 or OS 27; consult the symbol's availability and the SDK used to compile the app.

## Failure handling

[`notEligible`](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/noteligible) means the application is not an authorized partner. Resolve enrollment with the channel partnership program rather than repeatedly retrying or asking the user to change account credentials.

The registration contract also identifies [`failed`](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/failed) for other failures, including a person not being signed into an Apple Media & Purchases account or a system error. Preserve the unsuccessful linking state, provide a retry path where appropriate, and avoid claiming that a service entitlement is linked until registration succeeds. Handle unknown errors defensively without exposing account identifiers or token contents.

## Sources

- [ServicesAccountLinking](https://developer.apple.com/documentation/servicesaccountlinking)
- [ResellerAccount](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount)
- [Token registration](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registertoken(_:))
- [Partner eligibility error](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/noteligible)

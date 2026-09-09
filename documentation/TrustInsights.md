# Trust Insights

Use privacy-preserving signals to help recognize potentially coerced transactions.

**Evaluation API declarations:** iOS 27.0+ | iPadOS 27.0+. The framework catalog additionally lists Mac Catalyst 27; see the declaration/provisioning distinction below.

**Status:** Beta APIs; reviewed against Apple documentation available September 8, 2026.

## Overview

Trust Insights helps an app decide whether an action merits additional checks for social engineering. It evaluates the circumstances of an interaction, rather than authenticating an identity, validating a payment, or proving that a transaction is safe.

An app supplies an operation context to `InsightEvaluator`. The documented categories cover payments, account changes, resource use, communication, and other actions. The currently documented insight, `IsLikelyBeingCoachedInsight`, concerns indications that another person may be coaching the interaction.

## Authorization and configuration

- Enable the [Trust Insights entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.trustinsights.base) through the target's capability configuration. `com.apple.developer.trustinsights.base` is a **string-valued** entitlement, not a Boolean permission switch; do not invent its value.
- The framework's availability metadata includes Mac Catalyst 27.0, while the authorization/evaluation methods and entitlement reference list iOS and iPadOS. The catalog alone does not establish functional Catalyst or native macOS evaluation support.
- Check [`authorizationStatus(for:)`](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationStatus(for:)) for the current context. `.notDetermined` and `.deniedRequestable` permit an authorization request; `.denied` and `.unavailable` do not authorize evaluation.
- Explain the purpose before calling [`requestAuthorization(for:)`](https://developer.apple.com/documentation/trustinsights/insightevaluator/requestAuthorization(for:)). Respect refusal and recheck authorization rather than treating a previous grant as permanent.

## Evaluation and failure handling

Construct a context with the required operation category and insight request, then use [`requestEvaluation(context:)`](https://developer.apple.com/documentation/trustinsights/insightevaluator/requestEvaluation(context:)). Handle both request failures and failures in an individual insight's outcome.

The documented evaluation includes on-device and Apple-server processing and can take several seconds; it is not an instant, offline-only check.

Keep an explicit fallback for unavailable service, denied permission, unknown results, and future cases. Missing evidence is not proof that an interaction is legitimate. Conversely, an elevated signal is not proof of fraud: an appropriate response may be an explanation or an additional confirmation, rather than an irreversible decision.

Before releasing an evaluation, report how it affected the interaction through [`reportConsumption(_:insightsUsed:)`](https://developer.apple.com/documentation/trustinsights/insightevaluation/reportConsumption(_:insightsUsed:)), including when its results were not used. Failure to report consumption can result in rate limiting or loss of service access. Keep diagnostics free of transaction secrets and unnecessary personal information.

## Topics

- [InsightEvaluator](https://developer.apple.com/documentation/trustinsights/insightevaluator) — Context, authorization, and evaluation entry points.
- [IsLikelyBeingCoachedInsight](https://developer.apple.com/documentation/trustinsights/islikelybeingcoachedinsight) — The documented coaching-related signal.
- [InsightEvaluation](https://developer.apple.com/documentation/trustinsights/insightevaluation) — Evaluation results and consumption reporting.
- [AuthorizationStatus](https://developer.apple.com/documentation/trustinsights/insightevaluator/authorizationstatus) — Authorized, requestable, denied, and unavailable states.
- [InsightError](https://developer.apple.com/documentation/trustinsights/insighterror) — Insight-specific failure conditions.

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/trustinsights)
- [Readable framework documentation](https://developer.apple.com/documentation/trustinsights.md)
- [Entitlement reference](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.trustinsights.base.md)

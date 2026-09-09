# Account Data Transfer

Download App Store information, app-install activity, and push-notification activity with the account holder's authorization.

**Platforms:** Account Data Transfer 1.0+

## Overview

This web API exports account-level information with the person's approval. It is distinct from [App Data Transfer](AppDataTransfer.md), which concerns your own app, and [AppMigrationKit](AppMigrationKit.md), which transfers on-device app resources to another platform. Service scope is not tied to the OS 27 SDK.

## Authorization and regions

The [canonical reference](https://developer.apple.com/documentation/accountdatatransfer) now lists the **EU, UK, and Japan**, including push-notification activity alongside app-install activity. The portal includes `data-transfer-user-profile` when requesting other scopes.

| Data | EU scope | UK scope | Japan scope |
| --- | --- | --- | --- |
| App Store information | `appstore-info-account-data-for-EU-users` | `appstore-info-account-data-for-UK-users` | `appstore-info-account-data-for-JP-users` |
| App install and push activity | `app-install-activity-account-data-for-EU-users` | `app-install-activity-account-data-for-UK-users` | `app-install-activity-account-data-for-JP-users` |

Combine categories only as allowed in the reference's same-region scope table. Previously approved `appstore-user-profile` and older scope names remain accepted for the EU/UK compatibility path; that does not establish a Japan grant. [Request access](https://developer.apple.com/contact/request/account-data-transfer-api/) for the required scopes and use the [authorization endpoint](https://developer.apple.com/documentation/accountorganizationaldatasharing/request-an-authorization).

After Apple grants Account Data Transfer access, the reference says an authorization-token request for **App Data Transfer** need not include `consent_mode`. Do not generalize this exception to unrelated authorization flows.

### HTTP headers

- `Authorization`: Supply authorization for the approved profile and requested data scopes. Follow the [Submit request endpoint](https://developer.apple.com/documentation/accountdatatransfer/submit-request); the redacted value in Apple's example is not a usable credential. Keep tokens out of source code and logs.
- `X-Apple-Transaction-Id`: Generate a UUID for the request and retain it for support diagnostics.

## Request lifecycle

### Submission

Submit a `POST` request for the required data with `mode: ONE_TIME`, or use `DAILY_30`/`WEEKLY_180` for supported recurring requests. Save the returned `requestId`, any `parentRequestId`, and `statusCheckDelay` in seconds.

Use the canonical scope/frequency table rather than assuming arbitrary scopes can be mixed. A second pending recurring request returns an error identifying the existing request.

### Status and download

Wait at least `statusCheckDelay` before querying status, and honor updated delays in status responses. Inspect `jobStatus`, not merely the operation's `status` field. When `jobStatus` is `completed` or `completed_with_error`, request download URLs using the corresponding one-time or recurring endpoint; inspect any reported errors instead of treating partial completion as an entirely successful export.

Download links can be requested for three days after the download request completes. Each set of returned URLs expires after 15 minutes. Keep those URLs private and avoid persisting them as permanent resource identifiers. Consult the [data-file guide](https://privacy.apple.com/file-guides/transfer/accountdata) when interpreting the downloaded content.

### Recurrence and cancellation

Resubmit an eligible recurring instance with `parentRequestId` and the most recent instance's `requestId`. Checking status does not enqueue another export. The current reference gives expiry after 40 days for an unresubmitted `DAILY_30` series and 190 days for an unresubmitted `WEEKLY_180` series, measured from the initial submission.

Cancellation succeeds only while a request is in progress, including during the initial status-check delay.

### Source contract discrepancies

- The scope table lists recurring support for App Store information, but the frequency and resubmission prose specifically describes app-install/push activity. Do not infer unrestricted App Store-only recurrence from the table; confirm eligibility for the approved scopes.
- The [`CancellationRequest`](https://developer.apple.com/documentation/accountdatatransfer/cancellationrequest) property description says to supply the recurring **parent** UUID as `requestId`; the [cancellation example](https://developer.apple.com/documentation/accountdatatransfer/cancel-request) supplies an **instance** UUID. Confirm the required identifier before automating recurring cancellation; the sources do not establish that these are interchangeable.
- The cancellation endpoint's URL definition uses `/api/transfer/accountdata/cancel`. The recurring example's `accountadata` spelling is inconsistent with that definition and should not be copied.

## Topics

### Request creation
- [Submit request](https://developer.apple.com/documentation/accountdatatransfer/submit-request) - Starts a download job.
- **JobSubmission**, **CreatedJob** - Submission and created-job data.
- [Resubmit request](https://developer.apple.com/documentation/accountdatatransfer/resubmit-request) - Enqueues the next recurring instance.
- **ResubmissionRequest**, **ResubmissionResponse** - Recurrence request and response data.

### Status
- [Get one-time request status](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-status)
- [Get recurring request status](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-status)
- **RequestStatus** - Job status and associated data.

### Downloads
- [Get one-time request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-download-urls)
- [Get recurring request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-download-urls)
- **DownloadLinks**, **DownloadError** - Download locations and preparation errors.

### Cancellation
- [Cancel request](https://developer.apple.com/documentation/accountdatatransfer/cancel-request)
- **CancellationRequest**, **CancellationResponse** - The selected request and cancellation result.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccountDataTransfer)*

# App Data Transfer

Download App Store information and app-install activity about your app.

**Platforms:** App Data Transfer 1.0+

## Overview

Use this web API to export authorized App Store and app-install information specific to your app for users in the **EU and UK**. Integrate each app separately. This service is not [AppMigrationKit](AppMigrationKit.md), which transfers local app resources between device platforms, or [Account Data Transfer](AccountDataTransfer.md), which covers broader account information.

## Authorization and scope compatibility

The [current reference](https://developer.apple.com/documentation/appdatatransfer) requires `data-transfer-user-profile` and at least one of:

- `appstore-info-readonly`
- `app-install-activity-readonly`

It retains compatibility for previously approved `appstore-user-profile` and older scope names in the **EU/UK**, without requiring a new token request for that transition. Do not infer Japan coverage here from the separate Account Data Transfer API.

Obtain the required permission through [Account & Organizational Data Sharing](https://developer.apple.com/help/account/share-account-data/share-account-and-organizational-data/) and use the [authorization endpoint](https://developer.apple.com/documentation/accountorganizationaldatasharing/request-an-authorization).

### HTTP headers

- `Authorization`: Supply authorization for the approved scopes using the [Submit request contract](https://developer.apple.com/documentation/appdatatransfer/submit-request). Apple's redacted example is not a usable token; never commit credentials.
- `X-Apple-Transaction-Id`: Assign a request UUID and retain it for troubleshooting.

## Request lifecycle

1. **Submit:** Send a `POST` request for `app-store` data. Use `ONE_TIME` for a single export, or `DAILY_30`/`WEEKLY_180` for the documented recurring modes.
2. **Retain identifiers:** Store `requestId`, `parentRequestId` for a recurring series, and `statusCheckDelay` in seconds. A second pending recurring request returns an error identifying the existing series.
3. **Check status:** Wait for the server's delay before using the matching one-time or recurring status endpoint, and honor updated delays. Inspect `jobStatus`, not merely the operation's `status`. `completed_with_error` requires checking error details, not assuming every requested file is present.
4. **Download:** Ask for URLs after completion. The download window lasts three days; each returned URL lasts 15 minutes. Handle expiration by following the download-URL flow, not by caching links indefinitely. See the [data-file guide](https://privacy.apple.com/file-guides/transfer/appdata).
5. **Resubmit or cancel:** Enqueue a recurring instance with `parentRequestId` and the latest instance's `requestId`, or cancel an active request. Cancellation succeeds only while the request is in progress, including during the initial delay.

Recurrence requires explicit resubmission. The current reference gives expiry after 40 days for an unresubmitted `DAILY_30` series and 190 days for an unresubmitted `WEEKLY_180` series. These are service rules, not OS 27 deployment requirements.

### Recurring cancellation qualification

The [`CancellationRequest`](https://developer.apple.com/documentation/appdatatransfer/cancellationrequest) property description says to place the recurring **parent** UUID in `requestId`, while the [cancellation example](https://developer.apple.com/documentation/appdatatransfer/cancel-request) supplies an **instance** UUID. Confirm the required identifier before automating recurring cancellation; the sources do not establish that these are interchangeable.

## Topics

### Request creation
- [Submit request](https://developer.apple.com/documentation/appdatatransfer/submit-request)
- **JobSubmission**, **CreatedJob** - Submission and created-job data.
- [Resubmit request](https://developer.apple.com/documentation/appdatatransfer/resubmit-request)
- **ResubmissionRequest**, **ResubmissionResponse** - Recurrence request and response data.

### Status
- [Get one-time request status](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-status)
- [Get recurring request status](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-status)
- **RequestStatus** - Job status.

### Downloads
- [Get one-time request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-download-urls)
- [Get recurring request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-download-urls)
- **DownloadLinks**, **DownloadError** - Download locations and preparation errors.

### Cancellation
- [Cancel request](https://developer.apple.com/documentation/appdatatransfer/cancel-request)
- **CancellationRequest**, **CancellationResponse** - Cancellation input and result.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppDataTransfer)*

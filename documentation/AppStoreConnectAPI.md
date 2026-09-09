# App Store Connect API

Automate the tasks you perform on the Apple Developer website and in App Store Connect.

**Service:** Independently versioned REST API; its version numbers are not Apple OS deployment targets.

## Overview

The App Store Connect API automates supported App Store Connect and developer-account operations. Use Apple's [OpenAPI specification](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip) when generating a client or checking exact request and response schemas.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization's App Store Connect account. See Creating API Keys for App Store Connect API to create your keys and tokens.

Important: Changes you make using the App Store Connect API affect the production data you use for development and distribution.

The API provides resources to automate these areas of App Store Connect:

- **In-App Purchases and Subscriptions.** Manage in-app purchases and auto-renewable subscriptions for your app.
- **TestFlight.** Manage beta builds of your app, testers, and groups.
- **Xcode Cloud.** Read Xcode Cloud data, manage workflows, and start builds.
- **Users and Access.** Send invitations for users to join your team. Adjust their level of access or remove users.
- **Provisioning.** Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
- **App Metadata.** Create new versions, manage App Store information, and submit your app to the App Store.
- **App Clip Experiences.** Read existing App Clip metadata and create, update, or delete its experiences.
- **Reporting.** Download sales and financial reports.
- **Power and Performance Metrics.** Download aggregate metrics and diagnostics for App Store versions of your app.
- **Customer Reviews and Review Responses.** Get the customer reviews for your app and manage your responses to the customer reviews.

The App Store Connect API returns responses from resources that are consistent JSON data and contain links to additional related resources. Use these relationships to navigate to the related resources—for example, to find beta testers within specific beta groups in TestFlight. Apply filtering to requests on specific resources to refine the response.

## Service changes reviewed September 8, 2026

The [4.4.1 release notes](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-4-1-release-notes) add discrete metadata versions for in-app purchases, subscriptions, and subscription groups. Localizations are version-scoped; in-app purchase review images and subscription promotional images attach to their respective versions. Subscription group versions have localizations, not an image relationship. Review submission items can refer to `inAppPurchaseVersion`, `subscriptionVersion`, or `subscriptionGroupVersion`.

Review [`InAppPurchaseVersion`](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseversion), [`SubscriptionVersion`](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionversion), and [`SubscriptionGroupVersion`](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupversion) when updating automation. The notes formally deprecate older localization/image and submission resources in favor of version-scoped resources and Review submissions; they do not announce their immediate removal.

The same release adds `socialMedia` and `socialMediaAgeRestricted` age-rating declaration attributes. Check the current schema rather than assuming an older generated client exposes every field.

API versions, the App Store Connect application, TestFlight releases, and upload SDK requirements have separate lifecycles. See [App Store readiness](../guides/app-store-readiness.md) and [Regional distribution](../guides/regional-distribution.md) for submission and policy guidance; do not infer an OS 27 upload deadline from an API release.

### Authorization and failure handling

Team keys require an Admin to generate them and can access all apps within their assigned role; they are not restricted to one app. Individual keys inherit their user's app access and permissions, require the **Generate Individual API Keys** permission, and cannot use provisioning, Sales and Finance, or `notaryTool`. Download a private key once, store it securely on the server, and revoke a lost or compromised key; revocation cannot be undone.

Sign JWTs with ES256 and use the `appstoreconnect-v1` audience. Team tokens use `iss`; individual tokens use `sub: "user"` instead of `iss`. Most requests require a token lifetime of at most 20 minutes. The token guide permits up to six months only for explicitly scoped GET requests to its listed eligible resources—not for arbitrary reads or writes.

Read the returned `X-Rate-Limit` values; limits vary and use a rolling hour per API key. Handle HTTP 429 separately from authentication, permission, and validation errors. Follow pagination links and retain structured error codes and locations. Because writes affect production data, read and reconcile the relevant metadata version before retrying a timed-out mutation or submission.

Asset uploads require reservation, uploading all specified byte ranges, committing the upload, and checking processing completion. Use the returned upload URLs and headers rather than forwarding the API JWT to an asset URL. `UPLOAD_COMPLETE` is not final success: processing must reach `COMPLETE`; a terminal `FAILED` asset requires a new reservation after correcting the cause.

## Topics

### Essentials
- [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api) - Create API keys to sign JWTs and authorize API requests.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests) - Create JWTs signed with your private key.
- [Revoking API Keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys) - Revoke unused, lost, or compromised private keys.
- [Identifying Rate Limits](https://developer.apple.com/documentation/appstoreconnectapi/identifying-rate-limits) - Recognize and handle REST API rate limits.
- [Uploading Assets to App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect) - Upload screenshots, previews, review attachments, and routing coverage files.
- [App Store Connect API Release Notes](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-release-notes) - Review the service's versions independently of OS SDK releases.

### App Store
- **App Store** - Manage app metadata, App Clip records, in-app purchases, and customer reviews.

### TestFlight
- **Prerelease Versions and Beta Testers** - Manage your beta testing program, including beta testers and groups, apps, App Clips, and builds.

### Game Center
- **Game Center** - Manage Game Center data and configurations for your apps.

### Provisioning
- **Bundle IDs** - Manage the bundle IDs that uniquely identify your apps.
- **Bundle ID Capabilities** - Manage the app capabilities for a bundle ID.
- **Certificates** - Create, download, and revoke signing certificates for app development and distribution.
- **Devices** - Register devices for development and testing.
- **Profiles** - Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- **Merchant ID** - Manage your merchant ID for Apple Pay.
- **Pass type IDs** - Register, read, modify, and delete pass type identifiers; their signing certificates are separate resources.

### Xcode Cloud
- **Xcode Cloud Workflows and Builds** - Automate reading Xcode Cloud data, managing workflows, and starting builds.

### Webhooks
- **Webhook notifications** - Manage notifications from App Store about your apps and their statuses.

### Reporting
- **Sales and Finance** - Download your sales and financial reports.
- **Power and Performance Metrics and Logs** - Get power and performance metrics, logs, and signatures.
- **Analytics** - Get data about your apps and usage.

### Users and Access
- **Users** - Manage users on your App Store Connect team.
- **User Invitations** - Email invitations to join your App Store Connect team.
- **Sandbox Testers** - Manage sandbox testers on your App Store Connect team.

### Error Handling
- **Interpreting and Handling Errors** - Learn how the App Store Connect API returns errors and handle them in your code.

### Paging
- **Large Data Sets** - Retrieve large data sets with paging information.

### Alternative App Distribution
- **Alternative Marketplaces and Web Distribution** - Manage keys, packages, and search for alternative app distribution.

### Endpoints
These selected relationship endpoints return resource linkage, not full related objects. The 4.4.1 OpenAPI specification marks five as deprecated; their presence there is not a removal announcement.
- `GET /v1/appEncryptionDeclarations/{id}/relationships/app` — deprecated.
- `GET /v1/appStoreVersions/{id}/relationships/appStoreVersionExperiments` — deprecated.
- `GET /v1/apps/{id}/relationships/inAppPurchases` — deprecated.
- `GET /v1/builds/{id}/relationships/app`.
- `GET /v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievement` — deprecated.
- `GET /v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboard` — deprecated.

### Dictionaries
- **CiBranchStartCondition** - Settings for a start condition that starts a build if a branch changes.
- **CiFilesAndFoldersRule** - Settings Xcode Cloud uses to determine whether a change should start a new build or not.
- **CiGitUser** - Git-user display information, including a display name and avatar URL.
- **CiIssueCounts** - Counts of analyzer warnings, errors, test failures, and warnings.
- **CiPullRequestStartCondition** - Settings for a start condition that starts a build if a pull request changes.
- **CiScheduledStartCondition** - Settings for a start condition that starts a build based on a schedule.
- **CiTagStartCondition** - Settings for a start condition that starts a build if a Git tag changes.
- **CiTestDestination** - The test destination of a test action that Xcode Cloud performs.
- **DeliveryFileUploadOperation**
- **JsonPointer** - An object that contains the JSON pointer that indicates the location of the error.
- **Parameter** - An object that contains the query parameter that produced the error.
- **StringToStringMap**
- **SubscriptionOfferCodesLinkagesResponse**

### String and Enumeration Types
- **BackgroundAssetVersionState**
- **BuildAudienceType** - A string that represents the App Store Connect audience for a build.
- **BuildBundleType**
- **CiActionType** - A string that represents the type of an Xcode Cloud workflow's action.
- **CiCompletionStatus** - A string that represents the completion status of an Xcode Cloud build.
- **CiExecutionProgress** - A string that represents the progress of an ongoing Xcode Cloud build.
- **CiTestDestinationKind** - The string that represents the kind of a test destination.
- **CiTestStatus** - A string that represents test status information.
- **DeviceConnectionType**
- **DiagnosticInsightDirection** - A string that describes the diagnostic insight direction.
- **DiagnosticInsightType** - A string that describes the diagnostic insight type.
- **GameCenterLeaderboardFormatter** - The values you can select to describe the format of a leaderboard.
- **GameCenterVersionState**
- **TerritoryCode** - The App Store territory codes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppStoreConnectAPI)*

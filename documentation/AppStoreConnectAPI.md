# App Store Connect API

Automate the tasks you perform on the Apple Developer website and in App Store Connect.

**Platforms:** App Store Connect API 1.0+

## Overview

The App Store Connect API is a REST API that enables the automation of actions you take in App Store Connect. Click OpenAPI specification to download the specification file.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization's App Store Connect account. See Creating API Keys for App Store Connect API to create your keys and tokens.

Important: Changes you make using the App Store Connect API affect the production data you use for development and distribution.

The API provides resources to automate these areas of App Store Connect:

- **In-App Purchases and Subscriptions.** Manage in-app purchases and auto-renewable subscriptions for your app.
- **TestFlight.** Manage beta builds of your app, testers, and groups.
- **Xcode Cloud.** Read Xcode Cloud data, manage workflows, and start builds.
- **Users and Access.** Send invitations for users to join your team. Adjust their level of access or remove users.
- **Provisioning.** Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
- **App Metadata.** Create new versions, manage App Store information, and submit your app to the App Store.
- **App Clip Experiences.** Create an App Clip and manage App Clip experiences.
- **Reporting.** Download sales and financial reports.
- **Power and Performance Metrics.** Download aggregate metrics and diagnostics for App Store versions of your app.
- **Customer Reviews and Review Responses.** Get the customer reviews for your app and manage your responses to the customer reviews.

The App Store Connect API returns responses from resources that are consistent JSON data and contain links to additional related resources. Use these relationships to navigate to the related resources—for example, to find beta testers within specific beta groups in TestFlight. Apply filtering to requests on specific resources to refine the response.

## Topics

### Essentials
- [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/AppStoreConnectAPI/creating_api_keys_for_app_store_connect_api) - Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/AppStoreConnectAPI/generating_tokens_for_api_requests) - Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Revoking API Keys](https://developer.apple.com/documentation/AppStoreConnectAPI/revoking_api_keys) - Revoke unused, lost, or compromised private keys.
- [Identifying Rate Limits](https://developer.apple.com/documentation/AppStoreConnectAPI/identifying_rate_limits) - Recognize the rate limits that REST API responses provide and handle them in your code.
- [Uploading Assets to App Store Connect](https://developer.apple.com/documentation/AppStoreConnectAPI/uploading_assets_to_app_store_connect) - Upload screenshots, app previews, attachments for App Review, and routing app coverage files to App Store Connect.
- [App Store Connect API Release Notes](https://developer.apple.com/documentation/AppStoreConnectAPI/app_store_connect_api_release_notes) - Learn about new features and updates in the App Store Connect API.

### App Store
- **App Store** - Manage all aspects of your app, App Clips, in-app purchases, and customer reviews in the App Store.

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
- **Pass type Ids** - Create, download, and revoke pass type ids for app development and distribution.

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
- GET /v1/appEncryptionDeclarations/{id}/relationships/app
- GET /v1/appStoreVersions/{id}/relationships/appStoreVersionExperiments
- GET /v1/apps/{id}/relationships/inAppPurchases
- GET /v1/builds/{id}/relationships/app
- GET /v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievement
- GET /v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboard

### Dictionaries
- **CiBranchStartCondition** - Settings for a start condition that starts a build if a branch changes.
- **CiFilesAndFoldersRule** - Settings Xcode Cloud uses to determine whether a change should start a new build or not.
- **CiGitUser** - The data structure that represents a Git Users resource.
- **CiIssueCounts** - The data structure that represents an Issue Counts resource.
- **CiPullRequestStartCondition** - Settings for a start condition that starts a build if a pull request changes.
- **CiScheduledStartCondition** - Settings for a start condition that starts a build based on a schedule.
- **CiTagStartCondition** - Settings for a start condition that starts a build if a Git tag changes.
- **CiTestDestination** - The test destination of a test action that Xcode Cloud performs.
- **DeliveryFileUploadOperation**
- **JsonPointer** - An object that contains the JSON pointer that indicates the location of the error.
- **Parameter** - An object that contains the query parameter that produced the error.
- **StringToStringMap**
- **SubscriptionOfferCodesLinkagesResponse**

### Type Aliases
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
- **DiagnosticInsightType** - A string that desribes the diagnostic insight type.
- **GameCenterLeaderboardFormatter** - The values you can select to describe the format of a leaderboard.
- **GameCenterVersionState**
- **TerritoryCode** - The App Store territory codes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppStoreConnectAPI)*
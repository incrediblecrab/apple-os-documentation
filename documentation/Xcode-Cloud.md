# Xcode Cloud

Automatically build, test, and distribute your apps with Xcode Cloud to verify changes and create high-quality apps.

## Overview

Xcode Cloud lets you adopt continuous integration and delivery (CI/CD), a standard software development practice that helps you develop and maintain your code and deliver apps to testers and users. Xcode Cloud is a CI/CD system that combines the tools you use to create apps and frameworks for Apple platforms: Xcode, TestFlight, and App Store Connect.

A conceptual illustration that shows how Xcode Cloud builds a project and distributes an app to all kinds of devices.

With Xcode Cloud, you can automatically and frequently:

Build your project.

Run tests and perform verifications.

Distribute builds to testers and gather their feedback with TestFlight while protecting user privacy.

After successfully verifying a new version of your app with Xcode Cloud and TestFlight, you can quickly release it on the App Store.

For more information about continuous integration and delivery, see About continuous integration and delivery with Xcode Cloud. To learn more about configuring your project or workspace to use Xcode Cloud, see Configuring your first Xcode Cloud workflow.

Note

For additional information about Xcode Cloud that includes videos from WWDC21 and WWDC22, see The Xcode Cloud toolkit.

### OS 27 beta workflows

Record the workflow's selected Xcode version and test destinations rather than assuming it matches a developer's local installation. The [Xcode 27 beta 6 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) require **Apple silicon and macOS Tahoe 26.4+** for the local IDE; they do not establish which managed Xcode Cloud environments are available. Check the workflow editor and [Xcode Cloud documentation](https://developer.apple.com/documentation/xcode/xcode-cloud.md).

Retain a supported-release workflow while validating a beta workflow. Include [Swift Testing](Testing.md), [XCTest](XCTest.md), and applicable [App Intents Testing](AppIntentsTesting.md) tests. Gate model-backed [Evaluations](Evaluations.md) on actual runtime/model availability, and report unavailable environments separately from passing evaluations.

## Topics

### Essentials
- [About continuous integration and delivery with Xcode Cloud](https://developer.apple.com/documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud.md) - Learn how continuous integration and delivery with Xcode Cloud helps you create high-quality apps and frameworks.
- [Setting up your project to use Xcode Cloud](https://developer.apple.com/documentation/xcode/setting-up-your-project-to-use-xcode-cloud.md) - Review account, project, and source control requirements before configuring your project or workspace to use Xcode Cloud.
- [Configuring your first Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow.md) - Set up your project or workspace to use Xcode Cloud and adopt continuous integration and delivery.

### Setup and maintenance
- [Making dependencies available to Xcode Cloud](https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud.md) - Review dependencies and make them available to Xcode Cloud before you configure your project to use Xcode Cloud.
- [Configuring Xcode Cloud for your team](https://developer.apple.com/documentation/xcode/configuring-xcode-cloud-for-your-team.md) - Start using continuous integration and delivery with Xcode Cloud as a team.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](https://developer.apple.com/documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows.md) - Use custom aliases to share configurations with multiple workflows.
- [Sharing environment variables across Xcode Cloud workflows](https://developer.apple.com/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows.md) - Apply common configurations to multiple workflows by using shared environment variables.
- [Building Swift packages and Swift Playgrounds app projects with Xcode Cloud](https://developer.apple.com/documentation/xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) - Add your Swift package or Swift Playgrounds app project to an Xcode project to build it in Xcode Cloud.
- [Setting the next build number for Xcode Cloud builds](https://developer.apple.com/documentation/xcode/setting-the-next-build-number-for-xcode-cloud-builds.md) - Start numbering builds from a custom build number for your existing Mac app to avoid version collisions.
- [Including notes for testers with a beta release of your app](https://developer.apple.com/documentation/xcode/including-notes-for-testers-with-a-beta-release-of-your-app.md) - Add text files to your Xcode project to provide notes to beta testers about what to test.
- [Removing your project from Xcode Cloud](https://developer.apple.com/documentation/xcode/removing-your-project-from-xcode-cloud.md) - Remove your project from Xcode Cloud to delete app and workflow data, disconnect your Git repository, and remove the Slack integration.

### Usage data
- [Reviewing Xcode Cloud usage data](https://developer.apple.com/documentation/xcode/reviewing-xcode-cloud-usage-data.md) - Access Xcode Cloud usage information to understand how you and your team use Xcode Cloud.

### Workflows
- [Developing a workflow strategy for Xcode Cloud](https://developer.apple.com/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud.md) - Review how you can best create custom Xcode Cloud workflows to refine your continuous integration and delivery practice.
- [Xcode Cloud workflow reference](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference.md) - Configure metadata, start conditions, actions, post-actions, and more to create custom Xcode Cloud workflows.
- [Creating a workflow that builds your app for distribution](https://developer.apple.com/documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution.md) - Configure a workflow to build and sign your app for distribution to testers with TestFlight, in the App Store, or as a notarized app.

### Source code management
- [Source code management setup](https://developer.apple.com/documentation/xcode/source-code-management-setup.md) - Allow Xcode Cloud to access your Git repository.
- [Configuring requirements for merging a pull request](https://developer.apple.com/documentation/xcode/configuring-requirements-for-merging-a-pull-request.md) - Protect stable branches by requiring a successful Xcode Cloud build or action before it's possible to merge a pull request.

### Custom build scripts
- [Writing custom build scripts](https://developer.apple.com/documentation/xcode/writing-custom-build-scripts.md) - Extend your Xcode Cloud workflows with custom build scripts that perform custom tasks or install additional tools.
- [Environment variable reference](https://developer.apple.com/documentation/xcode/environment-variable-reference.md) - Review predefined environment variables you use in custom build scripts.

### Troubleshooting
- [Resolving common configuration and build issues](https://developer.apple.com/documentation/xcode/resolving-common-configuration-and-build-issues.md) - Review common configuration and build issues and learn how you can resolve them.
- [Resolve GitHub Enterprise connection issues](https://developer.apple.com/documentation/xcode/resolve-github-enterprise-connection-issues.md) - Verify that Xcode Cloud can access your GitHub Enterprise repository and fix configuration issues.
- [Reporting feedback for Xcode Cloud](https://developer.apple.com/documentation/xcode/reporting-feedback-for-xcode-cloud.md) - Provide feedback on issues you encounter when building with Xcode Cloud.

### Notifications
- [Configuring webhooks in Xcode Cloud](https://developer.apple.com/documentation/xcode/configuring-webhooks-in-xcode-cloud.md) - Configure webhooks that connect Xcode Cloud to other services and tools.
- [Xcode Cloud webhook payload reference](https://developer.apple.com/documentation/xcode/webhook-payload.md) - Review details of the webhook payload that Xcode Cloud sends, including the product, workflow, build, actions, results, and SCM metadata associated with it.
- [Connecting Xcode Cloud to Slack](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-slack.md) - Connect Xcode Cloud to Slack to keep your team informed about the latest Xcode Cloud builds.

### REST API
- [Xcode Cloud Workflows and Builds](https://developer.apple.com/documentation/appstoreconnectapi/xcode-cloud-workflows-and-builds.md) - Automate reading Xcode Cloud data, managing workflows, and starting builds.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Xcode/Xcode-Cloud)*

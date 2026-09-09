# Service Management

Manage startup items, launch agents, and launch daemons from within an app.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.6+

## Overview

Service Management includes older job-management APIs and the modern `SMAppService` interface for bundled login items, launch agents, and launch daemons. The bundled-helper registration and authorization workflow below requires **macOS 13+ / Mac Catalyst 16+**, not merely the framework's older catalog baseline.

### Helper Executable Types

**LoginItems**  
An app configured to launch when the user logs in. An approved helper login item's registration can also launch it immediately; registering `SMAppService.mainApp` instead affects subsequent logins. Launch-at-login registration does not guarantee continuous background execution or prevent an app from exiting normally.

**LaunchAgents**  
Jobs managed by `launchd` in a user's context. Register an agent from each user context in which it should be available. Loading a job is not proof that a process is continuously running: demand, launch conditions, and its `launchd` configuration govern execution.

**LaunchDaemons**  
System-domain jobs that can run before any user logs in. A daemon may run as root or under the identity selected by its `UserName`/`GroupName` configuration. System and user bootstrap namespaces differ, but that is not a universal prohibition on initiating IPC with a user process. Design explicit, authenticated communication rather than assuming every daemon is root or that a process name determines who may call it.

### Registration, approval, and lifecycle

- Put helper login-item apps in `Contents/Library/LoginItems`, agent property lists in `Contents/Library/LaunchAgents`, and daemon property lists in `Contents/Library/LaunchDaemons`. Use `BundleProgram` for a bundle-relative executable path. Code-sign the app and helpers; apps containing daemons require notarization.
- Call `register()` and handle registration, signature, authorization, and already-registered errors. A daemon needs administrator approval before it is bootstrapped; do not equate registration with a running service.
- Check `SMAppService.status` at launch and when XPC connections fail. `.enabled` means eligible to run, not proof of a live process. `.requiresApproval` also covers a person later revoking permission. Open Login Items settings to help restore access only after the person agrees.
- Unregistering a running helper login item, agent, or daemon terminates it. Unregistering `mainApp` removes future login launch without terminating the current main app. The synchronous unregister method can return before process exit; use the completion-based form before an immediate re-registration.
- Re-register after changing a helper executable or its property list, preferably unregistering the previous registration first.

Keep legacy deployment support separate: `SMJobBless` and `SMLoginItemSetEnabled` date to macOS 10.6 and are **deprecated in macOS 13**, not removed. Their replacements use `SMAppService` and the person's authorization state.

## Topics

### Essentials
- [Updating helper executables from earlier versions of macOS](https://developer.apple.com/documentation/servicemanagement/updating-helper-executables-from-earlier-versions-of-macos) - Migrate bundled helpers and authorization controls.
- [Updating your app package installer to use the new Service Management API](https://developer.apple.com/documentation/servicemanagement/updating-your-app-package-installer-to-use-the-new-service-management-api) - Package a GUI-less containing app and its separate launch-agent helper.

### Management
- [SMAppService](https://developer.apple.com/documentation/servicemanagement/smappservice) - Controls bundled helper executables; macOS 13+ / Mac Catalyst 16+.
- [SMJobBless](https://developer.apple.com/documentation/servicemanagement/smjobbless(_:_:_:_:)) (Deprecated in macOS 13) - Submits the executable for the given label as a job to `launchd`.

### Authorization Constants
- **Authorization Constants** - Constants that describe the ability to authorize helper executables or modify daemon applications.

### Property List Keys
- **Property List Keys** - Property list keys that describe the kinds of applications, daemons, and helper executables the framework manages.

### Enablement
- [SMLoginItemSetEnabled](https://developer.apple.com/documentation/servicemanagement/smloginitemsetenabled(_:_:)) (Deprecated in macOS 13) - Enables a helper login item in the main app bundle.

### Status
- [SMAppService.Status](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum) - Registration and authorization state, not process liveness.

### Errors
- **Service Management Errors** - Errors that the framework returns.

### Deprecated
- **Deprecated Symbols**

### Variables
- [SMAppServiceErrorDomain](https://developer.apple.com/documentation/servicemanagement/smappserviceerrordomain) - Error domain available in macOS 15+ / Mac Catalyst 18+; do not infer the whole framework started at those versions.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ServiceManagement)*

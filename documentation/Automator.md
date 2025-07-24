# Automator

Develop actions that the Automator app can load and run. View, edit, and run Automator workflows in your app.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.4+

## Overview

The Automator framework supports the development of actions for the Automator app, as well as the ability to run a workflow in developer apps. An action is a bundle that, when loaded and run, performs a specific task, such as copying a file or cropping an image. Using Automator, users can construct and execute workflows consisting of a sequence of actions. Developers can also load and execute workflows in their apps. As a workflow executes, the output of one action is typically passed as the input to the next action. Automator loads action bundles from standard locations in the file system: /System/Library/Automator, /Library/Automator, and ~/Library/Automator.

## Topics

### Actions
- **AMBundleAction** - An object that represents an Automator action that's a loadable bundle.
- **AMShellScriptAction** - An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.
- **AMAction** - An abstract class that defines the interface and general characteristics of Automator actions.

### Workflows
- **AMWorkflow** - An object that lets you use an Automator workflow in your app.
- **AMWorkflowController** - An object that lets you manage an Automator workflow in your app.
- **AMWorkflowView** - An object that lets you view and edit Automator workflows in your app.
- **AMWorkspace** - A workspace for running an Automator workflow.

### Errors
- **AMAutomatorErrorDomain** - A string that identifies the Automator error domain.
- **AMActionErrorKey** - A key to retrieve the action that caused an error.
- **AMError** - An Automator error.
- **Code** - Automator error codes.

### Deprecated
- **AMAppleScriptAction** - An object that represents Automator actions whose runtime behavior is driven by an AppleScript script. (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Automator)*
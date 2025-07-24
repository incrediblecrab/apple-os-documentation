# Playground Support

Share playground data, manage live views, and control the execution of a playground.

**Platforms:** macOS 12.0+ | Swift Playgrounds 2.0+

## Overview

You use Playground Support from within playgrounds to:

- Access a playground page and manage its execution
- Access and share persistent data
- Assess the progress of the learner, update hints, and show success text

You also use Playground Support to display and dismiss live views, which show the results of running the code in a playground. You can create live views for your own types by leveraging the built-in live view representations available on many existing types.

Traditional live views are available in playgrounds in Xcode and in Swift Playgrounds. They run in the same process as the code in the playground, so you can access their properties and methods as usual; however, they're reset each time you run the playground. The always-on live view in Swift Playgrounds, activated when you add LiveView.swift to a page, executes in its own process so you can persist information and visuals between successive runs. The always-on live view isn't reset until you leave the page.

## Topics

### Playground Pages

- **PlaygroundPage** - An object you use to configure the state of a playground page and its live view.

### Live Views

- **PlaygroundLiveViewable** - A protocol that displays an instance as a live view in a playground.
- **PlaygroundLiveViewRepresentation** - The supported types for displaying for live views in playgrounds.
- **PlaygroundLiveViewSafeAreaContainer** - A protocol that ensures that views fit without obstruction within the Swift Playgrounds user interface.

### Page-View Communication
Messaging Between a Playground Page and the Always-On Live View - Display the results of running a playground page's code in a persistent live view.

- **PlaygroundRemoteLiveViewProxy** - A proxy that facilitates message passing between the always-on live view and its corresponding playground page.
- **PlaygroundRemoteLiveViewProxyDelegate** - A delegate you use to receive messages from the always-on live view.
- **PlaygroundLiveViewMessageHandler** - A handler you use to send and receive messages between the always-on live view and its corresponding playground page.

### Data Persistence

- **PlaygroundKeyValueStore** - A data storage container you use to persist information across different sessions.
- **PlaygroundValue** - The types you can save in the key-value store or send in messages to live views.
- **playgroundSharedDataDirectory** - The path to the directory containing data shared between all playgrounds in Xcode.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/playgroundsupport)*
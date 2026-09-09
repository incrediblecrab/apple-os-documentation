# PackageDescription

Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.

## Overview

Swift packages are reusable components of Swift, Objective-C, Objective-C++, C, or C++ code that developers can use in their projects. They bundle source files, binaries, and resources in a way that's easy to use in your app's project.

Each Swift package requires a Package.swift file in the main directory of the package — referred to as the package manifest. When you create a Swift package, you use the **PackageDescription** library in the package manifest to list dependencies, configure localized resources, and set other configuration options.

For example, the package manifest from the SlothCreator: Building DocC Documentation in Xcode sample project below defines the SlothCreator package, with the SlothCreator library in it. It specifies the deployment targets, and that its resources are in the Resources folder.

```swift
// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "SlothCreator",
    platforms: [
        .macOS(.v11),
        .iOS(.v14),
        .watchOS(.v7),
        .tvOS(.v13)
    ],
    products: [
        .library(
            name: "SlothCreator",
            targets: ["SlothCreator"]
        )
    ],
    targets: [
        .target(
            name: "SlothCreator",
            resources: [
                .process("Resources/")
            ]
        )
    ]
)
```

The package manifest also allows you to define executable products, as well as plugins that Swift Package Manager can use to build other products in the manifest.

For more information about adding a package dependency to your app project and creating Swift packages with Xcode, see [Adding Package Dependencies to Your App](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app), [Creating a Standalone Swift Package with Xcode](https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode), and [Swift packages](swift-packages.md).

Support for Swift packages in Xcode builds on the open-source Swift Package Manager project. To learn more about the Swift Package Manager, visit [Swift.org](https://www.swift.org/package-manager/) and the [Swift Package Manager repository on GitHub](https://github.com/swiftlang/swift-package-manager).

### Migrating a manifest

The `// swift-tools-version:` declaration selects the required tools and manifest API version; `platforms` declares deployment minimums. Neither is the installed compiler's version number. Choose language mode intentionally when adopting Swift 6 concurrency checking rather than changing every setting to “6.4.” Preserve older deployment minimums when guarded APIs permit them. See the [concurrency migration recipe](../guides/swift-concurrency-migration.md) and [SwiftPM's manifest reference](https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html).

## Topics

### Creating a Package
- **Package** - The configuration of a Swift package.
- **Context** - The context information for a Swift package.

### Structures
- **GitInformation** - Information about the git status of a given package, if available.
- **Version** - A version according to the semantic versioning specification.

### Enumerations
- **WarningLevel** - The level at which a compiler warning should be treated.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PackageDescription)*

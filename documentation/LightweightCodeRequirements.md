# LightweightCodeRequirements

Test the identity of executable code on disk and in running processes.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 17.4+ | macOS 14.4+

## Overview

Code that is cryptographically signed carries tamper-proof statements about its identity in its code signature. Construct tests to distinguish different code files using the lightweight code requirement domain-specific language (DSL). Use the tests to distinguish code files on disk, running processes, and processes that the operating system launches. Code files on disk include:

- Executable binaries
- Dynamic or static libraries
- Frameworks
- Loadable bundles

### Define tests of signed code properties

The keywords you use to test code properties in the lightweight code requirement DSL are:

- **CodeDirectoryHash** - Tests whether the code's code directory hash matches a specific value, or is in a list of allowed values. For more information about code directory hashes, see TN3126: Inside Code Signing: Hashes.
- **ProcessCodeSigningFlags** - Tests whether the executable for a running process has particular flags, defined in ProcessCodeSigningFlags.ValueSet, set in its code signature.
- **OnDiskCodeSigningFlags** - Tests whether the code on disk has particular flags, defined in OnDiskCodeSigningFlags.ValueSet, set in its code signature.
- **EntitlementsQuery** - Tests whether the executable has a particular entitlement, optionally with a given value.
- **InfoPlistHash** - Tests whether the hash of the executable's Info.plist file (or embedded Info.plist, for a command-line tool) matches a specific value, or is in a list of allowed values. Depending on the code signature version, the hash uses the SHA-1 or SHA-256 algorithm. Test whether the hash is in a list that contains both versions.
- **IsInitProcess** - Tests whether the process is the initial process in the operating system, that is, launchd.
- **IsMainBinary** - Tests whether the executable is a main binary. A main binary has a code signature version of at least 0x20400 and an executable segment with the CS_EXECSEG_MAIN_BINARY flag set.
- **IsSIPProtected** - Tests whether the code is on a volume covered by System Integrity Protection (SIP).
- **PlatformType** - Tests whether the code targets a particular platform, for example iOS. The list of allowed values is defined in PlatformType.Value.
- **SigningIdentifier** - Tests whether the code's signing identifier matches a specific value, or is in a list of allowed values. The signing identifier is a string that's typically the bundle identifier for a code bundle, for example an app, and has a similar structure for other code, for example, a command-line tool.
- **TeamIdentifier** - Tests whether the team identifier of the developer team that signed the code matches a specific value, or is in a list of allowed values.
- **TeamIdentifierMatchesCurrentProcess** - Tests whether the team identifier of the developer team that signed the code for a running process matches the team identifier for the current process.
- **ValidationCategory** - Tests whether the code is signed for a specific category, or is in a list of allowed categories. The list of values is defined in ValidationCategory.Value.

For code signed by an organization or individual other than Apple, the code's identity is specified by its SigningIdentifier, TeamIdentifier, and ValidationCategory.

### Combine tests into requirements

The lightweight code requirement DSL provides operators that you use to build up complex requirements from individual tests. For example, the operators to construct on-disk code requirements are:

- **anyOf(requirement:)** - true if one or more of its arguments is true; false if all of its arguments are false.
- **allOf(requirement:)** - true if each of its arguments is true; false if any of its arguments is false.

ProcessCodeRequirement and LaunchCodeRequirement provide similar operators for building process code requirements and launch requirements.

The anyOf(requirement:) and allOf(requirement:) operators simplify their inputs as follows:

- An operator with a single constraint as its argument replaces itself with the direct evaluation of the given constraint.
- If any of the arguments to an anyOf(requirement:) operator are themselves anyOf(requirement:) operators, the arguments to both are merged into a single set of constraints evaluated by the top-level anyOf(requirement:) operator.
- If any of the arguments to an allOf(requirement:) operator are themselves allOf(requirement:) operators, the arguments to both are merged into a single set of constraints evaluated by the top-level allOf(requirement:) operator.

Both allOf(requirement:) and anyOf(requirement:) throw an error if the simplification results in the same constraint appearing twice in the arguments for one operator, for example, if an anyOf(requirement:) operator contains two tests of InfoPlistHash constraints. The exception to this simplification rule is that multiple EntitlementsQuery tests can appear in the arguments for one operator.

### Test whether a running process satisfies a lightweight code requirement

Create a ProcessCodeRequirement using the DSL and pass it to SecTaskValidateForRequirement(task:requirement:), along with a SecTask representing the running process. If the task's code satisfies the lightweight code requirement, then the function returns true; otherwise, it returns false.

### Test whether code on disk satisfies a lightweight code requirement

Create an OnDiskCodeRequirement using the DSL and pass it to SecStaticCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:) or SecCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:), depending on whether you construct a SecStaticCode or SecCode to represent the code. Both functions return a ValidationResult indicating whether the code has a valid signature, whether it satisfies the requirement, and any error that occurred.

### Restrict the executables you launch as new processes

Create a LaunchCodeRequirement using the DSL and set it as the launchRequirement on a Process instance, before you call run(). If the executable specified in the process's executableURL satisfies the launch requirement, the kernel launches the process; otherwise, run() throws an error. You can also encode your requirements as launch constraints in property list files that you embed in your executable's code signature to restrict which processes can launch your executable and which dynamic libraries your process can load. For more information, see Applying launch environment and library constraints.

## Topics

### Checking code requirements for running processes
- **SecTaskValidateForRequirement** - Tests whether a task's executable satisfies a lightweight code requirement.
- **ProcessCodeRequirement** - A lightweight code requirement that you use to evaluate a running process.
- **allOf(requirement:)** - Creates a constraint that requires a running process's executable to satisfy all of the provided constraints.
- **anyOf(requirement:)** - Creates a constraint that requires a running process's executable to satisfy any of the provided constraints.
- **ProcessConstraint** - A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- **ProcessCodeSigningFlags** - A constraint that matches the current code-signing flags of a process.
- **ProcessConstraintBuilder** - A custom parameter attribute that constructs process constraints from closures.
- **TeamIdentifierMatchesCurrentProcess** - A constraint that matches if a process has the same team identifier as the calling process.

### Checking code requirements for launching processes
- **SecCodeCheckValidityWithProcessRequirement** - Checks whether the code associated with a running process satisfies a lightweight code requirement.
- **launchRequirement** - A property to set launch requirements on a Process instance.
- **LaunchCodeRequirement** - A lightweight code requirement that you use to evaluate the executable for a launching process.
- **allOf(requirement:)** - Creates a constraint that requires a launching process's executable to satisfy all of the provided constraints.
- **anyOf(requirement:)** - Creates a constraint that requires a launching process's executable to satisfy any of the provided constraints.
- **LaunchConstraint** - A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.
- **LaunchConstraintBuilder** - A custom parameter attribute that constructs launch constraints from closures.

### Checking code requirements for code files on disk
- **SecStaticCodeCheckValidityWithOnDiskRequirement** - Checks whether static code on disk satisfies a lightweight code requirement.
- **SecCodeCheckValidityWithOnDiskRequirement** - Checks whether code on disk satisfies a lightweight code requirement.
- **ValidationResult** - A structure that represents the result of testing a lightweight code requirement.
- **OnDiskCodeRequirement** - A lightweight code requirement that you use to evaluate a code file on disk.
- **allOf(requirement:)** - Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- **anyOf(requirement:)** - Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- **OnDiskConstraint** - A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- **OnDiskCodeSigningFlags** - A constraint that tests the code-signing flags of a code file on disk.
- **OnDiskConstraintBuilder** - A custom parameter attribute that constructs on-disk constraints from closures.

### Testing properties of executable code
- **CodeDirectoryHash** - A constraint that matches the hash of a code directory of a code file or of a running or launching process.
- **EntitlementsQuery** - A constraint that tests values in the entitlements dictionary associated with a process or code file.
- **InfoPlistHash** - A constraint that tests the specified hash against the Information property list hash stored in the code signature of the process or code file.
- **IsInitProcess** - A constraint that tests whether a process is the operating system's initial process.
- **IsMainBinary** - A constraint that tests whether a code file is a main binary.
- **IsSIPProtected** - A constraint that tests whether a code file or process is on a volume protected by System Integrity Protection (SIP).
- **PlatformType** - A constraint that tests whether a code file or running process targets a given platform.
- **SigningIdentifier** - A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- **TeamIdentifier** - A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- **ValidationCategory** - A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.

### Handling errors
- **ConstraintError** - Error types that can be thrown from lightweight code requirement routines.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LightweightCodeRequirements)*
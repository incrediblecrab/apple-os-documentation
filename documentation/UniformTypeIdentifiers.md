# Uniform Type Identifiers

Provide uniform type identifiers that describe file types for storage or transfer.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

The **Uniform Type Identifiers** framework provides a collection of common types that map to MIME and file types. Use these types in your project to describe the file types in your app. These descriptions help the system properly handle file storage formats or in-memory data for transfer — for example, transferring data to or from the pasteboard. The identifier types can also identify other resources, such as directories, volumes, or packages.

Explicitly specify relationships between types by marking them as subtypes of other types. For example, the type **UTTypePNG** has the identifier `public.png` and is a subtype of **UTTypeImage** (`public.image`). **UTTypeImage** is in turn a subtype of both of the following:

- **UTTypeContent** (`public.content`), which implies the type can be a document
- **UTTypeData** (`public.data`), which implies the type is representable as a byte stream

**Note**

**UTTypeData** also conforms to **UTTypeItem** (`public.item`), which is a generic base type for most items in a file system, such as files or directories.

## Topics

### Essentials
- [Defining file and data types for your app](https://developer.apple.com/documentation/uniformtypeidentifiers/defining_file_and_data_types_for_your_app) - Declare uniform type identifiers to support your app's proprietary data formats.
- [System-declared uniform type identifiers](https://developer.apple.com/documentation/uniformtypeidentifiers/system-declared_uniform_type_identifiers) - Common types that the system declares.

### Uniform Type Identifiers
- **UTType** - A structure that represents a type of data to load, send, or receive.
- **UTTagClass** - A type that represents tag classes.
- **UTTypeReference** - An object that represents a type of data to load, send, or receive.

### Reference
- **UniformTypeIdentifiers Constants**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UniformTypeIdentifiers)*
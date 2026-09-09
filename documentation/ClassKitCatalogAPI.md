# ClassKit Catalog API

Declare the activities supported by your educational app through a web interface.

**Availability:** An authorized web service for apps adopting ClassKit; not an OS 27-only framework.

## Overview

Access the ClassKit Catalog API from your computer or server to declare an app's educational activities when you have an app that adopts the ClassKit framework. Traditionally your app declares its activities — represented as contexts — to the ClassKit framework at run time so that teachers can assign the activities using the Schoolwork app. As an alternative, the ClassKit Catalog API lets you declare contexts ahead of time to a central server so that:

- Teachers can browse your app's activities in the Schoolwork app before running your app for the first time on their device.
- You can include keywords describing your activities that help teachers find your content.
- Your app can support a large number of assignable activities without the app having to declare all the content to the ClassKit framework at run time.

Production catalog content becomes available to teachers using Schoolwork. The development environment is separate from production, but its content may be visible to other developers using Schoolwork's development environment; it is not a private student-data store. Publish dynamically generated or user-specific content only through the ClassKit framework.

## Authorization and operation completion

Authenticate each call with the cryptographically signed token described in [Authenticating Calls](https://developer.apple.com/documentation/classkitcatalogapi/authenticating-calls-to-the-classkit-catalog-api), and keep signing assets server-side. Test against the development environment before publishing production content.

A request can be accepted before its work is complete. On HTTP `202`, follow the returned `Location` to [Get Status](https://developer.apple.com/documentation/classkitcatalogapi/get-status). Inspect the operation's `state` and error details, not merely the status request's HTTP `200`, before reporting publication success. Handle validation and authorization failures without uploading private student data as a fallback. Keep context identities consistent with the corresponding [ClassKit](ClassKit.md) hierarchy.

## Topics

### Essentials
- [Authenticating Calls to the ClassKit Catalog API](https://developer.apple.com/documentation/ClassKitCatalogAPI/authenticating-calls-to-the-classkit-catalog-api) - Sign a token for each call.
- [Testing Your ClassKit Catalog Implementation](https://developer.apple.com/documentation/ClassKitCatalogAPI/testing-your-classkit-catalog-implementation) - Verify interactions in the development environment.

### Declaring Contexts
- [Preparing Context Data](https://developer.apple.com/documentation/ClassKitCatalogAPI/preparing-context-data) - Adjust context data for the web API.
- [Create or Replace Contexts](https://developer.apple.com/documentation/ClassKitCatalogAPI/create-or-replace-contexts) - Store assignable-content information.
- [Get a Context](https://developer.apple.com/documentation/ClassKitCatalogAPI/get-a-context) - Retrieve published context information.
- [Delete a Context](https://developer.apple.com/documentation/ClassKitCatalogAPI/delete-a-context) - Remove context information.
- **Context** - An area of your app that represents an assignable task, like a quiz or a chapter.
- **ContextsRequest** - A request that you make when modifying context information.
- **ContextsResponse** - The response you receive after modifying context information.

### Uploading Thumbnails
- [Create or Replace a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/create-or-replace-a-thumbnail) - Store an activity image.
- [Get a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/get-a-thumbnail) - Retrieve an activity image.
- [Delete a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/delete-a-thumbnail) - Remove an activity image.

### Retrieving Status
- [Get Status](https://developer.apple.com/documentation/ClassKitCatalogAPI/get-status) - Fetch the status of an earlier operation.
- **Status** - The state of a request that the API previously accepted, but didn't complete right away.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClassKitCatalogAPI)*

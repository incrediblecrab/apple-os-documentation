# ClassKit Catalog API

Declare the activities supported by your educational app through a web interface.

**Platforms:** ClassKit 1.0+

## Overview

Access the ClassKit Catalog API from your computer or server to declare an app's educational activities when you have an app that adopts the ClassKit framework. Traditionally your app declares its activities — represented as contexts — to the ClassKit framework at run time so that teachers can assign the activities using the Schoolwork app. As an alternative, the ClassKit Catalog API lets you declare contexts ahead of time to a central server so that:

- Teachers can browse your app's activities in the Schoolwork app before running your app for the first time on their device.
- You can include keywords describing your activities that help teachers find your content.
- Your app can support a large number of assignable activities without the app having to declare all the content to the ClassKit framework at run time.

Content that you upload to the ClassKit Catalog API becomes publicly available to all teachers using the Schoolwork app. If you have dynamically-generated or user-specific content, continue to publish that only through the ClassKit framework.

## Topics

### Essentials
- [Authenticating Calls to the ClassKit Catalog API](https://developer.apple.com/documentation/ClassKitCatalogAPI/authenticating_calls_to_the_classkit_catalog_api) - Establish your identity to the ClassKit Catalog server by providing a cryptographically signed token for each call.
- [Testing Your ClassKit Catalog Implementation](https://developer.apple.com/documentation/ClassKitCatalogAPI/testing_your_classkit_catalog_implementation) - Verify your server interaction before deployment by operating in a development environment.

### Declaring Contexts
- [Preparing Context Data](https://developer.apple.com/documentation/ClassKitCatalogAPI/preparing_context_data) - Adjust how you manage context data when working with the web API.
- [Create or Replace Contexts](https://developer.apple.com/documentation/ClassKitCatalogAPI/create_or_replace_contexts) - Store information about the assignable content that your educational app provides.
- [Get a Context](https://developer.apple.com/documentation/ClassKitCatalogAPI/get_a_context) - Fetch information that you previously stored about your app's assignable activities.
- [Delete a Context](https://developer.apple.com/documentation/ClassKitCatalogAPI/delete_a_context) - Remove information that you previously stored about your app's assignable activities.
- **Context** - An area of your app that represents an assignable task, like a quiz or a chapter.
- **ContextsRequest** - A request that you make when modifying context information.
- **ContextsResponse** - The response you receive after modifying context information.

### Uploading Thumbnails
- [Create or Replace a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/create_or_replace_a_thumbnail) - Store an image that represents one of your app's assignable activities.
- [Get a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/get_a_thumbnail) - Fetch the image for one of your app's assignable activities.
- [Delete a Thumbnail](https://developer.apple.com/documentation/ClassKitCatalogAPI/delete_a_thumbnail) - Remove one of the images for your app's assignable activities.

### Retrieving Status
- [Get Status](https://developer.apple.com/documentation/ClassKitCatalogAPI/get_status) - Fetch the status of an operation that you initiated earlier.
- **Status** - The state of a request that the API previously accepted, but didn't complete right away.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClassKitCatalogAPI)*
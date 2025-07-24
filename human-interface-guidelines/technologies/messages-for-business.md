# Messages for Business

Messages for Business helps customers connect with businesses through the Messages app in iOS, iPadOS, macOS, visionOS, and watchOS.

**Platforms:** iOS | iPadOS | macOS | visionOS | watchOS

## Overview

Using the Messages app, people can contact your company to ask questions, get support, schedule appointments, make payments with Apple Pay, and more.

People can use apps, features, and services like Maps and Spotlight to discover businesses and seamlessly initiate conversations with them. The familiar Messages app interface on iPhone, iPad, Mac, and Apple Watch ensures that customer interaction is intuitive and efficient, and the informality of messaging produces a customer service experience that feels personal and meaningful.

For developer guidance, and to sign up, see [Messages for Business Accounts](https://developer.apple.com/documentation/businesschat).

## Topics

### Branding

Although Messages for Business conversations occur within the experience of the Messages app, you can still leverage your logo and color scheme to call attention to your brand and build a memorable conversation experience.

- **Strive for uniqueness** - It's critical to avoid building an experience that might cause people to confuse your brand with other brands. In particular, your logo design and use of color must never cause people to think they're conversing with Apple.

### Buttons

Customers use Messages for Business buttons to start a conversation with your company. You can also support system features like Maps and Spotlight, so that customers can use them to locate your business and start a conversation.

- **Let people start conversations anytime** - Don't dim or turn off buttons or links that initiate conversations outside of your business hours. Even if you only respond to customer service inquiries during certain hours, people need to be able to start a conversation anytime.

- **Let the default button title encourage customers to contact you** - System-provided button titles like "Message Us," "Get Help," "Ask a Question," or "Contact an Agent" help people understand what the button does.

- **Show the buttons on supported devices** - If a customer is using an unsupported device, don't encourage a conversation by displaying a button.

- **Make sure Messages for Business buttons are discoverable** - People generally expect to find the button on contact information, support, order confirmation, product, and order history pages.

- **Display the button prominently** - Make Messages for Business buttons the same size or larger than similar contact initiation buttons, such as an email button.

- **Use only approved button styles** - For guidance, see Design your website and app to include the Messages buttons.

- **Maintain minimum and maximum button sizes and inner side margins** - Use appropriate values for maximum width (1000 pt), minimum height (40 pt), maximum height (150 pt), and minimum side margins (5% of height).

- **Don't make any other visual or functional modifications to buttons** - For example, don't change transparency values or add drop shadows.

- **Maintain minimum clear space** - The minimum amount of clear space required around the buttons is 10% of the button's height.

### Referring to Apple Messages for Business

- **Use the terms Apple Messages for Business or Apple Messages** - In customer-facing communications, avoid using the term Messages by itself, especially when paired with a logo-only button.

- **Use proper capitalization** - Use four words with an uppercase A, an uppercase M, and an uppercase B, and lowercase for all other letters.

- **Avoid using other terms** - Don't use terms like chat or text to refer to a Messages for Business button or flow.

- **Never use the Apple logo to represent the name Apple in text** - Apple Messages for Business is a service mark of Apple Inc.

### Color

When configuring your Messages for Business experience, you can customize the colors of the top toolbar and its Back and Info buttons in iOS. These same colors appear in the message header in watchOS, brand name in watchOS, and recipient bubble in macOS.

- **Use sufficient color contrast ratios** - Insufficient contrast makes content hard to see and can cause logos and buttons to blend in with the background. Strive for a minimum contrast ratio of 4.5:1, although 7:1 is preferred.

- **Consider Dark Mode** - On iPhone, your customers can use the system-wide appearance called Dark Mode. You might need to redesign your logo and picker icons so that they look good in both light and dark appearances.

- **Use colors that contrast well with both light and dark color palettes** - Dark transparencies and colors aren't visible in Dark Mode.

### Logo

Your logo visually identifies your business in Messages and other contexts throughout the system.

- **Test your logo's appearance in all contexts** - View your logo in the message list, top toolbar, and notifications, and make sure it's clear and distinct.

- **Provide your logo in both square and wide variations** - Make sure your logo looks great everywhere by creating a separate version for each variation.

- **Use adequate padding in your logo** - Unless your logo has full-bleed elements, it's best to inset key elements from the edges by 10% of the image's width and height.

- **Avoid using colors that make it hard for people to perceive your logo** - Consider color blind accessibility and ensure sufficient contrast.

#### Square Logo Specifications

Your square logo appears on the contact card for your business, in search results, in the message list view, and in the top toolbar of a conversation if you don't provide a wide logo.

- **Format:** PNG or JPEG
- **Minimum dimensions:** 1024x1024 px
- **Maximum file size:** 2 MB
- **Background:** Full color
- **Transparency:** No
- **Padding:** 10% of the image's width and height

#### Wide Logo Specifications

Your wide logo appears in the top toolbar of a conversation.

- **Format:** PNG
- **Maximum width:** 1706 px
- **Minimum height:** 256 px
- **Maximum file size:** 2 MB
- **Background:** Transparent
- **Transparency:** Yes
- **Shape:** Rectangular canvas. Allow transparency to define the logo shape.

### Message Bubble Content

Message bubbles for standard interactive messages like Apple Pay payment requests, rich links, and pickers include a title, and can optionally include additional text and an image.

- **Scale images based on the layout style** - When using the same image for multiple layout styles, provide a scaled image variation for each layout style.

- **Provide images at appropriate sizes** - Use 40x40 pt for icons, 60x60 pt for small images, and 263x150 pt for large images in interactive message bubbles.

- **Always provide high-resolution images with a scale factor of @3x** - The @3x images you provide automatically scale down to @2x or @1x for display at lower resolutions.

- **Produce artwork in the appropriate format** - Use de-interlaced PNG files for bitmap/raster artwork. Use JPEG for photos.

### Screenshots

By creating screenshots to display on your website or in emails, you can show customers the benefits of using Messages for Business to communicate with your company.

- **Use realistic conventions** - Use SF Pro Regular for conversation text and include the status bar with time set to 9:41.

- **Create consistent message bubbles** - Use #848E99 background with white text for customer messages, and #E6E5EB background with black text for agent messages.

- **Include proper toolbar elements** - Add a Back button, Info button, your company logo, and your company name with verification checkmark.

### Related Technologies

- [Messages for Business Accounts](https://developer.apple.com/documentation/businesschat) - Account setup and developer guidance

## Changelog

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/messages-for-business)*
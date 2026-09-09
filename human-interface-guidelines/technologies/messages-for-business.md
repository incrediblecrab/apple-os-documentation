# Messages for Business

Apple Messages for Business lets customers communicate with participating businesses through the Messages app.

**Platforms:** iOS | iPadOS | macOS | visionOS | watchOS

## Overview

Using the Messages app, people can contact your company to ask questions, get support, schedule appointments, make payments with Apple Pay, and more.

People can discover participating businesses through entry points such as Maps, websites, app buttons, and Message Suggest. Design conversations for asynchronous replies: customers should be able to return later without repeating information or being pressured to respond immediately.

Start with an Apple-approved Messaging Service Provider (MSP), register a test account, and complete Apple's experience and commercial-account review before enabling public entry points. See [Messages for Business Accounts](https://register.apple.com/messages) and the [current account guide](https://register.apple.com/resources/messages/messaging-documentation/).

This page distinguishes the current account guide — version 3.1, updated July 21, 2026 — from historical HIG material preserved in an [Apple article snapshot captured May 21, 2025](https://web.archive.org/web/20250521171308id_/https://developer.apple.com/tutorials/data/design/human-interface-guidelines/messages-for-business.json). The platform list above records that archived HIG's scope, including visionOS; current client and entry-point requirements come from the account guide and your MSP. The former HIG endpoint's absence isn't a service-deprecation notice.

## Topics

### Branding

Use approved business branding within the conversation experience, without implying that your business is Apple. Verify how supported branding options appear in the clients you support rather than expecting every historical header treatment to remain configurable.

- **Strive for uniqueness** - It's critical to avoid building an experience that might cause people to confuse your brand with other brands. In particular, your logo design and use of color must never cause people to think they're conversing with Apple.

### Buttons

Customers use Messages for Business buttons to start a conversation with your company. You can also support system features like Maps and Spotlight, so that customers can use them to locate your business and start a conversation.

- **Let people start conversations anytime after launch approval** - Don't disable entry points outside business hours. Explain when live support will return. Current channel policies require live-agent access during regular business hours, not a bot-only service.

- **Let the default button title encourage customers to contact you** - System-provided button titles like "Message Us," "Get Help," "Ask a Question," or "Contact an Agent" help people understand what the button does.

- **Show the buttons on supported devices** - If a customer is using an unsupported device, don't encourage a conversation by displaying a button.

- **Make sure Messages for Business buttons are discoverable** - People generally expect to find the button on contact information, support, order confirmation, product, and order history pages.

- **Display the button prominently** - Make Messages for Business buttons the same size or larger than similar contact initiation buttons, such as an email button.

- **Use only approved button styles** - Follow [the current entry-point and button guide](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers). Don't publish working entry points before your account is approved.

- **Historical HIG button metrics** - The archived HIG specified a maximum width of 1000 pt, heights from 40 to 150 pt, and inner side margins of at least 5% of height. These are selected legacy design values, not a universal CSS or current-client sizing contract; use the currently approved button implementation for new integrations.

- **Don't make any other visual or functional modifications to buttons** - For example, don't change transparency values or add drop shadows.

- **Historical HIG clear space** - The archived guide required surrounding clear space of at least 10% of button height. Keep current approved buttons unobscured and follow their applicable placement requirements.

### Referring to Apple Messages for Business

- **Use the terms Apple Messages for Business or Apple Messages** - In customer-facing communications, avoid using the term Messages by itself, especially when paired with a logo-only button.

- **Use proper capitalization** - Write the full name exactly as Apple Messages for Business; Apple Messages is the permitted short form. Don't substitute iMessage for the business channel.

- **Avoid using other terms** - Don't use terms like chat or text to refer to a Messages for Business button or flow.

- **Never use the Apple logo to represent the name Apple in text** - Apple Messages for Business is a service mark of Apple Inc.

### Color

The archived HIG described custom conversation-bar and button colors, with related treatments on watchOS and macOS. Treat those descriptions as historical UI behavior, not a guarantee about the customization available in every current client.

- **Check contrast for the actual content** - For normal text, 4.5:1 is the WCAG minimum-contrast target and 7:1 is the stricter target. Large text, incidental content, and logotypes have different criteria or exceptions; don't treat a palette or logo as blanket proof of accessibility. See [Accessibility](../foundations/accessibility.md).

- **Consider Dark Mode** - On iPhone, your customers can use the system-wide appearance called Dark Mode. You might need to redesign your logo and picker icons so that they look good in both light and dark appearances.

- **Test colors against the backgrounds actually displayed** - A dark color can disappear against a dark surface, but dark colors aren't inherently invisible in Dark Mode. Check both appearances rather than assuming one color treatment always works.

### Logo

Your logo visually identifies your business in Messages and other contexts throughout the system.

- **Test your logo's appearance in all contexts** - View your logo in the message list, top toolbar, and notifications, and make sure it's clear and distinct.

- **Prioritize the square logo for current clients** - The [current registration guide](https://register.apple.com/resources/messages/messaging-documentation/register-your-acct) says iOS 26 and macOS 26 removed wide-logo support. It still documents a legacy wide asset for older clients; don't present that asset as the current conversation-header design.

- **Use adequate padding in your logo** - Unless your logo has full-bleed elements, it's best to inset key elements from the edges by 10% of the image's width and height.

- **Avoid using colors that make it hard for people to perceive your logo** - Consider color blind accessibility and ensure sufficient contrast.

#### Square Logo Specifications

The current registration guide uses the square logo throughout the modern experience. Test legibility at small sizes as well as in larger business-information views.

- **Format:** PNG or JPEG
- **Minimum dimensions:** 1024x1024 px
- **Maximum file size:** 2 MB
- **Background:** Full color, not a photograph
- **Color space:** sRGB or P3
- **Transparency:** No
- **Padding:** 10% of the image's width and height

#### Wide Logo Specifications

These are legacy specifications retained for older-client compatibility. The registration guide identifies the wide logo with iOS 18 and earlier and explicitly says wide-logo support was removed in iOS 26 and macOS 26.

- **Format:** PNG
- **Maximum width:** 1706 px
- **Minimum height:** 256 px
- **Maximum file size:** 2 MB
- **Background:** Transparent
- **Transparency:** Yes
- **Shape:** Rectangular canvas. Allow transparency to define the logo shape.

### Message Bubble Content

Follow the [current conversation design standards](https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices) for each interactive feature. Introduce a picker or other interactive control with clear text outside it, use its appropriate title and imagery, and avoid long instructions that get cropped inside the control. The guide recommends Quick Reply for simple text-only choices with five options or fewer.

For Rich Link logos, the current guide specifies an image under 150 pixels wide. Don't confuse that rule with the historical native-bubble presets below.

- **Scale images based on the layout style** - When using the same image for multiple layout styles, provide a scaled image variation for each layout style.

- **Historical HIG image sizes** - The archived native-bubble guidance specified 40x40 pt icons, 60x60 pt small images, and 263x150 pt large images. These describe that older layout system, not a fixed size for every current message type.

- **Historical HIG resolution guidance** - Those presets used @3x assets, with downscaling for lower-resolution presentation. Check the current message type's asset requirements rather than treating @3x as a universal web-image rule.

- **Produce artwork in the appropriate format** - Use de-interlaced PNG files for bitmap/raster artwork. Use JPEG for photos.

### Screenshots

Use accurate, privacy-safe examples of the approved experience when showing customers how to communicate with your business. A screenshot or template must not imply account approval or features that your service doesn't provide.

- **Historical template conventions** - The archived HIG specified SF Pro Regular and a 9:41 status-bar time. These were marketing-template conventions, not mandatory runtime settings.

- **Historical template palette** - That template used #848E99 with white text for customer bubbles and #E6E5EB with black text for agent bubbles. This records an older mockup style, not current Messages rendering or proof that the colors meet a contrast target.

- **Represent the actual client and account status** - The old template showed Back and Info controls, a logo, and a verified business name. Don't manufacture a verification badge or reuse an obsolete header to imply that it is a current screenshot. Follow the applicable Apple asset terms; this documentation doesn't grant rights to unrelated local artwork.

### Related Technologies

- [Messages for Business Accounts](https://register.apple.com/messages) - Account entry point
- [Apple Messages for Business guide](https://register.apple.com/resources/messages/messaging-documentation/) - Current registration and implementation guidance
- [Channel policies](https://register.apple.com/resources/messages/messaging-documentation/policies) - Live support, consent, and permitted-use requirements

## Changelog

This entry is verified against the archived Apple HIG article, not presented as the current account guide's publication history.

### May 2, 2023
- Consolidated guidance into one page.

---

*Sources: [Current Apple Messages for Business documentation](https://register.apple.com/resources/messages/messaging-documentation/), [registration assets](https://register.apple.com/resources/messages/messaging-documentation/register-your-acct), and the [archived Apple HIG article](https://web.archive.org/web/20250521171308id_/https://developer.apple.com/tutorials/data/design/human-interface-guidelines/messages-for-business.json).*

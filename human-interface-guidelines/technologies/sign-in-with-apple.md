# Sign in with Apple

Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Supporting Sign in with Apple lets people use the Apple Account they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see Authentication Services.

You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.

Sign in with Apple makes it easy for people to authenticate with Face ID, Touch ID, or Optic ID and has two-factor authentication built in for an added layer of security. Apple doesn't use Sign in with Apple to profile people or their activity in apps.

## Topics

### Best Practices

**Offering Sign in with Apple**

- **Ask people to sign in only in exchange for value** - People need to understand why you're asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.
- **Delay sign-in as long as possible** - People often abandon apps when they're forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.
- **If you require an account, ask people to set it up before offering any sign-in options** - Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.
- **Consider letting people link an existing account to Sign in with Apple** - When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they've already set up.
- **In a commerce app, wait until after people make a purchase before asking them to create an account** - If you support a guest checkout system, give people a quick way to create an account after the transaction completes.
- **Welcome people to their new account as soon as Sign in with Apple completes** - Help people use their new account right away; don't delay the experience by asking for information that isn't required.
- **Indicate when people are currently signed in** - You can help people confirm their sign-in method by displaying a phrase like "Using Sign in with Apple" in places like a settings or account interface.

**Collecting Data**

- **Clarify whether the additional data you request is required or just recommended** - If the data is legally or contractually required, make sure people understand that they must supply the additional information to complete the setup of their account.
- **Don't ask people to supply a password** - A key benefit of Sign in with Apple is that people don't have to create and memorize additional passwords.
- **Avoid asking for a personal email address when people supply a private relay address** - Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account.
- **Give people a chance to engage with your app before asking for optional data** - As people use your app, you can help them discover places where they can benefit from sharing more information with you.
- **Be transparent about the data you collect** - People value knowing how you use the data that they share with you.

**Displaying Buttons**

- **Prominently display a Sign in with Apple button** - Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.
- **Use system-provided buttons when possible** - When you use the system-provided APIs to create a Sign in with Apple button, you get guaranteed Apple-approved appearance and automatic translation.
- **Choose the appropriate button title variant** - The system provides several variants: "Sign in with Apple," "Sign up with Apple," and "Continue with Apple."
- **Choose the appropriate button appearance** - The system provides up to three options: white, white with an outline, and black. Choose the appearance that works best with your background.
- **Maintain minimum button size and margin** - Use the following values for guidance: minimum width 140pt, minimum height 30pt, minimum margin 1/10 of the button's height.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Sign in with Apple button](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple-button) - Button design guidance

### Developer Documentation

- [Authentication Services](https://developer.apple.com/documentation/authenticationservices) - Framework
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web) - Web implementation

### Videos

- [Move beyond passwords](https://developer.apple.com/videos/play/wwdc2021/10106/)
- [Simplify sign in for your tvOS apps](https://developer.apple.com/videos/play/wwdc2021/10279/)
- [Introducing Sign In with Apple](https://developer.apple.com/videos/play/wwdc2019/706/)

## Changelog

### September 14, 2022
- Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status
- Consolidated guidance into one page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)*
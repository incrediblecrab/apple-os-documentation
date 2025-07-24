# Generative AI

Generative AI empowers you to enhance your app or game with dynamic content and offer intelligent features that unlock new levels of creativity, connection, and productivity.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Generative artificial intelligence uses machine learning models to create and transform text, images, and other content. Use it to offer novel, delightful features that help people express themselves creatively, communicate effectively, and complete tasks more easily. For instance, generative AI can enable people to edit text, create imaginative stories and images, or interact with a character in a game that uses AI-generated dialog.

## Topics

### Best Practices

- **Design your experience responsibly** - Responsible AI is the intentional design and development of AI features that considers their direct and indirect impacts on people, systems, and society. With generative AI, it's often easy to quickly prototype an exciting new feature for your app, yet challenging to create a robust experience that works in all real-world situations. Orient your design process around crafting AI experiences that are inclusive, designed with care, and protect privacy.
- **Keep people in control** - While AI can manipulate and create content, respect people's agency and ensure they remain in charge of decision making and the overall experience. Honor their requests when in scope and the expected output is clear, and handle sensitive content carefully. Give them the ability to dismiss new content they don't want, and revert or retry content transformations or other actions they don't agree with. Clearly identify when and where you use AI.
- **Ensure an inclusive experience for all** - AI models learn from data and tend to favor the most common information. This may lead to harmful, unintended biases and stereotypes. Take extra care when designing your AI feature to consider how assumptions and personal attributes might impact the feature you have in mind. Test your feature across a diverse set of people to identify and correct stereotypes, and ensure inclusive results.
- **Design engaging and useful generative features** - Generative AI is a powerful tool, but it's not the right solution for every situation. Offer generative features when and where they provide clear and specific value, like time savings, improved communication, or enhanced creativity.
- **Ensure a great experience even when generative features aren't available or people opt not to use them** - In some cases, generative AI may be essential to an experience, and there's no reasonable non-AI substitute. In other cases, AI may play a complementary role that enhances your app's core functionality, but isn't critical for people achieving their goals. When possible, consider offering a non-AI fallback so people can always enjoy your app or game.

### Transparency

- **Communicate where your app uses AI** - Letting people know when and where your app uses AI sets expectations and gives people the opportunity to knowingly choose to use an AI-powered feature. Never trick someone into thinking they're interacting with or viewing content authored by a human if they're actually interacting with AI. Ensure your approach to disclosure aligns with any regulations in the regions where you offer your app.
- **Set clear expectations about what your AI-powered feature can and can't do** - Clarifying your experience's capabilities and limitations helps people establish a mental model of your feature. For example, when you introduce a feature, you might offer a brief tutorial. For open-ended features like a search bar or generation prompt, consider offering curated suggestions that make it easy to get started. If your feature has known limitations, let people know up front, show them how to get good results, and explain why when inferior results occur.

### Privacy

- **Prefer on-device processing** - Depending on your needs, you may be able to get great responses using on-device models, which prevent people's information from leaving the device. For example, you may choose to use the on-device models available through the Apple Foundation Models framework. On-device models may also respond quicker than server-based models, and are available even when the device is offline.
- **Ask permission before using personal information and usage data** - Some interactions with an AI model may involve sensitive information, like personal details, messages, photos, and feature usage information. After obtaining permission, use the minimum data you need and always offer a clear way to opt out of its use. If you need sensitive data for model improvement or storage, get explicit permission and handle it with care.
- **Clearly disclose how your app and its model use and store personal information** - People are more likely to be comfortable sharing data when they understand how it's used. Empower people to make an informed decision about what data they share with your AI model. When asking for permission to use someone's information, explain the benefits in a way that's concise, specific, and easy to understand.

### Models and Datasets

- **Thoughtfully evaluate model capabilities** - There are different types of generative models, some of which possess general knowledge, while others are trained for specific tasks. It's important to understand the capabilities of any model you consider. As early as you can, get a hands-on look at the models and data available to help orient your design.
- **Be intentional when choosing or creating a dataset** - Whether you're training a model from scratch or customizing an existing model, the data you choose greatly impacts the model's behavior. When you teach and evaluate your AI model, choose datasets that include a diverse range of subject matter representations. Learn where your data comes from and how it was gathered.

### Inputs

- **Guide people on how to use your generative feature** - Consider how to steer and educate people toward producing great results. One technique is to offer diverse, predefined example inputs that hint at what's possible for a feature.
- **Raise awareness about and minimize the chance of hallucinations** - When a generative model is unsure how to respond to a request, it may produce content that seems plausible but is made up. These hallucinations can misinform people because the model may convincingly present the information as factual, even when it's not. You can minimize the chance of hallucinations and limit their impact by carefully scoping what you ask a model to generate.
- **Consider consequences and get permission before performing destructive or potentially problematic tasks** - Before performing a task, consider whether a mistake or the inability to reverse the action might cause more work or stress for people. Avoid automating destructive actions, like deleting photos, and actions that are hard to undo, like making a purchase on a person's behalf.

### Outputs

- **Help people improve requests when blocked or undesirable results occur** - Minimize scoped or blocked output by coaching people how to be more successful next time. For example, if prompted to generate harmful content, Image Playground says that it's "Unable to use that description." When possible, consider offering example requests that might lead to better results.
- **Reduce unexpected and harmful outcomes with thoughtful design and thorough testing** - People generally use apps with good intentions, but harmful outcomes can still arise from both accidental and purposeful misuse, and when responding to potentially sensitive topics. Consider ways people might interact with your feature and test those scenarios.
- **Strive to avoid replicating copyrighted content** - Large AI models are trained using vast datasets from the internet and other sources. This means most generative models are familiar with and can unintentionally produce content similar to published work, including copyrighted content. You can reduce the likelihood of copyright infringement by building upon existing models that already protect against this, and by carefully curating inputs.
- **Factor processing time into your design** - Latency is how much time it takes for a model to produce an output. Generative models typically take longer to produce a result, so design a loading experience or generate in the background while a person uses another part of the app.
- **Consider offering alternate versions of results** - Depending on the design of your feature, it might work best to present a single result or multiple meaningfully different results from which people can choose. Offering people a choice can give them a greater sense of control and help bridge the gap between the model's interpretation and what someone actually wants.

### Continuous Improvement

- **Consider ways to improve your model over time** - You may want to update your model to adapt to people's behavior, respond to feedback, include new data, and leverage enhanced capabilities. You can make some improvements, such as updating a list of blocked words, frequently and independent of the app development cycle.
- **Let people share feedback on outputs** - Feedback can help you identify and respond to unexpected outcomes and new potential issues that arise despite thorough testing. Feedback also gives people a way to celebrate what they like best about your AI experience and report concerns when outputs don't match their expectations.
- **Design flexible, adaptable features** - Generative AI is a rapidly advancing technology, and models and their resource needs are constantly evolving. Consider ways your app or game can adapt as capabilities and models improve. For example, you may want to separate your model from your user experience so you can swap out the model for other models over time.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- [Loading](https://developer.apple.com/design/human-interface-guidelines/loading)

### Developer Documentation

- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/apple-intelligence-and-machine-learning) - Apple Intelligence
- [Foundation Models](https://developer.apple.com/documentation/foundation-models) - Foundation Models
- [Acceptable Use Requirements for the Foundation Models Framework](https://developer.apple.com/ml-research/foundation-models)

## Changelog

### June 9, 2025
- New page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/generative-ai)*
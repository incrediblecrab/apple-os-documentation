# Machine Learning

Machine learning enables apps and games to learn from data and usage patterns, letting you improve existing experiences and create engaging new ones.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

In addition to providing familiar features like image recognition and content recommendations, your app can use machine learning to forge deep connections with people and help them accomplish more with less effort.

For related guidance on how to use machine learning models to enable intelligent content creation experiences, see [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai).

## Topics

### Planning Your Design

Machine learning apps use models to perform tasks like recognizing images or finding relationships among numerical data. A great machine learning app depends on well-designed models as much as it depends on a well-designed UI and user experience.

As you design your models, keep the intended experience of your app in mind. It can take a long time to adjust the behavior of models, so be prepared to change the way you use data and metrics if the app experience needs to change.

Designing the UI and user experience of a machine learning app can be uniquely challenging. Because a machine learning app bases its behavior on the data it receives — reacting to changing information and conditions — you can't design specific reactions to a static set of scenarios. Instead, you design the experience by teaching the app how to interpret data and react accordingly.

### The Role of Machine Learning in Your App

Machine learning systems vary widely, and the ways an app can use machine learning vary widely, too. Consider how your app's features use machine learning in each of the following areas:

#### Critical or Complementary

If an app can still work without the feature that machine learning supports, machine learning is complementary to the app; otherwise, it's a critical dependency.

- **Complementary example** - The keyboard uses machine learning to provide QuickType suggestions. Because the keyboard still works without these suggestions, machine learning plays a complementary role.
- **Critical example** - Face ID relies on machine learning to perform accurate face recognition. Without machine learning, Face ID would not work.

#### Private or Public

Machine learning results depend on data. The more sensitive the data, the more serious the consequences of inaccurate or unreliable results.

- **Sensitive data example** - If a health app misinterprets data and incorrectly recommends a visit to the doctor, people are likely to experience anxiety and may lose trust in the app.
- **Non-sensitive data example** - If a music app misinterprets data and recommends an artist that people don't like, they're likely to view the result as an inconsequential mistake.

#### Proactive or Reactive

- **Reactive** - A reactive app feature provides results when people ask for them or when they take certain actions. QuickType suggests words in reaction to what people type.
- **Proactive** - A proactive app feature provides results without people requesting it to do so. Siri Suggestions can proactively suggest a shortcut based on people's recent routines.

#### Visible or Invisible

- **Visible** - People are usually aware of visible app features because such features tend to offer suggestions or choices that people view and interact with.
- **Invisible** - An invisible feature provides results that aren't obvious to people. For example, the keyboard learns how people type over time so it can optimize the tap area for each key.

#### Dynamic or Static

- **Dynamic** - Some models improve dynamically, as people interact with the app feature. Face ID improves dynamically as people's faces gradually change over time.
- **Static** - Others improve offline and affect the feature only when the app updates. Photos improves its object recognition capabilities with every new iOS release.

### Explicit Feedback

Explicit feedback provides actionable information your app can use to improve the content and experience it presents to people.

- **Request explicit feedback only when necessary** - People must take action to provide explicit feedback, so it's best to avoid requesting it if possible.

- **Always make providing explicit feedback a voluntary task** - You want to communicate that explicit feedback can help improve the experience without making people feel that providing it is mandatory.

- **Use simple, direct language to describe each explicit feedback option** - Avoid using imprecise terms such as "dislike" because such terms don't convey consequences and can be hard to translate.

- **Consider offering multiple options when requesting explicit feedback** - Providing multiple options can give people a sense of control and help them identify unwanted suggestions.

- **Act immediately when you receive explicit feedback** - When you react immediately to feedback and show that your app remembers it, you build people's trust in the value of providing it.

### Implicit Feedback

Implicit feedback is information that arises as people interact with your app's features. Unlike the specific responses you get from explicit feedback, implicit feedback gives you a wide range of information about user behavior and preferences.

- **Always secure people's information** - Implicit feedback can gather potentially sensitive user information, so you must be particularly careful to maintain strict controls on user privacy.

- **Help people control their information** - Tell people how your app gets and shares their information and give people ways to restrict the flow of their information.

- **Don't let implicit feedback decrease people's opportunities to explore** - Implicit feedback tends to reinforce people's behavior, which can improve the user experience in the short term, but may worsen it in the long term.

- **Use multiple feedback signals to improve suggestions** - Incorporate implicit feedback from multiple sources and interactions to help you avoid misinterpreting people's intentions.

- **Consider withholding private or sensitive suggestions** - If your app receives implicit feedback related to private or sensitive topics, avoid offering recommendations based on that feedback.

- **Prioritize recent feedback** - People's tastes can change frequently, so base your recommendations on recent implicit feedback.

### Calibration

Calibration is a process during which people provide information that an app feature needs before it can function.

- **Only use calibration when your feature can't function without that initial information** - If your feature can work without calibration, consider using other ways to gather the information you need.

- **Be clear about why you need people's information** - Typically, calibration is required before people can use a feature, so it's essential that they understand the value of providing their information.

- **Collect only the most essential information** - Designing a unique experience that requests a minimal amount of information can make people more comfortable participating.

- **Avoid asking people to participate in calibration more than once** - As people continue using your app or feature, you can use implicit or explicit feedback to evolve your information about them.

- **Make calibration quick and easy** - An ideal calibration experience makes it easy for people to respond, without compromising the quality of the information they provide.

### Corrections

People use corrections to fix mistakes that apps make.

- **Give people familiar, easy ways to make corrections** - You can avoid causing confusion by showing the steps your app takes as it performs the automated task.

- **Provide immediate value when people make a correction** - Reward people's effort by instantly displaying corrected content and persist the updates so people don't have to make the same corrections again.

- **Let people correct their corrections** - Sometimes, people make a correction without realizing that they've made a mistake.

- **Always balance the benefits of a feature with the effort required to make a correction** - People may not mind when a feature that automates a task makes a mistake, but they're likely to stop using the feature if it seems easier to perform the task themselves.

- **Never rely on corrections to make up for low-quality results** - Although corrections can reduce the impact of a mistake, depending on them may erode people's trust in your app.

### Mistakes

It's inevitable that your app will make mistakes. To help you avoid negative consequences, it's crucial to:

- **Anticipate mistakes** - As much as possible, design ways to avoid mistakes and mitigate them when they happen.
- **Help people handle mistakes** - The tools you provide to handle a mistake must be able to address the consequences.
- **Learn from mistakes when doing so improves your app** - Use each mistake as a data point that can refine your machine learning models.

### Multiple Options

Providing multiple options can give people a greater sense of control and can help bridge the gap between your model's predictions and what people actually want.

- **Prefer diverse options** - When possible, balance the accuracy of a response with the diversity of multiple options.

- **Avoid providing too many options** - People must evaluate each option before making a choice, so more options increases cognitive load.

- **List the most likely option first** - When you know how your confidence values correlate with the quality of your results, you might use them to rank the options.

- **Make options easy to distinguish and choose** - When options look similar, help people distinguish between them by providing a brief description of each one.

### Confidence

Confidence indicates the measure of certainty for a result. Not all models produce confidence values by default, so you might consider generating them if you can use them to improve the user experience of your app.

- **Know what your confidence values mean before you decide how to present them** - You need to verify that your confidence values correspond to the quality of your results.

- **Translate confidence values into concepts that people already understand** - Simply displaying a confidence value doesn't necessarily help people understand how it relates to a result.

- **Help people make decisions by conveying confidence in terms of actionable suggestions** - Understanding people's goals is key to expressing confidence in ways that help them make decisions.

### Attribution

An attribution expresses the underlying basis or rationale for a result, without explaining exactly how a model works.

- **Consider using attributions to help people distinguish among results** - Including attributions can help people choose an option based on their understanding of the premise that led to it.

- **Avoid being too specific or too general** - The best attributions strike a balance between these extremes.

- **Keep attributions factual and based on objective analysis** - Don't provide an attribution that implies understanding or judgment of people's emotions, preferences, or beliefs.

- **Avoid technical or statistical jargon** - In most situations, using percentages, statistics, and other technical jargon doesn't help people assess the results you provide.

### Limitations

Every feature has certain limitations to what it can deliver. When there's a mismatch between people's expectations about a feature and what the feature can actually accomplish, a limitation can seem like a defect.

- **Help people establish realistic expectations** - When a limitation may have a serious effect on user experience but happens rarely, consider making people aware of the limitation before they use your app or feature.

- **Demonstrate how to get the best results** - When you proactively show people how to get good results, you help them benefit from the feature and establish a more accurate mental model of the feature's capabilities.

- **Explain how limitations can cause unsatisfactory results** - Ideally, your feature can recognize and describe the reasons for poor results to make people aware of the limitations.

- **Consider telling people when limitations are resolved** - When you update your app to remove a limitation, you might want to notify people so that they can adjust their mental model of your feature.

### Related Technologies

- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai) - Intelligent content creation experiences
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) - Protecting user information

### Developer Documentation

- [Apple Intelligence and machine learning](https://developer.apple.com/machine-learning/) - Apple Intelligence
- [Create ML](https://developer.apple.com/documentation/createml) - Create ML
- [Core ML](https://developer.apple.com/documentation/coreml) - Core ML

## Changelog

### October 24, 2023
- Added art to Corrections section.

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/machine-learning)*
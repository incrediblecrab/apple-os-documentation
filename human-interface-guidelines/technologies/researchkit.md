# ResearchKit

A research app lets people everywhere participate in important medical research studies.

**Platforms:** iOS | iPadOS

## Overview

The ResearchKit framework provides predesigned screens and transitions that make it easy to design and build an engaging custom research app.

*These guidelines are for informational purposes only and don't constitute legal advice. Contact an attorney to obtain advice with respect to the development of a research app and any applicable laws.*

## Topics

### Creating the Onboarding Experience

When opening a research app for the first time, people encounter a series of screens that introduce them to the study, determine their eligibility to participate, request permission to proceed with the study, and, when appropriate, grant access to personal data.

Always display the onboarding screens in the correct order:

1. **Introduction**
2. **Eligibility**
3. **Informed consent**
4. **Permission to access data**

#### 1. Introduction

- **Provide an introduction that informs and provides a call to action** - Clearly describe the subject and purpose of your study. Also allow existing participants to quickly log in and continue an in-progress study.

#### 2. Determine Eligibility

- **Determine eligibility as soon as possible** - People don't need to move on to the consent section if they're not eligible for the study. Only present eligibility requirements that are necessary for your study.

- **Use simple, straightforward language** - Describe the requirements clearly and make it easy to enter information.

#### 3. Get Informed Consent

- **Make sure participants understand your study before you get their consent** - ResearchKit helps you make the consent process concise and friendly, while still allowing you to incorporate into the consent any legal requirements or requirements set by an institutional review board or ethics review board.

- **Break a long consent form into easily digestible sections** - Each section can cover one aspect of the study, such as data gathering, data use, potential benefits, possible risks, time commitment, how to withdraw, and so on.

- **Use simple, straightforward language** - Provide a high-level overview for each section. If necessary, provide a more detailed explanation that participants can read by tapping a Learn More button.

- **If it makes sense, provide a quiz that tests the participant's understanding** - You might do this for questions the participant would otherwise be asked when obtaining consent in person.

- **Get the participant's consent and contact information** - After agreeing to join the study, participants receive a confirmation dialog, followed by screens in which they provide their signature and contact details.

#### 4. Request Permission to Access Data

- **Get permission to access the participant's device or data** - Clearly explain why your research app needs access to location, Health, or other data, and don't request access to data that isn't critical to your study.

- **Request permission to send notifications** - If your app requires it, also ask for permission to send notifications to the participant's device.

### Conducting Research

To get input from participants, your study might use surveys, active tasks, or a combination of both.

#### Surveys

- **Create surveys that keep participants engaged** - ResearchKit provides many customizable screens you can use in your surveys, and makes it easy to present questions that require different types of answers.

- **Tell participants how many questions there are and about how long the survey will take**

- **Use one screen per question**

- **Show participants their progress in the survey**

- **Keep the survey as short as possible** - Several short surveys tend to work better than one long survey.

- **For questions that require additional explanation** - Use the standard font for the question and a slightly smaller font for the explanatory text.

- **Tell participants when the survey is complete**

#### Active Tasks

An active task requires the participant to engage in an activity, such as speaking into the microphone, tapping fingers on the screen, walking, or performing a memory test.

- **Describe how to perform the task using clear, simple language**

- **Explain any requirements** - Such as if the task must be performed at a particular time or under specific circumstances.

- **Make sure participants can tell when the task is complete**

### Managing Personal Information and Providing Encouragement

ResearchKit offers a profile screen you can use to let participants manage personal information while they're in your research app.

- **Use a profile to help participants manage personal data related to your study** - A profile screen can let people edit data that might change during the course of the study and remind them of upcoming activities.

- **Provide an easy way to leave a study** - Include access to important information, such as the consent document and privacy policy.

- **Use a dashboard to show progress and motivate participants to continue** - If appropriate for your study, use a dashboard to provide encouraging feedback, such as daily progress, weekly assessments, and results from specific activities.

### Related Technologies

- [Research & Care > ResearchKit](https://developer.apple.com/researchkit/) - Framework overview

### Developer Documentation

- [Research & Care > Developers](https://developer.apple.com/health-fitness/) - Developer resources
- [Protecting user privacy — HealthKit](https://developer.apple.com/documentation/healthkit/protecting_user_privacy) - Privacy guidelines
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) - Open source framework

## Changelog

### September 12, 2023
- Updated artwork.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/researchkit)*
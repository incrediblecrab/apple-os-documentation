# ResearchKit

An open source software framework that makes it easy to create apps for medical research or for other research projects.

## Overview

The **ResearchKit™** framework is an open source software framework that makes it easy to create apps for medical research or for other research projects. The ResearchKit framework codebase supports iOS and requires Xcode 12.0 or newer. The ResearchKit framework has a Base SDK version of 13.0.

Use ResearchKit's rich functionality to create compelling research experiences:

- Create and present surveys with various question types
- Obtain informed consent from participants with customizable consent flows
- Conduct active tasks that collect sensor data during specific activities
- Build research studies with modular, reusable components

The framework provides pre-built user interfaces for surveys, consent processes, and active tasks, which can be presented modally on iPhone or iPad. ResearchKit active tasks are not diagnostic tools nor medical devices of any kind and output from those active tasks may not be used for diagnosis.

### Key Components

**Surveys** - The ResearchKit framework provides a pre-built user interface for surveys, which can be presented modally on an iPhone or iPad. Use **ORKFormStep** and various answer formats to collect participant responses.

**Consent** - ResearchKit provides classes that you can customize to explain the details of your research study and obtain a signature if needed. Use **ORKInstructionStep** and **ORKBodyItem** to create informative consent flows.

**Active Tasks** - Some studies may need data beyond survey questions. ResearchKit's active tasks invite users to perform activities under semi-controlled conditions, while iPhone sensors actively collect data. Examples include dBHL tone audiometry, spatial span memory tests, and more.

## Topics

### Getting Started
- View the ResearchKit framework documentation by setting ResearchKit as your target in Xcode and selecting 'Build Documentation' in the Product menu
- The included **ORKCatalog** app demonstrates the different modules available in ResearchKit

### Installation
- Download the project source code and drag in **ResearchKit.xcodeproj**
- Embed ResearchKit framework in your app by adding it to the "Frameworks, Libraries, and Embedded Content" section

### Core Classes
- **ORKInstructionStep** - Create instruction and welcome steps for studies
- **ORKFormStep** - Build survey forms with various question types  
- **ORKFormItem** - Individual form items and questions
- **ORKBodyItem** - Rich content items with text, images, and learn more options
- **ORKAnswerFormat** - Various answer formats like height, scale, choice, etc.
- **ORKOrderedTask** - Predefined tasks for common research activities
- **ORKTaskViewController** - Present research tasks to participants

### Active Tasks
- **dBHLToneAudiometryTask** - Hearing assessment task
- **SpatialSpanMemoryTask** - Spatial memory assessment
- **TowerOfHanoiTask** - Problem-solving assessment
- And many other validated research tasks

### Sample Code Examples

```swift
import ResearchKit
import ResearchKitUI

// Create a height question
let sectionHeaderFormItem = ORKFormItem(sectionTitle: "Your question here.")
let heightQuestionFormItem = ORKFormItem(identifier: "heightQuestionFormItem1", 
                                       text: nil, 
                                       answerFormat: ORKAnswerFormat.heightAnswerFormat())
heightQuestionFormItem.placeholder = "Tap here"

let formStep = ORKFormStep(identifier: "HeightQuestionIdentifier", 
                          title: "Height", 
                          text: "Local system")
formStep.formItems = [sectionHeaderFormItem, heightQuestionFormItem]
```

```swift
// Create an active task
let orderedTask = ORKOrderedTask.dBHLToneAudiometryTask(withIdentifier: "dBHLToneAudiometryTaskIdentifier",
                                                       intendedUseDescription: nil, 
                                                       options: [])
let taskViewController = ORKTaskViewController(task: orderedTask, taskRun: nil)
taskViewController.delegate = self
present(taskViewController, animated: true)
```

---

*Source: [ResearchKit GitHub Repository](https://github.com/ResearchKit/ResearchKit)*
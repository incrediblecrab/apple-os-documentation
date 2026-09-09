# ResearchKit

An open source software framework that makes it easy to create apps for medical research or for other research projects.

## Overview

The **ResearchKit™** framework provides reusable components for research apps. The current repository README lists Xcode 16 or newer and a Base SDK of 17.0. Its `main` project sets an iOS 17.0 deployment target for ResearchKit, ResearchKitUI, and ResearchKitActiveTask. These are requirements of that checkout, not the original availability of every ResearchKit release; select and pin a compatible release for an existing app.

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
- Add the framework products your app uses to "Frameworks, Libraries, and Embedded Content": the examples below use **ResearchKit**, **ResearchKitUI**, and, for the active task, **ResearchKitActiveTask**. Follow the selected checkout's README for integration rather than assuming the core product supplies every UI and active-task API.

### Core Classes
- **ORKInstructionStep** - Create instruction and welcome steps for studies
- **ORKFormStep** - Build survey forms with various question types
- **ORKFormItem** - Individual form items and questions
- **ORKBodyItem** - Rich content items with text, images, and learn more options
- **ORKAnswerFormat** - Various answer formats like height, scale, choice, etc.
- **ORKOrderedTask** - A collection of steps presented in a fixed order, such as a sequential survey
- **ORKTaskViewController** - Present research tasks to participants

### Active Tasks
These are predefined-task factory methods on `ORKOrderedTask`, supplied by ResearchKitActiveTask, rather than standalone classes:
- **dBHLToneAudiometryTask** - Collect responses to tones presented through the task's audio workflow
- **spatialSpanMemoryTask** - Present and recall a sequence of spatial targets
- **towerOfHanoiTask** - Present a disk-moving puzzle

Choose tasks and equipment appropriate to the study protocol. Their inclusion in ResearchKit is not a claim of clinical validation or permission to use their output for diagnosis.

### Sample Code Examples

These are independent fragments, not a complete study app. The first constructs a form step to include in a task; a section header has no answer format, while the height item supplies one. Height entry follows the locale's measurement system, but its numeric result is reported in centimeters.

```swift
import ResearchKit
import ResearchKitUI

let sectionHeaderFormItem = ORKFormItem(sectionTitle: "Your question here.")
let heightQuestionFormItem = ORKFormItem(identifier: "heightQuestionFormItem1",
                                       text: nil,
                                       answerFormat: ORKAnswerFormat.heightAnswerFormat())
heightQuestionFormItem.placeholder = "Tap here"

let formStep = ORKFormStep(identifier: "HeightQuestionIdentifier",
                          title: "Height",
                          text: "Enter your height.")
formStep.formItems = [sectionHeaderFormItem, heightQuestionFormItem]
```

For the second fragment, place imports at file scope and the statements inside a `UIViewController` that implements `ORKTaskViewControllerDelegate`. Supply an already-created, writable, per-run file URL named `outputDirectory`. The dBHL task requires an output directory for its result files; omitting it can prevent logging or make recorder steps fail.

```swift
import UIKit
import ResearchKit
import ResearchKitUI
import ResearchKitActiveTask

let orderedTask = ORKOrderedTask.dBHLToneAudiometryTask(withIdentifier: "dBHLToneAudiometryTaskIdentifier",
                                                      intendedUseDescription: nil,
                                                      options: [])
let taskViewController = ORKTaskViewController(task: orderedTask, taskRun: nil)
taskViewController.outputDirectory = outputDirectory
taskViewController.delegate = self
present(taskViewController, animated: true)
```

Handle task completion, cancellation, and errors in the delegate's `taskViewController(_:didFinishWith:error:)` callback, dismiss the controller, and process results according to the participant's consent and the study's storage policy. Recorder errors, including unavailable sensor data or insufficient disk space, are separate from successful task completion. A consent UI does not replace the study's required review or its responsibility for protecting collected data.

---

*Source: [ResearchKit GitHub Repository](https://github.com/ResearchKit/ResearchKit)*

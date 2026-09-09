# WorkoutKit

Create, preview, and sync workout compositions to the Workout app.

**Plan and scheduler declarations:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 18.0+ | macOS 15.0+ | watchOS 10.0+. Runtime scheduling support and individual operations remain device-specific.

## Overview
The WorkoutKit framework provides models and utilities for creating and previewing workouts in your iOS and watchOS apps, and for syncing scheduled workouts to the Workout app on Apple Watch. The framework supports the following types of workouts:

**CustomWorkout**  
A structured interval workout with a series of steps containing custom goals and alerts

**SingleGoalWorkout**  
A workout with a single goal, such as distance, energy, or time

**PacerWorkout**  
A workout with distance and time goals

**SwimBikeRunWorkout**  
A workout that allows triathletes to seamlessly transition between swim, bike, and run activities

You define a workout and wrap it in a `WorkoutPlan`. On watchOS, [`openInWorkoutApp()`](https://developer.apple.com/documentation/workoutkit/workoutplan/openinworkoutapp()) opens the plan in Workout; do not assume this method is available to an iPhone app. Export using the throwing [`dataRepresentation`](https://developer.apple.com/documentation/workoutkit/workoutplan/datarepresentation) property (`try plan.dataRepresentation`). The symbol reference declares a property even though the framework overview still names a `dataRepresentation(as:)` method.

You can also use WorkoutKit to create and maintain a workout schedule and, with the user’s permission, sync scheduled compositions to Apple Watch. These compositions appear in a dedicated space in the Workout app and include your app’s icon and name.

Before scheduling, check [`WorkoutScheduler.isSupported`](https://developer.apple.com/documentation/workoutkit/workoutscheduler/issupported), then request authorization from its shared instance. `requestAuthorization()` asynchronously returns an authorization state. `schedule(_:at:)` is also asynchronous and accepts `DateComponents`; it is not a throwing operation. Respect the scheduler's [`maxAllowedScheduledWorkoutCount`](https://developer.apple.com/documentation/workoutkit/workoutscheduler/maxallowedscheduledworkoutcount) rather than hard-coding a capacity.

To access recorded health data for a workout, use [HealthKit](HealthKit.md). In particular, OS 27's heart-rate and cycling-power zone measurements belong to HealthKit; they are not a new minimum OS requirement for all WorkoutKit plan-authoring APIs.

## Authorization and failure handling

[`WorkoutScheduler`](https://developer.apple.com/documentation/workoutkit/workoutscheduler) authorization controls scheduling and is separate from HealthKit read/write authorization. Keep preview/export available where appropriate when scheduling permission is denied, and inspect the scheduling state rather than assuming that creating a plan has synchronized it to Apple Watch.

Validate workout goals and steps for their activity, check the availability of the specific plan or preview operation, and handle [`StateError`](https://developer.apple.com/documentation/workoutkit/stateerror) when opening a composition. A scheduled plan describes intended exercise; it is not evidence of a completed workout or measured health data.

## Topics

### Essentials
- [Customizing workouts with WorkoutKit](https://developer.apple.com/documentation/workoutkit/customizing-workouts-with-workoutkit) - Create, preview, and sync workouts for use in the Workout app on Apple Watch.

### Common workouts
- **SingleGoalWorkout** - A workout with a single goal.
- **PacerWorkout** - A workout in which a person covers a specific distance in a given time.
- **SwimBikeRunWorkout** - A workout for multisport activities that include running, biking, and swimming.

### Custom interval workouts
- **CustomWorkout** - A workout that includes a repeating series of work and recovery steps.
- **WorkoutStep** - A step in a workout.
- **IntervalBlock** - Blocks of work and recovery steps that repeat in a custom workout.
- **IntervalStep** - An interval that represents a work or recovery step in a workout.
- **WorkoutGoal** - A value that specifies the goal for a workout.
- **WorkoutAlert** - An alert that notifies the user of significant events during a workout.

### Workout plans and schedules
- **WorkoutPlan** - A wrapper around a workout object that your app can use to open the object in Workout or schedule it for later.
- [**ScheduledWorkoutPlan**](https://developer.apple.com/documentation/workoutkit/scheduledworkoutplan) - A workout plan with scheduled date components and a completion flag.
- **WorkoutScheduler** - An object for scheduling and managing workouts.

### Errors
- **StateError** - An error that occurs while previewing a workout composition.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WorkoutKit)*

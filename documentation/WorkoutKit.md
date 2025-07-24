# WorkoutKit

Create, preview, and sync workout compositions to the Workout app.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | watchOS 10.0+

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

You define a workout by initializing one of these workout types. Then you use the workout to create a WorkoutPlan, which provides methods for previewing, syncing, or exporting the plan. To open the plan in Workout on Apple Watch, call openInWorkoutApp(). To export the plan, call the dataRepresentation(as:) method.

You can also use WorkoutKit to create and maintain a workout schedule and, with the user’s permission, sync scheduled compositions to Apple Watch. These compositions appear in a dedicated space in the Workout app and include your app’s icon and name.

Before you can schedule a workout, you must ask for permission. Get the shared WorkoutScheduler instance, and call its requestAuthorization() method. Then call the schedule(_:at:) method to schedule workouts.

To access health data for the workout, see the HealthKit framework.

## Topics

### Essentials
- [Customizing workouts with WorkoutKit](https://developer.apple.com/documentation/workoutkit/customizing_workouts_with_workoutkit) - Create, preview, and sync workouts for use in the Workout app on Apple Watch.

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
- **ScheduledWorkoutPlan** - A wrapper around a workout plan that your app can use to schedule the workout plan.
- **WorkoutScheduler** - An object for scheduling and managing workouts.

### Errors
- **StateError** - An error that occurs while previewing a workout composition.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WorkoutKit)*

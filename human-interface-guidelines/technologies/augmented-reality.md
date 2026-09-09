# Augmented Reality

Augmented reality (or AR) lets you deliver immersive, engaging experiences that seamlessly blend virtual objects with the real world.

**Platforms:** iOS | iPadOS | visionOS

## Overview

On iPhone and iPad, an AR app can combine a live camera view with rendered virtual objects. ARKit supplies tracking and environmental information, while the app's rendering and interaction layers create the experience. People can explore from different viewpoints, interact with content, or join a supported multiuser session. visionOS uses a different, provider-based ARKit interface; don't assume the handheld camera-view architecture applies unchanged. See [ARKit](https://developer.apple.com/documentation/arkit).

**Check capabilities before offering AR.** An AR-first app needs an appropriate device requirement. For optional AR features, check the specific capability and avoid presenting an action that can only fail on the current device. See [Verifying Device Support and User Permission](https://developer.apple.com/documentation/arkit/verifying-device-support-and-user-permission).

**Note:** The following guidance applies to apps that run in iOS and iPadOS. To learn about using ARKit to create immersive augmented reality experiences in visionOS, see [ARKit](https://developer.apple.com/documentation/arkit).

Test controls against bright, dark, and changing camera or passthrough content. Preserve contrast and useful feedback with supported [accessibility preferences](../foundations/accessibility.md), and avoid overwhelming motion or interactions that require unsafe movement.

## Topics

### Best Practices

**Let people use the entire display.** Devote as much of the screen as possible to displaying the physical world and your app's virtual objects. Avoid cluttering the screen with controls and information that diminish the immersive experience.

**Strive for convincing placement and consistent motion.** Use appropriate scale, textures, lighting, and contact shadows so realistic objects appear grounded in detected surroundings. The HIG describes 60 scene updates per second as a handheld AR design target, not a guaranteed rate for every device or configuration. Profile your rendering and selected capture format; camera frame rate and rendering cadence are separate concerns, and merely requesting a rate doesn't guarantee smooth output.

**Consider how virtual objects with reflective surfaces show the environment.** Reflections in ARKit are approximations based on the environment captured by the camera. To help maintain the illusion that an AR experience is real, prefer small or coarse reflective surfaces that downplay the effect of these approximations.

**Use audio and haptics to enhance the immersive experience.** A sound effect or bump sensation is a great way to confirm that a virtual object has made contact with a physical surface or other virtual object. Background music can also help envelop people in the virtual world. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio) and [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics).

**Minimize text in the environment.** Display only the information that people need for your app experience.

**Distinguish screen-space overlays from world-anchored content.** A screen-space control stays in the device view's coordinate system while the camera scene changes beneath it. A world-anchored label or object instead stays associated with an environmental position and changes its projected screen position as the device moves. Choose deliberately rather than describing both as screen space.

**Consider using indirect controls when you need to provide persistent controls.** Indirect controls are not part of the virtual environment — instead, they are 2D controls displayed in screen space. If people need access to persistent controls in your app, consider placing the controls so that people don't have to adjust how they're holding the device to reach them. Also, consider using translucency in an indirect control to help avoid blocking the underlying scene. For example, the Measure app uses screen space to display a mix of translucent and opaque controls that people use to measure objects in the real world.

**Anticipate that people will use your app in a wide variety of real-world environments.** People may open your app in a place where there isn't much room to move around or there aren't any large, flat surfaces. Clearly communicate your app's requirements and expectations to people up front to help them understand how their physical environment can affect their AR experience. You might also consider offering different sets of features for use in different environments.

**Be mindful of people's comfort.** Holding a device at a certain distance or angle for a prolonged period can be fatiguing. To help avoid causing fatigue, consider placing objects at a distance that reduces the need to move the device closer to the object; in a game, consider keeping levels short and intermixed with brief periods of downtime.

**If your app encourages people to move, introduce motion gradually.** For example, you might not want to make people dodge a virtual projectile as soon as they enter your AR game. Give people time to adapt to the AR experience in your app and then progressively encourage movement.

**Be mindful of people's safety.** When people are immersed in an AR experience, they're not necessarily aware of their physical surroundings, so making rapid, sweeping, or expansive motions might be dangerous. Consider ways of making your app safe to operate; for example, a game could avoid encouraging large or sudden movements.

### Providing Coaching

**Guide setup and recovery.** When tracking needs information about the surroundings, show understandable instructions and progress. The system's [ARCoachingOverlayView](https://developer.apple.com/documentation/arkit/arcoachingoverlayview) can help during initial setup and relocalization after an interruption.

**Hide unnecessary app UI while coaching is visible.** A configured coaching overlay has automatic activation enabled by default and responds to its goal and the session's tracking state, including initialization or degraded tracking. Coordinate your app's controls with the overlay rather than assuming every AR session automatically supplies coaching UI.

**If necessary, offer a custom coaching experience.** Although you can configure the system-provided coaching view to help people provide specific information — such as the detection of a horizontal or vertical plane — you might need additional information or want to use a different visual style. If you want to design a custom coaching experience, use the system-provided coaching view for reference.

### Helping People Place Objects

**Show people when to locate a surface and place an object.** You can use the system-provided coaching view to help people find a horizontal or vertical flat surface on which to place an object. After ARKit detects a surface, your app can display a custom visual indicator to show when object placement is possible. You can help people understand how the placed object will look in the environment by aligning your indicator with the plane of the detected surface.

**Respond promptly to placement, then refine carefully.** Use the best available placement estimate and, when appropriate, make subtle corrections as tracking improves. Surface understanding is ongoing, not a one-time process with a universal completion event. Avoid abrupt jumps or silently changing an important user choice. See [ARTrackedRaycast](https://developer.apple.com/documentation/arkit/artrackedraycast) for queries that produce refined positions over time.

**Consider guiding people toward offscreen virtual objects.** Sometimes, it can be difficult for people to locate an object that's positioned offscreen. When this is the case, you can help people find such objects by offering visual or audible cues. For example, if an object is offscreen to the left, you could display an indicator along the left edge of the screen that guides people to point the camera in that direction.

**Avoid trying to precisely align objects with the edges of detected surfaces.** In AR, surface boundaries are approximations that may change as people's surroundings are further analyzed.

**Use plane classification only when supported and appropriate.** A floor or table classification can help guide furniture or game-board placement, but not every device supplies classification. Check [isClassificationSupported](https://developer.apple.com/documentation/arkit/arplaneanchor/isclassificationsupported), account for unclassified results, and provide a suitable fallback or explain a genuine capability requirement.

### Designing Object Interactions

**Let people use direct manipulation to interact with objects when possible.** It's more immersive and intuitive when people can interact with onscreen 3D objects by touching them directly, than by using indirect controls in screen space. However, in situations where people are moving around as they use your app, indirect controls can work better.

**Let people directly interact with virtual objects using standard, familiar gestures.** For example, consider supporting a single-finger drag gesture for moving objects, and a two-finger rotation gesture for spinning objects. For guidance, see [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures).

**In general, keep interactions simple.** Touch gestures are inherently two-dimensional, but an AR experience involves the three dimensions of the real world. Consider the following approaches to simplifying people's interactions with virtual objects.

**Respond to gestures within reasonable proximity of interactive virtual objects.** It can be difficult for people to be precise when aiming to touch specific points on objects that are small, thin, or placed at a distance. When your app detects a gesture near an interactive object, it's usually best to assume that people want to affect that object.

**Let people initiate object scaling when it makes sense in your app.** For example, if your app lets people explore an imaginary environment, it probably makes sense to support object scaling because your app doesn't need to represent the real world. On the other hand, if your app helps shoppers decide on furniture to buy, letting people scale a chair object doesn't help them visualize how the chair will look in a room.

**Tip:** Regardless of the purpose of your app, don't use scaling as a way to adjust the distance of an object. If you enlarge a distant object in an effort to make it appear closer, the result is a larger object that still looks far away.

**Be wary of potentially conflicting gestures.** A two-finger pinch gesture, for example, is similar to a two-finger rotation gesture. If you implement two similar gestures like this, be sure to test your app and make sure they're interpreted properly.

**Strive for virtual object movement that's consistent with the physics of your app's AR environment.** People don't necessarily expect an object to move smoothly over a rough or uneven surface, but they do expect objects to remain visible during movement. Aim to keep moving objects attached to real-world surfaces and avoid causing objects to jump or vanish and reappear as people resize, rotate, or move them.

**Explore even more engaging methods of interaction.** Gestures aren't the only way for people to interact with virtual objects in AR. Your app can use other factors, like motion and proximity, to bring content to life. A game character, for example, could turn its head to look at a person as they walk toward it.

### Offering a Multiuser Experience

**Plan for a shared understanding of the environment.** In a multiuser experience, each participant's tracking must contribute to consistent placement of shared content. Review ARKit's collaboration support and its implementation requirements through [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled).

**Use occlusion when it supports believable placement.** On supported devices, letting a person in the camera view obscure virtual content can clarify its position in the scene. See [Occluding virtual content with people](https://developer.apple.com/documentation/arkit/occluding-virtual-content-with-people).

**Let people join an ongoing experience when appropriate.** Avoid requiring everyone to restart merely to add a participant. Account for the joining person's tracking and shared-content state when implementing [isCollaborationEnabled](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled).

### Reacting to Real-World Objects

**Use recognizable real-world references purposefully.** A detected image or object can anchor relevant virtual content, such as an explanation next to an exhibit. Provide suitable reference data and guide people toward what the experience can recognize. See [Detecting Images in an AR Experience](https://developer.apple.com/documentation/arkit/detecting-images-in-an-ar-experience).

**Distinguish image detection from continuous image tracking.** In a world-tracking configuration, `detectionImages` identifies candidate images; a nonzero `maximumNumberOfTrackedImages` enables close pose tracking for up to four images simultaneously. Its default of zero disables that tracking, although detected anchors can still receive infrequent position updates. This isn't a claim that all ARKit configurations share the four-image limit.

**Use a brief grace period for transient tracking loss when appropriate.** The HIG suggests waiting up to one second before fading or removing attached content to reduce flicker. This is a visual-design recommendation, not a guaranteed detection timeout.

**Keep the detection set manageable.** The [`detectionImages`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/detectionimages) documentation recommends around 100 reference images or fewer for accuracy and performance; this isn't a hard limit or the number that can be continuously tracked at once. For larger collections, change the active set by context and rerun the updated configuration as the API requires. A museum app, for example, could narrow the set to the current exhibit, requesting location access only if it actually uses location services.

**Limit the number of reference images requiring an accurate position.** Updating the position of a reference image requires more resources. Use a tracked image when the image may move in the environment or when an attached animation or virtual object is small compared to the size of the image.

### Communicating with People

**If you must display instructional text, use approachable terminology.** AR is an advanced concept that may be intimidating to some people. To help make it approachable, avoid using technical terms like ARKit, world detection, and tracking. Instead, use friendly, conversational terms that most people will understand.

| Do | Don't |
|---|---|
| Unable to find a surface. Try moving to the side or repositioning your phone. | Unable to find a plane. Adjust tracking. |
| Tap a location to place the [name of object to be placed]. | Tap a plane to anchor an object. |
| Try turning on more lights and moving around. | Insufficient features. |
| Try moving your phone more slowly. | Excessive motion detected. |

**In a three-dimensional context, prefer 3D hints.** For example, placing a 3D rotation indicator around an object is more intuitive than displaying text-based instructions in a 2D overlay. Avoid displaying textual overlay hints in a 3D context unless people aren't responding to contextual hints.

**Make important text readable.** Screen-space labels can keep critical instructions accessible as the camera moves. For text placed in 3D, face it toward the viewer and preserve a readable apparent size; don't let an object's distance make its annotation too small to read.

**If necessary, provide a way to get more information.** Design a visual indicator that fits with your app experience to show people that they can tap for more information.

### Handling Interruptions

**Handle interruptions explicitly.** After tracking stops, previously placed content may no longer align with the surroundings. Explain the recovery process and support relocalization rather than treating stale placement as accurate. See [Managing Session Life Cycle and Tracking Quality](https://developer.apple.com/documentation/arkit/managing-session-life-cycle-and-tracking-quality).

**Consider using the system-provided coaching view to help people relocalize.** During relocalization, ARKit attempts to reconcile its previous state with new observations of the current environment. To make these observations more useful, you can use the coaching view to help people return the device to its previous position and orientation.

**Consider hiding previously placed virtual objects during relocalization.** To avoid flickering or other unpleasant visual effects during relocalization, it can be best to hide virtual objects and redisplay them in their new positions.

**Minimize interruptions if your app supports both AR and non-AR experiences.** One way to avoid interruptions is by embedding a non-AR experience within an AR experience so that people can handle the task without exiting and re-entering AR. For example, if your app helps people decide on a piece of furniture to purchase by placing the item in a room, you might let them change the upholstery without leaving the AR experience.

**Allow people to cancel relocalization.** Without a useful view near the previous position and orientation, relocalization can remain unresolved indefinitely. Recovery isn't guaranteed, especially when the surroundings have changed. If coaching doesn't help, offer a reset or another way to restart.

**For face-tracking experiences, indicate sustained tracking loss.** The HIG suggests showing concise feedback after roughly half a second without face tracking. Treat this as feedback-timing guidance, not an ARKit timeout or a claim that every device supports the same face-tracking capabilities.

### Suggesting Problem Resolutions

**Let people reset the experience if it doesn't meet their expectations.** Don't force people to wait for conditions to improve or struggle with object placement. Give them a way to start over again and see if they have better results.

**Suggest possible fixes if problems occur.** Analysis of the real-world environment and surface detection can fail or take too long for a variety of reasons — insufficient light, an overly reflective surface, a surface without enough detail, or too much camera motion. If your app is notified of these problems, use straightforward, friendly language to offer suggestions for resolving them.

| Problem | Possible suggestion |
|---|---|
| Insufficient features detected. | Try turning on more lights and moving around. |
| Excessive motion detected. | Try moving your phone slower. |
| Surface detection takes too long. | Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface. |

### Icons and Badges

**Apps can display an AR icon in controls that launch ARKit-based experiences.** You can download this icon in [Resources](https://developer.apple.com/design/resources/).

**Use the AR glyph as intended.** The glyph is strictly for initiating an ARKit-based experience. Never alter the glyph (other than adjusting its size and color), use it for other purposes, or use it in conjunction with AR experiences not created using ARKit.

**Maintain minimum clear space.** The minimum amount of clear space required around an AR glyph is 10% of the glyph's height. Don't let other elements infringe on this space or occlude the glyph in any way.

**Apps that include collections of products or other objects can use badging to identify specific items that can be viewed in AR using ARKit.** For example, a department store app might use a badge to mark furniture that people can preview in their home before making a purchase.

**Use the AR badges as intended and don't alter them.** You can download AR badges, available in collapsed and expanded form, in [Resources](https://developer.apple.com/design/resources/). Use these images exclusively to identify products or other objects that can be viewed in AR using ARKit. Never alter the badges, change their color, use them for other purposes, or use them in conjunction with AR experiences not created with ARKit.

**Prefer the AR badge to the glyph-only badge.** In general, use the glyph-only badge for constrained spaces that can't accommodate the AR badge. Both badges work well at their default size.

**Use badging only when your app contains a mixture of objects that can be viewed in AR and objects that cannot.** If all objects in your app can be viewed in AR, then badging is redundant.

**Keep badge placement consistent and clear.** A badge looks best when displayed in one corner of an object's photo. Always place it in the same corner and make sure it's large enough to be seen clearly (but not so large that it occludes important detail in the photo).

**Maintain minimum clear space.** The minimum amount of clear space required around an AR badge is 10% of the badge's height. Don't allow other elements to infringe on this space and occlude the badge in any way.

### Platform Considerations

**iOS | iPadOS**  
The handheld guidance above describes the iOS and iPadOS experience. Don't treat HIG coverage as a complete SDK availability list: current [ARKitSession](https://developer.apple.com/documentation/arkit/arkitsession) and [WorldTrackingProvider](https://developer.apple.com/documentation/arkit/worldtrackingprovider) declarations also include macOS 26, while specific hardware, runtime, provider, and authorization requirements still apply.

**visionOS**  
Use individual ARKit data providers for capabilities such as planes, world anchors, hand tracking, and scene reconstruction. Check each provider's support and required authorizations, explain requested access, and handle denial or revocation with usable alternatives. Hand-tracking data and world-sensing data have distinct privacy requirements. See [ARKit in visionOS](https://developer.apple.com/documentation/arkit/arkit-in-visionos) and [Setting up access to ARKit data](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data).

### Related Components

- [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) - How it enhances AR experiences

- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) - Interaction patterns for AR

### Developer Documentation

- [ARKit](https://developer.apple.com/documentation/arkit) - Framework (ARKit)
- [maximumNumberOfTrackedImages](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/maximumnumberoftrackedimages) - World-tracking image updates and limits
- [ARImageTrackingConfiguration](https://developer.apple.com/documentation/arkit/arimagetrackingconfiguration) - Distinct image-only tracking configuration
- [ARConfiguration.VideoFormat](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class) - Supported capture resolution and frame rate

## Historical API Context

These are framework-availability notes, not HIG article-update dates.

### visionOS 1.0
- The provider-based ARKit interface, including `ARKitSession` and `WorldTrackingProvider`, is documented from visionOS 1.0. Check individual providers for their own availability.

### iOS 11.0
- ARKit and `ARWorldTrackingConfiguration` are documented from iOS 11.0. Later capabilities have separate OS and device requirements.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/augmented-reality)*

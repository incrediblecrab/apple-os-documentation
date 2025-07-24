# Loading

The best content-loading experience finishes before people become aware of it.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

If your app or game loads assets, levels, or other content, design the behavior so it doesn't disrupt or negatively impact the user experience.

## Topics

### Best practices

- **Show something as soon as possible** - If you make people wait for loading to complete before displaying anything, they can interpret the lack of content as a problem with your app or game. Instead, consider showing placeholder text, graphics, or animations as content loads, replacing these elements as content becomes available.

- **Let people do other things while waiting** - Loading content in the background helps give people access to other actions. For example, a game could load content in the background while players learn about the next level or view an in-game menu. For developer guidance, see Improving the player experience for games with large downloads.

- **Provide interesting content for long loads** - If loading takes an unavoidably long time, give people something interesting to view while they wait. For example, you might provide gameplay hints, display tips, or introduce people to new features. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy your placeholder content or having so much time that you need to repeat it.

- **Download large assets in the background** - Improve installation and launch time by downloading large assets in the background. Consider using the Background Assets framework to schedule asset downloads — like game level packs, 3D character models, and textures — to occur immediately after installation, during updates, or at other nondisruptive times.

### Showing progress

- **Communicate loading clearly** - Clearly communicate that content is loading and how long it might take to complete. Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called progress indicators — to show that loading is ongoing. In general, you use a determinate progress indicator when you know how long loading will take, and you use an indeterminate progress indicator when you don't. For guidance, see Progress indicators.

- **Consider custom loading views for games** - Standard progress indicators work well in most apps, but can sometimes feel out of place in a game. Consider designing a more engaging experience by using custom animations and elements that match the style of your game.

### Platform considerations

**iOS, iPadOS, macOS, tvOS, visionOS**  
No additional considerations.

**watchOS**  
As much as possible, avoid showing a loading indicator in your watchOS experience. People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it's better to display a loading indicator than a blank screen.

### Related

- [Launching](https://developer.apple.com/design/human-interface-guidelines/launching)
- [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)

### Developer documentation

- [Background Assets](https://developer.apple.com/documentation/backgroundassets)

### Videos

- [Discover Apple-Hosted Background Assets](https://developer.apple.com/videos/play/wwdc2024/10057)

## Changelog

### June 9, 2025
- Revised guidance for storing downloads to reflect downloading large assets in the background.

### June 10, 2024
- Added guidelines for showing progress and storing downloads, and enhanced guidance for games.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/loading)*
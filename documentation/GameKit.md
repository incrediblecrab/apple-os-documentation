# GameKit

Enable players to interact with friends, compare leaderboard ranks, earn achievements, and participate in multiplayer games.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.1+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

Use the GameKit framework to implement Game Center social-gaming network features. Game Center is an Apple service that provides a single account that identifies players across all their games and devices. After players sign in to Game Center on their device, they can access their friends and use Game Center features you implement.

Before you can use GameKit classes, you must enable Game Center in your project and initialize the local player in your code; otherwise, your game receives a GKError.Code.notAuthenticated error.

If you have an existing Unity project, you can access the GameKit framework using the Apple Unity Plug-ins.

### Implement Game Center Features

After you've enabled Game Center, you can implement many useful features to enhance the gaming experience.

You can add leaderboards that let players see how well they rank amongst friends and players all over the world. Create recurring leaderboards to organize regular competitions that provide players more chances to earn the top score. As players progress through your game, you can reward them with achievements that encourage them to keep playing.

GameKit supports real-time and turn-based multiplayer experiences. Players can choose automatic matching or invite their friends to join a game. You can support turn-based gaming in which a match plays out over a series of alternating turns, and players can receive invitations even when your game isn't in the foreground.

GameKit also provides user interface components for your players to see highlights and access their Game Center data directly in your game. The access point provides a way for players to open a dashboard in which they can browse their profile, leaderboards, and achievements, as well as manage their friends list.

For designing Game Center features in your app, see Human Interface Guidelines > Technologies > Game Center.

## Topics

### Essentials
- [Initializing and configuring Game Center](https://developer.apple.com/documentation/gamekit/initializing_and_configuring_game_center) - Enable Game Center, configure features, and test them locally in your Xcode project.
- [Authenticating a player](https://developer.apple.com/documentation/gamekit/authenticating_a_player) - Confirm player credentials and device capabilities and check for account restrictions.
- [Improving the player experience for games with large downloads](https://developer.apple.com/documentation/gamekit/improving_the_player_experience_for_games_with_large_downloads) - Provide ample content in your base installation and then use on-demand resources and the Background Assets API to handle additional content.
- **Game Center Entitlement** - A Boolean value that indicates whether users of the app may see and compare achievements on a leaderboard, invite friends, and start multiplayer games.

### Players
- [Connecting players with their friends in your game](https://developer.apple.com/documentation/gamekit/connecting_players_with_their_friends_in_your_game) - Give players the ability to connect and interact with friends in your game.
- [Saving the player's game data to an iCloud account](https://developer.apple.com/documentation/gamekit/saving_the_player_s_game_data_to_an_icloud_account) - Save game data during play or after a game in the player's iCloud account that's accessible from any device.
- [Protecting the player's privacy using scoped identifiers](https://developer.apple.com/documentation/gamekit/protecting_the_player_s_privacy_using_scoped_identifiers) - Use the scoped identifiers that GameKit provides you as player IDs when transmitting or saving player data.
- **GKLocalPlayer** - The local player who signs in to Game Center on the device running the game.
- **GKPlayer** - A remote player who the local player running your game can invite and communicate with through Game Center.
- **GKBasePlayer** - A class that provides common data and methods for the different player objects.
- **GKLocalPlayerListener** - A protocol that handles events for Game Center players.
- **GKPlayerAuthenticationDidChangeNotificationName** - A notification that posts after GameKit authenticates the local player.
- **GKPlayerDidChangeNotificationName** - A notification that posts when a player object's data changes.

### Game Center Interfaces
- [Adding an access point to your game](https://developer.apple.com/documentation/gamekit/adding_an_access_point_to_your_game) - Provide your users a convenient connection to the Game Center dashboard.
- [Displaying the Game Center dashboard](https://developer.apple.com/documentation/gamekit/displaying_the_game_center_dashboard) - Provide an interface for players to navigate to their Game Center data from your game.
- **GKAccessPoint** - An object that allows players to view and manage their Game Center information from within your game.
- **GKDialogController** - An object that provides the ability to present the dashboard in macOS games.
- **GKViewController** - The abstract base protocol adopted by GameKit view controller classes.

### Leaderboards
- [Encourage progress and competition with leaderboards](https://developer.apple.com/documentation/gamekit/encourage_progress_and_competition_with_leaderboards) - Let players measure their own progress and compare their skills with friends and others.
- [Creating recurring leaderboards](https://developer.apple.com/documentation/gamekit/creating_recurring_leaderboards) - Create a leaderboard for your game that ranks player scores based on a schedule.
- [Adding Recurring Leaderboards to Your Game](https://developer.apple.com/documentation/gamekit/adding_recurring_leaderboards_to_your_game) - Encourage competition in your games by adding leaderboards that have a duration and repeat.
- **GKLeaderboard** - A leaderboard for a game that Game Center stores.
- **GKLeaderboardSet** - Organizes leaderboards into logical and coherent groups.
- **GKLeaderboardScore** - Information about a player's score on a leaderboard.

### Achievements
- [Rewarding players with achievements](https://developer.apple.com/documentation/gamekit/rewarding_players_with_achievements) - Use achievements to motivate players and engage them more in your game.
- **GKAchievement** - An achievement you can award a player as they make progress toward and reach a goal in your game.
- **GKAchievementDescription** - An object containing the text and artwork used to present an achievement to a player.

### Challenges
- [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/gamekit/creating_engaging_challenges_from_leaderboards) - Encourage friendly competition by adding challenges to your game.
- [Choosing a leaderboard for your challenges](https://developer.apple.com/documentation/gamekit/choosing_a_leaderboard_for_your_challenges) - Understand what gameplay works well when configuring challenges in your game.
- **GKChallengeDefinition** - An object that represents the static metadata you define for the challenge. (Beta)
- **GKShowChallengeBanners** - A Boolean value that indicates whether GameKit can display challenge banners in a game. (Deprecated)

### Activities
- [Creating activities for your game](https://developer.apple.com/documentation/gamekit/creating_activities_for_your_game) - Use activities to surface game content to players and encourage them to connect with each other.
- **GKGameActivity** - An object that represents a single instance of a game activity for the current game. (Beta)
- **GKGameActivityDefinition** - An object that represents the static metadata you define for the activity. (Beta)
- **GKGameActivityListener** - An object that responds to activity events. (Beta)

### Real-time Games
- [Creating real-time games](https://developer.apple.com/documentation/gamekit/creating_real-time_games) - Develop games where multiple players interact in real time.
- [Finding multiple players for a game](https://developer.apple.com/documentation/gamekit/finding_multiple_players_for_a_game) - Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](https://developer.apple.com/documentation/gamekit/exchanging_data_between_players_in_real-time_games) - Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](https://developer.apple.com/documentation/gamekit/adding_voice_chat_to_multiplayer_games) - Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [Matchmaking rules](https://developer.apple.com/documentation/gamekit/matchmaking_rules) - Game Center applies different type of rules you create in a particular order to find the best matches.
- **GKMatchRequest** - An object that encapsulates the parameters to create a real-time or turn-based match.
- **GKMatchmaker** - An object that creates matches with other players without presenting an interface to the players.
- **GKMatchmakerViewController** - An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.
- **GKInviteEventListener** - A protocol that handles invite events from Game Center.
- **GKInvite** - An invitation to join a match sent to the local player from another player.
- **GKMatch** - A peer-to-peer network between a group of players that sign into Game Center.

### Turn-based Games
- [Creating turn-based games](https://developer.apple.com/documentation/gamekit/creating_turn-based_games) - Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](https://developer.apple.com/documentation/gamekit/starting_turn-based_matches_and_passing_turns_between_players) - Let Game Center store and forward match data between players in a turn-based game.
- [Sending messages to players in turn-based games](https://developer.apple.com/documentation/gamekit/sending_messages_to_players_in_turn-based_games) - Notify players of match events by sending messages and game data.
- [Exchanging data between players in turn-based games](https://developer.apple.com/documentation/gamekit/exchanging_data_between_players_in_turn-based_games) - Add the ability for players to exchange game data and send messages while waiting for their turns.
- **GKTurnBasedMatchmakerViewController** - An interface that allows a player to invite other players to a turn-based match and automatch to fill any empty slots.
- **GKTurnBasedMatch** - An object that encapsulates the match data for games where players take turns.
- **GKTurnBasedParticipant** - A participant in a turn-based match.
- **GKTurnBasedEventListener** - The protocol that handles turn-based and data-exchange events between participants in a match.
- **GKTurnBasedExchange** - Exchange request information that participants send in a turn-based match.
- **GKTurnBasedExchangeReply** - Details about a recipient's response to an exchange request.
- **GKGameCenterBadgingDisabled** - A Boolean value indicating whether GameKit can add badges to a turn-based game icon.

### Errors
- **GKError** - The error structure used by this framework.
- **Code** - Error codes for the GameKit error domain.
- **GKErrorDomain** - The error domain for general game errors.

### Deprecated
- [Deprecated symbols](https://developer.apple.com/documentation/gamekit/deprecated_symbols) - Review unsupported symbols and their replacements.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GameKit)*
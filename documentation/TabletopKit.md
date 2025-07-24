# TabletopKit

Create multiplayer spatial games on a virtual table surface and use FaceTime to invite players.

**Platforms:** visionOS 2.0+

## Overview

TabletopKit helps you create a spatial multiplayer game on a table surface for visionOS, where players join your game using SharePlay. TabletopKit provides support for designing your game, implementing rules, rendering effects, and syncing multiplayer game state.

Follow these steps to implement your TabletopKit game:

1. **Configure your game** on the tabletop and create the game pieces or equipment that players interact with. You provide the renderer that draws your game and its pieces.

2. **Implement the game rules** and player interactions with the equipment. TabletopKit processes and represents player gestures as interactions. You observe the interactions and append your game-specific actions.

3. **Add effects** to the RealityKit entities of renderable equipment and trigger them during interactions. For example, play a sound effect when a player throws a piece or an animation when a player achieves a goal.

4. **Set up multiplayer** using SharePlay. Start a Group Activities session and provide it to TabletopKit. Then customize the spatial experience of your game. For example, place the players in their seats and spectators around the room.

To get started, create a **TabletopGame** object that represents your game instance and a **TableSetup** object that represents your game layout and equipment.

## Topics

### Essentials
- [Creating tabletop games](https://developer.apple.com/documentation/tabletopkit/creating_tabletop_games) - Develop a spatial board game where multiple players interact with pieces on a table
- [Synchronizing group gameplay with TabletopKit](https://developer.apple.com/documentation/tabletopkit/synchronizing_group_gameplay_with_tabletopkit) - Maintain game state across multiple players in a race to capture all the coins
- **TabletopGame** - An object that manages the setup and gameplay of a tabletop game
- **TableSetup** - An object that represents the arrangement of seats, equipment, and counters around the game table
- **Tabletop** protocol - A protocol for the table surface in your game
- **EntityTabletop** protocol - A protocol for the table surface in your game when you render it using RealityKit
- **TabletopShape** - An object that represents the physical properties of the table

### Seats
- **TableSeat** protocol - A protocol for seats at the table that players occupy
- **EntityTableSeat** protocol - A protocol for seats at the table that you render using RealityKit
- **TableSeatIdentifier** - A unique identifier for seats
- **TableSeatState** - The data associated with a seat that a player occupies
- **SeatState** protocol - A protocol for seat data that TabletopKit syncs between players

### Equipment
- **Equipment** protocol - A protocol for equipment that players directly interact with in a game
- **EntityEquipment** protocol - A protocol for equipment in a game that you render using RealityKit
- **EquipmentIdentifier** - A unique identifier for equipment
- **EquipmentState** protocol - A protocol for the equipment data that TabletopKit syncs between players
- **BaseEquipmentState** - A state for equipment that contains no equipment-specific data
- **CardState** - A state for cards that contains face up and down information
- **DieState** - A state for dice that contains the current value
- **RawValueState** - A state for equipment that contains a game-specific value
- **ControllingSeats** - The seats that can manipulate or interact with the equipment

### Equipment Layout
- **EquipmentLayout** protocol - A protocol for objects that describe the layout of equipment
- **DefaultEquipmentLayout** - An object that provides a standard configuration for equipment layout
- **EquipmentPose2D** - An object that represents the position and rotation of equipment on the XZ plane
- **EquipmentPose3D** - An object that represents the 3D position and orientation of equipment on the table

### Score Counters
- **ScoreCounter** - An object that keeps a score in a tabletop game

### Players
- **Player** - A player in a tabletop game
- **PlayerIdentifier** - A unique identifier for players

### Actions
- **TabletopAction** protocol - A protocol for objects that describe an action in a tabletop game
- **MoveEquipmentAction** - An action that moves a piece of equipment on the table or changes the grouping
- **UpdateEquipmentAction** - An action that updates properties of equipment on the table
- **SetTurnAction** - An action that sets the current seats participating in the current turn
- **UpdateCounterAction** - An action that updates the game counter
- **CreateBookmarkAction** - An action that takes a snapshot of the game

### Interactions
- **TabletopInteraction** - A protocol for objects that manage the entire flow of players interacting with equipment
- **TossableRepresentation** - An object that represents geometric shapes that the player can throw during gameplay, such as dice
- **TableSnapshot** - A snapshot of the current state of the table
- **TableVisualState** - A structure that represents the appearance of an object on the table
- **TableCursor** - A cursor conveys information about one equipment that is currently being controlled by an interaction
- **TableCursorIdentifier** - A unique identifier for cursors

### Bookmarks
- **StateBookmark** - A snapshot of the game state at a point in time
- **StateBookmarkIdentifier** - A unique identifier for bookmarks

### Multiplayer Network Session
- **TabletopNetworkSession** - An object that coordinates network-related tasks in multiplayer games
- **TabletopNetworkSessionCoordinator** protocol - A protocol for objects that manage network sessions between peers
- **TabletopSendMessageResult** - The possible results of sending messages in a network session

### Debugging
- **DebugDrawOptions** - Types of items in a rendering that you want to debug

### Protocols (Beta)
- **CustomAction** protocol - A protocol that represents an action whose behavior is implemented outside of TabletopKit
- **CustomEquipmentState** protocol - A specialized protocol for the equipment state that allows to accommodate custom data that TabletopKit syncs between players
- **MutableEquipmentState** protocol - A protocol for equipment data that TabletopKit syncs between players, and that can be mutated

### Structures (Beta)
- **CounterCollection** - A collection of score counters that can be inspected and modified
- **EquipmentCollection** - A collection of equipment whose state can be inspected and modified
- **EquipmentStateCollection** - A collection of equipment states that can be inspected and modified
- **TableState** - The state of the table that can be queried and modified

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TabletopKit)*
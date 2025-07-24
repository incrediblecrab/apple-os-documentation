# GameplayKit

Architect and organize your game logic. Incorporate common gameplay behaviors such as random number generation, artificial intelligence, pathfinding, and agent behavior.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | tvOS 9.0+ | visionOS 1.0+

## Overview

GameplayKit is an object-oriented framework that provides foundational tools and technologies for building games. GameplayKit includes tools for designing games with functional, reusable architecture, as well as technologies for building and enhancing gameplay features such as character movement and opponent behavior.

### Getting Started with GameplayKit

GameplayKit covers many aspects of game design and development. For deeper discussions of the game design patterns you can leverage with GameplayKit, along with tutorials that illustrate building games with GameplayKit features, see GameplayKit Programming Guide.

### Related Sample Code

To experiment with GameplayKit in action, see these sample code projects:

- Boxes: GameplayKit Entity-Component Basics
- Dispenser: GameplayKit State Machine Basics
- Pathfinder: GameplayKit Pathfinding Basics
- AgentsCatalog: Using the Agents System in GameplayKit
- FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI
- DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit

## Topics

### Entities and Components
A general architecture for designing composable, reusable gameplay logic.
- **GKEntity** - An object relevant to gameplay, with functionality entirely provided by a collection of component objects.
- **GKComponent** - The abstract superclass for creating objects that add specific gameplay functionality to an entity.
- **GKComponentSystem** - Manages periodic update messages for all component objects of a specified class.

### State Machines
A modular system for defining state-dependent gameplay logic.
- **GKState** - The abstract superclass for defining state-specific logic as part of a state machine.
- **GKStateMachine** - A finite-state machine—a collection of state objects that each define logic for a particular state of gameplay and rules for transitioning between states.

### Spatial Partitioning
Data structures that organize the objects in a game world for quick searching by position or proximity.
- **GKQuadtree** - A data structure for organizing objects based on their locations in a two-dimensional space.
- **GKQuadtreeNode** - A helper class for managing the objects you organize in a quadtree.
- **GKOctree** - A data structure for organizing objects based on their locations in a three-dimensional space.
- **GKOctreeNode** - A helper class for managing the objects you organize in an octree.
- **GKRTree** - A data structure that adaptively organizes objects based on their locations in a two-dimensional space.

### Strategists
A form of AI for planning moves in turn-based games. Describe your gameplay by creating classes that adopt the game model protocols, then use those classes with a strategist object to create AI players or suggest moves.
- **GKStrategist** - A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.
- **GKMinmaxStrategist** - An AI that chooses moves in turn-based games using a deterministic strategy.
- **GKMonteCarloStrategist** - An AI that chooses moves in turn-based games using a probabilistic strategy.
- **GKGameModel** - Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.
- **GKGameModelPlayer** - Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.
- **GKGameModelUpdate** - Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.

### Decision Trees
Define a series of questions and possible answers leading to a final action, or automatically build a predictive model based on data your provide.
- **GKDecisionTree** - A data structure that models a set of specific questions, their possible answers, and the actions that follow from a series of answers.
- **GKDecisionNode** - A node for use in manually creating decision trees, representing a specific question and possible answers, or an action that follows from answering other questions.

### Pathfinding
Create graphs that model the navigability of your game world, allowing GameplayKit to plan optimal routes for game characters to follow.
- **GKGraph** - A collection of nodes that describes the navigability of a game world and provides pathfinding methods to search for routes through that space.
- **GKObstacleGraph** - A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- **GKMeshGraph** - A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.
- **GKGridGraph** - A navigation graph for 2D game worlds where movement is constrained to an integer grid.
- **GKGraphNode** - A single node in a navigation graph for use in pathfinding.
- **GKGraphNode2D** - A node in a navigation graph, associated with a point in continuous 2D space.
- **GKGraphNode3D** - A node in a navigation graph, associated with a point in continuous 3D space.
- **GKGridGraphNode** - A node in a navigation graph, associated with a position on a discrete two-dimensional grid.

### Agents, Goals, and Behaviors
Add autonomous movement to characters and other game objects by combining high-level goals such as moving to a target, following a path, or avoiding obstacles.
- **GKAgent** - A component that moves a game entity according to a set of goals and realistic constraints.
- **GKAgent2D** - An agent that operates in a two-dimensional space.
- **GKAgent3D** - An agent that operates in a three-dimensional space.
- **GKGoal** - An influence that motivates the movement of one or more agents.
- **GKBehavior** - A set of goals that together influence the movement of an agent.
- **GKCompositeBehavior** - A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- **GKPath** - A polygonal path that can be followed by an agent.
- **GKAgentDelegate** - Implement this protocol to synchronize the state of an agent with its visual representation in your game.

### Obstacles
Classes that model impassable areas in a game world, for use with Pathfinding and Agents.
- **GKObstacle** - The abstract base class for objects representing impassable areas in a game world.
- **GKCircleObstacle** - A circular impassable area to be avoided by agents.
- **GKSphereObstacle** - A spherical impassable volume to be avoided by agents.
- **GKPolygonObstacle** - A polygon-shaped impassable area in a 2D game world.

### Procedural Noise
Generate fields of coherent random noise, then use them to create texture images resembling natural phenomena such as clouds or wood grain, build procedural game worlds of unlimited size, and more.
- **GKNoiseSource** - The abstract superclass for procedural noise generators.
- **GKNoise** - A representation of procedural noise, generated by a noise source, that you can use to process, transform, or combine noise.
- **GKNoiseMap** - A sample of procedural noise data from which you can read noise values directly or create noise textures.
- **GKCoherentNoiseSource** - The abstract superclass for procedural noise generators that create coherent noise.
- **GKBillowNoiseSource** - A procedural noise generator whose output is a type of fractal coherent noise with smooth features.
- **GKPerlinNoiseSource** - A procedural noise generator whose output is a type of fractal coherent noise resembling natural phenomena such as clouds and terrain.
- **GKRidgedNoiseSource** - A procedural noise generator whose output is a type of multifractal coherent noise with sharply defined features.
- **GKVoronoiNoiseSource** - A procedural noise generator whose output (also called Worley noise or cellular noise) divides space into discrete cells surrounding random seed points.
- **GKCylindersNoiseSource** - A procedural noise generator whose output is a 3D field of concentric cylindrical shells.
- **GKSpheresNoiseSource** - A procedural noise generator whose output is a 3D field of concentric spherical shells.
- **GKCheckerboardNoiseSource** - A procedural noise generator whose output is an alternating square pattern.
- **GKConstantNoiseSource** - A procedural noise generator that outputs a field of a single constant value.

### Randomization
Robust, flexible implementations of standard algorithms that let you add unpredictability to gameplay without compromising testability.
- **GKRandom** - The common interface for all randomization classes in (or usable with) GameplayKit.
- **GKRandomSource** - The superclass for all basic randomization classes in GameplayKit.
- **GKARC4RandomSource** - A basic random number generator implementing the ARC4 algorithm, which is suitable for most gameplay mechanics.
- **GKLinearCongruentialRandomSource** - A basic random number generator implementing the linear congruential generator algorithm, which is faster but less random than the default random source.
- **GKMersenneTwisterRandomSource** - A basic random number generator implementing the Mersenne Twister algorithm, which is more random, but slower than the default random source.
- **GKRandomDistribution** - A generator for random numbers that fall within a specific range and that exhibit a specific distribution over multiple samplings.
- **GKGaussianDistribution** - A generator for random numbers that follow a Gaussian distribution (also known as a normal distribution) across multiple samplings.
- **GKShuffledDistribution** - A generator for random numbers that are uniformly distributed across many samplings, but where short sequences of similar values are unlikely.

### Rule Systems
Separate game design from executable code to speed up your gameplay development cycle, or implement fuzzy logic reasoning to add realistic behavior to your game.
- **GKRule** - A rule to be used in the context of a rule system, with a predicate to be tested and an action to be executed when the test succeeds.
- **GKNSPredicateRule** - A rule for use in a rule system that uses a Foundation NSPredicate object to evaluate itself.
- **GKRuleSystem** - A list of rules, together with a context for evaluating them and interpreting results, for use in constructing data-driven logic or fuzzy logic systems.

### Xcode and SpriteKit Integration
Classes and protocols to support easy creation and editing of GameplayKit features with the SpriteKit scene editor in Xcode.
- **GKScene** - A container for associating GameplayKit objects with a SpriteKit scene.
- **GKSceneRootNodeType** - Identifies scene classes from other frameworks that support embedded GameplayKit information.
- **GKSKNodeComponent** - A component that manages a SpriteKit node.

### Reference
- **GameplayKit Constants**
- **GameplayKit Structures**
- **GameplayKit Enumerations**

### Classes
- **GKSCNNodeComponent**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GameplayKit)*
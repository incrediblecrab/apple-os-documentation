# 🤖 Bot & LLM Instructions for Apple OS Documentation

> **For AI assistants, LLMs, and automated tools consuming this repository**

## Quick Start for Bots

This repository contains **~570,000 tokens** of Apple OS 26 documentation. Due to token limitations, **selective loading is essential**.

### Priority Loading Order

```yaml
1. CRITICAL (Load First):
   - /os26-intro/iOS.md          # 1,166 tokens - OS 26 overview
   - /liquid-glass/introduction.md # 1,506 tokens - New design system

2. CONTEXT-SPECIFIC (Load as needed):
   - /documentation/SwiftUI.md    # 4,837 tokens - If SwiftUI help needed
   - /documentation/UIKit.md      # 7,149 tokens - If UIKit help needed
   - /figma/                      # Visual references only

3. REFERENCE (Query-based):
   - /human-interface-guidelines/ # 271K tokens - Too large for full load
   - /documentation/              # 286K tokens - Load specific files only
```

## Token Budget Management

### Repository Size Breakdown

| Directory | Tokens | Strategy |
|-----------|--------|----------|
| `documentation/` | ~286,000 | Load individual files on-demand |
| `human-interface-guidelines/` | ~271,000 | Query specific topics |
| `liquid-glass/` | ~6,000 | Can load fully if needed |
| `os26-intro/` | ~7,000 | Load platform-specific files |
| `figma/` | 250+ images | Reference visually, don't load |

### Recommended Chunking Strategy

```python
# Example: Smart loading for 32K token context window
def load_for_task(task_type):
    base_context = {
        'os26_overview': 'os26-intro/iOS.md',      # 1,166 tokens
        'liquid_glass': 'liquid-glass/*.md',       # ~6,000 tokens
    }
    
    if 'swiftui' in task_type.lower():
        return base_context + {'swiftui': 'documentation/SwiftUI.md'}
    elif 'design' in task_type.lower():
        return base_context + {'hig': 'human-interface-guidelines/components/buttons.md'}
    # Add more conditions based on task
```

## Efficient Navigation Patterns

### 1. Framework Documentation Search

```bash
# DON'T: Load entire documentation folder
# L cat documentation/*.md  # 286K tokens!

# DO: Search first, then load specific files
grep -l "URLSession" documentation/*.md
# Then load only: documentation/Foundation.md
```

### 2. Design Guidelines Lookup

```bash
# DON'T: Load all HIG files
# L cat human-interface-guidelines/**/*.md  # 271K tokens!

# DO: Navigate to specific component
cat human-interface-guidelines/components/buttons.md  # ~2K tokens
```

### 3. Visual Component Reference

```bash
# For visual components, reference image paths without loading
ls figma/Buttons/*.png
# Returns: Button designs for Liquid Glass implementation
```

## Task-Specific Loading Strategies

### For Code Generation

```yaml
Required:
  - /documentation/SwiftUI.md OR /documentation/UIKit.md
  - /liquid-glass/adopting-liquid-glass.md
Optional:
  - /os26-liquid-glass-example/Landmarks/[specific files]
Skip:
  - /figma/* (visual reference only)
  - /human-interface-guidelines/* (unless specific component needed)
```

### For UI/UX Design Questions

```yaml
Required:
  - /liquid-glass/introduction.md
  - /human-interface-guidelines/foundations/color.md
  - /human-interface-guidelines/components/[specific].md
Reference:
  - /figma/[component]/* (describe images, don't load)
Skip:
  - /documentation/* (API details not needed)
```

### For Migration/Compatibility

```yaml
Required:
  - /os26-intro/[platform].md
  - /liquid-glass/adopting-liquid-glass.md
Optional:
  - Specific framework docs as needed
Skip:
  - /figma/*
  - Detailed API documentation
```

## Structured Query Patterns

### Pattern 1: Hierarchical Navigation

```
1. Start with platform overview (/os26-intro/)
2. Identify specific framework needed
3. Load only that framework's documentation
4. Reference HIG for design patterns if needed
```

### Pattern 2: Component-Based Loading

```
1. Identify UI component (e.g., "button")
2. Load: /human-interface-guidelines/components/buttons.md
3. Reference: /figma/Buttons/ for visual examples
4. If implementing: Load /documentation/SwiftUI.md sections
```

### Pattern 3: Feature Implementation

```
1. Load Liquid Glass fundamentals
2. Check sample app for implementation pattern
3. Load specific framework documentation
4. Skip unrelated platforms/frameworks
```

## Metadata for Intelligent Loading

### File Importance Scores

```json
{
  "critical": [
    "os26-intro/iOS.md",
    "liquid-glass/introduction.md"
  ],
  "high": [
    "documentation/SwiftUI.md",
    "documentation/UIKit.md",
    "documentation/Foundation.md"
  ],
  "medium": [
    "human-interface-guidelines/components/*.md",
    "os26-liquid-glass-example/Landmarks/LandmarksApp.swift"
  ],
  "low": [
    "figma/*",
    "documentation/[specialized frameworks]"
  ]
}
```

### Topic Mapping

```yaml
SwiftUI Development:
  - documentation/SwiftUI.md
  - liquid-glass/introduction.md
  - os26-liquid-glass-example/Landmarks/*.swift

UIKit Development:
  - documentation/UIKit.md
  - documentation/Foundation.md
  - human-interface-guidelines/components/

Design System:
  - liquid-glass/*.md
  - human-interface-guidelines/foundations/
  - figma/ (reference only)

Platform-Specific:
  iOS: os26-intro/iOS.md
  macOS: os26-intro/macOS.md
  visionOS: os26-intro/visionOS.md

WWDC 2025 Key Additions:
  - documentation/FoundationModels.md    # On-device AI/LLM framework
  - documentation/DeclaredAgeRange.md    # Age-appropriate content API
  - documentation/Charts.md              # Includes Chart3D for 3D charts
  - documentation/Containerization.md    # Linux containers on Mac (Apple silicon only)
```

## Optimization Tips

### 1. Use Search Before Loading

```python
# Good practice
def find_relevant_docs(query):
    # Search first
    results = search_index(query)
    # Load only top 3 relevant files
    return load_files(results[:3])
```

### 2. Cache Common Patterns

```python
# Cache frequently used combinations
COMMON_CONTEXTS = {
    'swiftui_basics': ['SwiftUI.md', 'liquid-glass/introduction.md'],
    'uikit_migration': ['UIKit.md', 'liquid-glass/adopting-liquid-glass.md'],
    'design_system': ['liquid-glass/*.md']
}
```

### 3. Progressive Enhancement

```python
# Start minimal, add as needed
context = load_base_context()  # ~7K tokens
if needs_more_detail():
    context += load_specific_framework()  # +5-10K tokens
if needs_visual_reference():
    context += describe_figma_images()  # Reference, not load
```

## Response Generation Guidelines

### When Referencing This Repository

1. **Always cite file paths**: Use format `path/to/file.md:section`
2. **Indicate token usage**: Mention if loading large sections
3. **Suggest alternatives**: If token limit reached, recommend specific files
4. **Use summaries**: For large files, provide summaries instead of full content

### Example Response Pattern

```markdown
Based on the Liquid Glass design system (`liquid-glass/introduction.md`), 
the new iOS 26 button components use multilayer blur effects. 

For implementation details, see:
- SwiftUI: `documentation/SwiftUI.md:Button` (specific section)
- Visual reference: `figma/Buttons/` (contains 8 component designs)
- Sample code: `os26-liquid-glass-example/Landmarks/Views/`

Note: Full SwiftUI documentation is ~4,837 tokens. Loading specific Button section only.
```

## API Endpoints for Smart Loading

### Suggested Repository API Structure

```yaml
/api/search:
  - Query: "button implementation"
  - Returns: Relevant file paths with token counts

/api/load:
  - Path: "documentation/SwiftUI.md"
  - Options: { sections: ["Button", "View"], max_tokens: 2000 }
  - Returns: Filtered content within token budget

/api/describe:
  - Path: "figma/Buttons/"
  - Returns: Text description of visual components

/api/summary:
  - Path: "human-interface-guidelines/"
  - Topic: "navigation"
  - Returns: Condensed summary (~500 tokens)
```

## Common Pitfalls to Avoid

### ❌ DON'T

- Load entire directories recursively
- Include image files in token count
- Load all platform docs when only one is needed
- Parse HTML/binary files as text
- Load deprecated OS versions when OS 26 is requested

### ✅ DO

- Search before loading
- Load incrementally based on need
- Use file summaries for large documents
- Reference images by path/description
- Cache commonly requested combinations

## Integration Examples

### For GitHub Copilot / Code Assistants

```javascript
// Optimal loading for code completion
const loadForCodeCompletion = async (language, framework) => {
  const base = await loadFile('liquid-glass/introduction.md');
  
  if (framework === 'SwiftUI') {
    return base + await loadFile('documentation/SwiftUI.md', {
      sections: ['Views', 'Modifiers'],
      maxTokens: 5000
    });
  }
  // Additional framework conditions...
};
```

### For ChatGPT / Claude Custom Instructions

```
When using apple-os-documentation repository:
1. Start with os26-intro/ for overview (1-2K tokens)
2. Load specific framework docs only when needed
3. Reference figma/ paths without loading images
4. Use grep/search before loading large directories
5. Summarize HIG content instead of loading fully
```

### For Documentation Bots

```python
class AppleDocBot:
    def __init__(self):
        self.token_budget = 32000
        self.loaded = {}
        
    def answer_question(self, question):
        # Always load base context
        self.load_base()  # ~7K tokens
        
        # Conditionally load based on question
        if 'design' in question:
            self.load_design_basics()  # +3K tokens
        elif 'code' in question:
            self.load_framework_specific()  # +5K tokens
            
        return self.generate_response()
```

## Maintenance & Updates

### Version Tracking

- **Current Version**: OS 26.4 (current GA across iOS/iPadOS/macOS/tvOS/visionOS/watchOS)
- **Upcoming Version**: OS 26.5 (in developer beta — Beta 4 as of May 2026)
- **Last Updated**: 2026-05-02
- **Token Counts**: May vary with updates

### Key Deadlines

| Date | Requirement |
|------|-------------|
| **April 2026** | All App Store submissions now require Xcode 26 and iOS 26 SDK (in effect) |
| **Fall 2026** | Liquid Glass adoption mandatory (UIDesignRequiresCompatibility removed in iOS 27) |

### Platform Version Reference

All Apple platforms now use unified "26" versioning:
- iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, watchOS 26, **visionOS 26**
- Note: visionOS jumped from 2.x directly to 26 (no visionOS 3-25)

### Change Detection

```bash
# Check for updates in specific areas
git diff HEAD~1 liquid-glass/  # Design system changes
git diff HEAD~1 documentation/SwiftUI.md  # Framework updates
```

## Contact & Support

For questions about optimal consumption patterns:
- Review: `/README.md` for human-readable overview
- Reference: This file for bot-specific guidance

---

**Remember**: This repository is designed for selective, intelligent consumption. Don't try to load everything at once - be smart about what you need for each specific task.
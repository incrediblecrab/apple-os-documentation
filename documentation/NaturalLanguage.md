# Natural Language

Analyze natural language text and deduce its language-specific metadata.

**Platforms:** iOS 12.0+ | iPadOS 12.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 12.0+ | visionOS 1.0+ | watchOS 5.0+

## Overview

The Natural Language framework provides a variety of natural language processing (NLP) functionality with support for many different languages and scripts. Use this framework to segment natural language text into paragraphs, sentences, or words, and tag information about those segments, such as part of speech, lexical class, lemma, script, and language.

Use this framework to perform tasks like:

- **Language identification** - automatically detecting the language of a piece of text
- **Tokenization** - breaking up a piece of text into linguistic units or tokens
- **Parts-of-speech tagging** - marking up individual words with their part of speech
- **Lemmatization** - deducing a word's stem based on its morphological analysis
- **Named entity recognition** - identifying tokens as names of people, places, or organizations

You can also use this framework with Create ML to train and deploy custom natural language models. For more information, see Creating a text classifier model and Creating a word tagger model.

## Topics

### Tokenization
- [Tokenizing natural language text](https://developer.apple.com/documentation/naturallanguage/tokenizing_natural_language_text) - Enumerate the words in a string
- **NLTokenizer** - A tokenizer that segments natural language text into semantic units

### Language Identification
- [Identifying the language in text](https://developer.apple.com/documentation/naturallanguage/identifying_the_language_in_text) - Detect the language in a piece of text by using a language recognizer
- **NLLanguageRecognizer** - The language of a body of text
- **NLLanguage** - The languages that the Natural Language framework supports

### Linguistic Tags
- [Identifying parts of speech](https://developer.apple.com/documentation/naturallanguage/identifying_parts_of_speech) - Classify nouns, verbs, adjectives, and other parts of speech in a string
- [Identifying people, places, and organizations](https://developer.apple.com/documentation/naturallanguage/identifying_people_places_and_organizations) - Use a linguistic tagger to perform named entity recognition on a string
- **NLTagger** - A tagger that analyzes natural language text

### Text Embedding
- [Finding similarities between pieces of text](https://developer.apple.com/documentation/naturallanguage/finding_similarities_between_pieces_of_text) - Calculate the semantic distance between words or sentences
- **NLEmbedding** - A map of strings to vectors, which locates neighboring, similar strings

### Contextual Embedding
- **NLContextualEmbedding** - A model that computes sequences of embedding vectors for natural language utterances
- **NLContextualEmbeddingKey** - Contextual embedding keys
- **NLScript** - The writing scripts that the Natural Language framework supports

### Natural Language Models
- [Creating a text classifier model](https://developer.apple.com/documentation/naturallanguage/creating_a_text_classifier_model) - Train a machine learning model to classify natural language text
- [Creating a word tagger model](https://developer.apple.com/documentation/naturallanguage/creating_a_word_tagger_model) - Train a machine learning model to tag individual words in natural language text
- **NLModel** - A custom model trained to classify or tag natural language text

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NaturalLanguage)*
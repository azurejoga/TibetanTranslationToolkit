# freedom for tibet!

## Overview

The Tibetan Translation Script is a Python-based tool designed to facilitate the translation of text into Tibetan, specifically from various source languages, such as Portuguese. The script includes functionalities for transliteration between Wylie and Unicode formats, phonetic generation, and exploration of the Tibetan writing system. It is aimed at linguists, translators, and learners of the Tibetan language who require an efficient means of converting and understanding Tibetan text.

## Features

1. **Text Translation**: Translates user-provided text from a specified source language to Tibetan Unicode.
2. **Transliteration**: Converts Tibetan text between Wylie transliteration and Unicode formats for easier reading and writing.
3. **Phonetic Representation**: Generates a phonetic representation of Tibetan text to assist with pronunciation.
4. **User-Friendly Interface**: Interactive command-line interface that prompts users for input, making it accessible for users with varying levels of technical expertise.

## Tibetan Alphabet

The Tibetan script is an abugida, meaning each character typically represents a consonant with an inherent vowel sound. Here are the key components of the Tibetan writing system:

### Consonants
- Tibetan consists of 30 basic consonant letters, which include sounds analogous to those in English as well as unique phonemes specific to Tibetan.
- Each consonant has an inherent vowel sound (usually /a/) that can be altered by the addition of vowel diacritics.

### Vowels
- Tibetan vowels are not represented as separate letters; instead, they are indicated by diacritics added to consonants:
  - **a** (ཨ)
  - **i** (ཨི)
  - **u** (ཨུ)
  - **e** (ཨེ)
  - **o** (ཨོ)

### Prescribed and Overscribed Letters
- Certain characters can carry additional marks or combinations that modify their pronunciation or meaning, known as prescribed (སྦྱིན་) and overscribed (སྤྱིན་) letters.

### Numerals
- Tibetan numerals (0-9) have unique characters, allowing for numerical representation:
  - 0 (༠), 1 (༡), 2 (༢), 3 (༣), 4 (༤), 5 (༥), 6 (༦), 7 (༧), 8 (༨), 9 (༩).

### Punctuation
- Tibetan punctuation marks include:
  - **Tsheg (ཚེར་)**: Similar to a space, used to separate syllables.
  - **End of Sentence Marker (༌)**: Used to indicate the end of a sentence.

### Syllables
- A typical Tibetan syllable consists of a consonant followed by a vowel, and it may include additional characters for nasal or sibilant sounds.

### Nasal and Sibilant Sounds
- **Nasal Sounds**: Represented by special characters (e.g., ང).
- **Sibilant Sounds**: Consonants that produce a hissing sound, such as ཤ (sha) and ས (sa).

## Wylie and Unicode

### Wylie Transliteration
- Wylie is a system for representing Tibetan text using the Roman alphabet. This method allows for easy typing and sharing of Tibetan text on standard keyboards. For example, the Tibetan word for 'Tibet' is written as **'bod'** in Wylie.

### Unicode
- Unicode is a universal character encoding standard that allows for the representation of text across various writing systems, including Tibetan. The Unicode standard includes characters for all Tibetan letters, diacritics, and punctuation marks, ensuring accurate digital representation.

## Purpose of the Script

The script serves multiple purposes:
- **Translation**: Allows users to convert text from languages such as Portuguese to Tibetan.
- **Transliteration**: Facilitates the conversion between Wylie and Unicode, making Tibetan text more accessible for reading and writing.
- **Phonetic Analysis**: Provides a phonetic representation of Tibetan words, aiding users in pronunciation.

## How to Use the Script

### Requirements
- Install the required Python libraries:
  ```bash
  pip install requests translate
  ```
- Ensure you have an active internet connection for API calls to work.

### Running the Script
1. Execute the script in a Python environment:
   ```bash
   python main.py
   ```
2. When prompted, input the source language code (e.g., 'pt' for Portuguese).
3. Enter the text you wish to translate into Tibetan.
4. The script will display:
   - The translated text in Tibetan Unicode.
   - The Wylie transliteration of the translated text.
   - The Unicode representation of the Wylie transliteration.
   - The phonetic transcription of the translated Tibetan text.
5. Type 'exit' to terminate the program.

### Example Usage
```plaintext
Available languages for translation.
The target will always be Tibetan (code: 'bo').

Enter the source language code (e.g., 'pt' for Portuguese): en
Enter the text you wish to translate into Tibetan (or 'exit' to quit): Hello, how are you?
Translated text in Tibetan: བཀྲ་ཤིས་བདེ་བའི་མཇུག་གསུམ།
Wylie from Unicode: bkra shis bde ba'i mjug gsum
Unicode from Wylie: བཀྲ་ཤིས་བདེ་བའི་མཇུག་གསུམ།
THL Phonetics: kʂa ʃɪ ʋɛ ɓæ ˈmi ˈʤʊŋ
```

## Conclusion

The Tibetan Translation Script is a comprehensive tool that enhances the accessibility and understanding of Tibetan text. By bridging the gap between different writing systems, the script enables users to interact with Tibetan language content effectively. The inclusion of Wylie transliteration and phonetic generation not only aids in accurate pronunciation but also supports learners and enthusiasts of the Tibetan language in their studies and translations. This script represents a significant step towards making Tibetan language resources more widely available and usable in a digital format.  

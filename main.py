import requests
from translate import Translator

# Function to transliterate from Wylie to Unicode
def transliterate_wylie_to_unicode(wylie_text):
    url = "http://www.thlib.org/cgi-bin/thl/lbow/wylie.pl"
    params = {
        "plain": "true",
        "conversion": "wy2uni",
        "input": wylie_text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Error calling the Wylie to Unicode transliteration API.")
        return None

# Function to transliterate from Unicode to Wylie
def transliterate_unicode_to_wylie(unicode_text):
    url = "http://www.thlib.org/cgi-bin/thl/lbow/wylie.pl"
    params = {
        "plain": "true",
        "conversion": "uni2wy",
        "input": unicode_text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Error calling the Unicode to Wylie transliteration API.")
        return None

# Function to generate phonetics from Unicode
def generate_phonetics(unicode_text):
    url = "http://www.thlib.org/cgi-bin/thl/lbow/phonetics.pl"
    params = {
        "plain": "true",
        "input": unicode_text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Error calling the phonetic generation API.")
        return None

# Function to translate text
def translate(text, source_language, destination_language):
    try:
        translator = Translator(from_lang=source_language, to_lang=destination_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

def main():
    print("Available languages for translation.")
    print("The destination will always be Tibetan (code: 'bo').\n")

    source_language = input("Enter the source language code (e.g., 'pt' for Portuguese): ")
    destination_language = "bo"  # Code for Tibetan

    while True:
        text = input("Enter the text you wish to translate to Tibetan (or 'exit' to quit): ")
        
        if text.lower() == 'exit':
            break
        
        # Translation of the text
        translated_text = translate(text, source_language, destination_language)
        if translated_text is not None:
            print(f"Translated text to Tibetan: {translated_text}")

            # Get transliterations using the APIs
            unicode_translated = translated_text.strip()
            wylie_from_unicode = transliterate_unicode_to_wylie(unicode_translated)
            print(f"Wylie from Unicode: {wylie_from_unicode}")

            # Now, if you want the transliteration from Wylie to Unicode:
            wylie_text = wylie_from_unicode.strip()
            unicode_from_wylie = transliterate_wylie_to_unicode(wylie_text)
            print(f"Unicode from Wylie: {unicode_from_wylie}")

            phonetics_from_unicode = generate_phonetics(unicode_translated)
            print(f"THL Phonetics: {phonetics_from_unicode}")

        else:
            print("Could not perform the translation.")

if __name__ == "__main__":
    main()

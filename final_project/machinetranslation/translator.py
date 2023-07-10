"""Module has a two functions that serve as a translator from en-fr and fr-en"""

from deep_translator import MyMemoryTranslator, GoogleTranslator

def english_to_french(english_text):
    #Translate english text into french
    if english_text is None:
        return "Please type a phrase in English"
    french_text = GoogleTranslator(source="english", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    #Translate french text into english
    if french_text is None:
        return "Please type a phrase in French"
    english_text = GoogleTranslator(source="french", target="english").translate(french_text)
    return english_text
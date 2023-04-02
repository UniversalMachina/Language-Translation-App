from translate import Translator
from langdetect import detect

def translate_text(text, source_language, target_language):
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

def detect_language(text):
    detected_language = detect(text)
    return detected_language

if __name__ == "__main__":
    text = "Hello, how are you?"
    detected_language = detect_language(text)
    print(f"Detected language: {detected_language}")

    target_language = "es"
    translated_text = translate_text(text, detected_language, target_language)
    print(f"Translated text: {translated_text}")

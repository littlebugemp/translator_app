from translate import Translator

def translate(text):
    translator = Translator(to_lang="German")
    translation = translator.translate(text)
    return translation


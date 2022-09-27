'''This Simple python script is to translate any text from any language to any other language using google server'''

import translators as ts

text = input("Enter text to Translate: ")

code = input("Enter language Code to translate(e.g, 'en' for English):")


def translation():
    try:
        print("Translated text is: " + ts.google(text, to_language=code))
    except ts.apis.TranslatorError as e:
        print("Error! Unsupported Language code! ")


translation()
exit()

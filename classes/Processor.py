import openai
import bs4
import requests


class TextProcessor():
    def __init__(self, key):

        openai.api_key = key

    def prompt(self, text):

        if text.startswith('/translate'):
            return self.openai_translate(
                text.replace('/translate', '').strip()
            )
        elif text.startswith('/sumary'):
            return self.openai_text_sumary(
                text.replace('/sumary', '').strip()
            )
        elif text.startswith('/imagine'):
            return self.openai_image(
                text.replace('/imagine', '').strip()
            )
        elif text.startswith('/code'):
            return self.openai_code(
                text.replace('/code', '').strip()
            )
        elif text.startswith('/generate'):
            return self.openai_text_generator(
                text.replace('/generate', '').strip()
            )

        return {
            'type': 'text',
            'content' : 'Je ne comprends pas votre demande'
        }

    def openai_translate(self, msg):

        return_gpt = openai.Completion.create(
            model="text-davinci-003",
            prompt=msg,
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        return {
            'type': 'text',
            'content' : return_gpt['choices'][0]['text']
        }

    def openai_text_sumary(self, msg):

        return_gpt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": 'Ton ojectif est de synthétiser un texte.'},
                {"role": "user",
                 "content": "Je veux résumer le texte suivant : %s" % msg},
            ],
            max_tokens=100,
            temperature=0.9,
        )

        return {
            'type': 'text',
            'content' : return_gpt['choices'][0]['message']['content']
        }

    def openai_text_generator(self, msg):

        return_gpt = openai.Completion.create(
            model="davinci",
            prompt=msg,
            temperature=0.3,
            max_tokens=100
        )

        return {
            'type': 'text',
            'content' : return_gpt['choices'][0]['text']
        }

    def openai_code(self, msg):

        return_gpt = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                    "content": 'Ton ojectif est de vérifier la syntaxe d\'un code.'},
                {"role": "user",
                    "content": "Je veux vérifier le code suivant : %s" % msg},
            ],
            temperature=0.3,
            max_tokens=100
        )

        return {
            'type': 'code',
            'content' : return_gpt['choices'][0]['message']['content']
        }



    def openai_image(self, msg):

        return_gpt = openai.Image.create(
            prompt=msg,
            n=1,
            size="512x512"
        )

        return {
            'type': 'image',
            'content': return_gpt['data'][0]['url']
        }

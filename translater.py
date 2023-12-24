import googletrans
import requests




# s = r.text


def norris_joke():
    r = requests.get('https://geek-jokes.sameerkumar.website/api')
    return r.text


def translate(s: str, lang: str):
    translater = googletrans.Translator(service_urls=['translate.google.com'])
    return translater.translate(s,dest=lang).text



# print(s)
# print(translater.translate(s, dest='ru').text)

if __name__ == '__main__':

    x = norris_joke()

    z = translate(x, lang="ru")
    print(x, z)



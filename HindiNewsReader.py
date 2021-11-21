from gtts import gTTS
from playsound import playsound
import requests
import json
import os


def newspaper_reader(str):
    language = 'hi'
    myobj = gTTS(text=str, lang=language, slow=True)
    myobj.save("hindinews.mp3")
    playsound("hindinews.mp3")
    os.remove("hindinews.mp3")


if __name__ == '__main__':
    newspaper_reader("Starting to read India's top headline for today")
    url = "https://newsapi.in/newsapi/news.php?key=WriteYourAPIkeyHere=hindi_state"
    num = 1
    news_json = requests.get(url).text
    news_py = json.loads(news_json)
    arts = news_py["News"]
    for article in arts:
        print(f"Here is the headline-{num}: {article['title']}\nIf you want to read more, please refer to this link: "
              f"{article['url']}\nYou can also read description here :{article['description']}")
        newspaper_reader(article['title'])
        num = num + 1
        newspaper_reader("Moving to the next headline, listen carefully."

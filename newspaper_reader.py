from win32com.client import Dispatch
import requests
import json

def newspaper_reader(str):
    read = Dispatch("SAPI.Spvoice")
    read.Speak(str)

if __name__ =='__main__':
    newspaper_reader("Starting to read India's top headline for today")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=2aab9df35b5842fab8833c3f23871bad"
    num = 0
    news_json = requests.get(url).text
    news_py = json.loads(news_json)
    arts = news_py["articles"]
    values = news_py["totalResults"]
    for article in arts:
        print(f"Here is the headline: {article['title']}\nIf you want to read more, please refer to this link: "
              f"{article['url']}")
        newspaper_reader(article['title'])
        num = num + 1
        compare = values
        if num < compare:
            newspaper_reader("Moving to the next headline, listen carefully.")
        if num == compare:
            newspaper_reader("Thanks for listening")

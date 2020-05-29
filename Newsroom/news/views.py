from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as Bsoup
from news.models import Headline

#used for web-scraping 
def scrape(request):
    #make a connection to the server
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html"}
    url = "https://www.theonion.com/"
    #store response from server
    content = session.get(url, verify=False).content
    soup = Bsoup(content, "html.parser")
    News = soup.find_all('div', {"class":"curation-module__item"})
    for article in News:
        main = article.find_all('a')[0]
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main['title']
        #store in database
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
    return redirect("../")

#extract all data from db, reverse list to provide latest news first
def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)
    

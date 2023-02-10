from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    return render(request, "dictapp/index.html", {})

def search(request):
    word = request.GET.get('word')

    if len(word) > 0:
        res = requests.get('https://www.dictionary.com/browse/' + word)
        res2 = requests.get('https://www.thesaurus.com/browse/' + word)

        if res:
            soup = BeautifulSoup(res.text, 'lxml')

            meaning = soup.find_all('div', {'value': '1'})
            meaning = meaning[0].getText()
        else:
            word = 'Sorry, ' + word + ' was not found'
            meaning = ''

        if res2:
            soup2 = BeautifulSoup(res2.text, 'lxml')

            synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
            ss = []

            for b in synonyms[0:]:
                re = b.text.strip()
                ss.append(re)
            syn = ss                  
        else:
            syn = ''

        results = {
            'word' : word,
            'meaning' : meaning,
        }

    return render(request, "dictapp/search.html", {'syn': syn, 'results': results})        


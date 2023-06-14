from django.shortcuts import render
import requests
API_KEY = '65234c28fe5a4d179bc241fdf38eac2b'


# Create your views here.


def home(request):
    category = request.GET.get('category')

    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)


from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    # get list of categories
    categories_url = 'https://api.thecatapi.com/v1/categories'
    categories_response = requests.get(categories_url)
    categories = categories_response.json()
    # if we recieve a form get a random cat image using category from form data
    if request.method == "POST":
        category_id = int(request.POST['category_id'])
        response = requests.get('https://api.thecatapi.com/v1/images/search', params={'category_ids':category_id})
        print(response.url)
    else:
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url)
        category_id = ''

    data = response.json()
    print(response)
    cat_image = data[0]['url']
    context = {
        'cat_image':cat_image,
        'categories':categories,
        'category_id':category_id,
    }

    return render(request, 'caturdayapp/index.html', context)

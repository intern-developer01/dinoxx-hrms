from django.shortcuts import render

# Create your views here.


def get_api(response):
    return render(response, "api/api.html", {})
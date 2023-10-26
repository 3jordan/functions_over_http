from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def hey_you(request, name):
    return HttpResponse(f"Hey, {name}!")


def how_old(request, end, birthyear):
    age_in_end_year = end - birthyear
    return HttpResponse(age_in_end_year)


def can_i_take_your_order(request, burgers, fries, drinks):
    total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
    return HttpResponse(f"${total}")

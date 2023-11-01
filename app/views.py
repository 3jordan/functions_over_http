from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def hey_you(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def how_old(request: HttpRequest, end, birthyear) -> HttpResponse:
    age_in_end_year = end - birthyear
    return HttpResponse(age_in_end_year)


def can_i_take_your_order(request: HttpRequest, burgers, fries, drinks) -> HttpResponse:
    total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
    return HttpResponse(f"${total}")

from django.shortcuts import render, HttpResponse

# Create your views here.


def main(request):
    return render(request, 'OfficeApp/main.html')


def contact(request):
    return render(request, "OfficeApp/contact.html")


def change(request):
    return render(request, "OfficeApp/change.html")


def currency_rate(request):
    return render(request, "OfficeApp/currency_rate.html")


def client(request):
    return render(request, "OfficeApp/client.html")

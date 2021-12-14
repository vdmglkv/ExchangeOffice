from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user
from .models import Operation
from .forms import Convert

# Create your views here.


def main(request):
    return render(request, 'OfficeApp/main.html')


def contact(request):
    return render(request, "OfficeApp/contact.html")


def change(request):
    if request.method == 'POST':
        form = Convert(request.POST)
        if form.is_valid():
            user = get_user(request)
            operation = Operation.objects.create(user_id=user.id, value_in=1, value_out=1)
            operation.save()
            return HttpResponseRedirect('/change_done/')
    else:
        form = Convert()
    return render(request, "OfficeApp/change.html", {'form': form})


def change_done(request):
    return render(request, "OfficeApp/convert_done.html")


def currency_rate(request):
    return render(request, "OfficeApp/currency_rate.html")


def client(request):
    return render(request, "OfficeApp/client.html")

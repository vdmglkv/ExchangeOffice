from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            try:
                user = get_user(request)
                operation = Operation.objects.create(**form.cleaned_data, user_id=user.id)
                operation.save()
                return HttpResponseRedirect('/change_done/')
            except:
                form.add_error(None, 'Ошибка при конвертации.')
    else:
        form = Convert()
    return render(request, "OfficeApp/change.html", {'form': form})


def change_done(request):
    return render(request, "OfficeApp/convert_done.html")


def currency_rate(request):
    return render(request, "OfficeApp/currency_rate.html")


def client(request):
    return render(request, "OfficeApp/client.html")

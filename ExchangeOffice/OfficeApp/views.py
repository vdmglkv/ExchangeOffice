from datetime import datetime
from .converter import get_pair_rates
from django.shortcuts import render
from django.contrib.auth import get_user
from .models import Operation
from .forms import Convert


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
                operation = Operation.objects.create(From=form.cleaned_data['From'],
                                                     value=form.cleaned_data['value'],
                                                     To=form.cleaned_data['To'],
                                                     result=form.cleaned_data['value'] * get_pair_rates(
                                                         form.cleaned_data['From'],
                                                         form.cleaned_data['To']),
                                                     user_id=user.id)
                operation.save()
                return render(request, "OfficeApp/convert_done.html",
                              {'form': form, 'data': datetime.now,
                               'convert': form.cleaned_data['value'] * get_pair_rates(form.cleaned_data['From'],
                                                                                      form.cleaned_data['To'])})
            except Exception as ex:
                print(ex)
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

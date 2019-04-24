from django.shortcuts import render
from django.http import HttpResponse
from .models import Fertiliser, FertiliserUser, Application, Field, FertiliserInUse
from .forms import FertiliserUserForm, ApplicationUserForm
import json


def landing_page(request):
    return render(request, 'turf_app/landing_page.html')


def dashboard_page(request):
    user = request.user
    fertilisers = user.fertilisers.all()
    liquidFertilisersNames = json.dumps([fertiliser.fertiliser.name for fertiliser in fertilisers if fertiliser.fertiliser.type == 'Liquid'])
    liquidFertilisersIds = json.dumps([fertiliser.id for fertiliser in fertilisers if fertiliser.fertiliser.type == 'Liquid'])
    solidFertilisersNames = json.dumps([fertiliser.fertiliser.name for fertiliser in fertilisers if fertiliser.fertiliser.type == 'Granulate'])
    solidFertilisersIds = json.dumps([fertiliser.id for fertiliser in fertilisers if fertiliser.fertiliser.type == 'Granulate'])
    applications = user.applications.all()
    return render(request, 'turf_app/dashboard.html', {'user': user, 'fertilisers': fertilisers, 'liquidFertilisersNames': liquidFertilisersNames,
                                                       'liquidFertilisersIds': liquidFertilisersIds,
                                                       'solidFertilisersNames': solidFertilisersNames,
                                                       'solidFertilisersIds': solidFertilisersIds,
                                                       'applications': applications})


def market_page(request):
    form = FertiliserUserForm()
    fertilisers = Fertiliser.objects.all()
    status_list = []
    for f in fertilisers:
        if len(f.used_by.filter(user=request.user)) > 0:
            status_list.append('In')
            print(True)
        else:
            status_list.append('Out')
            print(False)
    return render(request, 'turf_app/market.html', {'fertilisers': fertilisers, 'status_list': status_list, 'form': form})


def add_user_fertiliser(request):
    if request.method == 'POST':
        user = request.user
        fertiliser = Fertiliser.objects.get(id=request.POST.get('id'))
        price = request.POST.get('price')
        stock = request.POST.get('quantity')
        new_user_fertiliser = FertiliserUser.objects.create(user=user, fertiliser=fertiliser, price=price, stock=stock)
        new_user_fertiliser.save()
        status = 'In'
        json_response = {'status_fertiliser': status}
        return HttpResponse(json.dumps(json_response), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'Message': 'Nothing to return'}))


def add_user_application(request):
    if request.method == 'POST':
        user = request.user
        units = 'Kg'
        field_id = request.POST.get('field_id')
        type = request.POST.get('type')
        date = request.POST.get('date')
        quantity = 0
        products = request.POST.get('products')
        print(products)
        if type == 'Liquid':
            volum = request.POST.get('volum')
            units = 'L'
            quantity = int(volum)
        else:
            for product in products:
                quantity += int(product[1])

        application = Application.objects.create(
            user=user,
            field=Field.objects.get(id=field_id),
            type=type,
            units=units,
            quantity=quantity,
            scheduled_date=date
        )
        application.save()

        for product in products:
            productInUse = FertiliserInUse.objects.create(
                fertiliser=FertiliserUser.objects.get(id=product[0]),
                quantity=int(product[1]),
                application=application
            )
            productInUse.save()
        json_response = {'field': application.field, 'type_': application.type, 'scheduled': application.scheduled_date}
        return HttpResponse(json.dumps(json_response), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'Message': 'Nothing to return'}))






# Create your views here.

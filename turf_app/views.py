from django.shortcuts import render
from django.http import HttpResponse
from .models import Fertiliser, FertiliserUser
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
    return render(request, 'turf_app/dashboard.html', {'user': user, 'fertilisers': fertilisers, 'liquidFertilisersNames': liquidFertilisersNames,
                                                       'liquidFertilisersIds': liquidFertilisersIds,
                                                       'solidFertilisersNames': solidFertilisersNames,
                                                       'solidFertilisersIds': solidFertilisersIds})


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
        field_id = request.POST.get('field_id')
        type = request.POST.get('type')
        date = request.POST.get('date')
        if type == 'Liquid':
            volum = request.POST.get('volum')
        products = request.POST.getlist('products[]')
        print(field_id)
        print(type)
        print(date)
        print(volum)
        print(products)

    return HttpResponse(json.dumps({'Message': 'Nothing to return'}))






# Create your views here.

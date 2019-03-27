from django.shortcuts import render
from .models import Fertiliser, FertiliserUser
from .forms import FertiliserUserForm


def landing_page(request):
    return render(request, 'turf_app/landing_page.html')


def dashboard_page(request):
    user = request.user
    fertilisers = FertiliserUser.objects.all()
    return render(request, 'turf_app/dashboard.html', {'user': user, 'fertilisers': fertilisers})


def products_page(request):
    form = FertiliserUserForm()
    fertilisers = Fertiliser.objects.all()
    status = []
    for f in fertilisers:
        if len(f.used_by.filter(user=request.user)) > 0:
            status.append(True)
            print(True)
        else:
            status.append(False)
            print(False)
    return render(request, 'turf_app/products.html', {'fertilisers': fertilisers, 'status': status,
                                                      'form': form})


def add_user_fertiliser(request):
    pass

# Create your views here.

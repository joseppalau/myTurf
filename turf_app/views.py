from django.shortcuts import render


def landing_page(request):
    return render(request, 'turf_app/landing_page.html')

# Create your views here.

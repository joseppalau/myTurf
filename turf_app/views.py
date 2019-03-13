from django.shortcuts import render


def landing_page(request):
    return render(request, 'turf_app/landing_page.html')


def dashboard_page(request):
    user = request.user
    return render(request, 'turf_app/dashboard.html', {'user': user})

# Create your views here.

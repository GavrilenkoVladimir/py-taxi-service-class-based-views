from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class DriversView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriversDetailView(generic.DetailView):
    model = Driver


class CarsView(generic.ListView):
    model = Car
    paginate_by = 5


class CarsDetailView(generic.DetailView):
    model = Car


class ManufacturersView(generic.ListView):
    model = Manufacturer
    paginate_by = 5

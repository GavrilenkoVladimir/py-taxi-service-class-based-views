from django.urls import path

from .views import (
    index,
    DriversView,
    DriversDetailView,
    CarsView,
    CarsDetailView,
    ManufacturersView
)

urlpatterns = [
    path("", index, name="index"),
    path("drivers/", DriversView.as_view(), name="drivers"),
    path(
        "drivers/<int:pk>",
        DriversDetailView.as_view(),
        name="drivers_detail"
    ),
    path("cars/", CarsView.as_view(), name="cars"),
    path("cars/<int:pk>", CarsDetailView.as_view(), name="cars_detail"),
    path("manufacturers/", ManufacturersView.as_view(), name="manufacturers"),
]

app_name = "taxi"

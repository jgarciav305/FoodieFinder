from django.urls import path
from .views import showfoodPageView
from .views import newyorkPageView
from .views import chicagoPageView
from .views import langelesPageView
from .views import austinPageView
from .views import norleansPageView
from .views import sfriscoPageView

urlpatterns = [
    path("newyork/", newyorkPageView, name="newyork"),
    path("chicago/", chicagoPageView, name="chicago"),
    path("langeles/", langelesPageView, name="langeles"),
    path("austin/", austinPageView, name="austin"),
    path("norleans/", norleansPageView, name="norleans"),
    path("sfrisco/", sfriscoPageView, name="sfrisco"),
    path("", showfoodPageView, name="showfood"),
]

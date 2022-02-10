from django.urls import path

from .api.list_of_outlets import GetListOfOutlets
from .api.make_visit import MakeVisit


app_name = "app"

urlpatterns = [
    path('getlistofoutlets/<str:phone>/', GetListOfOutlets.as_view()),
    path('makevisit/', MakeVisit.as_view()),
]
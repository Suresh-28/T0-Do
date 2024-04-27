from django.urls import path
from . import views


urlpatterns= [
    path("",views.index,name="app"),
    path("remove/<str:item_id>", views.remove,name="app")
]
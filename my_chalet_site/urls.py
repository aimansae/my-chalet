from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('description/<chalet_id>',
         views.ChooseChalet.as_view(), name="description"),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('chalet_detail/<int:chalet_id>/', views.ChaletDetail.as_view(), name="chalet_detail"),
]

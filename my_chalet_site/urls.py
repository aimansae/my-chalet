from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('chalet_detail/<int:chalet_id>/',
         views.ChaletDetail.as_view(), name="chalet_detail"),
    path('reservation/<int:chalet_id>/', views.reservation, name="reservation"),
    path('my_reservations/', views.my_reservations, name="my_reservations"),
    path('edit_reservation/<int:reservation_id>/',
         views.edit_reservation, name="edit"),
    path('delete_reservation/<int:reservation_id>/',
         views.delete_reservation, name="delete"),
]

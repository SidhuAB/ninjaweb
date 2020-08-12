from django.urls import path
from . import views

urlpatterns = [
    path('buy_side',views.buy_side, name='buy_side')
]

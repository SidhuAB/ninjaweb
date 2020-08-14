from django.urls import path
from . import views

urlpatterns = [
    path('buy_side',views.buy_side, name='buy_side'),
    path('buy_prof',views.buy_prof,name='buy_prof'),
    path('prod_page',views.prod_page,name='prod_page'),
    path('prod_detail',views.prod_detail,name='prod_detail')
]

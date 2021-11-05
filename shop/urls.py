from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.things_list_all, name='thing_list'),
    path('<int:thing_id>/', views.thing_detail, name='detail'),
    path('category/<str:thing_category>/', views.things_list_category, name='list_category'),
    path('brand/<str:thing_brand>/', views.things_list_brand, name='list_brand'),

]

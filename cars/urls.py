from django.urls import path
from cars import views


urlpatterns = [
    path('',views.MainView.as_view(),name='index'),
    path('makes/',views.MakeListView.as_view(), name='make_list'),
    path('make/create',views.MakeCreateView.as_view(), name='make_create'),
    path('make/<int:pk>/update',views.MakeUpdateView.as_view(), name='make_update'),
    path('make/<int:pk>/delete',views.MakeDeleteView.as_view(), name='make_delete'),
    path('cars/create',views.CarsCreateView.as_view(), name='cars_create'),
    path('cars/<int:pk>/update',views.CarsUpdateView.as_view(),name='cars_update'),
    path('cars/<int:pk>/delete',views.CarsDeleteView.as_view(),name='cars_delete')
]

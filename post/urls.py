from django.urls import path
from .import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('get_data_by_cat/<int:id>/',views.get_data_by_cat,name='get_data_by_cat')
]
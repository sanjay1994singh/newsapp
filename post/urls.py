from django.urls import path
from .import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('<int:id>/',views.home_page,name='home_page'),
    path('get_data_by_cat/<int:id>/',views.get_data_by_cat,name='get_data_by_cat'),
    path('view_post_details/<int:obj_id>/',views.view_post_details,name='view_post_details')
]
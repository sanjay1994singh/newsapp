from django.urls import path
from .import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('<int:id>/',views.home_page,name='home_page'),
    path('get_data_by_cat/<int:id>/',views.get_data_by_cat,name='get_data_by_cat'),
    path('view_post_details/<int:obj_id>/',views.view_post_details,name='view_post_details'),
    path('add-post/',views.add_post,name='add_post'),
    path('add-post/<int:id>/',views.add_post,name='add_post'),
    path('list_page/',views.list_page,name='list_page'),
    path('delete-post/<int:id>/',views.delete_post,name='delete_post')
]
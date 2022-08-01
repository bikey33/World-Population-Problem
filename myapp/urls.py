from .import views
from django.urls import path
urlpatterns =[
    path('home/',views.home,name='home'),
    path('post_data/',views.post_data, name='post_data'),
    path('help/', views.help, name='help'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_total/', views.get_total_populations, name='get_total'),
    path('data/', views.get_plot_data, name='get_plot_data'),

]
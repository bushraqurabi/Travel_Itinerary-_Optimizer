from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index_page),
    path('base', views.render_index_page),
    path('optimize-itinerary/', views.optimize_itinerary_api, name='optimize_itinerary'),  
]
from django.urls import path
from . import views  # Ensure views is imported from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Route for the index view
    path('results/', views.results, name='results'),  # Route for the results view
]

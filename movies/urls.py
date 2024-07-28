from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='actor_create_list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDeleteView.as_view(), name='movie_detail'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie_stats')
]

from django.urls import path
from .views import *

urlpatterns = [
    path("info/", InfoView.as_view()),
    path("partners/", PartnersView.as_view()),
    path("team/", TeamView.as_view()),
    path("jamoa/", JamoaView.as_view()),
    path("category/", CategoryView.as_view()),
    path("news/", NewsView.as_view()),
    path("news/all/", NewsAllView.as_view()),
    path("news/for/single/", NewsForSingleView.as_view()),
    path("news/<int:pk>/", NewsOneView.as_view()),
    path("news/three/", NewsThreeView.as_view()),
    path("projects/", ProjectsView.as_view()),
    path("project/single/<int:pk>/", ProjectSingleView.as_view()),
    path("region/", RegionView.as_view()),
    path("trips/", TripsView.as_view()),
    path("news/by/category/<int:pk>/", NewsByCategory.as_view()),
    path("trip/by/region/<int:pk>/", TripByRegion.as_view()),
    path("news/by/week/", NewsByWeekView.as_view()),
    path("news/next/week/", NewsByNextWeekView.as_view()),
    path("about/xpk/", AboutXPKView.as_view()),
    path("category/project/", CategoryProjectsView.as_view()),
    path("project/by/category/<int:pk>/", ProjectbyCategoryView.as_view()),
    path("streaming/", StreamingApi.as_view()),
    path("photos/", PhotoView.as_view()),
    path("videos/", VideosView.as_view()),

]

from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Home, name="home"),

    path('information/', InformationView, name="information"),
    path('change-info/<int:pk>/', ChangeInfo, name="change-info"),
    path('delete-info/<int:pk>/', DeleteInfo, name="delete-info"),

    path('partner/', PartnerView, name="partner"),
    path('delete-logo/<int:pk>/', DeleteLogo, name="delete-logo"),
    path('change-logo/<int:pk>/', ChangeLogo, name="change-logo"),
    path('add-logo/', AddLogo, name="add-logo"),

    path('team/', TeamView, name="team"),
    path('delete-team/<int:pk>/', DeleteTeam, name="delete-team"),
    path('change-team/<int:pk>/', ChangeTeam, name="change-team"),
    path('add-team/', AddTeam, name="add-team"),

    path('jamoa/', JamoaView, name="jamoa"),
    path('delete-jamoa/<int:pk>/', DeleteJamoa, name="delete-jamoa"),
    path('add-jamoa/', AddJamoa, name="add-jamoa"),
    path('change-jamoa/<int:pk>/', ChangeJamoa, name="change-jamoa"),

    path('news/', NewsView, name="news"),
    path('change-new/<int:pk>/', ChangeNews, name="change-new"),
    path('single-new/<int:pk>/', SingleNews, name="single-new"),
    path('add-news/', AddNews, name="add-new"),
    path('delete-news/<int:pk>/', DeleteNews, name="delete-news"),

    path('trips/', TripsView, name="trips"),
    path('single-trip/<int:pk>/', SingleTrip, name="single-trip"),
    path('change-trip/<int:pk>/', ChangeTrip, name="change-trip"),
    path('delete-trip/<int:pk>/', DeleteTrip, name="delete-trip"),
    path('add-trip/', AddTrip, name="add-trip"),

    path('projects/', ProjectsView, name="projects"),
    path('change-project/<int:pk>/', ChangeProject, name="change-project"),
    path('add-project/', AddProject, name="add-project"),
    path('delete-project/<int:pk>/', DeleteProject, name="delete-project"),
    path('single-project/<int:pk>/', SingleProject, name="single-project"),

    path('single-about/<int:pk>/', SingleAbout, name="single-about"),
    path('delete-about/<int:pk>/', DeleteAbout, name="delete-about"),
    path('about/', About, name="about"),
    path('add-about/', AddAbout, name="add-about"),
    path('change-about/<int:pk>/', ChangeAbout, name="change-about"),

    path('delete-category/<int:pk>/', DeleteCategory, name="delete-category"),
    path('add-category/', AddCategory, name="add-category"),
    path('change-category/<int:pk>/', ChangeCategory, name="change-category"),

    path('change-category-project/<int:pk>/', ChangeCategoryProject, name="change-category-project"),
    path('delete-category-project/<int:pk>/', DeleteCategoryProject, name="delete-category-project"),
    path("add-project-category/", AddProjectCategory, name="add-project-category"),

    path('change-region/<int:pk>/', ChangeRegion, name="change-region"),
    path('delete-region/<int:pk>/', DeleteRegion, name="delete-region"),
    path('add-region/', AddRegion, name="add-region"),

    path('', Loginpage, name="login"),
    path('logout/', LogoutView, name="logout"),

    path("streaming/", StreamingView, name="streaming"),
    path("change-streaming/<int:pk>/", ChangeStreaming, name="change-streaming"),
    path("delete-streaming/<int:pk>/", DeleteStreaming, name="delete-streaming"),
    path("add-streaming/", AddStreaming, name="add-streaming"),
    path("change-status-streaming/", ChangeStatusStreaming, name="change-status-streaming"),

    path("photos/", PhotosView, name="photos"),
    path("add-photo/", AddPhoto, name="add-photo"),
    path("delete-photo/<int:pk>/", DeletePhoto, name="delete-photo"),
    path("change-photo/<int:pk>/", ChangePhoto, name="change-photo"),

    path("videos/", VideosView, name="videos"),
    path("delete-video/<int:pk>/", delete_video, name="delete-video"),
    path("add-video/", add_video, name="add-video"),
    path("change-video/<int:pk>/", change_video, name="change-video"),


    path("settings/", setting_view, name="setting"),
    path("change-username/", change_username, name="change-username"),
    path("change-password/", change_password, name="change-password"),

]

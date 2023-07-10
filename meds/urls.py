from django.urls import path

from .views import HomePageView, MedicationListView, LogCreateView, LogListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("meds/", MedicationListView.as_view(), name="med_list"),
    path("logs/create/", LogCreateView.as_view(), name="log_create"),
    path("logs/", LogListView.as_view(), name="log_list"),
]

app_name = "meds"

from typing import Any
from django.views.generic import TemplateView, ListView, CreateView

from .models import Perscription, Log


class HomePageView(TemplateView):
    """Home page view."""

    template_name = "home.html"


class MedicationListView(ListView):
    """List all perscriptions."""

    template_name = "meds/med_list.html"
    model = Perscription


class LogCreateView(CreateView):
    """Create a new log entry for a perscription."""

    template_name = "meds/log_create.html"
    model = Log
    fields = ("perscription", "taken", "notes")

    def get_initial(self) -> dict[str, Any]:
        """Get initial data for the form. Sets perscription to the GET param."""
        data = super().get_initial()
        if self.request.GET.get("perscription"):
            data["perscription"] = self.request.GET.get("perscription")
        return data


class LogListView(ListView):
    """List all logs."""

    template_name = "meds/log_list.html"
    model = Log

    def get_queryset(self):
        """Get the queryset for the view. Can filter by perscription id."""
        qs = super().get_queryset()
        if self.request.GET.get("perscription"):
            qs = qs.filter(perscription_id=self.request.GET.get("perscription"))
        return qs

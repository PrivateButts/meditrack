from django.db import models


class Perscription(models.Model):
    """Perscription model."""

    name = models.CharField(max_length=100)
    dosage = models.PositiveIntegerField()
    interval = models.DurationField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def last_taken(self: "Perscription") -> str:
        """Return the last time the perscription was taken."""
        if self.log_set.count() == 0:
            return "Never"
        return self.log_set.last().created_at

    @property
    def next_dose(self: "Perscription") -> str:
        """Return the next time the perscription should be taken."""
        if self.log_set.count() == 0:
            return "Whenever"
        return self.log_set.last().created_at + self.interval

    def __str__(self: "Perscription") -> str:
        """Return a string representation of the model."""
        return self.name


class Log(models.Model):
    """Log model."""

    perscription = models.ForeignKey(Perscription, on_delete=models.CASCADE)
    taken = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self: "Log") -> str:
        """Return a string representation of the model."""
        return f"{self.perscription.name} - {self.created_at}"

from django.db import models


class ConversionRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['from_currency', 'to_currency']

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency}: {self.rate}"

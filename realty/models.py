from decimal import Decimal
from django.db import models



class PaymentPlan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PaymentPlanMilestone(models.Model):
    name = models.CharField(max_length=255)
    payment_plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)
    order = models.IntegerField(null=True)
    total_percent = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    recurring_count = models.IntegerField(default=1)

    def _get_percent(self):
        return self.total_percent / Decimal(self.recurring_count) if self.recurring_count != 0 and self.total_percent is not None else 0
    
    percent = property(_get_percent)


    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class PaymentPlanFee(models.Model):
    name = models.CharField(max_length=255)
    milestone = models.ForeignKey(PaymentPlanMilestone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

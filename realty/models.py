from django.db import models



class PaymentPlan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PaymentPlanMilestone(models.Model):
    name = models.CharField(max_length=255)
    payment_plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PaymentPlanFee(models.Model):
    name = models.CharField(max_length=255)
    milestone = models.ForeignKey(PaymentPlanMilestone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

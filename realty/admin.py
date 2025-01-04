from django.contrib import admin
import nested_admin

from .models import PaymentPlan, PaymentPlanFee, PaymentPlanMilestone


# Register your models here.

class FeesInline(nested_admin.NestedTabularInline):
    model = PaymentPlanFee
    extra = 0
    verbose_name = 'Fee'
    verbose_name_plural = 'Fees'

class MilestoneInline(nested_admin.NestedTabularInline):
    model = PaymentPlanMilestone
    inlines = [FeesInline, ]
    extra = 0
    verbose_name = 'Milestone'
    verbose_name_plural = 'Milestones'

class PaymentPlanAdmin(nested_admin.NestedModelAdmin):
    inlines = [MilestoneInline, ]

admin.site.register(PaymentPlan, PaymentPlanAdmin)
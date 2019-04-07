from django.db import models
from django.db.models import Q

IA_STATUS_CHOICES = (
    ('I', "In Progress"),
    ('S', "Submitted"),
    ('A', "Approved")
)

WORK_STATUS_CHOICES =(
    ('R', "Requested IA"),
    ('W', "Awating Approval"),
    ('A', "Approved")
)

STATUS = (
    ('O', "Open"),
    ('C', "Closed")
)
# Create your models here.
"""
class iaStatus(models.Model):
    statValue = models.CharField(max_length=10)

    def __str__(self):
        return self.statValue

class workStatus(models.Model):
    statValue = models.CharField(max_length=10)

    def __str__(self):
        return self.statValue
"""

class projQueryset (models.QuerySet):
    def approvedProjs(self):
        return self.filter(ia_status='A')

    def notApprovedProjs(self):
        return self.filter(
            Q(ia_status ='I') | Q(ia_status = 'S')
        )

class project(models.Model):
    group = models.CharField(max_length=10)
    opera_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    ia_status = models.CharField(max_length=20, choices=IA_STATUS_CHOICES)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES)
    """ia_status = models.ForeignKey (iaStatus, on_delete=models.CASCADE, choices=IA_STATUS_CHOICES)
    work_status = models.ForeignKey(workStatus, on_delete=models.CASCADE, choices=)"""
    nwa_code = models.CharField(max_length=20)
    manager = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS)
    approved_amount = models.IntegerField(default=0)
    invoiced_amount = models.IntegerField(default=0)
    residual_amount = models.IntegerField(default=0)

    objects = projQueryset.as_manager()

    def __str__(self):
        return self.opera_id

class monthlyBilling(models.Model):
    opera_id = models.ForeignKey(project, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)
    billed_amount = models.IntegerField()

    def __str__(self):
        return self.month

from django.db import models

class ItemsInfo(models.Model):
    name_item = models.CharField()
    quantity_item = models.IntegerField()

class ReportInfo(models.Model):
    name_report_file = models.CharField(primary_key=True)
    name_user = models.CharField()
    date_upload_report = models.DateField()
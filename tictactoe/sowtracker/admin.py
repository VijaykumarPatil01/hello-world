from django.contrib import admin

# Register your models here.
from .models import project, monthlyBilling

#admin.site.register(project)
@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('group','opera_id','name','ia_status','work_status','nwa_code','manager','status','approved_amount','invoiced_amount','residual_amount')
    list_editable = ('ia_status','work_status','status')


admin.site.register(monthlyBilling)
from django.forms import ModelForm

from .models import project, monthlyBilling

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = '__all__'

class billingForm(ModelForm):
    class Meta:
        model = monthlyBilling
        fields = '__all__'
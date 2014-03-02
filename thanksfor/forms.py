from django.forms import ModelForm
from thanksfor.models import Submission

class DocumentForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['image','name','email','user_agent']

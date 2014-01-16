from django.contrib import admin
from thanksfor.models import Submission

# class CustomSubmissionForm(forms.ModelForm):
#     first = forms.CharField()

#     class Meta:
#         model = FooModel
#         fields = ('second',)

class SubmissionAdmin(admin.ModelAdmin):
	readonly_fields=('ip_address',)
    #form = CustomSubmissionForm

admin.site.register(Submission, SubmissionAdmin)

from django import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        
        widgets = {
            'submission_time':forms.TimeInput(),
        }
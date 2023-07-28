from django import forms
from power.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['firstname', 'admission', 'course']
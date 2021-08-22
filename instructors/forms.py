from django import forms
from django.forms import ModelForm, Textarea

from instructors.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating", "review"]
        widgets = {"review": Textarea(attrs={"cols": 40, "rows": 10})}

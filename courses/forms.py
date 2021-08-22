from django import forms
from django.forms import ModelForm, Textarea

# from ckeditor.widgets import CKEditorWidget
from .models import Comment, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {"comment": Textarea(attrs={"cols": 40, "rows": 2})}
        # widgets = {
        #     'comment': CKEditorWidget()
        # }


class CommentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['course_slug'] = forms.CharField(
    #         widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ["msg"]
        widgets = {"msg": Textarea(attrs={"cols": 40, "rows": 2})}
        # widgets = {
        #     'msg': CKEditorWidget()
        # }

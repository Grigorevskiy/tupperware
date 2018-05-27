from django import forms

from product import models


class CommentForm(forms.Form):
    class Meta:
        name = forms.CharField()
        url = forms.URLField()
        body = forms.CharField(widget=forms.Textarea())

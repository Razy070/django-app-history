from django import forms

from .models import Comment, Img


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")


class PostForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ['title', 'cover']

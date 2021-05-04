from django import forms
from .models import ArticlePost
from django.contrib.auth.models import User

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')




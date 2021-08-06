from django import forms
from rango.models import Page, Category, Comment,Article
from django.contrib.auth.models import User


class PageForm(forms.ModelForm):
    clothname = forms.CharField(max_length=Page.MAX_LENGTH, help_text="Please enter the name of the clothes.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please enter the description of the clothes.")
    price = forms.DecimalField(max_digits=8, decimal_places=2 ,help_text="Please enter the price of the clothes.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the clothes.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # new
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Page
        exclude = ('category','img','typeAuto') 


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        exclude = ('page','author', 'comdate',)

        
class ArticleForm(forms.ModelForm):
    title=forms.CharField(max_length=Article.MAX_LENGTH, help_text="Please enter the title of the article.")
    authorName=forms.CharField(max_length=Article.MAX_LENGTH, help_text="Please enter the author of the article.")
    content=forms.CharField(widget=forms.Textarea, help_text="Please enter the content.")

    class Meta:
        model = Article
        fields=('title','authorName','content')
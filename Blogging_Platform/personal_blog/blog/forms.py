from django import forms
from .models import Post

class CommentsForm(forms.Form):
    """
    A form class for sunmitting comments.

    Attributes:
        author (charField): A field for entering the author's name.
        body (CharField): A field for entering the comment body.
    """
    
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class":"form-control", "placeholder":"Leave a comment!"}
        )
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
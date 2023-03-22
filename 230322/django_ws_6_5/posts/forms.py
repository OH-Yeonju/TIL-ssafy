from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':5,
            }
        )
    )
    class Meta:
        model = Post
        fields = '__all__'
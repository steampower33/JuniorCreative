from django import forms
from .models import Book, Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['author', 'text', 'grade']

        widgets={
            "author": forms.TextInput(attrs={'placeholder': '작성자', 'class': 'form-control'}),
            "text":forms.Textarea(attrs={'placeholder':'배려와 매너가 밝은 커뮤니티를 만듭니다.', 'class':'form-control','rows':5}),
            "grade": forms.NumberInput(attrs={'min': '1', 'max': '5', 'class': 'form-control'}),
        }

        labels={
            "author":"",
            "text":"",
            "grade":"",
        }
        

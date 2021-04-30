from django import forms
from .models import Feedback,Item

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('Name', 'Email','Desc','Img',)


class Create(forms.ModelForm):
    class Meta:
        model=Item
        fields=('itemtype','itemcategory','name','img','desc','price','quant','scale','offer')


   
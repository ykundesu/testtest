from django import forms
from .models import getlist
 
 
class getform(forms.ModelForm):
    class Meta():
        model = getlist
        # モデルのインスタンスを生成
 
        fields = '__all__'
        # fieldsに__all__をセットすると、モデル内の全てのフィールドが用いられる

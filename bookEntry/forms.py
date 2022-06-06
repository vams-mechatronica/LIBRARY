from django import forms  
from bookEntry.models import BookEntry  

class bookForm(forms.ModelForm):  
    class Meta:  
        model = BookEntry  
        fields = "__all__" 
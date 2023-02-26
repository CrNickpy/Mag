from .models import Otzyv,Client
from django.forms import ModelForm,TextInput, Textarea,DateInput

class OtzyvForm(ModelForm):
    class Meta:
        model = Otzyv
        fields = ['name','text', 'tel','date']

        widgets = {
                'name': TextInput(attrs={
                     'class':'clform',
                    'placeholder':"Ваше имя"}), 
                
                'tel': TextInput(attrs={
                    'class':'clform',
                    'placeholder':"Ваш телефон"
                }), 
                'text': Textarea(attrs={
                    'class':'clform2',
                    'placeholder':"Напишите отзыв"
                }),
                 'date': DateInput(attrs={
                    'class':'clform',
                    'placeholder':"Введите дату"
                })

        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'tel']
        
        widgets = {
            'name': TextInput(attrs={
                     'class':'clform',
                    'placeholder':" Ваше имя"}), 
                
                'tel': TextInput(attrs={
                    'class':'clform',
                    'placeholder':" Ваш телефон"
                }), }
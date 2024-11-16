
from django import forms  # Імпортуємо бібліотеку для створення форм
from .models import Notes  # Імпортуємо нашу модель Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes 
        fields = ['title', 'content'] 
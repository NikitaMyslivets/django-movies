from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    # Корректная Форма отзыва
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
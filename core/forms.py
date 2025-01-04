from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        # label="Текущий пароль",
        widget=forms.PasswordInput(attrs={'class': 'input-set-password', 'placeholder': 'Введите текущий пароль'})
    )
    new_password1 = forms.CharField(
        # label="Новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'input-set-password', 'placeholder': 'Новый пароль'})
    )
    new_password2 = forms.CharField(
        # label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'input-set-password', 'placeholder': 'Подтвердите новый пароль'})
    )
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit, Div, ButtonHolder
from crispy_forms.helper import FormHelper
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField() #additional field

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('register')
        self.helper.layout = Layout(Div(
            'username',
            'password1',
            'password2',
            ButtonHolder(Submit( 'Register', 'Register', css_class='btn-primary')),
            css_class="col-sm-6 container my-4")
            )

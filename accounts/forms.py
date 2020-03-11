from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):

    username = forms.CharField()
    # We want to render a normal text input box but we want it to be of type password 
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationform(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput)
    
    # An inner class is a class that we can use to provide some information
    # about this form. Django uses them internally to determine things about
    # the class. we can also use it to specify the model that we want store
    # information in and to specify the fields that we're going to expose.
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    # self contains the cleaned data that has been cleaned by Django it's the
    # clean data that we would use when we use the .is_valid method
    def clean_email(self):
        # we get the email by doing self.cleaned_data.get('email') and we do
        # the same for username.
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        # we filter to check to see if we have someone in the database with
        # that email address already
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please conform your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2

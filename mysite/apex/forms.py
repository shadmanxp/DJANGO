from django import forms
from django.core.exceptions import ValidationError

from .accounts_dal import *


class SignUpForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'id': "fullName", 'placeholder': "Input full name"}))
    user_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "userEmail", 'placeholder': "example@example.com"}))
    user_pass = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'id': "userPassword", 'placeholder': "Must be 8 character long"}), min_length=8)
    conf_pass = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'id': "Conf_Password", 'placeholder': "Repeat Password"}),
        min_length=8,
    )
    country = forms.CharField(widget=forms.Select(
        choices=get_country_list(),
        attrs={'class': "form-control", 'id': "country"})
    )
    company = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "company", 'placeholder': "Exact company name"})
    )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        user_pass = cleaned_data.get("user_pass")
        conf_pass = cleaned_data.get("conf_pass")
        user_email = cleaned_data.get("user_email")
        if len(get_user_email(user_email)) >= 1:
            msg = "Already have an account under this email"
            self.add_error('user_email', msg)

        elif user_pass and conf_pass and user_pass != conf_pass:
            msg = "Password did not match!"
            self.add_error('user_pass', msg)
            self.add_error('conf_pass', msg)


class SignInForm(forms.Form):
    user_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "userEmail", 'placeholder': "example@example.com"}))
    user_pass = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'id': "userPassword", 'placeholder': "Must be 8 character long"}))

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        user_email = cleaned_data.get("user_email")
        user_pass = cleaned_data.get("user_pass")
        user_detail = get_user_email(user_email)
        for detail in user_detail:
            database_user_pass = detail.user_pass
        if len(get_user_email(user_email)) < 1:
            msg = "Does not have an account under this email"
            self.add_error('user_email', msg)
        elif get_user_email(user_email) and user_pass != database_user_pass:
            msg = "Enter the correct password"
            self.add_error('user_pass', msg)

    # def password_check(self):
    #     data = self.cleaned_data
    #     if data.get('user_pass') and data.get('conf_pass') and data.get('user_pass') != data.get('conf_pass'):
    #         # self.fields['user_pass'].widget.attrs.update({'class': 'form-control is-invalid' , 'id': "userPassword", 'placeholder': "Password did not match"})
    #         # raise forms.ValidationError({"user_pass": "Passwords do not match!"})
    #         # raise ValidationError(self.fields['conf_pass'].error_messages['pass_error'])
    #         self.add_error('conf_pass', "Passwords do not match!")
    #         return False
    #     else:
    #         return True

    # def clean(self):
    #     data = self.cleaned_data
    #     if data.get('user_pass') and data.get('conf_pass') and data.get('user_pass') != data.get('conf_pass'):
    #         raise forms.ValidationError("Passwords do not match!")
    #         self.add_error('conf_pass', "Passwords do not match!")
    #     return data

# class SignUpPasswordForm(forms.Form):
#     user_pass = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': "form-control", 'id': "userPassword", 'placeholder': "Must be 8 character long"}), min_length=8)
#     conf_pass = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': "form-control", 'id': "conf_pass", 'placeholder': "Repeat Password"}), min_length=8)
#
#     def confirm_password_check(self):
#         # cleaned_data = super(SignUpPasswordForm, self).clean()
#         user_pass = self.cleaned_data.get(self, "user_pass")
#         conf_pass = self.cleaned_data.get(self, "conf_pass")
#         if user_pass and conf_pass and user_pass != conf_pass:
#             raise ValidationError(
#                 self.add_error('conf_pass', "Password does not match"),
#                 code='password_mismatch',
#             )
#         else:
#             return conf_pass

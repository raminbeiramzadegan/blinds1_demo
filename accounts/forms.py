import re
from django import forms
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter Password'}),
)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter Password Confirmation'})
)
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','birthdate_day','birthdate_month','birthdate_year')
 



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Passwords do not match. Please try again.")

        return cleaned_data
    


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # Regular expression pattern for phone numbers with specific area codes
        area_codes_pattern = r'^(403|587|780|825|368|236|604|672|250|778|204|431|584|506|709|867|782|902|226|437|548|647|905|289|365|416|742|249|613|683|753|807|343|519|705|474|306|639)$'
        
        if not re.match(area_codes_pattern, phone_number):
            raise forms.ValidationError('Invalid phone number or area code.')
        
        return phone_number


    def save(self, commit=True):
        user = super().save(commit =False)
        user. set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email already exists. Please use a different email.')
        return email
    


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','birthdate_day','birthdate_month','birthdate_year')



class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter Password'}))







class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter Password Confirmation'}))

    class Meta:
        model = User
        fields= ('email','first_name','last_name','gender','birthdate_day','birthdate_month','birthdate_year')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Last Name'}),
            'email' : forms.EmailInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter E-mail'}),
            'gender' : forms.Select(attrs={'class': 'select-box select-box--primary-style u-w-100'}),
            'birthdate_day' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
            'birthdate_month' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
            'birthdate_year' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists. Please use a different email.')
        return email
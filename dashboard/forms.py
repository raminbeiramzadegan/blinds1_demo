import re
from django import forms
from accounts.models import User
from .models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','birthdate_day','birthdate_month','birthdate_year','phone_number')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Last Name'}),
            'email' : forms.EmailInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter E-mail'}),
            'gender' : forms.Select(attrs={'class': 'select-box select-box--primary-style u-w-100'}),
            'birthdate_day' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
            'birthdate_month' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
            'birthdate_year' : forms.Select(attrs={'class': 'select-box select-box--primary-style'}),
            'phone_number' : forms.EmailInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter your phone number'}),
        }
        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email already exists. Please use a different email.')
    #     return email


    def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            
            # Regular expression pattern for phone numbers with specific area codes
            pattern = r'^(403|587|780|825|368|236|604|672|250|778|204|431|584|506|709|867|782|902|226|437|548|647|905|289|365|416|742|249|613|683|753|807|343|519|705|474|306|639|514)\d{7}$'
        
            
            if not re.match(pattern, phone_number):
                raise forms.ValidationError('Invalid phone number format. Please use the format: Area Code + Main Number (e.g., 4031234567).')
        
            
            return phone_number



class AddressBookForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Last Name'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Enter your phone'}))

    # New fields from the Profile model
    street_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Street Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'City'}))
    province = forms.ChoiceField(choices=Profile.PROVINCE, widget=forms.Select(attrs={'class': 'select-box select-box--primary-style'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Zip/Postal Code'}))

    class Meta:
        model = Profile
        fields = ('street_address', 'city', 'province', 'zip_code', 'first_name', 'last_name', 'phone_number')
        exclude = ('user',) 
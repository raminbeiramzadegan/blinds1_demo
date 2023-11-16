from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
from accounts.models import User
from .forms import AddressBookForm, EditProfileForm,Password_change,Default_shipping
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import Profile
from django.contrib.auth import update_session_auth_hash

from django.urls import reverse

# Create your views here.


class Dashboard(View):
    def get(self,request,id):
        user = get_object_or_404(User,id = id)
     


        return render(request,'dashboard/dashboard.html',{'user':user})



        

def profile(request,id):
    user = get_object_or_404(User,id=id)
    return render(request,'dashboard/dash-my-profile.html',{'user':user})




class UserProfileUpdate(View):
    form_class = EditProfileForm
    template_name = 'dashboard/dash-edit-profile.html'

    def get(self, request, id=None):
        user = get_object_or_404(User, id=id)  
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, id=None):
        user = get_object_or_404(User, id=id)  
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard:profile', user.id)
        return render(request, self.template_name, {'form': form})
    



def address_book(request,id):
    user = get_object_or_404(User,id=id)
    profiles = Profile.objects.filter(user=user)

    return render(request,'dashboard/dash-address-book.html',{'profiles':profiles,'user':user})



class AddNewAddress(View):
    form_class = AddressBookForm
    template_name = 'dashboard/dash-address-add.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs ):
        form = self.form_class(request.POST, instance=request.user)
        
        if form.is_valid():
            
            street_address = form.cleaned_data['street_address']
            city = form.cleaned_data['city']
            province = form.cleaned_data['province']
            zip_code = form.cleaned_data['zip_code']
            Profile.objects.create(user=request.user,street_address = street_address, city= city, province=province, zip_code =zip_code)
            new_address = form.save(commit=False)

            new_address.first_name = form.cleaned_data['first_name']
            new_address.last_name = form.cleaned_data['last_name']
            new_address.phone_number = form.cleaned_data['phone_number']

           
            new_address.save()      
            return redirect('dashboard:address_book', request.user.id)

        return render(request, self.template_name, {'form': form})
   
     
       



class AddressUpdate(View):
    form_class = AddressBookForm
    template_name = 'dashboard/dash-address-edit.html'

    def get(self, request, id=None):
        profile = get_object_or_404(Profile, id=id)
        user = profile.user  # Get the associated User instance

        form = self.form_class(instance=profile,initial={'first_name': user.first_name, 'last_name': user.last_name, 'phone_number': user.phone_number})
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, id=None):
        profile = get_object_or_404(Profile, id=id) 
        user = get_object_or_404(User,id =request.user.id)
        form2= self.form_class(request.POST, instance=user,initial={'first_name': user.first_name, 'last_name': user.last_name, 'phone_number': user.phone_number})
        form = self.form_class(request.POST, instance=profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('dashboard:address_book', request.user.id)
        return render(request, self.template_name, {'form': form})
    

class PasswordChange(View):
    form_class = Password_change
    template_name = 'dashboard/change_password.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['password']
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been successfully changed.")
            
            return redirect('dashboard:dashboard' , request.user.id) 
        return render(request, self.template_name, {'form': form})
    


class DefaultShippingAdd(View):
    form_class = Default_shipping
    template_name = 'dashboard/dash-address-make-default.html'

    def get(self, request, id):
        user_profile = get_object_or_404(Profile,id=id)
        form = self.form_class(instance=user_profile)
        return render(request, self.template_name, {'form': form, 'profiles': user_profile})

    def post(self, request, id):
        user_profile = get_object_or_404(Profile,id=id)
        form = self.form_class(request.POST,instance=user_profile)

        if form.is_valid():
            form.save()  

        return render(request, self.template_name, {'form': form, 'profiles': user_profile})


from django.http import HttpResponseRedirect
from .forms import SignupForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Family, Profile, Records
from .forms import UpdateProfileForm, RecordsForm, FamilyForm
from django.contrib.auth.models import User
from django.views.generic.edit import View 

# Create your views here.


# @login_required(login_url='login')
def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form} ) 

def Record(request):
    all_record = Records.objects.all()
    all_record = all_record[::-1]
    params = {
        'all_record': all_record,
    }
    return render(request, 'record.html', params) 


def create_record(request):
    if request.method == 'POST':
        form = Records(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.admin = request.user.profile
            record.save()
            return redirect('record')
    else:
        form = Records()
    return render(request, 'newrecord.html', {'form': form})




def profile(request, username):
    return render(request, 'profile.html')



def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})


class logout:
  def get(self,request):
    logout(request)
    return redirect('index') 



def search_record(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Records.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search_record.html', params)
    else:
        message = "You haven't searched for any record"
    return render(request, "search_record.html")


def family(request):
    family_record = Family.objects.all()
    family_record = family_record[::-1]
    params = {
        'family_record': family_record,
    }
    return render(request, 'Family_record.html', params) 



def single_record(request, record_id):
    record = Record.objects.get(id=record_id)
    family = Family.objects.filter(Record=record)
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.Record = record
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-record', record.id)
    else:
        form = FamilyForm()
    params = {
        'record': Records,
        'Family': Family,
        'form': form,
        
    }
    return render(request, 'single_hood.html', params)

def  login(request):
    return

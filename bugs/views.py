from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from . forms import BugForm,SignUpForm

# Create your views here.

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def report(request):
    if request.method == 'POST':
     
        form=BugForm(request.POST)
        if form.is_valid():
            report=form.save(commit=False)
            report.user=request.user
            report.save()
            return redirect('success')
    else:
        form=BugForm()
    return render(request,'report.html',{'form':form})

@login_required
def success(request):
    return render(request,'success.html')

def sign_up(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request,'registration/sign_up.html',{'form':form})

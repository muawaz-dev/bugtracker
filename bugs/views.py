from django.shortcuts import render,redirect
from . forms import BugForm,SignUpForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def report(request):
    if request.method == 'POST':
        form=BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=BugForm()
    return render(request,'report.html',{'form':form})

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

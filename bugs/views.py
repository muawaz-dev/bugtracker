from django.shortcuts import render,redirect
from . forms import BugForm

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
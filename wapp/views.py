from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
	err_msg=""
	if request.session.get('user_name', None) is not None:
		return redirect('home')
	if request.method == 'POST':
		form_email=request.POST['email']
		form_password=request.POST['password']
		try:
			user = User.objects.get(email=form_email, password=form_password)
			if user is not None:
				request.session['user_name']=user.name
				return redirect('home')
		except User.DoesNotExist:
			err_msg="Invalid credentials"
	return render(request, 'login.html', {'err_msg':err_msg})

def logout(request):
	del request.session['user_name']
	return redirect('login')

def home(request):
	user_name=request.session['user_name']
	return render(request, 'home.html', {'user_name':user_name})

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			obj = User(**form.cleaned_data)
			obj.save()
			return HttpResponseRedirect('/login')
	else:
		form=UserForm()
	return render(request, 'register.html', {'form': form})

def validate_user(request):
	email = request.GET.get('email', None)
	data = {
	    'is_taken': User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)
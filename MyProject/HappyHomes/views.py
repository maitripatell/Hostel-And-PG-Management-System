from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpRequest
from HappyHomesAdmin.models import *

# Create your views here.


def index(request):
	return render(request, 'tenant/home.html')


def login(request):
	return render(request, 'login.html')


def logincheck(request):
	mail = request.POST.get("email")
	pwd = request.POST.get("password")

	request.session['email'] = mail

	if User.objects.filter(email=mail) and User.objects.filter(password=pwd):
		return render(request, 'tenant/home.html')

	else:
		return render(request, 'registration.html')


def logout(request):
	return render(request, 'login.html')


def registration(request):
	return render(request, 'registration.html')


def reg(request):
	email = request.POST.get("email")
	password = request.POST.get("password")
	userType = request.POST.get("type")
	dob = request.POST.get("dob")

	# print(userType)

	User.objects.create(email=email, password=password, dob=dob, user_role_type=userType)
	request.session['email'] = email
	
	if(userType == "Owner"):
		return HttpResponseRedirect(reverse('HappyHomesAdmin:home'))
	else:
		return render(request, 'tenant/home.html')


def profile(request):
	return render(request, 'tenant/profile.html')


def edit_profile(request):
	return render(request, 'tenant/edit-profile.html')


def pg_hostel_showall(request):
	residenceList = Residence.objects.values()
	typeList = Residence_type.objects.values()
	facilityList = Facility.objects.values()

	residenceDict = {
	"Residence": residenceList,
	"Facility": facilityList
	}

	print(residenceList);
	return render(request, 'tenant/pg-hostel-showall.html', {"residenceDict": residenceDict})


def pg_hostel(request):
	resID = request.GET.get('id')
	search = Residence.objects.get(id=resID)
	searchFacility = Facility.objects.get(residence_id=resID)

	search = {
	"searchRes": search,
	"searchFacility": searchFacility
	}

	return render(request, 'tenant/pg-hostel.html', search)


def pg_hostel_booking(request):
	return render(request, 'tenant/booking.html')


def contact_us(request):
	return render(request, 'tenant/contact-us.html')




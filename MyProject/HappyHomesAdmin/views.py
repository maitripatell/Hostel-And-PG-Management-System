from django.shortcuts import render
from HappyHomesAdmin.models import *
from django.http import JsonResponse

# Create your views here.


def index(request):
	return render(request, 'home.html')


def addnew(request):

	return render(request, 'addnew.html')



def add_data(request):

	name = request.GET.get("name")
	address = request.GET.get("address")
	city = request.GET.get("city")
	state = request.GET.get("state")
	pincode = request.GET.get("pincode")
	description = request.GET.get("description")
	rent = request.GET.get("rent")
	facility = request.GET.get("facility")
	residence_type = request.GET.get("residence-type")
	image = request.GET.get("image")

	# print(name)
	# print(address)
	# print(city)
	# print(state)
	# print(pincode)
	# print(description)
	# print(rent)
	# print(facility)
	# print(residence_type)

	residence = Residence.objects.create(residence_name=name, residence_address=address, residence_city=city, residence_state=state, residence_pincode=pincode, description=description, rent=rent, image=image)
	Facility.objects.create(residence_id=residence, facility_type=facility)
	Residence_type.objects.create(residence_id=residence, residence_type=residence_type)


	return render(request, 'view-all.html')



def editable(request):
	return render(request, 'update-delete.html')


def edit(request):
	return render(request, 'view-all.html')


def view_all(request):

	residenceList = Residence.objects.values()
	typeList = Residence_type.objects.values()
	facilityList = Facility.objects.values()

	residenceDict = {
	"Residence": residenceList,
	"Type": typeList,
	"Facility": facilityList
	}

	print(residenceDict)

	print(residenceList);
	return render(request, 'view-all.html', {"residenceDict": residenceDict})



def json_format(request):
	userList = list(User.objects.values())
	userRoleList = list(User_role_type.objects.values())
	occupationList = list(Occupation.objects.values())
	residenceList = list(Residence.objects.values())
	facilityList = list(Facility.objects.values())
	residenceTypeList = list(Residence_type.objects.values())
	bookingList = list(Booking.objects.values())

	dataList = [userList, userRoleList, occupationList, residenceList, facilityList, residenceTypeList, bookingList]

	return JsonResponse(dataList, safe=False)

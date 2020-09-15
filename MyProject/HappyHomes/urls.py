from django.urls import path
from HappyHomes import views

app_name = "HappyHomes"

urlpatterns = [
	path('index/', views.index),
    path('login/', views.login),
    path('logincheck/', views.logincheck),
    path('logout/', views.logout),
    path('registration/', views.registration),
    path('reg/', views.reg),
    path('profile/', views.profile),
    path('edit_profile/', views.edit_profile),
    path('pg_hostel_showall/', views.pg_hostel_showall),
    path('pg_hostel/', views.pg_hostel),
    path('pg_hostel_booking/', views.pg_hostel_booking),
    path('contact_us/', views.contact_us),
]
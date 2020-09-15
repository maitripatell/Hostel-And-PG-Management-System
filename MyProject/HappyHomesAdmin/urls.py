from django.urls import path
from HappyHomesAdmin import views

app_name = "HappyHomesAdmin"

urlpatterns = [
	path('index/', views.index, name="home"),
	path('addnew/', views.addnew),
	path('add_data/', views.add_data),
	path('editable/', views.editable),
	path('view_all/', views.view_all),
	path('json_format/', views.json_format),
]
from django.db import models

# Create your models here.


class User(models.Model):
	user_name = models.CharField(max_length=20, blank=True)
	user_address = models.CharField(max_length=30, blank=True)
	user_city = models.CharField(max_length=20, blank=True)
	user_state = models.CharField(max_length=20, blank=True)
	pincode = models.IntegerField(default='0', blank=True)
	dob = models.DateField(blank=True)
	gender = models.CharField(max_length=6, blank=True)
	email = models.EmailField(blank=True)
	password = models.CharField(max_length=12, blank=True)
	user_role_type = models.CharField(max_length=20)


class Occupation(models.Model):
	user_id = models.ForeignKey('User', default='1', on_delete=models.CASCADE, blank=True)
	occupation_type = models.CharField(max_length=10)
	occupation_name = models.CharField(max_length=20)
	occupation_address = models.CharField(max_length=30)
	occupation_phno = models.IntegerField()

	def __str__(self):
		return self.occupation_type


class Residence(models.Model):
	residence_name = models.CharField(max_length=30)
	residence_address = models.CharField(max_length=30)
	residence_city = models.CharField(max_length=20)
	residence_state = models.CharField(max_length=20)
	residence_pincode = models.IntegerField()
	description = models.CharField(max_length=255)
	rent = models.IntegerField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.residence_name


class Facility(models.Model):
	residence_id = models.ForeignKey('Residence', on_delete=models.CASCADE)
	facility_type = models.CharField(max_length=30)


class Residence_type(models.Model):
	residence_id = models.ForeignKey('Residence', on_delete=models.CASCADE)
	residence_type = models.CharField(max_length=7)


class Booking(models.Model):
	residence_id = models.ForeignKey('Residence', on_delete=models.CASCADE)
	user_id = models.ForeignKey('User', on_delete=models.CASCADE)
	min_stay_duration = models.CharField(max_length=20)
	joining_date = models.DateField()
	status  = models.CharField(max_length=10, default='Pending')


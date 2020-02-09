from django.db import models

# Create your models here.
class AdmissionPerson(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_email = models.CharField(max_length=300)
    student_number = models.CharField(max_length=400)
    student_address = models.TextField(max_length=500)
    student_address2 = models.TextField(max_length=500)
    student_city = models.CharField(max_length=50)
    student_state = models.CharField(max_length=50)
    student_zip = models.CharField(max_length=20)
    student_course = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

from django.db import models



    
class doctor(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    doc_department = models.CharField(max_length=255)
    doc_image = models.ImageField(upload_to='doctors')
    
    def __str__(self):
        return 'Dr.' + self.doc_name + ' -(' +self. doc_spec + ')'
class booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=255)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


class feedback(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=255)
    p_email = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255)



  

# Create your models here.

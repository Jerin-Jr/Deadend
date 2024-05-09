from django.contrib import admin
from. models import doctor,booking,feedback



admin.site.register(doctor)

class bookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on',)
admin.site.register(booking,bookingAdmin)

class feedbackAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','feedback',)

admin.site.register(feedback,feedbackAdmin)
# Register your models here.

from django import forms
from. models import booking,feedback

class DateInput(forms.DateInput):
    input_type = 'date'

class bookingform(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        
        widgets={
            'booking_date' : DateInput(),
            }
        
        labels={
            'p_name' : "Patient Name:", 
            'p_phone' : "Patient Phone_No.:",
            'p_email' : "Patient Email:",         
            'doc_name ' :"Doctor Name:",
            'booking_date' : "Booking Date:",
        }

class feedbackform(forms.ModelForm):
    class Meta :
        model = feedback
        fields = '__all__'


        labels ={
            'p_name' : "Patient Name:", 
            'p_phone' : "Patient Phone_No.:",
            'p_email' : "Patient Email:",
            'feedback' : "Feedback",   
            
            }              
 

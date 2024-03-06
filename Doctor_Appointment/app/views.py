from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'select_doctor.html')

def book_appo(request):
    return render(request,'book_appointment.html')
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
# Create your views here.
import ssl
import certifi 
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where()) 
from django.http import HttpResponse



def resume(request):  
  if request.method == 'POST': 
    try:
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('number')
      message = request.POST.get('details')   
    
    
      full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
      print(full_message) 
       
      send_mail(
            subject,
            full_message,
            'khansajid01379@gmail.com',    
            ['khans61101@gmail.com'],  
            fail_silently=False,
        )

      return redirect('/folio/')  
    except Exception as e:
            return HttpResponse(f"<h2>Error: {e}</h2>")
  return render(request, 'demo.html')   
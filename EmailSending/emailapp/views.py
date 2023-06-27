from django.shortcuts import render
from django.core.mail import send_mail



# Create your views here.

def submit(request):  
          
          if request.method=='POST':
             un=request.POST.get('username')
             sub=request.POST.get('sub')
             msg=request.POST.get('mess')

            #  subject='FRIENDSHIP FOREVER'
             sender="naikmanali1208@gmail.com"
             send_mail(
                 sub,
                 msg,
                 sender,
                 [un],
                 fail_silently=False,
             )
             context={}
             context['success']="Email send Successfully"
            
             return render(request,'login.html',context)                    
          else:             
             return render(request,'login.html')
             
             
             
      

               

            
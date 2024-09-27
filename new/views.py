from django.shortcuts import render

# Create your views here.
def calculator(request):
    return render(request,'calculator.html')

def calculator(request):
    a=""
    try:
        if request.method=="POST":
            reset=request.POST.get('reset')
            if reset=='reset':
               a=""
            else:
               n1=int(request.POST.get("num1"))
               n2=int(request.POST.get("num2"))
               opr=request.POST.get("operation")
               if opr=="+":
                 a=n1+n2
               elif opr=="-":
                 a=n1-n2
               elif opr=="*":
                 a=n1*n2
               elif opr == "/":
                 if n2 != 0:
                    a = n1 / n2
                
    except:
       a = ("Invalid operation selected")
       print(a)
    return render(request, "calculator.html", {"result": a})
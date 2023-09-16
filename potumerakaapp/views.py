from django.shortcuts import render,redirect
from .models import PotumerakaData,Expenditure

def mainpage(request):
    return render(request,'mainpage.html')

def adddata(request):
    if request.method=='GET':
        data=PotumerakaData.objects.all()
        return render(request,'adddata.html',{'data':data})
    else:
        PotumerakaData(
            name=request.POST.get('name'),
            sur_name=request.POST.get('sur_name'),
            father_name=request.POST.get('father_name'),
            amount=request.POST.get('amount'),
            payment_type=request.POST.get('payment_type'),
            date=request.POST.get('date'),
            recieved_by=request.POST.get('recieved_by')
            
    ).save()
    return redirect('mainpage')

def see_sub(request):
    data=PotumerakaData.objects.all()
    return render(request,'see_sub.html',{'data':data})

def update(request,id):
    data=PotumerakaData.objects.get(id=id)
    return render(request,'update.html',{'data':data})

def update_data(request,id):
    data=PotumerakaData.objects.get(id=id)
    data.name=request.POST.get('name')
    data.sur_name=request.POST.get('sur_name')
    data.father_name=request.POST.get('father_name')
    data.amount=request.POST.get('amount')
    data.payment_type=request.POST.get('payment_type')
    data.date=request.POST.get('date')
    data.recieved_by=request.POST.get('recieved_by')
    data.save()
    return redirect('see_sub')

def delete(request,id):
    data=PotumerakaData.objects.get(id=id)
    data.delete()
    return redirect('see_sub')

def expenditure(request):
    if request.method=='GET':
        exp=Expenditure.objects.all()
        return render(request,'expenditure.html',{'exp':exp})

    else:
        Expenditure(
            exp_name=request.POST.get('exp_name'),
            exp_incurred=request.POST.get('exp_incurred')
        ).save()
    exp=Expenditure.objects.all()
    return render(request,'expenditure.html',{'exp':exp})

def update_exp(request,id):
    exp=Expenditure.objects.get(id=id)
    return render(request,'update_exp.html',{'exp':exp})
    
def updated_exp(request,id):
    exp=Expenditure.objects.get(id=id)
    exp.exp_name=request.POST.get('exp_name')
    exp.exp_incurred=request.POST.get('exp_incurred')
    exp.save()
    return redirect('expenditure')

def delete_exp(request,id):
    exp=Expenditure.objects.get(id=id)
    exp.delete()
    return redirect('expenditure')


def total_amount(request):
    total= PotumerakaData.objects.all()
    total_amount = sum(i.amount for i in total)

    return render(request, 'total_amount.html', {'total_amount':total_amount})

def help(request):
    return render(request,'help.html')

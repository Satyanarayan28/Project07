from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class ProductView(View):
    def get(self,request):
     return render(request,'input.html')
class ProductInsert(View):
    def post(self,request):
        p_id=int(request.POST["t1"])
        p_name=request.POST["t2"]
        p_cost=float(request.POST["t3"])
        p_mfdt=request.POST["t4"]
        p_expdt=request.POST["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        return render(request,'links.html')
class ProductDisplay(View):
    def get(self,request):
        QS=Product.objects.all()
        con_dic={"records":QS}
        return render(request,'display.html',con_dic)

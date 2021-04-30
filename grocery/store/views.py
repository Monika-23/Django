from django.views import View
from .forms import FeedbackForm,Create
from .models import Item,Feedback
from django.shortcuts import render
itemss=Item.objects.all()
itemcat=itemss.values_list('itemcategory',flat=True).distinct()
send=0
class MyView(View):

    global itemss,itemcat,send
    form_class = FeedbackForm
    create_form = Create
    template_name = 'index.html'
    

    def get(self,request,*args, **kwargs):
        
        global itemss,itemcat,send
        send=0
        form=self.form_class()
        return render(request, self.template_name, {"items":itemss,'itemcats':itemcat,'form':form,'send':send})

    def post(self,request,*args, **kwargs):
        global itemss,itemcat,send
        form=self.form_class()
        send=1
    
        if request.POST.get('optradio'):
            send=1
            value=request.POST.get('optradio')
            if value=='all':
                items= Item.objects.all()
                itemcats=items.values_list('itemcategory',flat=True).distinct()
                return render(request,self.template_name,{"items":items,'itemcats':itemcats,'form':form,'send':send})  
            else:
                    items=Item.objects.filter(itemtype=value)  
                    itemcats=items.values_list('itemcategory',flat=True).distinct()
                    itemss=items.all()
                    return render(request,self.template_name,{"items":items,'itemcats':itemcats,'form':form,'send':send})      
        if request.POST.get('dropdown'): 
                send=1
                answer=request.POST.get('dropdown')
                itemcats=itemss.values_list('itemcategory',flat=True).distinct()

                if answer=='DESC':
                    item1=itemss.order_by('-price') 
                if answer=="ASC":
                    item1=itemss.order_by('price')
                return render(request,self.template_name,{"items":item1,'itemcats':itemcats,'form':form,'send':send}) 
        if request.POST.get('checkbox'):
                send=1
                answer=request.POST.getlist('checkbox') 
                items=Item.objects.none()

                for i in answer:
                    items1=Item.objects.filter(itemcategory=i) 
                    items=items|items1
                itemss=items.all()  
                return render(request,self.template_name,{"items":items,'itemcats':answer,'form':form,'send':send})   

       
        if request.POST.get('crud'):
                itemses=Item.objects.all()
                itemcats=itemses.values_list('itemcategory',flat=True).distinct()
                send=2
                answer=request.POST.get('crud')
                if answer=="C":
                    value=0
                    form1=self.create_form()
                    return render(request,self.template_name, {"items":itemses,'itemcats':itemcats,'form':form,'send':send,'cform':form1,'value':value})
                if answer=="U":
                    value=2
                    itemfiels=Item._meta.get_fields
                    
                    return render(request,self.template_name, {"items":itemses,'itemcats':itemcat,'form':form,'send':send,'value':value,"itemfields":itemfiels})    
                if answer=="D":
                    value=1
                    return render(request,self.template_name, {"items":itemses,'itemcats':itemcats,'form':form,'send':send,'value':value})
                else:
                    return render(request,self.template_name, {"items":itemses,'itemcats':itemcats,'form':form,'send':send})    
        if request.POST.get('del'):
            send=1
            answer=request.POST.get('del')
            if answer in Item.objects.all().values_list('name',flat=True).distinct():
                Item.objects.get(name=answer).delete()
            itemses=Item.objects.all()
            itemcats=itemses.values_list('itemcategory',flat=True).distinct()
            return render(request,self.template_name,{"items":itemses,'itemcats':itemcats,'form':form,'send':send})

        

        else:
                crform=self.create_form(request.POST,request.FILES)                
                form=self.form_class(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    itemcats=itemss.values_list('itemcategory',flat=True).distinct()
                    form=self.form_class()
                    send=1
                    return render(request,self.template_name,{"items":itemss,'itemcats':itemcats,'form':form,'send':send})
                if crform.is_valid():
                    crform.save()
                    itemses=Item.objects.all()
                    itemcats=itemses.values_list('itemcategory',flat=True).distinct()
                    form=self.form_class()
                    send=1
                    return render(request,self.template_name,{"items":itemses,'itemcats':itemcats,'form':form,'send':send})
                else:
                    form=self.form_class()
                    itemcats=itemss.values_list('itemcategory',flat=True).distinct()
                    send=2
                    answer='here'
                    return render(request,self.template_name,{"items":itemss,'itemcats':itemcats,'form':form,'send':send,'answer':answer})   

   
import datetime

from django.shortcuts import render

# Create your views here.
from myapp.models import *
import time
from django.contrib import messages
import datetime


import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


def login(request):
    return render(request,'login.html')

def login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if user.objects.filter(username=username,password=password).exists():
            a=user.objects.filter(username=username,password=password).exists()
            print('this is my tesst',a)
            loginobj=user.objects.get(username=username,password=password)
            print('this is my obj',loginobj)
            request.session['userid']=loginobj.id
            print('my test id is',request.session['userid'])
            role=loginobj.role
            print('my role is ',role)
            nam=loginobj.username
            print('my name is',nam)

            if role=='Admin':
                request.session['username'] = username
                us = request.session['username']

                l = []
                t = consolidated.objects.all()
                for i in t:
                    l.append(i.order_qty_br1)
                ll = []
                tt = consolidated.objects.all()
                for j in tt:
                    ll.append(j.item_sales_rate)
                s = []
                for i in range(len(l)):
                    s.append(l[i] * ll[i])
                sum = 0
                for i in s:
                    sum = sum + i
                # *****
                profit1 = []
                p = consolidated.objects.all()
                for i in p:
                    profit1.append(i.item_production_cost)
                sp = []
                for i in range(len(l)):
                    sp.append(l[i] * profit1[i])
                profitsum1 = 0
                for i in sp:
                    profitsum1 = profitsum1 + i

                ##############################

                l2 = []
                t2 = consolidated.objects.all()
                for i in t2:
                    l2.append(i.order_qty_br2)
                ll2 = []
                tt2 = consolidated.objects.all()
                for j in tt2:
                    ll2.append(j.item_sales_rate)
                s2 = []
                for i in range(len(l2)):
                    s2.append(l2[i] * ll2[i])
                sum2 = 0
                for i in s2:
                    sum2 = sum2 + i
                # *****
                profit2 = []
                p2 = consolidated.objects.all()
                for i in p2:
                    profit2.append(i.item_production_cost)
                sp2 = []
                for i in range(len(l2)):
                    sp2.append(l2[i] * profit2[i])
                profitsum2 = 0
                for i in sp2:
                    profitsum2 = profitsum2 + i

                ##############################

                l3 = []
                t3 = consolidated.objects.all()
                for i in t3:
                    l3.append(i.order_qty_br3)
                ll3 = []
                tt3 = consolidated.objects.all()
                for j in tt3:
                    ll3.append(j.item_sales_rate)
                s3 = []
                for i in range(len(l3)):
                    s3.append(l3[i] * ll3[i])
                sum3 = 0
                for i in s3:
                    sum3 = sum3 + i

                profit3 = []
                p3 = consolidated.objects.all()
                for i in p3:
                    profit3.append(i.item_production_cost)
                sp3 = []
                for i in range(len(l2)):
                    sp3.append(l3[i] * profit3[i])
                profitsum3 = 0
                for i in sp3:
                    profitsum3 = profitsum3 + i

                #############
                tot = sum + sum2 + sum3
                br1per = sum / tot * 100
                br2per = sum2 / tot * 100
                br3per = sum3 / tot * 100

                tu = user.objects.all()
                tus = len(tu)
                tb = branch.objects.all()
                tbs = len(tb)
                ti = item.objects.all()
                tis = len(ti)

                yy = []
                yy.append(sum)
                yy.append(sum2)
                yy.append(sum3)
                print(yy)
                tdpr = profitsum1 + profitsum2 + profitsum3
                totcos = sum + sum2 + sum3
                context = {
                    'y': yy,
                    'z': consolidated.objects.all(),
                    'pr1': profitsum1,
                    'pr2': profitsum2,
                    'pr3': profitsum3,
                    's1': sum,
                    's2': sum2,
                    's3': sum3,
                    'br1p': br1per,
                    'br2p': br2per,
                    'br3p': br3per,
                    'tu': tus,
                    'tb': tbs,
                    'ti': tis,
                    'totp': tdpr,
                    'totc': totcos,

                    'conord': branch.objects.all(),
                    'viewitem': item.objects.all().filter(item_flag=1),
                    'br1': branch_1.objects.all(),
                    'br2': branch_2.objects.all(),
                    'con': consolidated.objects.all().order_by('id')[:5],
                    'dt': datetime.date.today(),
                    'user': loginobj,
                    'name': request.session['username']
                }


                return render(request,'admindashboard/index.html',context)

            if role == 'User':
                p = time.strftime('%H:%M:%S', time.localtime())
                if p > '16:00:00' or p < '10:00:00':
                    context = {
                        'msg': 'Login failed,please try in official time',

                    }

                    return render(request, 'login.html', context)
                else:
                    request.session['username'] = username
                    us = request.session['username']

                    return render(request, 'admindashboard/index.html',context={'user': loginobj, 'name': request.session['username']})
            if role == 'BR1':
                p = time.strftime('%H:%M:%S', time.localtime())
                if p > '18:00:00' or p < '04:00:00':
                    context = {
                        'msg': 'Login failed,please try in official time',

                    }

                    return render(request, 'login.html', context)
                else:
                    request.session['username'] = username
                    us = request.session['username']

                    return render(request, 'branches/branch1/br1_order_page.html',context={'user': loginobj, 'name': request.session['username'],'items':branch_1.objects.all()})
            if role == 'BR2':
                p = time.strftime('%H:%M:%S', time.localtime())
                if p > '18:00:00' or p < '04:00:00':
                    context = {
                        'msg': 'Login failed,please try in official time',

                    }

                    return render(request, 'login.html', context)
                else:
                    request.session['username'] = username
                    us = request.session['username']

                    return render(request, 'branches/branch2/br2_order_page.html',context={'user': loginobj, 'name': request.session['username'],'items':branch_2.objects.all()})
            if role == 'BR3':
                p = time.strftime('%H:%M:%S', time.localtime())
                if p > '18:00:00' or p < '16:00:00':
                    context = {
                        'msg': 'Login failed,please try in official time',

                    }

                    return render(request, 'login.html', context)
                else:
                    request.session['username'] = username
                    us = request.session['username']

                    return render(request, 'branches/branch3/br3_order_page.html',context={'user': loginobj, 'name': request.session['username'],'items':branch_3.objects.all()})

            if role == 'Production':
                request.session['username'] = username
                us = request.session['username']
                tu = user.objects.all()
                tus = len(tu)
                tb = branch.objects.all()
                tbs = len(tb)
                ti = item.objects.all()
                tis = len(ti)

                context = {
                    'conord': branch.objects.all(),
                    'viewitem': item.objects.all().filter(item_flag=1),
                    'br1': branch_1.objects.all(),
                    'br2': branch_2.objects.all(),
                    'con': consolidated.objects.all(),
                    'dt': datetime.date.today(),
                    'tu': tus,
                    'tb': tbs,
                    'ti': tis,
                    'user': loginobj,
                    'name': request.session['username'],
                    'items': branch_1.objects.all()
                }
                request.session['username'] = username
                us = request.session['username']

                return render(request, 'admindashboard/reports/production/production_home.html',context)

            if role == 'Despatch':
                request.session['username'] = username
                us = request.session['username']
                context={
                    'user': loginobj,
                    'name': request.session['username'],
                    'brre':branch_1.objects.all(),

                }

                return render(request, 'admindashboard/reports/despatch/br1.html',context)




            else:
                request.session['username'] = username
                us = request.session['username']
                context = {
                    'user': loginobj,
                    'name': us,
                }
                print('my test name is ',request.session['username'])
                return render(request,'apm.html',context)

        else:

            return render(request,'login.html',context={'msg':'Login failed !... User Name or Password Incorrect'})
    else:
        return render(request,'login.html')
#*********USER START HERE ***********

def admin_dashboard(request):

    l = []
    t = consolidated.objects.all()
    for i in t:
        l.append(i.order_qty_br1)
    ll = []
    tt = consolidated.objects.all()
    for j in tt:
        ll.append(j.item_sales_rate)
    s = []
    for i in range(len(l)):
        s.append(l[i] * ll[i])
    sum = 0
    for i in s:
        sum = sum + i
    # *****
    profit1 = []
    p = consolidated.objects.all()
    for i in p:
        profit1.append(i.item_production_cost)
    sp = []
    for i in range(len(l)):
        sp.append(l[i] * profit1[i])
    profitsum1 = 0
    for i in sp:
        profitsum1 = profitsum1 + i

    ##############################

    l2 = []
    t2 = consolidated.objects.all()
    for i in t2:
        l2.append(i.order_qty_br2)
    ll2 = []
    tt2 = consolidated.objects.all()
    for j in tt2:
        ll2.append(j.item_sales_rate)
    s2 = []
    for i in range(len(l2)):
        s2.append(l2[i] * ll2[i])
    sum2 = 0
    for i in s2:
        sum2 = sum2 + i
    # *****
    profit2 = []
    p2 = consolidated.objects.all()
    for i in p2:
        profit2.append(i.item_production_cost)
    sp2 = []
    for i in range(len(l2)):
        sp2.append(l2[i] * profit2[i])
    profitsum2 = 0
    for i in sp2:
        profitsum2 = profitsum2 + i

    ##############################

    l3 = []
    t3 = consolidated.objects.all()
    for i in t3:
        l3.append(i.order_qty_br3)
    ll3 = []
    tt3 = consolidated.objects.all()
    for j in tt3:
        ll3.append(j.item_sales_rate)
    s3 = []
    for i in range(len(l3)):
        s3.append(l3[i] * ll3[i])
    sum3 = 0
    for i in s3:
        sum3 = sum3 + i

    profit3 = []
    p3 = consolidated.objects.all()
    for i in p3:
        profit3.append(i.item_production_cost)
    sp3 = []
    for i in range(len(l2)):
        sp3.append(l3[i] * profit3[i])
    profitsum3 = 0
    for i in sp3:
        profitsum3 = profitsum3 + i

    #############
    tot = sum + sum2 + sum3
    br1per = sum / tot * 100
    br2per = sum2 / tot * 100
    br3per = sum3 / tot * 100

    tu = user.objects.all()
    tus = len(tu)
    tb = branch.objects.all()
    tbs = len(tb)
    ti = item.objects.all()
    tis = len(ti)

    yy = []
    yy.append(sum)
    yy.append(sum2)
    yy.append(sum3)
    print(yy)
    tdpr=profitsum1+profitsum2+profitsum3
    totcos=sum+sum2+sum3
    context = {
        'y': yy,
        'z': consolidated.objects.all(),
        'pr1': profitsum1,
        'pr2': profitsum2,
        'pr3': profitsum3,
        's1': sum,
        's2': sum2,
        's3': sum3,
        'br1p': br1per,
        'br2p': br2per,
        'br3p': br3per,
        'tu': tus,
        'tb': tbs,
        'ti': tis,
        'totp': tdpr,
        'totc':totcos,

        'conord': branch.objects.all(),
        'viewitem': item.objects.all().filter(item_flag=1),
        'br1': branch_1.objects.all(),
        'br2': branch_2.objects.all(),
        'con': consolidated.objects.all().order_by('id')[:5],
        'dt': datetime.date.today(),

        'name': request.session['username']
    }

    return render(request,'admindashboard/index.html',context)

def create_user(request):
    return render(request,'admindashboard/users/user_creation.html')

def user_regi(request):
    itname = request.POST.get('username')
    chkitemname = user.objects.filter(username=itname).exists()
    if chkitemname == True:
        messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'admindashboard/users/user_creation.html', )
    else:
        if request.method == 'POST':
            ucode=request.POST.get('code')
            empname = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            urole = request.POST.get('role')
            uemail = request.POST.get('email')
            udes = request.POST.get('description')
            fl = request.POST.get('eanable_disable')
            chk = 11
            if fl == None:
                chk = 0
            else:
                chk = 1
            uc=user()
            uc.user_code = ucode
            uc.emp_name = empname
            uc.username = uname
            uc.password = upass
            uc.role = urole
            uc.email = uemail
            uc.user_description=udes
            uc.user_flage = chk
            uc.save()

    messages.info(request,'user created sucessfully')
    context = {
        'users': user.objects.all()
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def view_all_users(request):
    context={
        'users':user.objects.all()
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

def user_update(request,id):
    if request.method == 'POST':
        ucode=request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')
        uemail = request.POST.get('email')
        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc=user.objects.get(id=id)
        uc.user_code = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole
        uc.email = uemail
        uc.user_description=udes
        uc.user_flage=chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_users(request)

    context = {
        'users': user.objects.all(),
        'sd':user.objects.get(id=id),
    }

    return render(request,'admindashboard/users/update_user.html',context)

def del_user(request,id):
    d=user.objects.get(id=id)
    d.delete()
    context = {
        'users': user.objects.all()
    }
    return render(request,'admindashboard/users/view_all_users.html',context)

#*********USER END HERE ***********
def test(request):
    l=[]
    t=consolidated.objects.all()
    for i in t:
        l.append(i.order_qty_br1)
    ll = []
    tt = consolidated.objects.all()
    for j in tt:
        ll.append(j.item_sales_rate)
    s=[]
    for i in range(len(l)):
        s.append(l[i]*ll[i])
    sum=0
    for i in s:
        sum=sum+i
    #*****
    profit1 = []
    p = consolidated.objects.all()
    for i in p:
        profit1.append(i.item_production_cost)
    sp = []
    for i in range(len(l)):
        sp.append(l[i] * profit1[i])
    profitsum1=0
    for i in sp:
        profitsum1=profitsum1+i

##############################

    l2 = []
    t2 = consolidated.objects.all()
    for i in t2:
        l2.append(i.order_qty_br2)
    ll2 = []
    tt2 = consolidated.objects.all()
    for j in tt2:
        ll2.append(j.item_sales_rate)
    s2 = []
    for i in range(len(l2)):
        s2.append(l2[i] * ll2[i])
    sum2 = 0
    for i in s2:
        sum2 = sum2 + i
    #*****
    profit2 = []
    p2 = consolidated.objects.all()
    for i in p2:
        profit2.append(i.item_production_cost)
    sp2 = []
    for i in range(len(l2)):
        sp2.append(l2[i] * profit2[i])
    profitsum2=0
    for i in sp2:
        profitsum2=profitsum2+i

##############################


    l3 = []
    t3 = consolidated.objects.all()
    for i in t3:
        l3.append(i.order_qty_br3)
    ll3 = []
    tt3 = consolidated.objects.all()
    for j in tt3:
        ll3.append(j.item_sales_rate)
    s3 = []
    for i in range(len(l3)):
        s3.append(l3[i] * ll3[i])
    sum3 = 0
    for i in s3:
        sum3 = sum3 + i

#############
    tot=sum+sum2+sum3
    br1per=sum/tot*100
    br2per = sum2 / tot * 100
    br3per = sum3 / tot * 100

    tu = user.objects.all()
    tus=len(tu)
    tb=branch.objects.all()
    tbs=len(tb)
    ti = item.objects.all()
    tis = len(ti)

    yy=[]
    yy.append(sum)
    yy.append(sum2)
    yy.append(sum3)
    print(yy)
    context={
        'y':yy,
        'z':consolidated.objects.all(),
        'pr1':profitsum1,
        'pr2': profitsum2,
        's1':sum,
        's2':sum2,
        's3':sum3,
        'br1p':br1per,
        'br2p':br2per,
        'br3p':br3per,
        'tu':tus,
        'tb':tbs,
        'ti':tis,

        'conord': branch.objects.all(),
        'viewitem': item.objects.all().filter(item_flag=1),
        'br1': branch_1.objects.all(),
        'br2': branch_2.objects.all(),
        'con': consolidated.objects.all().order_by('id')[:5],
        'dt': datetime.date.today(),
    }


    return render(request,'test.html',context)

def admindashboard(request):
    return render(request,'admindashboard/index.html')

###********* ITEM CREATION START HERE *************

def item_main_page(request):
    return render(request,'admindashboard/items/item_main_page.html')

def item_creation_page(request):
    context = {

        'iuom': uom.objects.all(),
        'icat': catergory.objects.all(),
        'idep': department.objects.all(),
    }
    return render(request,'admindashboard/items/item_creation.html',context)

def item_creation(request):
    itc=request.POST.get('code')
    chkitem=item.objects.filter(item_code=itc).exists()

    if chkitem == True:

        context={
            'msg':'item code already exists'
        }
        messages.info(request, 'item code already exists!. please try another one')
        return render(request,'admindashboard/items/item_creation.html',context)

    itname = request.POST.get('name')
    chkitemname = item.objects.filter(item_name=itname).exists()
    if chkitemname == True:
        messages.info(request,'item name already exists!. please try another one')
        return render(request,'admindashboard/items/item_creation.html',)

    else:
        itemcode = request.POST.get('code')
        print('my item cod is ',itemcode)
        itemname =request.POST.get('name')
        itemuom =request.POST.get('uom')
        itembarcode =request.POST.get('barcode')
        itemcategory =request.POST.get('category')
        itemkitchen =request.POST.get('kitchen')
        itemproduction_cost =request.POST.get('pcost')
        itemsales_rate =request.POST.get('srate')
        itembranch_sales_rate =request.POST.get('bsrate')
        itemmrp =request.POST.get('mrp')
        #itemimage =request.POST.get('itemimages')
        itemimage = request.FILES['itemimages']
        itemdescription=request.POST.get('description')

        ic=item()
        ic.item_code = itemcode
        ic.item_name = itemname
        ic.item_uom = itemuom
        ic.item_barcode = itembarcode
        ic.item_category = itemcategory
        ic.item_kitchen = itemkitchen
        ic.item_production_cost = itemproduction_cost
        ic.item_sales_rate = itemsales_rate
        ic.item_branch_sales_rate = itembranch_sales_rate
        ic.item_mrp = itemmrp
        ic.item_image = itemimage
        ic.item_description = itemdescription
        ic.item_flag = 1
        ic.save()

        ic = consolidated()
        ic.item_code = itemcode
        ic.item_name = itemname
        ic.item_uom = itemuom
        ic.item_barcode = itembarcode
        ic.item_category = itemcategory
        ic.item_kitchen = itemkitchen
        ic.item_production_cost = itemproduction_cost
        ic.item_sales_rate = itemsales_rate
        ic.item_branch_sales_rate = itembranch_sales_rate
        ic.item_mrp = itemmrp
        ic.item_image = itemimage
        ic.item_description = itemdescription
        ic.item_created_by = request.session['username']
        ic.order_qty_br1 = 0
        ic.order_qty_br1_date = datetime.datetime.now()
        ic.order_qty_br2 = 0
        ic.order_qty_br2_date = datetime.datetime.now()
        ic.order_qty_br3 = 0
        ic.order_qty_br3_date = datetime.datetime.now()
        ic.item_flag = 1
        ic.save()

        icb = branch_1()
        icb.item_name = itemname
        icb.item_uom = itemuom
        icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        icb = branch_2()
        icb.item_name = itemname
        icb.item_uom = itemuom
        icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        icb = branch_3()
        icb.item_name = itemname
        icb.item_uom = itemuom
        icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        def show_items():
            si = item.objects.all()
            return si

        context = {
            'showitem': show_items,
            'iuom': uom.objects.all(),
            'icat': catergory.objects.all(),
            'idep': department.objects.all(),
        }

        messages.info(request, 'Your item has been created successfully!')
        return render(request,'admindashboard/items/view_all_items.html',context)

def view_all_items(request):
    def show_items():
        si=item.objects.all()
        return si
    context={
        'showitem':show_items,
        'name':request.session['username'],
    }
    return render(request, 'admindashboard/items/view_all_items.html',context)

def del_items(request,id):
    dobj=item.objects.filter(id=id)
    dobj.delete()

    dbrobj = consolidated.objects.filter(id=id)
    dbrobj.delete()

    dbrobj=branch_1.objects.filter(id=id)
    dbrobj.delete()
    dbrobj=branch_2.objects.filter(id=id)
    dbrobj.delete()
    dbrobj = branch_3.objects.filter(id=id)
    dbrobj.delete()


    def show_items():
        si = item.objects.all()
        return si

    context = {
        'showitem': show_items
        }
    messages.info(request,'Item deleted Sucessfully!')
    return render(request,'admindashboard/items/view_all_items.html',context)
def update_item_page(request):
    return render(request,'admindashboard/items/update_item.html')

def update_item(request,id):
    if request.method=='POST':
        itemcode = request.POST.get('code')
        print('my item cod is ', itemcode)
        itemname = request.POST.get('name')
        itemuom = request.POST.get('uom')
        itembarcode = request.POST.get('barcode')
        itemcategory = request.POST.get('category')
        itemkitchen = request.POST.get('kitchen')
        itemproduction_cost = request.POST.get('pcost')
        itemsales_rate = request.POST.get('srate')
        itembranch_sales_rate = request.POST.get('bsrate')
        itemmrp = request.POST.get('mrp')
        #itemimage = request.POST.get('itemimages')
        itemimage = request.FILES['itemimages']
        itemdescription = request.POST.get('description')

        ic = item.objects.get(id=id)
        ic.item_code = itemcode
        ic.item_name = itemname
        ic.item_uom = itemuom
        ic.item_barcode = itembarcode
        ic.item_category = itemcategory
        ic.item_kitchen = itemkitchen
        ic.item_production_cost = itemproduction_cost
        ic.item_sales_rate = itemsales_rate
        ic.item_branch_sales_rate = itembranch_sales_rate
        ic.item_mrp = itemmrp
        ic.item_image = itemimage
        ic.item_description = itemdescription
        ic.item_flag = 1
        ic.save()

        ic = consolidated.objects.get(id=id)
        ic.item_code = itemcode
        ic.item_name = itemname
        ic.item_uom = itemuom
        ic.item_barcode = itembarcode
        ic.item_category = itemcategory
        ic.item_kitchen = itemkitchen
        ic.item_production_cost = itemproduction_cost
        ic.item_sales_rate = itemsales_rate
        ic.item_branch_sales_rate = itembranch_sales_rate
        ic.item_mrp = itemmrp
        ic.item_image = itemimage
        ic.item_description = itemdescription
        ic.item_created_by = request.session['username']
        #ic.order_qty_br1 = 0
        ic.order_qty_br1_date = datetime.datetime.now()
        #ic.order_qty_br2 = 0
        ic.order_qty_br2_date = datetime.datetime.now()
        #ic.order_qty_br3 = 0
        ic.order_qty_br3_date = datetime.datetime.now()
        ic.item_flag = 1
        ic.save()

        icb = branch_1.objects.get(id=id)
        icb.item_name = itemname
        icb.item_uom = itemuom
        #icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        icb = branch_2.objects.get(id=id)
        icb.item_name = itemname
        icb.item_uom = itemuom
        #icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        icb = branch_3.objects.get(id=id)
        icb.item_name = itemname
        icb.item_uom = itemuom
        # icb.item_qty = 0
        icb.date_time = datetime.datetime.now()
        icb.updated_by = request.session['username']
        icb.save()

        messages.info(request, 'Your Item has been updated successfully!')
        return view_all_items(request)
    itema = item.objects.get(id=id)

    def show_items():
        si = item.objects.all()
        return si

    return render(request,'admindashboard/items/update_item.html',context={'sd':itema,'showitem': show_items(),'iuom': uom.objects.all(),'icat': catergory.objects.all(),'idep': department.objects.all()})






###********* ITEM CREATION END HERE *************
###********* CATEGORY CREATION END HERE *************

def create_category(request):
    return render(request,'admindashboard/category/create_category.html')

def category_regi(request):
    cat=request.POST.get('category')
    cc=catergory()
    cc.catergory_name=cat
    cc.catergory_created_by=request.session['username']
    cc.catergory_flag=1
    cc.save()
    context = {
        'cat': catergory.objects.all(),
    }

    return render(request,'admindashboard/category/view_all_catergory.html',context)

def view_all_catergory(request):
    context={
        'cat':catergory.objects.all(),
    }
    return render(request,'admindashboard/category/view_all_catergory.html',context)

def catergory_delete(request,id):
    cd=catergory.objects.get(id=id)
    cd.delete()
    context = {
        'cat': catergory.objects.all(),
    }
    return render(request, 'admindashboard/category/view_all_catergory.html', context)

def update_category(request,id):
    if request.method == 'POST':
        cat = request.POST.get('category')
        cc = catergory.objects.get(id=id)
        cc.catergory_name = cat
        cc.catergory_created_by = request.session['username']
        cc.catergory_flag = 1
        cc.save()
        return view_all_catergory(request)

    context = {
        'cd':catergory.objects.get(id=id),
        'cat': catergory.objects.all(),
    }
    return render(request,'admindashboard/category/update_category.html',context)
###********* CATEGORY CREATION END HERE *************
###********* Department CREATION START HERE *************

def create_department(request):
    return render(request,'admindashboard/department/create_department.html')

def department_regi(request):
    cat=request.POST.get('category')
    cc=department()
    cc.department_name=cat
    cc.department_created_by=request.session['username']
    cc.department_flag=1
    cc.save()
    context = {
        'cat': department.objects.all(),
    }

    return render(request,'admindashboard/department/view_all_department.html',context)

def view_all_department(request):
    context={
        'cat':department.objects.all(),
    }
    return render(request,'admindashboard/department/view_all_department.html',context)

def department_delete(request,id):
    cd=department.objects.get(id=id)
    cd.delete()
    context = {
        'cat': department.objects.all(),
    }
    return render(request, 'admindashboard/department/view_all_department.html', context)

def department_update(request,id):
    if request.method=='POST':
        cat=request.POST.get('category')
        cc=department.objects.get(id=id)
        cc.department_name=cat
        cc.department_created_by=request.session['username']
        cc.department_flag=1
        cc.save()
        return view_all_department (request)
    context = {
        'cd':department.objects.get(id=id),
        'cat': department.objects.all(),
    }

    return render(request,'admindashboard/department/update_department.html',context)


###********* Department CREATION END HERE *************
###********* UOM CREATION START HERE *************

def create_uom(request):
    return render(request,'admindashboard/uom/create_uom.html')

def uom_regi(request):
    cat=request.POST.get('category')
    cc=uom()
    cc.uom_name=cat
    cc.uom_created_by=request.session['username']
    cc.uom_flag=1
    cc.save()
    context = {
        'cat': uom.objects.all(),
    }

    return render(request,'admindashboard/uom/view_all_uom.html',context)

def view_all_uom(request):
    context={
        'cat':uom.objects.all(),
    }
    return render(request,'admindashboard/uom/view_all_uom.html',context)

def uom_delete(request,id):
    cd=uom.objects.get(id=id)
    cd.delete()
    context = {
        'cat': uom.objects.all(),
    }
    return render(request, 'admindashboard/uom/view_all_uom.html', context)

def uom_update(request,id):
    if request.method=='POST':
        cat=request.POST.get('category')
        cc=uom.objects.get(id=id)
        cc.uom_name=cat
        cc.uom_created_by=request.session['username']
        cc.uom_flag=1
        cc.save()
        return view_all_uom (request)
    context = {
        'cd':uom.objects.get(id=id),
        'cat': uom.objects.all(),
    }

    return render(request,'admindashboard/uom/update_uom.html',context)

###********* UOM CREATION END HERE *************
###********* BRANCH CREATION END HERE *************

def branch_creation_page(request):
    return render(request,'admindashboard/branch/branch_creation.html')

def branch_cration(request):
    if request.method=='POST':
        branchcode=request.POST.get('code')
        branchname=request.POST.get('name')
        branchdescripiton=request.POST.get('description')

        bc=branch()
        bc.branch_code = branchcode
        bc.branch_name = branchname
        bc.branch_description = branchdescripiton
        bc.branch_created_by = request.session['username']
        bc.branch_flag = 1
        bc.save()

    name=request.session['username']
    iname=request.POST.get('name')
    messages.info(request,str(name) +' You successfully created created the Branch named ' + str(iname))
    return render(request,'admindashboard/branch/branch_creation.html')

def view_all_branch(request):
    context={
        'branch':branch.objects.all(),
    }
    return render(request,'admindashboard/branch/view_all_branch.html',context)

def branch_update(request,id):
    if request.method=='POST':
        branchcode=request.POST.get('code')
        branchname=request.POST.get('name')
        branchdescripiton=request.POST.get('description')

        bc=branch.objects.get(id=id)
        bc.branch_code = branchcode
        bc.branch_name = branchname
        bc.branch_description = branchdescripiton
        bc.branch_created_by = request.session['username']
        bc.branch_flag = 1
        bc.save()
        messages.info(request,'branch updated succesfully')
        return view_all_branch(request)
    context={
        'bcu':branch.objects.get(id=id),
        'branch': branch.objects.all(),
    }
    return render(request,'admindashboard/branch/update_branch.html',context)

###********* BRANCH CREATION END HERE *************

###********* CONSOLIDATED ORDER START HERE *************

def consolidated_order(request):
    tu = user.objects.all()
    tus = len(tu)
    tb = branch.objects.all()
    tbs = len(tb)
    ti = item.objects.all()
    tis = len(ti)

    context={
        'conord':branch.objects.all(),
        'viewitem':item.objects.all().filter(item_flag=1),
        'br1':branch_1.objects.all(),
        'br2':branch_2.objects.all(),
        'con':consolidated.objects.all(),
        'dt': datetime.date.today(),
        'tu': tus,
        'tb': tbs,
        'ti': tis,
        'name':request.session['username'],
        }
    return render(request,'admindashboard/orders/consolidated_order.html',context)

def consolidated_order2(request):
    context = {
        'conord': branch.objects.all(),
        'viewitem': item.objects.all().filter(item_flag=1),
        'br1': branch_1.objects.all(),
        'br2': branch_2.objects.all(),
        'con': consolidated.objects.all(),
        'dt': datetime.date.today(),
    }
    return render(request,'admindashboard/orders/consolidated_order2.html',context)

###********* CONSOLIDATED ORDER END HERE *************

###********* REPORTS ORDER END HERE *************

def department_wise(request):
    kit=request.POST.get('kitchen')
    context={
        'con': consolidated.objects.all(),
        'conord': branch.objects.all(),
        'idep': department.objects.all(),
    }
    return render(request,'admindashboard/reports/department_wise.html',context)
def department_wises(request):
    kit=request.POST.get('kitchen')
    print('this ism y kit',kit)
    context={
        'con': consolidated.objects.all().filter(item_kitchen=kit),
        'kitc':kit,
        'conord': branch.objects.all(),
        'idep':department.objects.all(),

    }
    return render(request,'admindashboard/reports/department_wise.html',context)

#*********PRODUCTION REPORTS START HERE **************

def production_home(request):
    tu = user.objects.all()
    tus = len(tu)
    tb = branch.objects.all()
    tbs = len(tb)
    ti = item.objects.all()
    tis = len(ti)

    context={
        'conord':branch.objects.all(),
        'viewitem':item.objects.all().filter(item_flag=1),
        'br1':branch_1.objects.all(),
        'br2':branch_2.objects.all(),
        'con':consolidated.objects.all(),
        'dt': datetime.date.today(),
        'tu': tus,
        'tb': tbs,
        'ti': tis,
        }
    return render(request,'admindashboard/reports/production/production_home.html',context)

def total_order(request):
    tu = user.objects.all()
    tus = len(tu)
    tb = branch.objects.all()
    tbs = len(tb)
    ti = item.objects.all()
    tis = len(ti)
    context = {
        'conord': branch.objects.all(),
        'viewitem': item.objects.all().filter(item_flag=1),
        'br1': branch_1.objects.all(),
        'br2': branch_2.objects.all(),
        'con': consolidated.objects.all(),
        'dt': datetime.date.today(),
        'tu': tus,
        'tb': tbs,
        'ti': tis,
    }
    return render(request,'admindashboard/reports/production/total_order.html',context)

def pro_department_wises(request):
    kit=request.POST.get('kitchen')
    print('this ism y kit',kit)
    tu = user.objects.all()
    tus = len(tu)
    tb = branch.objects.all()
    tbs = len(tb)
    ti = item.objects.all()
    tis = len(ti)
    context={
        'con': consolidated.objects.all().filter(item_kitchen=kit),
        'kitc':kit,
        'conord': branch.objects.all(),
        'tu': tus,
        'tb': tbs,
        'ti': tis,
        'idep': department.objects.all(),

    }
    return render(request,'admindashboard/reports/production/pro_department_wise.html',context)

#*********PRODUCTION REPORTS START HERE **************

#*********DESPATH REPORTS START HERE **************

def des_br1_rep(request):
    br=request.POST.get('bran')
    ti = item.objects.all()
    tis = len(ti)

    to=branch_1.objects.filter(item_qty__gt = 0)
    tto = len(to)
    tu = branch_1.objects.filter(item_qty=0)
    ttu = len(tu)

    context={
        'brre':branch_1.objects.all(),
        'kitc':br,
        'ti': tis,
        'to':tto,
        'tu': ttu,
    }
    return render(request,'admindashboard/reports/despatch/br1.html',context)

def des_br2_rep(request):
    br=request.POST.get('bran')
    ti = item.objects.all()
    tis = len(ti)

    to = branch_2.objects.filter(item_qty__gt=0)
    tto = len(to)
    tu = branch_2.objects.filter(item_qty=0)
    ttu = len(tu)

    context={
        'brre':branch_2.objects.all(),
        'kitc':br,
        'ti': tis,
        'to': tto,
        'tu': ttu,
    }
    return render(request,'admindashboard/reports/despatch/br2.html',context)


def des_br3_rep(request):
    br=request.POST.get('bran')
    ti = item.objects.all()
    tis = len(ti)

    to = branch_3.objects.filter(item_qty__gt=0)
    tto = len(to)
    tu = branch_3.objects.filter(item_qty=0)
    ttu = len(tu)

    context={
        'brre':branch_3.objects.all(),
        'kitc':br,
        'ti': tis,
        'to': tto,
        'tu': ttu,
    }
    return render(request,'admindashboard/reports/despatch/br3.html',context)

#*********DESPATH REPORTS END HERE **************

###********* REPORTS ORDER END HERE *************


###********************************************* ALL BRANCH START HERE *************
###********* BRANCH1 START HERE *************

def br1_order_page(request):
    context={
        'items':branch_1.objects.all()
    }
    return render(request,'branches/branch1/br1_order_page.html',context)

def br1_order_update(request,id):
    if request.method=='POST':
        br1_qty=request.POST.get('brqty')
        br1q=branch_1.objects.get(id=id)
        br1q.item_qty=br1_qty
        br1q.date_time=datetime.datetime.now()
        br1q.updated_by=request.session['username']
        br1q.save()

        br1q = consolidated.objects.get(id=id)
        br1q.order_qty_br1 = br1_qty

        br1q.order_qty_br1_date = datetime.date.today()
        br1q.save()

        #messages.info(request, 'Your Item has been ORDERED successfully!')
        return br1_order_page(request)

    itema = branch_1.objects.get(id=id)
    def show_items():
        si = branch_1.objects.all()
        return si
    dt=datetime.date.today()
    print(dt)
    return render(request,'branches/branch1/br_order_update.html', context={'sd': itema, 'items': show_items(),'dt':datetime.date.today()})

def copit(request):
    t1 = branch_1.objects.filter(item_name=True)
    for i in t1.values():
        print('his is my iii',i)
        qt=branch_2.objects.create(item_qty=10)
        #entry.branch_2.add(qt)

    context={
        'items':branch_1.objects.all()
    }

    return render(request, 'branches/branch1/br1_order_page.html', context)



###********* BRANCH1 END HERE *************
###********* BRANCH2 START HERE *************

def br2_order_page(request):
    context={
        'items':branch_2.objects.all()
    }
    return render(request,'branches/branch2/br2_order_page.html',context)

def br2_order_update(request,id):
    if request.method=='POST':
        br1_qty=request.POST.get('brqty')
        br1q=branch_2.objects.get(id=id)
        br1q.item_qty=br1_qty
        br1q.date_time=datetime.datetime.now()
        br1q.updated_by=request.session['username']
        br1q.save()

        br1q = consolidated.objects.get(id=id)
        br1q.order_qty_br2 = br1_qty

        br1q.order_qty_br2_date = datetime.date.today()
        br1q.save()

        #messages.info(request, 'Your Item has been ORDERED successfully!')
        return br2_order_page(request)

    itema = branch_2.objects.get(id=id)
    def show_items():
        si = branch_2.objects.all()
        return si
    dt=datetime.date.today()
    print(dt)
    return render(request,'branches/branch2/br2_order_update.html', context={'sd': itema, 'items': show_items(),'dt':datetime.date.today()})

###********* BRANCH2 END HERE *************
###********* BRANCH3 START HERE *************

def br3_order_page(request):
    context={
        'items':branch_3.objects.all()
    }
    return render(request,'branches/branch3/br3_order_page.html',context)

def br3_order_update(request,id):
    if request.method=='POST':
        br1_qty=request.POST.get('brqty')
        br1q=branch_3.objects.get(id=id)
        br1q.item_qty=br1_qty
        br1q.date_time=datetime.datetime.now()
        br1q.updated_by=request.session['username']
        br1q.save()

        br1q = consolidated.objects.get(id=id)
        br1q.order_qty_br3 = br1_qty

        #br1q.order_qty_br3_date = datetime.date.today()
        br1q.save()

        #messages.info(request, 'Your Item has been ORDERED successfully!')
        return br3_order_page(request)

    itema = branch_3.objects.get(id=id)
    def show_items():
        si = branch_3.objects.all()
        return si
    dt=datetime.date.today()
    print(dt)
    return render(request,'branches/branch3/br3_order_update.html', context={'sd': itema, 'items': show_items(),'dt':datetime.date.today()})

###********* BRANCH3 END HERE *************
###******************************************** ALL BRANCH END HERE *************


#**** logout start here

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request,'login.html')

#**** logout end here


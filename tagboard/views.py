from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import LocTags,PartTags,Users,Locations
from . import forms
from django.views.decorators.csrf import csrf_protect
import sqlite3, string

# Create your views here.
@csrf_protect
def LocTagPage(request):
    query_request = LocTags.objects.all().order_by('tagname')
    return(render(request,'loctagboard.html',{'obj': query_request}))


def PartTagPage(request):
    query_set = PartTags.objects.all().order_by('tagname')
    return(render(request,'parttagboard.html',{'object': query_set}))

def HomePage(request):
    return(render(request,'taghome.html'))

def addLocTag(request):
    form = forms.LocTagForm()
    return(render(request,"addlt.html",{"form":form}))

def addPartTag(request):
    form = forms.PartTagForm()
    return(render(request,"addpt.html",{"form":form}))

def NewLocTag(request):
    if(request.method == "POST"):
        f = forms.LocTagForm(request.POST)
        if(f.validate()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('Insert into tagboard_loctags values(?);',(f.cleaned_data['tagname'],))
            conn.commit()
            conn.close()
        else:
            f = forms.LocTagForm()
            return(render(request,"addlt.html",{"form":f,"ErrorMessage":"already existing tag"}))
    else:
        f = forms.LocTagForm()
        return(render(request,'addlt.html',{"form":f}))
    return(LocTagPage(request))

def NewPartTag(request):
    if(request.method == "POST"):
        f = forms.PartTagForm(request.POST)
        if(f.validate()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('Insert into tagboard_parttags values(?);',(f.cleaned_data['tagname'],))
            conn.commit()
            conn.close()
        else:
            f = forms.PartTagForm()
            return(render(request,"addpt.html",{"form":f,"ErrorMessage":"already existing tag"}))
    else:
        f = forms.PartTagForm()
        return(render(request,'addpt.html',{"form":f}))
    return(PartTagPage(request))


def EditUserTags(request,error=''):
    all_users = Users.objects.all()
    return(render(request,'showusers.html',{'users':all_users,'error':error}))

def ModifyUser(request):
   if(request.method=="POST"):
        f = forms.EditUserTagForm(request.POST)
        tags = ''.join(f.retrieveTag())
        if(tags is None):
            error = "No such user exists"
            return(EditUserTags(request,error))
        else:
            taglist = tags.split(',')
            taglist.sort()
            return(render(request,'modut.html',{'tags':taglist,"uid":request.POST.get('uid')}))


def DeleteTag(request):
    if(request.method=="POST"):
        f = forms.DeleteTagForm(request.POST)
        if(f.is_valid()):
            d = request.POST.get('uid')
            t = request.POST.get('tag')
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('select tags from tagboard_users where uid = ?;',(d,))
            row = cur.fetchone()
            s = ''.join(row)
            l = s.split(',')
            l.sort()
            s = ''
            for entry in l:
                if(entry != t):
                    s += ','+entry
                    if(s[0] == ','):
                        s = s[1:]
            cur.execute('update tagboard_users set tags = ? where uid = ?;',(s,d,))
            conn.commit()
            conn.close()
            return(ModifyUser(request))


def AddUserTag(request,error=''):
    if(request.method=="POST"):
        return(render(request,'addut.html',{'uid':request.POST.get('uid'),'ErrorMessage':error}))


def AddUTag(request):
    if(request.method=='POST'):
        f = forms.AddTagForm(request.POST)
        s = f.retrieveTags()
        if(s is not None):
            s = ''.join(s)
            l = s.split(',')
            l.sort()
            t = request.POST.get('tag')
            u = request.POST.get('uid')
            if(t in l):
                return(AddUserTag(request,'The tag already exists'))
            else:
                s += ','+t
                if(s[0] == ','):
                    s = s[1:]
                conn = sqlite3.connect('db.sqlite3')
                cur = conn.cursor()
                cur.execute('update tagboard_users set tags = ? where uid = ?;',(s,u,))
                conn.commit()
                conn.close()
                return(AddUserTag(request,'Tag Successfully Added'))

def DelLocTag(request):
    if(request.method=="POST"):
        delTag = request.POST.get('tagname')
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute('delete from tagboard_loctags where tagname=?;',(delTag,))
        conn.commit()
        conn.close()
        return(LocTagPage(request))

def DelPartTag(request):
    if(request.method=="POST"):
        delTag = request.POST.get('tagname')
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute('delete from tagboard_parttags where tagname=?;',(delTag,))
        conn.commit()
        conn.close()
        return(PartTagPage(request))


def EditLocTags(request,error=''):
    all_locations = Locations.objects.all()
    return(render(request,'showlocs.html',{'locations':all_locations,'error':error}))

def ModifyLoc(request):
   if(request.method=="POST"):
        f = forms.EditLocTagForm(request.POST)
        tags = ''.join(f.retrieveTag())
        if(tags is None):
            error = "No such location exists"
            return(EditLocTags(request,error))
        else:
            taglist = tags.split(',')
            taglist.sort()
            return(render(request,'modlt.html',{'tags':taglist,"locname":request.POST.get('locname')}))


def AddLocTag(request,error=''):
    if(request.method=="POST"):
        return(render(request,'addloct.html',{'locname':request.POST.get('locname'),'ErrorMessage':error}))


def DeleteLocTag(request):
    if(request.method=="POST"):
        f = forms.DeleteLocTagForm(request.POST)
        if(f.is_valid()):
            d = request.POST.get('locname')
            t = request.POST.get('tag')
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute('select tags from tagboard_locations where locname = ?;',(d,))
            row = cur.fetchone()
            s = ''.join(row)
            l = s.split(',')
            l.sort()
            s = ''
            for entry in l:
                if(entry != t):
                    s += ','+entry
                    if(s[0] == ','):
                        s = s[1:]
            cur.execute('update tagboard_locations set tags = ? where locname = ?;',(s,d,))
            conn.commit()
            conn.close()
            return(ModifyLoc(request))

def AddLTag(request):
    if(request.method=='POST'):
        f = forms.AddLocTagForm(request.POST)
        s = f.retrieveTags()
        if(s is not None):
            l = s.split(',')
            l.sort()
            t = request.POST.get('tag')
            u = request.POST.get('locname')
            if(t in l):
                return(AddLocTag(request,'The tag already exists'))
            else:
                s += ','+t
                if(s[0] == ','):
                    s = s[1:]
                conn = sqlite3.connect('db.sqlite3')
                cur = conn.cursor()
                cur.execute('update tagboard_locations set tags = ? where locname = ?;',(s,u,))
                conn.commit()
                conn.close()
                return(AddLocTag(request,'Tag Successfully Added'))

def SearchPage(request):
    if(request.method == "POST"):
        f = forms.SearchForm(request.POST)
        if(f.is_valid()):
            tn = request.POST.get('tablename')
            s = request.POST.get('searchtag')
            if(tn == 'loc_name'):
                query = Locations.objects.filter(locname=s)
                return(render(request,'showlocs.html',{'locations':query,'error':''}))
            elif(tn == 'user_id'):
                query = Users.objects.filter(uid=s)
                return(render(request,'showusers.html',{'users':query,'error':''}))
            elif(tn == 'ptb'):
                query = PartTags.objects.filter(tagname=s).values_list('tagname',flat=True)
                return(render(request,'parttagboard.html',{'obj':query}))
            elif(tn == 'ltb'):
                query = LocTags.objects.filter(tagname=s).values_list('tagname',flat=True)
                return(render(request,'loctagboard.html',{'obj':query}))




def EventStep1(request):
    if(request.method == "POST"):
        f = forms.Step1Form(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('eedate')
            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'eedate':f8}

            #conn = sqlite3.connect('db.sqlite3')
            #cur = conn.cursor()
            #cur.execute('insert into tablename(ename,esdate,estime,eetime) values(?,?,?,?);',(f2['ename'],f2['esdate'],f2['estime'],f2['eetime'],))
            #conn.commit()

            return(render(request,'tables.html',args))

    #return(HttpResponse("you have reached here"))

def EventBooking1(request):
    return(render(request,'eventbooking.html'))

def EventBooking2(request):
    return(render(request,'tables.html'))

def plist(request):
    return render(request,'plist.html')

def EventStep2(request):
    if(request.method == "POST"):
        f = forms.Step2Form(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('etag')
            f9 = request.POST.get('eedate')

            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'etag':f8,'eedate':f9}

            return(render(request,'permission.html',args))

def EventStep3(request):
    if(request.method == "POST"):
        f = forms.Step3Form(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('eedate')
            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'eedate':f8}
            return(render(request,'final.html',args))

def EventStep4(request):
    if(request.method == 'POST'):
        f = forms.Step4Form(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('eedate')
            f9 = request.POST.get('p3tag')
            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'eedate':f8,'p3tag':f9}

            return(render(request,'plist.html',args))

def EventStep5(request):
    if(request.method == 'POST'):
        f = forms.Step5Form(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('eedate')
            f9 = request.POST.get('ptag')
            f10 = request.POST.get('p3tag')
            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'eedate':f8,'ptag':f9,'p3tag':f10}
            return(render(request,'final.html',args))

def people(request):
    if(request.method == 'POST'):
        f = forms.People(request.POST)
        if(f.is_valid()):
            f1 = request.POST.get('ename')
            f2 = request.POST.get('esdate')
            f3 = request.POST.get('estime')
            f4 = request.POST.get('eetime')
            f5 = request.POST.get('cname')
            f6 = request.POST.get('pno')
            f7 = request.POST.get('eid')
            f8 = request.POST.get('eedate')
            args = {'ename':f1,'esdate':f2,'estime':f3,'eetime':f4,'cname':f5,'pno':f6,'eid':f7,'eedate':f8}
            return(render(request,'people.html',args))

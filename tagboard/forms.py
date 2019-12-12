from django import forms
from django.shortcuts import render
import sqlite3
class PartTagForm(forms.Form):
    tagname = forms.CharField(max_length=50, required=True)
    def validate(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            data = self.cleaned_data['tagname']
            cur.execute('select * from tagboard_parttags where tagname = ?;',(data,))
            rows = cur.fetchone()
            if(rows is None):
                return(True)
            else:
                return(False)
class LocTagForm(forms.Form):
    tagname = forms.CharField(max_length=50, required=True)
    def validate(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            data = self.cleaned_data['tagname']
            cur.execute('select * from tagboard_loctags where tagname = ?;',(data,))
            rows = cur.fetchone()
            if(rows is None):
                return(True)
            else:
                return(False)

class EditUserTagForm(forms.Form):
    uid = forms.CharField(max_length=50, required=True)
    def retrieveTag(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            data = self.cleaned_data['uid']
            cur.execute('select tags from tagboard_users where uid = ?;',(data,))
            row = cur.fetchone()
            return(row)


class DeleteTagForm(forms.Form):
    uid = forms.CharField(max_length=50)
    tag = forms.CharField()

class DeleteLocTagForm(forms.Form):
    locname = forms.CharField(max_length=50)
    tag = forms.CharField()

class AddTagForm(forms.Form):
    uid = forms.CharField(max_length=50)
    tag = forms.CharField()

    def retrieveTags(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cd = self.cleaned_data
            uid = cd['uid']
            tag = cd['tag']
            cur.execute('select tags from tagboard_users where uid = ?;',(uid,))
            res = cur.fetchone()
            s = ''.join(res,)
            return(s)

class EditLocTagForm(forms.Form):
    locname = forms.CharField(max_length=50, required=True)
    def retrieveTag(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            data = self.cleaned_data['locname']
            cur.execute('select tags from tagboard_locations where locname = ?;',(data,))
            row = cur.fetchone()
            return(row)


class AddLocTagForm(forms.Form):
    locname = forms.CharField(max_length=50)
    tag = forms.CharField()

    def retrieveTags(self):
        if(self.is_valid()):
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cd = self.cleaned_data
            locname = cd['locname']
            tag = cd['tag']
            cur.execute('select tags from tagboard_locations where locname = ?;',(locname,))
            res = cur.fetchone()
            s = ''.join(res,)
            return(s)

class SearchForm(forms.Form):
    searchtag = forms.CharField()
    tablename = forms.CharField()


class Step1Form(forms.Form):
    ename = forms.TextInput()
    esdate = forms.DateInput()
    estime = forms.TimeInput()
    eetime = forms.TimeInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()

class Step2Form(forms.Form):
    etag = forms.CheckboxInput()
    ename = forms.HiddenInput()
    esdate = forms.HiddenInput()
    estime = forms.HiddenInput()
    eetime = forms.HiddenInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()

class Step3Form(forms.Form):
    ename = forms.HiddenInput()
    esdate = forms.HiddenInput()
    estime = forms.HiddenInput()
    eetime = forms.HiddenInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()

class Step4Form(forms.Form):
    p3tag = forms.HiddenInput()
    ename = forms.HiddenInput()
    esdate = forms.HiddenInput()
    estime = forms.HiddenInput()
    eetime = forms.HiddenInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()

class Step5Form(forms.Form):
    ename = forms.HiddenInput()
    esdate = forms.HiddenInput()
    estime = forms.HiddenInput()
    eetime = forms.HiddenInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()
    p3tag = forms.HiddenInput()
    ptag = forms.CheckboxInput()

class People(forms.Form):
    ename = forms.HiddenInput()
    esdate = forms.HiddenInput()
    estime = forms.HiddenInput()
    eetime = forms.HiddenInput()
    cname = forms.TextInput()
    pno = forms.NumberInput()
    eid = forms.EmailField()
    eedate = forms.DateField()

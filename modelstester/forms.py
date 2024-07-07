from django import forms
class school_form(forms.Form):
    # too delete from database
    # a = student.objects.all()
    # b = a[0].name
    # print(b)
    # student.objects.filter(name = b).delete()
    name = forms.CharField()


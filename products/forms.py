from django import forms



class UploadFileForm(forms.Form):
    file  = forms.FileField()
    description = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'rows':3}))
    price = forms.FloatField()
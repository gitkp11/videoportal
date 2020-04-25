from django import forms


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()


class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
    video = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

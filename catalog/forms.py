# не нужные формы
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SomeForm(forms.Form):
    foo = forms.TextField(widget=SummernoteWidget())

class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())

class FormFromBookModel(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }

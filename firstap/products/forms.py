from django import forms
from .models import Product
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'name',
			'category',
			'featured',
			'img',
		]

# class SomeForm(forms.Form):
#     foo = forms.CharField(widget=SummernoteWidget())

# class AnotherForm(forms.Form):
#     bar = forms.CharField(widget=SummernoteInplaceWidget())

# class FormFromProductModel(forms.ModelForm):
#     class Meta:
#         model = Product
#         widgets = {
#             'foo': SummernoteWidget(),
#             'bar': SummernoteInplaceWidget(),
        # }
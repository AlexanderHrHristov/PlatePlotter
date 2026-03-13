from django import forms
from .models import Store, Product, Inventory


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Продукт'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Mарка/Производител'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Цена на продукта'}),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'


class InventoryEditForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].disabled = True


class DeleteProductForm(forms.Form):
    confirm = forms.BooleanField(label='Потвърди изтриването на продукта')
    
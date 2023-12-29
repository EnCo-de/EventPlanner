from django import forms
from .models import Order, Entertainment


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  ['real', 'shows', 'category', 'venue', 'date', 'budget_min', 'budget_max', 'participants', 'children', 'corporate', 'company', 'details']
        """ labels = {
            'date': '15/01/2023 12:34',
        } """

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'shows':
                field.widget.attrs['class'] = 'form-select form-select-lg mb-2'
            elif name in ['children', 'corporate']:
                field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                field.widget.attrs['class'] = 'form-control mb-2'
        self.fields.get('date').widget.attrs['placeholder'] = '25.12.23 15:30'
        self.fields.get('date').input_formats = ['%d.%m.%y', '%d.%m.%y %H:%M', '%d/%m/%y', '%d/%m/%y %H:%M', '%d/%m/%Y', '%d/%m/%Y %H:%M', '%d-%m-%y', '%d-%m-%y %H:%M', '%d-%m-%y %H:%M:%S', '%d-%m-%Y', '%d-%m-%Y %H:%M', '%d-%m-%Y %H:%M:%S',]
        
    error_css_class = "is-invalid"
    # required_css_class = "required"

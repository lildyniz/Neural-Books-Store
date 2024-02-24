from django import forms

# BOOK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# class CartAddProductForm(forms.Form):
#     # quantity = forms.TypedChoiceField(choices=BOOK_QUANTITY_CHOICES,
#     #                                   coerce=int)
#     quantity = 1
#     override = forms.BooleanField(required=False,
#                                   initial=False,
#                                   widget=forms.HiddenInput)

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=20)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

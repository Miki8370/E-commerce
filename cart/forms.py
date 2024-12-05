from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int #coerce is an argument used primarily in form fields to specify a function that converts (or "coerces") input data into a desired type.
    )

    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    ) 
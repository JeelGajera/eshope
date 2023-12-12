from django import forms

from .models import Item

INPUT_CLASS = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
                }),
            'name': forms.TextInput(attrs={
                'placeholder': 'type your item name',
                'is_required': True,
                'class': INPUT_CLASS
                }),
            'description': forms.Textarea(attrs={
                'placeholder': 'type your item description',
                'is_required': True,
                'class': INPUT_CLASS
                }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'enter your item price',
                'is_required': True,
                'class': INPUT_CLASS
                }),
            'image': forms.FileInput(attrs={
                'is_required': True,
                'class': INPUT_CLASS
                }),
        }
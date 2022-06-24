from django import forms
from .models import Product, Category
from rest_framework.response import Response
from django.db import IntegrityError, transaction
from menucode.serializers import CategorySeriliazer
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'placementId']

    
 

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    
   
    def save_model(self, request, obj, form, change):
        placementId = form.cleaned_data.get('placementId')
        
        if placementId > 0:
            print(f"İsmi: {obj} +  + {form.cleaned_data.get('placementId')} ++ {obj.pk}")
            allCategory = Category.objects.all()
            for categories in allCategory:
                if placementId == categories.placementId:
                    categoryExists = Category.objects.get(placementId=placementId)
                    categoryExists.placementId = obj.placementId
                    obj.placementId = placementId
                    categoryExists.save()
                    return obj.save(update_fields=['placementId', 'name'])
                    
                else:
                    obj.placementId = placementId
                    return obj.save(update_fields=['placementId', 'name'])
    def clean(self):
        data = super().clean()
        cleaned_data = self.cleaned_data
        placementId = cleaned_data.get('placementId')
        name = cleaned_data.get('name')
        if name == None:
            raise forms.ValidationError(u"Lütfen kategori ismi giriniz.")
        
        if placementId == None:
            raise forms.ValidationError(u"Lütfen sıralama numarası giriniz.")
        else:
            try:
                with transaction.atomic():
                    allCategory = Category.objects.all()
                    for categories in allCategory:
                        if placementId == categories.placementId:
                            categoryExists = Category.objects.get(placementId=placementId)
                            if categoryExists:
                                obj = Category.objects.get(name=data['name'])
                                categoryExists.placementId = obj.placementId
                                obj.placementId = placementId
                                obj.name = name
                                categoryExists.save()
                                return obj.save(update_fields=['placementId', 'name'])
                        elif placementId != categories.placementId and name == categories.name:
                            existCategory = Category.objects.get(name=data['name'])
                            if existCategory:
                                 existCategory.placementId = placementId
                                 existCategory.name = name
                                 return existCategory.save(update_fields=['placementId', 'name'])
                        elif placementId != categories.placementId and name != categories.name:
                            existCategories = Category.objects.get(placementId=categories.placementId)
                            changeCategories = Category.objects.get(placementId=placementId)
                            changeCategories.placementId = categories.placementId
                            existCategories.placementId = placementId
                            existCategories.name = name
                            changeCategories.save()
                            return existCategories.save(update_fields=['placementId', 'name'])
                        else:
                             categoryExists = Category.objects.get(placementId=placementId)

                             oldCategory = Category.objects.get(name=data['name'])
                             categoryExists.placementId = oldCategory.placementId
                             oldCategory.placementId = placementId
                             oldCategory.name = name
                             categoryExists.save()
                             
                             return oldCategory.save(update_fields=['placementId', 'name'])

                self.fail("Bir hata oluştu.Lütfen Tekrar deneyiniz!")
            except IntegrityError:
                pass
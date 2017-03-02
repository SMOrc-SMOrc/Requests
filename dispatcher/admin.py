from django.contrib import admin
from .models import Client, LabRequest, MedCenRequest, ReqCategory, Delivery


class ClientList (admin.ModelAdmin):

    list_display = ('last_name', 'first_name', 'middle_name', 'birthday')


class LabRequestList (admin.ModelAdmin):

    list_display = ('client', 'serial_number', 'category', 'create_date', 'modify_date', 'delete_date' )


class MedCenRequestList (admin.ModelAdmin):

    list_display = ('client', 'serial_number', 'category', 'req_delivery', 'create_date', 'modify_date', 'delete_date')


class ReqCategoryList (admin.ModelAdmin):

    list_display = ('title',)


class DeliveryList (admin.ModelAdmin):

    list_display = ('address', 'delivery_method', 'date_of')


admin.site.register(Client, ClientList)
admin.site.register(LabRequest, LabRequestList)
admin.site.register(MedCenRequest, MedCenRequestList)
admin.site.register(ReqCategory, ReqCategoryList)
admin.site.register(Delivery, DeliveryList)
# Register your models here.

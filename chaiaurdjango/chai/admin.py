from django.contrib import admin  #type:ignore

from .models import chaiverity,chaiReview,chaiCertificate,store

# Register your models here.

class chaiReviewsinline(admin.TabularInline):
    model = chaiReview
    extra = 2
class chaiverityadmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'date_added','price')
    inlines= [chaiReviewsinline]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varaities',)

class chaicertificateadmin(admin.ModelAdmin):
    list_display = ('chai' , 'certificate_no' , 'issued_date' )

admin.site.register(chaiverity, chaiverityadmin)
admin.site.register(store, storeAdmin)
admin.site.register(chaiCertificate, chaicertificateadmin)
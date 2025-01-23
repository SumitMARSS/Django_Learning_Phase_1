from django.contrib import admin
from .models import ChaiVarity, ChaiCertificate, ChaiReview, Store


# Register your models here.

class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVerifyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInLine]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities', )

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certifiate_number')

admin.site.register(ChaiVarity, ChaiVerifyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)

 
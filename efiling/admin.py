from django.contrib import admin
from import_export.admin import ImportExportMixin
from efiling.models import Documentations, Party
# Register your models here.

@admin.register(Documentations)
class AdminDoc(ImportExportMixin, admin.ModelAdmin):
    fields = (
        'document_number', 'document_purpose', 'document_author',
        'document_parties', 'document_date', 'document_upload',
        'document_requestor',
    )

    list_display = (
        'document_number', 'document_purpose', 'document_author',
        'document_parties', 'document_date', 'document_upload',
        'document_requestor',
    )

    date_hierarchy ='document_date'

    search_fields = (
        'document_number',
    )

@admin.register(Party)
class Adminparty(ImportExportMixin, admin.ModelAdmin):
    fields = (
        'party_initials', 'party_name',
    )

    list_display = (
        'party_initials', 'party_name',
    )

    search_fields = (
        'party_initials', 'party_name',
    )
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

# Register your models here.
class Party(models.Model):
    party_name = models.CharField(_('Parties Name'), max_length=50, default='-', blank=True, null=True)
    party_initials = models.CharField(_('Parties Initials'), max_length=10, default='-', blank=True, null=True)

    class Meta:
        verbose_name = _('The Parties')
        verbose_name_plural = _('The Parties')
        ordering = ['party_name']

    def __str__(self):
        return (f'{self.party_initials} | {self.party_name}')

class Documentations(models.Model):
    document_number = models.CharField(_('List Number'), max_length=50, blank=True, null=True)
    document_purpose = models.CharField(_('Document Purpose'), max_length=300, blank=True, null=True)
    document_author = models.CharField(_('Author'), max_length=30, blank=True, null=True, default='BUMANIK')
    document_parties = models.ForeignKey(Party, on_delete=models.CASCADE, blank=True, null=True)
    document_date = models.DateField(_('Document Date'), null=True, blank=True)
    document_upload = models.FileField(upload_to='files', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
    document_requestor = models.CharField(_('Requested By'), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _('Archive')
        verbose_name_plural = _('Archive')
        ordering = ['document_number']

    def __str__(self):
        return self.document_number
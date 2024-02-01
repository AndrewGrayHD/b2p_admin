from ast import Import
from django.contrib import admin
from main.models import b2p_site
from main.models import b2p_project_name
from main.models import b2p_reference
from main.models import b2p_flex_nesting_agents_program
from main.models import b2p_flex_sme_ratio_program
from main.models import b2p_rates_program
from main.models import b2p_program
from main.models import b2p_assignment
from main.models import b2p_program_source

import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class  B2p_program_Admin(admin.ModelAdmin):
    search_fields=('program',)
    ordering = ['program']

class  B2p_assignment_Admin(admin.ModelAdmin):
    search_fields=('assignment',)
    ordering = ['assignment']


class  B2p_site_Admin(admin.ModelAdmin):
    search_fields=('site',)
    ordering = ['site']

class  B2p_project_nameAdmin(admin.ModelAdmin):
    search_fields=('true_program__program','project_1','site__site')
    list_display = ('true_program','project_1','site','effective_date','expiration_date',)
    ordering = ['-true_program__program']

class  B2p_reference_Admin(admin.ModelAdmin,ExportCsvMixin):
    search_fields=('project__program','site__site','billing_type','effective_date','expiration_date',)
    list_display = ('project','site','billing_type','effective_date','b2p_target','aht_cap','ob_cap','fte_cap','fte_capping','shrink','sme_shrink','flex_sme_ratio',)
    ordering = ['-effective_date']
    actions = ["export_as_csv"]

class  B2p_flex_nesting_agents_program_Admin(admin.ModelAdmin,ExportCsvMixin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment__assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']
    actions = ["export_as_csv"]

class  B2p_flex_sme_ratio_program_Admin(admin.ModelAdmin, ExportCsvMixin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment__assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']
    actions = ["export_as_csv"]

class  B2p_rates_program_Admin(admin.ModelAdmin, ExportCsvMixin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment__assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']
    actions = ["export_as_csv"]

class  B2p_program_sourceAdmin(admin.ModelAdmin):
    search_fields=('true_program__program','source','site__site')
    list_display = ('true_program','source','site','effective_date','expiration_date',)
    ordering = ['-true_program__program']


admin.site.register(b2p_site,B2p_site_Admin)
admin.site.register(b2p_project_name,B2p_project_nameAdmin)
admin.site.register(b2p_reference,B2p_reference_Admin)
admin.site.register(b2p_flex_nesting_agents_program,B2p_flex_nesting_agents_program_Admin)
admin.site.register(b2p_flex_sme_ratio_program,B2p_flex_sme_ratio_program_Admin)
admin.site.register(b2p_rates_program,B2p_rates_program_Admin)
admin.site.register(b2p_program,B2p_program_Admin)
admin.site.register(b2p_assignment,B2p_assignment_Admin)
admin.site.register(b2p_program_source,B2p_program_sourceAdmin)
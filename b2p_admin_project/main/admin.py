from ast import Import
from django.contrib import admin
from main.models import b2p_site
from main.models import b2p_project_name
from main.models import b2p_reference
from main.models import b2p_flex_nesting_agents_program
from main.models import b2p_flex_sme_ratio_program
from main.models import b2p_rates_program
from main.models import b2p_program



class  B2p_program_Admin(admin.ModelAdmin):
    search_fields=('program',)
    ordering = ['program']



class  B2p_site_Admin(admin.ModelAdmin):
    search_fields=('site',)
    ordering = ['site']

class  B2p_project_nameAdmin(admin.ModelAdmin):
    search_fields=('project_2','project_1','site__site')
    list_display = ('project_2','project_1','site','effectived_date','expiration_date',)
    ordering = ['-project_2']

class  B2p_reference_Admin(admin.ModelAdmin):
    search_fields=('project__program','site__site','billing_type','effectived_date','expiration_date',)
    list_display = ('project','site','billing_type','effectived_date',)
    ordering = ['-effectived_date']

class  B2p_flex_nesting_agents_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']

class  B2p_flex_sme_ratio_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']

class  B2p_rates_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site','true_program__program','true_site__site','assignment',)
    list_display = ('lob','site','true_program','true_site','assignment',)
    ordering = ['-true_program__program']


admin.site.register(b2p_site,B2p_site_Admin)
admin.site.register(b2p_project_name,B2p_project_nameAdmin)
admin.site.register(b2p_reference,B2p_reference_Admin)
admin.site.register(b2p_flex_nesting_agents_program,B2p_flex_nesting_agents_program_Admin)
admin.site.register(b2p_flex_sme_ratio_program,B2p_flex_sme_ratio_program_Admin)
admin.site.register(b2p_rates_program,B2p_rates_program_Admin)
admin.site.register(b2p_program,B2p_program_Admin)

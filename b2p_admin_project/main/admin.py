from ast import Import
from django.contrib import admin
from main.models import b2p_site
from main.models import b2p_project_name
from main.models import b2p_reference
from main.models import b2p_flex_agents_program
from main.models import b2p_flex_sme_ratio_program
from main.models import b2p_rates_program


class  B2p_site_Admin(admin.ModelAdmin):
    search_fields=('site',)


class  B2p_project_nameAdmin(admin.ModelAdmin):
    search_fields=('project_2','project_1',)


class  B2p_reference_Admin(admin.ModelAdmin):
    search_fields=('project','billing_type','effectived_date',)

class  B2p_flex_agents_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site',)

class  B2p_flex_sme_ratio_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site',)

class  B2p_rates_program_Admin(admin.ModelAdmin):
    search_fields=('lob','site',)


admin.site.register(b2p_site,B2p_site_Admin)
admin.site.register(b2p_project_name,B2p_project_nameAdmin)
admin.site.register(b2p_reference,B2p_reference_Admin)
admin.site.register(b2p_flex_agents_program,B2p_flex_agents_program_Admin)
admin.site.register(b2p_flex_sme_ratio_program,B2p_flex_sme_ratio_program_Admin)
admin.site.register(b2p_rates_program,B2p_rates_program_Admin)

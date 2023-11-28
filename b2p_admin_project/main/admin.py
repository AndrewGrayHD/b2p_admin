from ast import Import
from django.contrib import admin
from main.models import b2p_site
from main.models import b2p_project_name
from main.models import b2p_reference
from main.models import b2p_flex_agents_program
from main.models import b2p_flex_sme_ratio_program
from main.models import b2p_rates_program


class  B2p_project_nameAdmin(admin.ModelAdmin):
    search_fields=('project_2','project_1',)

admin.site.register(b2p_site)
admin.site.register(b2p_project_name,B2p_project_nameAdmin)
admin.site.register(b2p_reference)
admin.site.register(b2p_flex_agents_program)
admin.site.register(b2p_flex_sme_ratio_program)
admin.site.register(b2p_rates_program)

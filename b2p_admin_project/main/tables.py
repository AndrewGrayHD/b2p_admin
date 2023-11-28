import django_tables2 as tables
from .models import b2p_project_name

class ProjectNamesTable(tables.Table):
    class Meta:
        model = b2p_project_name
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", )
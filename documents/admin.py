# Register your models here.
from django.contrib import admin
from utils.utils import get_model

Document = get_model(app_name="documents", model_name="Document")


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created", "modified")
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_filter = ("created", "modified")
    ordering = ("-created",)
    list_per_page = 25
    date_hierarchy = "created"
    readonly_fields = ("created", "modified")

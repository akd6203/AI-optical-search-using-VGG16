from django.contrib import admin
from myapp.models import SearchResults

admin.site.site_header = "AIHub - Optical Search"

admin.site.register(SearchResults)

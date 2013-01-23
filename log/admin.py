from django.contrib import admin

from .models import Log, RequestLog


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'varname', 'stamp', 'value')
    ordering = ('-stamp',)
    list_filter = ('user',)
    search_fields = ('user__username', 'varname')
    save_on_top = True
admin.site.register(Log, LogAdmin)


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'url', 'stamp')
    ordering = ('-stamp',)
    list_filter = ('user',)
    save_on_top = True
admin.site.register(RequestLog, RequestLogAdmin)

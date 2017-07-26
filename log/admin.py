from django.contrib import admin, auth

from .models import Log, RequestLog


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'varname', 'stamp', 'value')
    ordering = ('-stamp',)
    list_filter = ('user',)
    search_fields = (
        'user__{}'.format(auth.get_user_model().USERNAME_FIELD),
        'varname',
    )
    save_on_top = True
admin.site.register(Log, LogAdmin)


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'url', 'stamp')
    ordering = ('-stamp',)
    list_filter = ('user',)
    save_on_top = True
admin.site.register(RequestLog, RequestLogAdmin)

# -*- coding:utf-8 -*-
from django.contrib import admin
from models import SisServe, OaUser, SisUserAuthor


class SisServeAdmin(admin.ModelAdmin):
    list_display = ('serv_id', 'serv_ip', 'serv_port', 'serv_name', 'pub_key', 'description',)


class OaUserAdmin(admin.ModelAdmin):
    list_display = ('oa_user_id', 'oa_username', 'passwd',)


class SisUserAuthorAdmin(admin.ModelAdmin):
    list_display = ('serv_id', 'sis_username', 'oa_user_id', 'is_save_cookie', 'is_default',)


admin.site.register(SisServe, SisServeAdmin)
admin.site.register(OaUser, OaUserAdmin)
admin.site.register(SisUserAuthor, SisUserAuthorAdmin)

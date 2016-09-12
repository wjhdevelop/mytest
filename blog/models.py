# coding=utf-8
from django.db import models


class SisServe(models.Model):
    serv_id = models.CharField(max_length=20, primary_key=True, verbose_name='服务器ID')
    serv_ip = models.GenericIPAddressField(verbose_name='服务器IP')
    serv_port = models.IntegerField(default=8081, verbose_name='服务器端口')
    serv_name = models.CharField(max_length=30, verbose_name='服务器名称')
    pub_key = models.CharField(max_length=32, verbose_name='Sisense公钥')
    description = models.TextField(verbose_name='描述')
    # default = 8081,

    def __unicode__(self):
        return u'%s' % self.serv_id

    class Meta:
        verbose_name = 'Sisense服务器配置'
        verbose_name_plural = 'Sisense服务器配置'


class OaUser(models.Model):
    oa_user_id = models.IntegerField(primary_key=True)
    oa_username = models.CharField(max_length=50, verbose_name='OA用户名')
    passwd = models.CharField(max_length=50, verbose_name='OA用户密码')

    def __unicode__(self):
        return u'%s' % self.oa_username

    class Meta:
        verbose_name = 'OA用户配置'
        verbose_name_plural = 'OA用户配置'


class SisUserAuthor(models.Model):
    serv_id = models.ForeignKey(SisServe, verbose_name='服务器ID')
    sis_username = models.EmailField(verbose_name='Sisense用户名/邮箱')
    oa_user_id = models.CharField(max_length=50, verbose_name='OA用户名')
    is_save_cookie = models.BooleanField(default=False, verbose_name='是否保存cookie')
    is_default = models.BooleanField(default=True, verbose_name='是否为默认登录平台')

    def __unicode__(self):
        return u'%s' % self.sis_username

    class Meta:
        verbose_name = 'Sisense用户配置'
        verbose_name_plural = 'Sisense用户配置'

# -*- coding: utf8 -*-

"""
    OParoquiano - Solução completa que tem por objetivo ajudar as paroquias,
    capelas, igrejas, dioceses a divulgar suas atividades para comunidade
    local e da região por meio de um sistema web + app android.

    Copyright (C) 2019 - Luis Vitório

    Este programa é um software livre: você pode redistribuí-lo e/ou
    modificá-lo sob os termos da Licença Pública Geral Affero GNU,
    conforme publicado pela Free Software Foundation, seja a versão 3
    da Licença ou (a seu critério) qualquer versão posterior.

    Este programa é distribuído na esperança de que seja útil,
    mas SEM QUALQUER GARANTIA; sem a garantia implícita de
    COMERCIALIZAÇÃO OU ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Veja a
    Licença Pública Geral Affero GNU para obter mais detalhes.

    Você deve ter recebido uma cópia da Licença Pública Geral Affero GNU
    junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

    linkedin: https://www.linkedin.com/in/vitorioluis/
    email: vitorioluis@gmail.com

"""



import re
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.core import validators
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    # TIPO_USER = ((1, 'Administrador'), (2, 'Site'), (3, 'Android'),)
    # username = models.CharField(
    #     'Nome de Usuario', max_length=30, unique=True,
    #     validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
    #                                           'O nome de usuario so pode conter letras, digitos ou os '
    #                                           'seguintes caracteres: @/./+/-/_', 'invalid')]
    # )
    # username = models.EmailField('Username', unique=True)
    username = models.CharField(
        'Nome de Usuario', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'O nome de usuario so pode conter letras, digitos ou os '
                                              'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('Email', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    # tipo = models.IntegerField('Tipo', choices=TIPO_USER, default=3)

    is_active = models.BooleanField('Esta ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)

    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']

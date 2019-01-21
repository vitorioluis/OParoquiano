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


import os

from django.conf import settings
from django.db import models

from oparoquiano.accounts.models import User
from oparoquiano.core.models import UF, Planos


class Diocese(models.Model):
    dio_name = models.CharField('Diocese', max_length=100, unique=False)
    dio_padroeiro = models.CharField('Padroeiro', max_length=100, unique=False)
    dio_cidade = models.CharField('Cidade', max_length=100)
    dio_logo = models.ImageField(upload_to='diocese/logo', verbose_name='Logo', blank=True,
                                 default=settings.LOGO_PADRAO)

    def __str__(self):
        return self.dio_name

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.dio_logo.name))
        super(Diocese, self).delete(*args, **kwargs)

    # organiza lista admin
    class Meta:
        verbose_name = 'Diocese'
        verbose_name_plural = 'Diocese'
        ordering = ['dio_name', 'dio_padroeiro', 'dio_cidade', 'dio_logo']


############## Paroquia ######################e
class ParoquiaManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(par_name__icontains=query))


# tabela Paroquia
class Paroquia(models.Model):

    StatusCad_CHOICES = ((0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado'),)

    par_name = models.CharField('Paroquia', max_length=100)
    par_site = models.URLField('Site', max_length=100, blank=True)
    par_tel = models.CharField('Telefone:', max_length=12)
    par_endereco = models.CharField('Endereço', max_length=100, blank=True)
    par_num = models.CharField('Número', max_length=100, blank=True)
    par_cep = models.CharField('CEP', max_length=100, blank=True)
    par_cidade = models.CharField('Cidade', max_length=100, blank=True)
    par_status = models.IntegerField('Situação Cadastral', choices=StatusCad_CHOICES, default=1, blank=True)
    par_propaganda = models.BooleanField('Deseja exibir propaganda?', default=True, blank=False)
    par_logo = models.ImageField(upload_to='paroquia/logo', verbose_name='Logo', blank=True,
                                 default=settings.LOGO_PADRAO)

    uf = models.ForeignKey(UF, verbose_name='UF')
    user = models.ForeignKey(User, verbose_name='Usuário')
    diocese = models.ForeignKey(Diocese, verbose_name='Diocese')
    #plano = models.ForeignKey(Produtos, verbose_name='Plano')

    publicar_app = models.BooleanField("Publicar no app",default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ParoquiaManager()
    default = True

    # retorna na tela de lista de name
    def __str__(self):
        return self.par_name

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.par_logo.name))
        super(Paroquia, self).delete(*args, **kwargs)

    # organiza lista de cursos admin
    class Meta:
        verbose_name = 'Paroquia'
        verbose_name_plural = 'Paroquia'
        ordering = ['par_name', 'diocese']


class Planos_X_Paroquia(models.Model):
    paroquia = models.ForeignKey(Paroquia)
    planos = models.ForeignKey(Planos)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return 'Planos'

    class Meta:
        verbose_name = "Planos por Paróquia"
        verbose_name_plural = "Planos por Paróquia"
        ordering = ['paroquia', 'planos']

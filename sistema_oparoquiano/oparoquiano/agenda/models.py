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

from oparoquiano.paroquia.models import Paroquia


class Tipo_Agendamento(models.Model):
    tipo_agendamento = models.CharField(
        'Tipo', blank=False, unique=True, max_length=100
    )
    tipo_img = models.ImageField(upload_to='tipo/logo', verbose_name='Logo', blank=False, default=settings.LOGO_PADRAO)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.tipo_agendamento

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.tipo_img.name))
        super(Tipo_Agendamento, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Tipo de agendamento"
        verbose_name_plural = "Tipo de agendamentos"
        ordering = ['tipo_agendamento']


class AgendaManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(age_data__icontains=query) |
            models.Q(age_hora_inicio__icontains=query) |
            models.Q(age_desc__icontains=query) |
            models.Q(age_local_evento__icontains=query) |
            models.Q(tip_id__icontains=query)
        )


class Agenda(models.Model):
    # choices=((1, 'Todo Domingo'), (2, 'Toda Segunda'), (3, 'Toda Terça'), (4, 'Toda Quarta'),(5, 'Toda Quinta'), (6, 'Toda Sexta'), (7, 'Todo Sábado'), (8, 'Diário'), (9, 'Mensal'), (10, 'A cada 15 dias'), (11, 'Bimestral'), (12, 'Trimestral'), (13, 'Semestral'), (14, 'Anual'),)

    age_recorente = models.BooleanField(verbose_name='O evento é Recorrente?', blank=True, default=False,
                                        help_text="Marque está opção se o evento se repetir.")
    age_data_inicio = models.DateField(verbose_name='Data de início Evento', blank=False, null=True)
    age_data_fim = models.DateField(verbose_name='Data de término do Evento', blank=True, null=True)
    age_hora_inicio = models.TimeField(verbose_name='Horário de início do Evento', blank=True, null=True,
                                       help_text="Exemplo do formato da hora 10:00")
    age_hora_fim = models.TimeField(verbose_name='Horário de término do Evento', blank=True, null=True,
                                    help_text="Exemplo do formato da hora 10:00")
    age_desc = models.TextField(verbose_name='Descrição', blank=True, null=True)
    age_local_evento = models.CharField(verbose_name='Local Evento', blank=True, max_length=50, default=None)
    age_publicar = models.BooleanField(verbose_name='Publicar?', default=False,
                                       help_text="O evento só estará disponivel no celular se está opção for marcada.")
    age_img = models.ImageField(upload_to='agenda/img', verbose_name='Imagem', blank=True,
                                default=None, help_text="Está imagem será exibida junta com o texto")
    age_dia_recorrencia = models.CharField(verbose_name='Tipo de Recorrencia', max_length=30, blank=True, null=True)

    paroquia = models.ForeignKey(Paroquia, verbose_name='Paroquia')
    tipo = models.ForeignKey(Tipo_Agendamento, verbose_name='Tipo')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='agendas')

    objects = AgendaManager()

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def delete(self, *args, **kwargs):
        if settings.LOGO_PADRAO != self.age_img.name:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.age_img.name))
        super(Agenda, self).delete(*args, **kwargs)

    #
    # def save(self, size=(600, 480)):
    #     """
    #     Save Photo after ensuring it is not blank.  Resize as needed.
    #     """
    #     super(Agenda, self).save()
    #
    #     filename = self.age_img.name
    #     image = Image.open(filename)
    #
    #     image.thumbnail(size, Image.ANTIALIAS)
    #     image.save(filename)

    def __str__(self):
        return self.age_desc

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['tipo', 'user', 'age_recorente', '-age_data_inicio', 'age_hora_inicio']

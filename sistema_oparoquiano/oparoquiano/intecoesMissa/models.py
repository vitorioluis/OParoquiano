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
from django.db import models

from oparoquiano.paroquia.models import Paroquia


class IntencoesMissa(models.Model):

    nome = models.CharField('Nome', max_length=50, blank=False, null=False)
    paroquia = models.ForeignKey(Paroquia)
    intecao = models.TextField('Intenção', max_length=255, blank=False, null=False)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.intecao

    class Meta:
        verbose_name = "Intenções da Missa"
        verbose_name_plural = "Intenções da Missa"
        ordering = ['created_at', 'paroquia','nome']

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



class UF(models.Model):
    uf_cod_ibge = models.IntegerField('Código IBGE', default=0)
    uf_sigla = models.CharField('UF', max_length=2, unique=True)
    uf_name = models.CharField('Estado', max_length=50)

    def __str__(self):
        return self.uf_sigla

    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UF'
        ordering = ['uf_sigla']


class Planos(models.Model):
    choices = ((1, 'Paroquia'), (2, 'Diocese'),)

    planos = models.CharField('Plano', max_length=50, blank=False)
    tipo = models.IntegerField('Tipo de Plano', choices=choices, default=1)
    descricao = models.CharField('Descrição', max_length=250, blank=True)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=18)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.planos

    class Meta:
        verbose_name = "Planos"
        verbose_name_plural = "Planos"
        ordering = ['planos']



# class Versao(models.Model):
#     tabela = models.CharField('Tabela', max_length=50, blank=False)
#     paroquia = models.CharField('Paroquia', max_length=100, blank=True)
#     versao = models.IntegerField('Versao', default=1)
#
#     def __str__(self):
#         return self.tabela
#
#     class Meta:
#         verbose_name_plural = 'Versão do Banco de Dados'
#         ordering = ['-tabela', 'paroquia']

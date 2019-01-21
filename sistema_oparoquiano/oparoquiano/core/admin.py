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

from django.contrib import admin

from oparoquiano.core.models import UF, Planos


class UFAdmin(admin.ModelAdmin):
    list_display = ['uf_name', 'uf_sigla', 'uf_cod_ibge', 'id', ]
    search_fields = ['uf_cod_ibge', 'uf_sigla', 'uf_name', ]


admin.site.register(UF, UFAdmin)


class PlanosAdmin(admin.ModelAdmin):
    list_display = ['planos', 'tipo', 'descricao', 'valor', 'created_at', 'updated_at', 'id', ]
    search_fields = ['planos', 'tipo', 'descricao', ]


admin.site.register(Planos, PlanosAdmin)



#
# class VersaoAdmin(admin.ModelAdmin):
#     list_display = ['tabela', 'paroquia', 'versao', ]
#     search_fields = ['tabela', 'paroquia', 'versao', ]
#
#
# admin.site.register(Versao, VersaoAdmin)

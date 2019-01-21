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

from .models import Paroquia, Diocese, Planos_X_Paroquia


class DioceseAdmin(admin.ModelAdmin):
    list_display = ['dio_name', 'dio_padroeiro', 'dio_cidade', 'id', ]
    search_fields = ['dio_name', 'dio_padroeiro', 'dio_cidade', ]


admin.site.register(Diocese, DioceseAdmin)


class ParoquiaAdmin(admin.ModelAdmin):
    list_display = ['par_name','publicar_app', 'par_site', 'diocese_id', 'par_endereco', 'par_propaganda',
                    'par_num', 'par_cep', 'par_cidade', 'uf', 'user', 'par_logo', 'id', ]
    search_fields = ['diocese_id', 'par_name', 'par_cidade', ]


admin.site.register(Paroquia, ParoquiaAdmin)


class Planos_X_ParoquiaAdmin(admin.ModelAdmin):
    list_display = ['paroquia', 'planos', 'created_at', 'updated_at', 'id', ]
    search_fields = ['paroquia', 'planos', ]


admin.site.register(Planos_X_Paroquia, Planos_X_ParoquiaAdmin)

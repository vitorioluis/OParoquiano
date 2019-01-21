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




import json

from django.conf import settings
# from django.contrib.auth import authenticate
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone

from oparoquiano.agenda.models import Agenda
from oparoquiano.api.models import log_Acesso
from oparoquiano.paroquia.models import Paroquia

json_raiz = 'fields'


def gera_json_paroquia(request, token, primeira="1"):
    if autenticar(token):
        dic = {json_raiz: []}

        result = Paroquia.objects.select_related().filter(par_status=1, publicar_app=True)
    
        for item in result.values('id', 'par_name', 'par_site', 'par_endereco', 'par_num', 'par_cep',
                                  'par_cidade', 'par_propaganda', 'par_logo', 'diocese__dio_name'):
            dic[json_raiz].append(item)

        return HttpResponse(json.dumps(dic), content_type='json; charset=utf8')
    else:
        return redirect(settings.SITE)


def gera_json_agenda(request, token, par_id):
    if autenticar(token):
        dic = {json_raiz: []}
        data_agora = timezone.now()
        result = Agenda.objects.select_related().filter(paroquia=par_id, age_publicar=True)

        result = result.filter(models.Q(age_recorente=True) | models.Q(age_data_inicio__gte=data_agora))

        log_Acesso(id_paroquia=par_id).save()

        for item in result.values('id', 'age_data_inicio', 'age_data_fim', 'age_hora_inicio', 'age_hora_fim',
                                  'age_desc', 'age_local_evento', 'paroquia__par_name', 'tipo__tipo_agendamento',
                                  'tipo__tipo_img', 'paroquia__id', 'age_recorente', 'age_dia_recorrencia', 'age_img'):

            if item['age_recorente']:
                nd = item['age_dia_recorrencia']
            else:
                nd = '{0} - {1}'.format(formata_data(str(item['age_data_inicio'])),
                                        formata_data(str(item['age_data_fim'])))

            item['age_data_inicio'] = nd
            item['age_data_fim'] = ''

            if item['age_hora_fim'] not in (None, ''):
                tm = '{0} - {1}'.format(str(item['age_hora_inicio']), str(item['age_hora_fim']))
            else:
                tm = str(item['age_hora_inicio'])

            item['age_hora_inicio'] = tm
            item['age_hora_fim'] = ''

            dic[json_raiz].append(item)

        return HttpResponse(json.dumps(dic), content_type='json; charset=utf8')
    else:
        return redirect(settings.SITE)


def autenticar(token):
    lista = ['92ad3305eadff39c271384f3912c704dbd053734974e5e0e14dbdfca6586d153cafb6aee6217443800b3aa872be4da07']

    if token in lista:
        retorno = True
    else:
        retorno = False

    return retorno


def formata_data(dt):
    nova_data = dt[-2:]
    nova_data += '/' + dt[5:7] + '/'
    nova_data += dt[:4]
    return nova_data

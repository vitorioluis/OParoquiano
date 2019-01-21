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



from datetime import date, datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from oparoquiano.api.models import log_Acesso
from oparoquiano.paroquia.models import Paroquia


@login_required
def home(request):
    template_name = 'base.html'
    par_logo = Paroquia.objects.select_related().filter(user_id=request.user.id).values('logo_par')[:1]
    return render(request, template_name, {'logo', par_logo})


@login_required
def home_grafos(request):
    paroquia = Paroquia.objects.select_related().filter(user_id=request.user.id).values('id', 'par_logo')[:1]
    par_id = paroquia[0]['id']
    # par_logo = settings.URL_RAIZ_MEDIA + paroquia[0]['par_logo']

    hj = date.today()
    trinta_dias_anteriores = date.fromordinal(hj.toordinal() - 30)
    ano_anterior = date.fromordinal(hj.toordinal() - 365)

    log_a = log_Acesso.objects.select_related().filter(id_paroquia=par_id)
    log_a = log_a.extra({'acessado_em': 'date(acessado_em)'}).values('acessado_em').annotate(
        Count('id_paroquia')).order_by('-acessado_em')

    log_m = log_Acesso.objects.select_related().filter(acessado_em__gte=ano_anterior, id_paroquia=par_id)
    log_m = log_m.extra({'acessado_em': 'date(acessado_em)'}).values('acessado_em').annotate(
        Count('id_paroquia')).order_by('-acessado_em')

    log_d = log_Acesso.objects.select_related().filter(acessado_em__gte=trinta_dias_anteriores, id_paroquia=par_id)
    log_d = log_d.extra({'acessado_em': 'date(acessado_em)'}).values('acessado_em').annotate(
        Count('id_paroquia')).order_by('-acessado_em')

    lst_soma_mes = monta_dic_grafo(log_m, 7)
    dic_soma_ano = monta_dic_grafo(log_a, 4)

    template_name = 'grafos.html'
    context = {'grafo_line_diario': log_d,
               'grafo_line_mensal': lst_soma_mes,
               'grafo_line_anual': dic_soma_ano,
               'ano': datetime.now().year,
               # 'par_logo': par_logo,
               }

    return render(request, template_name, context)


def monta_dic_grafo(log, qtd):
    dic_soma = {}
    for mes in log:
        mm = str(mes['acessado_em'])[0:qtd]
        count = mes['id_paroquia__count']
        if mm not in dic_soma:
            dic_soma[mm] = 0
        dic_soma[mm] += count

    lst = []
    for item in sorted(dic_soma, reverse=True):
        lst.append({'acessado_em': item, 'id_paroquia__count': dic_soma[item]})
    return lst

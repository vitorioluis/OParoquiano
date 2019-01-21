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



# from django.db.models import F
# from oparoquiano.core.models import Versao
# from decimal import Decimal
#
# com=1
#
# def post_save_versao_tipo_agendamento(created, instance,**kwargs):
#     tab='Tipo de Agendamentos'
#     v=Versao.objects.filter(tabela=tab)
#     print(kwargs,created,instance)
#     if len(v)==0:
#         v=Versao(tabela=tab)
#         v.save()
#     else:
#         v.update(versao=F('versao')+com)
#
# def post_delete_versao_tipo_agendamento(instance,**kwargs):
#     tab='Tipo de Agendamentos'
#     v=Versao.objects.filter(tabela=tab)
#     v.update(versao=F('versao')+com)
#
#
# #Paroquia
# def post_save_versao_paroquia(created, instance,**kwargs):
#         tab='Paroquia'
#         v=Versao.objects.filter(tabela=tab)
#         if len(v)==0:
#             v=Versao(tabela=tab)
#             v.save()
#         else:
#             v.update(versao=F('versao')+com)
#
# def post_delete_versao_paroquia(instance,**kwargs):
#     tab='Paroquia'
#     v=Versao.objects.filter(tabela=tab)
#     v.update(versao=F('versao')+com)
#
#
#
#
# #Diocese
# def post_save_versao_diocese(created, instance,**kwargs):
#     tab='Diocese'
#     v=Versao.objects.filter(tabela=tab)
#     if len(v)==0:
#         v=Versao(tabela=tab)
#         v.save()
#     else:
#         v.update(versao=F('versao')+com)
#
#
# def post_delete_versao_diocese(instance,**kwargs):
#     tab='Diocese'
#     v=Versao.objects.filter(tabela=tab)
#     v.update(versao=F('versao')+com)
#
#
# #agenda
# def post_save_versao_agenda(created, instance,**kwargs):
#     v=Versao.objects.filter(paroquia=instance)
#     print(instance,'instance',len(v),v)
#     if len(v) == 0:
#         v=Versao(tabela='Agenda',paroquia=instance.par_id)
#         v.save()
#     else:
#         v.update(versao=F('versao')+com)
#
# def post_delete_versao_agenda(instance,**kwargs):
#     v=Versao.objects.filter(paroquia=instance)
#     v.update(versao=F('versao')+com)

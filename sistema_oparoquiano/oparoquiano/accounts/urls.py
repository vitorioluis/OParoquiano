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



from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from oparoquiano.accounts import views

urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),

    url(r'^$', views.ListarUser.as_view(), name='dashboard'),
    url(r'^edit/(?P<pk>\w+)/$', views.UpdateUser.as_view(), name='edit'),
    url(r'^novo/$', views.CreateUser.as_view(), name='new'),

    url(r'^password-reset/$', views.password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^edit-password/$', views.edit_password, name='edit_password'),
]

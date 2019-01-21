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
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
# from django.views.static import serve

admin.autodiscover()


urlpatterns = [
    url(r'^', include('oparoquiano.core.urls', namespace='core')),
    url(r'^manager/', include(admin.site.urls)),
    url(r'^accounts/', include('oparoquiano.accounts.urls', namespace='accounts')),
    url(r'^agenda/', include('oparoquiano.agenda.urls', namespace='agenda')),
    url(r'^paroquia/', include('oparoquiano.paroquia.urls', namespace='paroquia')),
    #  url(r'^news/', include('oparoquiano.news.urls', namespace='news')),
    url(r'^api/', include('oparoquiano.api.urls', namespace='api')),
]

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#xxxxx

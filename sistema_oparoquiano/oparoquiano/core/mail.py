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
from django.core.mail import EmailMultiAlternatives
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string


def send_mail_template(subject, template_name, context, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL,
                       fail_silenty=False):
    message_html = render_to_string(template_name, context)
    message_txt = striptags(message_html)
    email = EmailMultiAlternatives(subject=subject, body=message_txt, from_email=from_email, to=recipient_list)
    email.attach_alternative(message_html, "text/html")
    email.send(fail_silently=fail_silenty)

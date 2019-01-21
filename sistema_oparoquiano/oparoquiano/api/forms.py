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



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateField

from .models import log_Acesso


class logAcessoApiForm(forms.ModelForm):
    acessado_em = DateField(input_formats='%Y-%m-%d')

    class Meta:
        model = log_Acesso
        fields = ('id_paroquia', 'acessado_em',)


class RegisterlogAcessoApiForm(UserCreationForm):
    def save(self, commit=True):
        log = super(logAcessoApiForm, self).save(commit=False)
        if commit:
            log.save()
        return log

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



from datetime import date
from functools import partial
from io import BytesIO

from PIL import Image
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Agenda

User = get_user_model()

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


# wysihtml5 = partial(forms.TextInput,{'class':'wysihtml5'})
# TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})

class AgendaForm(forms.ModelForm):
    age_data_inicio = forms.DateField(widget=DateInput())
    age_data_fim = forms.DateField(widget=DateInput())

    # age_hora_inicio = forms.TimeField(initial='12:00:00')
    # age_hora_fim = forms.TimeField(initial='12:00:00')

    data_ini = ''
    recorrente = False

    def clean_age_hora_termino(self):
        hora_inicio = self.cleaned_data['age_hora_inicio']
        hora_fim = self.cleaned_data['age_hora_fim']
        recorrente = self.cleaned_data['age_recorente']

        if recorrente is False:
            if hora_fim not in ('', None):
                if hora_fim <= hora_inicio:
                    raise forms.ValidationError(
                        'Horario de término do Evento não pode ser menor ou igual que a hora de inicio do Evento...')
        return hora_fim

    def clean_age_data_inicio(self):
        self.recorrente = self.cleaned_data['age_recorente']
        self.data_ini = self.cleaned_data['age_data_inicio']
        if self.recorrente is False:
            if self.data_ini <= date.today():
                raise forms.ValidationError('A data escolhida é menor do que a data de hoje!')

        return self.data_ini

    def clean_age_data_fim(self):
        # recorrente = self.cleaned_data['age_recorente']
        data_fim = self.cleaned_data['age_data_fim']
        if self.recorrente is False:
            if data_fim not in ('', None) and data_fim < self.data_ini:
                raise forms.ValidationError(
                    'Data de término do Evento não pode ser menor que a data de inicio do Evento...')

        return data_fim

    def clean_age_img(self):

        image_field = self.cleaned_data.get('age_img')
        if image_field and image_field != settings.LOGO_PADRAO:
            try:
                image_file = BytesIO(image_field.file.read())
                image = Image.open(image_file)
                image.thumbnail((600, 480), Image.ANTIALIAS)
                image_file = BytesIO()
                image.save(image_file, 'JPEG')
                image_field.file = image_file
                image_field.image = image

                return image_field
            except IOError:
                raise Exception("Error during resize image")

    class Meta:
        model = Agenda
        fields = ('tipo', 'age_local_evento', 'age_recorente', 'age_data_inicio', 'age_data_fim', 'age_hora_inicio',
                  'age_hora_fim', 'age_publicar', 'age_img', 'age_desc',)


class RegisterAgendaForm(UserCreationForm):
    # hora_f = forms.hora_fimlField(label='Horario de término do Evento')
    def save(self, commit=True):
        agenda = super(AgendaForm, self).save(commit=False)
        if commit:
            agenda.save()
        return agenda

# agenda_cnpj=forms.EmailField(label='agenda_cnpj')
# def clean_agenda_cnpj(self):
#     cnpj=self.cleaned_data['agenda_cnpj']
#     if agenda.objects.filter(email=email).exists():
#         raise forms.ValidationError('CNPJ ja cadastrado...')
#     return email

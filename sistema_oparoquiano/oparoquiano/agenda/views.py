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




from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from oparoquiano.paroquia.models import Paroquia
from .forms import AgendaForm
from .models import Agenda

User = get_user_model()


# __lte<=  menor igual
# __gte>= maior igual

class ListarAgenda(LoginRequiredMixin, TemplateView):
    template_name = 'agenda/agenda_data_table.html'

    def get(self, request, **Kwargs):
        agenda = Agenda.objects.select_related().filter(user_id=self.request.user.id)
        context = {'objects': agenda}
        return render(self.request, self.template_name, context)


class UpdateAgenda(LoginRequiredMixin, UpdateView):
    template_name = 'agenda/new_edit.html'
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('agenda:dashboard')

    def get_context_data(self, **kwargs):
        context = super(UpdateAgenda, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        context['texto'] = 'Agenda'
        context['cancela'] = 'agenda:dashboard'
        context['acao'] = 'Edit'
        return context

    def post(self, request, **Kwargs):
        dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
        agenda = get_object_or_404(Agenda, id=Kwargs['pk'])
        form = AgendaForm(request.POST or None, request.FILES or None, instance=agenda)
        context = {}
        if form.is_valid():
            agenda = form.save(commit=False)
            # paroquia = get_object_or_404(Paroquia,user_id=request.user.id)
            # agenda.par_id=paroquia
            agenda.age_dia_recorrencia = str(dias[agenda.age_data_inicio.weekday()])
            agenda.user = request.user
            agenda.save()
            context['objects'] = agenda
            return redirect('agenda:dashboard')

        context = {'form': form,
                   'user_id': self.request.user.pk,
                   'texto': 'Agenda',
                   'cancela': 'agenda:dashboard',
                   'acao': 'Novo'}

        return render(self.request, self.template_name, context)


class CreateAgenda(LoginRequiredMixin, CreateView):
    template_name = 'agenda/new_edit.html'
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('paroquia:dashboard')

    def get_context_data(self, **kwargs):
        context = super(CreateAgenda, self).get_context_data(**kwargs)

        context['user_id'] = self.request.user.pk
        context['texto'] = 'Agenda'
        context['cancela'] = 'agenda:dashboard'
        context['acao'] = 'Novo'

        return context

    def post(self, request, *args, **kwargs):
        dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
        form = AgendaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            agenda = form.save(commit=False)
            paroquia = get_object_or_404(Paroquia, user_id=request.user.id)
            agenda.paroquia = paroquia
            agenda.age_dia_recorrencia = str(dias[agenda.age_data_inicio.weekday()])
            agenda.user = request.user
            agenda.save()
            return redirect('agenda:dashboard')

        context = {'form': form,
                   'user_id': self.request.user.pk,
                   'texto': 'Agenda',
                   'cancela': 'agenda:dashboard',
                   'acao': 'Novo'}

        return render(self.request, self.template_name, context)


@login_required
def delete(request, id):
    template_name = 'agenda/delete.html'
    context = {}
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda:dashboard')
    context['object'] = agenda
    return render(request, template_name, context)

# @login_required
# def edit(request, id):
#     dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
#     template_name = 'agenda/edit.html'
#     context = {}
#     agenda = get_object_or_404(Agenda, id=id)
#     form = AgendaForm(request.POST or None, request.FILES or None, instance=agenda)
#     if form.is_valid():
#         agenda.age_dia_recorrencia = str(dias[agenda.age_data_inicio.weekday()])
#         form.save()
#         context['success'] = True
#         return redirect('agenda:dashboard')
#
#     context = {'form': form,
#                'objects': agenda,
#                'user_id': self.request.user.pk,
#                'texto': 'Agenda',
#                'cancela': 'agenda:dashboard',
#                'acao': 'Novo'}
#     return render(request, template_name, context)
#
#
# @login_required
# def new(request):
#     dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
#     template_name = 'agenda/new.html'
#     if request.method == 'POST':
#         form = AgendaForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             agenda = form.save(commit=False)
#             # paroquia = get_object_or_404(Paroquia,user_id=request.user.id)
#             # agenda.par_id=paroquia
#             agenda.age_dia_recorrencia = str(dias[agenda.age_data_inicio.weekday()])
#             agenda.user = request.user
#             agenda.save()
#             return redirect('agenda:dashboard')
#     else:
#         form = AgendaForm()
#     context = {'form': form}
#     return render(request, template_name, context)

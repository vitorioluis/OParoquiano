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


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView

from .forms import ParoquiaForm
from .models import Paroquia


class ListarParoquia(LoginRequiredMixin, View):
    template_name = 'paroquia/paroquia_data_table.html'

    def get(self, request):
        paroquia = Paroquia.objects.select_related().filter(user_id=request.user.id)
        return render(request, self.template_name, {'objects': paroquia})


class EditParoquias(LoginRequiredMixin, UpdateView):
    template_name = 'paroquia/new_edit.html'
    model = Paroquia
    form_class = ParoquiaForm
    success_url = reverse_lazy('paroquia:dashboard')

    def get_context_data(self, **kwargs):
        context = super(EditParoquias, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        context['texto'] = 'Paróquia'
        context['cancela'] = 'paroquia:dashboard'
        context['acao'] = 'Editar'

        return context


class CreateParoquias(LoginRequiredMixin, CreateView):
    template_name = 'paroquia/new_edit.html'
    model = Paroquia
    form_class = ParoquiaForm
    success_url = reverse_lazy('paroquia:dashboard')

    def get_context_data(self, **kwargs):
        context = super(CreateParoquias, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        context['texto'] = 'Paróquia'
        context['cancela'] = 'paroquia:dashboard'
        context['acao'] = 'Novo'

        return context


@login_required
def delete(request, id):
    template_name = 'paroquia/delete.html'
    context = {}
    paroquia = get_object_or_404(Paroquia, id=id)
    if request.method == 'POST':
        paroquia.delete()
        return redirect('paroquia:dashboard')
    context['object'] = paroquia
    return render(request, template_name, context)

#
# @login_required
# def edit(request, id):
#     template_name = 'paroquia/new_edit.html'
#     context = {}
#     paroquia = get_object_or_404(Paroquia, id=id)
#     form = ParoquiaForm(data=request.POST or None, instance=paroquia)
#     if form.is_valid():
#         form.save()
#         context['success'] = True
#         return redirect('paroquia:dashboard')
#     context['form'] = form
#     return render(request, template_name, context)


# @login_required
# def new(request):
#     template_name = 'paroquia/new_edit.html'
#     if request.method == 'POST':
#         form = ParoquiaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('paroquia:dashboard')
#     else:
#         form = ParoquiaForm()
#     context = {'form': form}
#     return render(request, template_name, context)

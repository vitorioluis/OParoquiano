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
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View

from .forms import PasswordResetForm, UserForm
from .models import PasswordReset

User = get_user_model()


class ListarUser(LoginRequiredMixin, View):
    template_name = 'accounts/accounts_data_table.html'

    def get(self, request):
        accounts = User.objects.all()
        return render(request, self.template_name, {'objects': accounts})


class CreateUser(LoginRequiredMixin, CreateView):
    template_name = 'accounts/new_edit.html'
    models = User
    form_class = UserForm
    success_url = reverse_lazy('accounts:dashboard')

    def get_context_data(self, **kwargs):
        context = super(CreateUser, self).get_context_data(**kwargs)
        context['texto'] = 'User'
        context['cancela'] = 'accounts:dashboard'
        context['acao'] = 'Novo'

        return context


class UpdateUser(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/new_edit.html'
    models = User
    form_class = UserForm
    success_url = reverse_lazy('accounts:dashboard')

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(UpdateUser, self).get_context_data(**kwargs)
        context['texto'] = 'User'
        context['cancela'] = 'accounts:dashboard'
        context['acao'] = 'Editar'

        return context


@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

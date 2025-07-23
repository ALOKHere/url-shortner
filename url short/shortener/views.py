from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .forms import URLForm
from .models import URL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import random
import string


def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


class HomeView(LoginRequiredMixin, FormView):
    template_name = 'shortener/home.html'
    form_class = URLForm
    success_url = reverse_lazy('shortener:home')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = URL.objects.filter(user=self.request.user).order_by('-created_at')
        return context

    def form_valid(self, form):
        original_url = form.cleaned_data['original_url']
        custom_code = form.cleaned_data.get('custom_code')

        if URL.objects.filter(original_url=original_url, user=self.request.user).exists():
            form.add_error('original_url', 'You have already shortened this URL.')
            return self.form_invalid(form)

        if custom_code:
            base_code = custom_code.strip()
            final_code = base_code
            suffix_attempts = 0

            while URL.objects.filter(short_code=final_code).exists():
                suffix_attempts += 1
                random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
                final_code = f"{base_code}{random_suffix}"
                if suffix_attempts > 5:
                    form.add_error('custom_code', 'Unable to generate unique code, try a different input.')
                    return self.form_invalid(form)
        else:
            final_code = generate_short_code()
            while URL.objects.filter(short_code=final_code).exists():
                final_code = generate_short_code()

        URL.objects.create(
            original_url=original_url,
            short_code=final_code,
            user=self.request.user
        )

        return super().form_valid(form)


def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    url.click_count += 1
    print(f"Click count for {url.short_code} is now {url.click_count}")
    url.save()
    print(f"Redirecting to {url.original_url} with code {code}")
    return redirect(url.original_url)



class RegisterView(FormView):
    template_name = 'shortener/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('shortener:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

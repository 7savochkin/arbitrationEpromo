from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from pages.forms import ContactUsForm


class IndexView(TemplateView):
    """Template view for home page"""
    template_name = 'index.html'


class ContactUsView(FormView):
    """Form view for contact us page"""
    form_class = ContactUsForm
    success_url = reverse_lazy('index')
    template_name = './pages/contact/contact_us.html'

    def form_valid(self, form):
        """Method will send email with contact data when form will be valid"""
        try:
            form.send_email()
            return super(ContactUsView, self).form_valid(form)
        except Exception: # noqa
            return super(ContactUsView, self).form_invalid(form)

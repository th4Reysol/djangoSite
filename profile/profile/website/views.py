from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"

class ServiceView(TemplateView):
    template_name="service/service.html"

class CareerView(TemplateView):
    template_name="career/career.html"

class RecentView(TemplateView):
    template_name="contact/recent.html"


from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'
class TestingPage(TemplateView):
    template_name = 'testing.html'
class LandingPage(TemplateView):
    template_name = 'cat.html'

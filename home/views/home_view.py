from django.views.generic.base import TemplateView

from ..models import HomePage


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page"] = HomePage.get_solo()
        ctx[
            "page_title"
        ] = "Lango -  Speak Like Native"
        ctx[
            "page_description"
        ] = """Lango is First online interactive courses website that you will learn any language from zero to hero"""
        return ctx

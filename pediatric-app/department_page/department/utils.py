from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'Расписание', 'url_name': 'timetables'},
    {'title': 'Образование', 'url_name': 'index'},
    {'title': 'Сотрудники', 'url_name': 'index'},
    {'title': 'МНО', 'url_name': 'index'},
    {'title': 'Регистрация', 'url_name': 'signupuser'},
    {'title': 'Войти', 'url_name': 'loginuser'},
]


class DataMixin:
    paginate_py = 1
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats

        return context

from django.contrib import admin
from app_student.models import IceCreamCategory, IceCreamLike, IceCreamComment

# Register your models here.

admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление моделями!'
admin.site.site_title = 'Панель3'


class IceCreamCategoryAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ReceiptCategory' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
    )
    list_display_links = (  # поля-ссылка
        'title',
    )
    list_editable = (  # поля для редактирования объекта на лету
    )
    list_filter = (  # поля для редактирования объекта на лету
        'title',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
    ]


admin.site.register(IceCreamCategory, IceCreamCategoryAdmin)
admin.site.register(IceCreamLike)
admin.site.register(IceCreamComment)
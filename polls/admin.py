from django.contrib import admin

from .models import *


class BookInfoAdmin(admin.ModelAdmin):
    #列表页显示效果
    list_display = ['id', 'title', 'pub']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10

    #修改页和添加页
    fieldsets = [#分组显示
        #(),()
    ]

    #


admin.site.register(BookInfo, BookInfoAdmin)

admin.site.register(HeroInfo)
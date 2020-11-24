from django.contrib import admin
from polling.models import Poll

# from polling.models import Question


admin.site.register(Poll)
# admin.site.register(Question)

# @admin.register(Poll)
# class PollAdmin
#
#
#
# # and a new admin registration
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     exclude = ('posts',)
#
#
# # Define an inline class here
# class CategoryInLine(admin.TabularInline):
#     model = Category.posts.through
#
#
# # Define an inline class here
# class PollInLine(admin.TabularInline):
#     model = Poll.posts.through
#
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = (CategoryInLine, PollInLine,)

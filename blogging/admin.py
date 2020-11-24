# a new import
from django.contrib import admin
from blogging.models import Post, Category, Poll
from polling.models import Poll

# from blogging.models import Poll
from django.db import models


# and a new admin registration
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


# Define an inline class here
class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


# Define an inline class here
class PollInLine(admin.TabularInline):
    model = Poll.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        CategoryInLine,
        PollInLine,
    )

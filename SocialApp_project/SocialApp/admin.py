
from django.contrib import admin
from .models import  Author, Post

from django import forms

from django.contrib.auth.models import Group
from django.utils.html import mark_safe
from django.urls import reverse

from django.forms import ModelForm, Textarea

admin.site.unregister(Group)

# class   AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Author, AuthorAdmin)
#
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)



# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ["first_name", "last_name","image"]
#
#         widgets = {
#             'first_name': Textarea(attrs={'cols': 100, 'rows': 20}),
#         }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    # form = AuthorForm
    list_display = ("first_name", "last_name","image_tag")
    search_fields = ("first_name",)
    list_filter = ("first_name", "last_name")
    # list_display = ("first_name", "last_name","image_tag")


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#         widgets = {
#             'details': Textarea(attrs={'cols': 130, 'rows': 20}),
#         }
#

@admin.register(Post)
class   PostAdmin(admin.ModelAdmin):

    # form = PostForm

    # list_display = ( "title","author","details","date")
    list_display = ( "title","author_link","details","date")


    def author_link(self, obj):
        url = reverse("admin:SocialApp_author_change", args=[obj.author.id])
        link = '<a href="%s">%s</a>' % (url, obj.author.first_name)
        return mark_safe(link)
    author_link.short_description = 'Author'

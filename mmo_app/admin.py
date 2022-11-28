from django.contrib import admin

from .models import Category, Ads, AdsCategory, Feedback


class AdsAdmin(admin.ModelAdmin):
    model = Ads
    list_display = ('pub_author', 'choice_field', 'pub_date', 'pub_title', 'pub_content')
    list_filter = ('pub_author', 'choice_field', 'pub_date')
    search_fields = ('pub_author', 'choice_field', 'pub_date')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


class AgsCategoryAdmin(admin.ModelAdmin):
    model = AdsCategory
    list_display = ('ac_publication', 'ac_category')
    list_filter = ('ac_publication', 'ac_category')
    search_fields = ('ac_publication', 'ac_category')


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ('reaction_to_pub', 'reaction_user', 'reaction_text', 'reaction_pub_date', 'reaction_status')
    list_filter = ('reaction_to_pub', 'reaction_user', 'reaction_text', 'reaction_pub_date', 'reaction_status')
    search_fields = ('reaction_to_pub', 'reaction_user', 'reaction_text', 'reaction_pub_date', 'reaction_status')


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AdsCategory, AgsCategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)

from django.contrib import admin
from . import models


class SingleObjectAdminMixin:
    def has_add_permission(self, request, obj=None):
        # Разрешаем создать только один объект
        settings_count = models.SiteSettings.objects.count()
        return settings_count < 1


# inline поле
class ServiceDescriptionsInline(admin.StackedInline):
    extra = 1
    model = models.ServiceDescriptions


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(SingleObjectAdminMixin, admin.ModelAdmin):
    pass


@admin.register(models.CompanyContacts)
class CompanyContactsAdmin(SingleObjectAdminMixin, admin.ModelAdmin):
    pass


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDescriptionsInline]


@admin.register(models.Masters)
class MastersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


@admin.register(models.Order)
class OrderAdmin(OrderAdmin):
    pass


@admin.register(models.YourModel)
class YourModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.TextPage, admin.ModelAdmin)
admin.site.register(models.FeedbackRequest, admin.ModelAdmin)
admin.site.register(models.TelegramBotCredentials, admin.ModelAdmin)

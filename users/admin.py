from django import forms
from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import KnowerUser


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    class Meta:
        model = KnowerUser
        fields = ["email", "first_name", "last_name", "mobile_number"]

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if not password:
            raise ValidationError("비밀번호를 입력하세요.")

        if not confirm_password:
            raise ValidationError("비밀번호를 재확인하세요.")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("비밀번호가 일치하지 않습니다.")

        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = KnowerUser
        fields = ["email", "first_name", "last_name", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserUpdateForm

    actions = ["make_inactivated", "make_activated"]
    list_display = [
        "email",
        "first_name",
        "last_name",
        "mobile_number",
        "is_active",
        "is_admin",
    ]
    list_filter = ["is_admin"]
    fieldsets = [
        ("인증 정보", {"fields": ["email", "password"]}),
        ("기본 정보", {"fields": ["mobile_number", "first_name", "last_name"]}),
        ("권한", {"fields": ["is_admin", "is_active"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password", "confirm_password"],
            },
        ),
    ]
    filter_horizontal = []
    ordering = ["email"]
    search_fields = ["email"]

    @admin.action(description="휴면 계정으로 전환하기")
    def make_inactivated(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"해당 계정이 휴면 계정으로 전환되었습니다.", messages.SUCCESS)

    @admin.action(description="활동 계정으로 전환하기")
    def make_activated(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"해당 계정이 활동 계정으로 전환되었습니다.", messages.SUCCESS)


admin.site.register(KnowerUser, UserAdmin)
admin.site.unregister(Group)

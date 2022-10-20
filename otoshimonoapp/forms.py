from django import forms

from otoshimonoapp.models import OtoshimonoInfo


class OtoshimonoRegisterForm(forms.ModelForm):
    """"落とし物登録画面のフォーム"""
    limit_image_size = 10 * 1024 * 1024

    class Meta:
        model = OtoshimonoInfo
        fields = ['obj_name', 'place_found', 'place_now', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_obj_name(self):
        obj_name = self.cleaned_data["obj_name"]
        if len(obj_name) > 200:
            raise forms.ValidationError(
                '200文字以内で入力してください。',
            )
        return obj_name

    def clean_image(self):
        image = self.cleaned_data["image"]
        if image is not None:
            if image.size > self.limit_image_size:
                raise forms.ValidationError(
                    '画像は10MB以下のものをアップロードしてください',
                )
        return image

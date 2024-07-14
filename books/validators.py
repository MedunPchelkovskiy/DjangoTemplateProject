from django.core.exceptions import ValidationError


def image_size_validator(image_file):
    if image_file.size > 3145728:
        raise ValidationError(f'Maximum size that can be uploaded is 5MB')

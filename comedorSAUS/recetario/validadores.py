from django.core.validators import FileExtensionValidator


imagen_validador = FileExtensionValidator(
    allowed_extensions=['png','jpg', 'jpeg'],
    message="Sólo se permiten imágenes PNG, JPG o JPEG"
)
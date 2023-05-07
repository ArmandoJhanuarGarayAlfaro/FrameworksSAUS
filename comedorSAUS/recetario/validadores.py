from django.core.validators import FileExtensionValidator


imagen_validador = FileExtensionValidator(
    allowed_extensions=['png','jpg'],
    message="Sólo se permiten imágenes PNG o JPG"
)
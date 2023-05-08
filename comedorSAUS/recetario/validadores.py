from django.core.validators import FileExtensionValidator, RegexValidator


imagen_validador = FileExtensionValidator(
    allowed_extensions=['png','jpg', 'jpeg'],
    message="Sólo se permiten imágenes PNG, JPG o JPEG"
)

rfc_validador = RegexValidator(
    regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$',
    message='El RFC no tiene un formato válido',
    code='rfc_invalido'
)
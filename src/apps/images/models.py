import os
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo = models.ImageField(
        _("image video"),
        upload_to="media",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg"])],
    )

    def __str__(self) -> str:
        return f"{self.uuid} | {self.photo.name}"

    @property
    def title(self) -> str:
        return os.path.split(self.photo.file.name)[-1]

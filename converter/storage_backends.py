from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
import os
import unicodedata

class UnicodeSafeStorage(FileSystemStorage):
    def get_valid_name(self, name):
        # Normalize Unicode characters
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
        name = super().get_valid_name(name)
        return name
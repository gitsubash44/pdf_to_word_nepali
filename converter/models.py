from django.db import models
import os
from django.utils.text import slugify
import unicodedata

def pdf_upload_path(instance, filename):
    # Normalize and sanitize filename
    name, ext = os.path.splitext(filename)
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    safe_name = slugify(name) + ext.lower()
    return f'pdf_files/{safe_name}'

def word_upload_path(instance, filename):
    # Normalize and sanitize filename
    name, ext = os.path.splitext(filename)
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    safe_name = 'converted_' + slugify(name) + ext.lower()
    return f'word_files/{safe_name}'

class PDFFile(models.Model):
    file = models.FileField(upload_to=pdf_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return os.path.basename(self.file.name)

class ConvertedFile(models.Model):
    original_pdf = models.ForeignKey(PDFFile, on_delete=models.CASCADE)
    word_file = models.FileField(upload_to=word_upload_path)
    converted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return os.path.basename(self.word_file.name)
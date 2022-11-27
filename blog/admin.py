from pathlib import Path
import logging
#import subprocess

from django.contrib import admin

from blog.models import Post, Etiqueta

logging.basicConfig(filename='adminlogs.log', encoding='utf-8', level=logging.DEBUG)

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        #logging.info(form.cleaned_data['contenido'])
        root = Path.home()
        archivo = Path(root, 'saas/bestpreicfes/blog/templates/blog', 'sandbox.html')
        with open(archivo, 'a') as html:
            html.write(form.cleaned_data['contenido'])
            logging.info('Content copied...')
        #subprocess.check_call('npx tailwindcss -i ./src/input.css -o ./static/css/output.css', shell=True)
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Etiqueta)

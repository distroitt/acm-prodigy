import pdfkit
import os
from django.conf import settings
from django.template.loader import render_to_string

PATH_WKHTMLTOPDF = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_WKHTMLTOPDF)

TEMPLATE_PATH = os.path.join('templates', 'diplom', 'diplom.html')
CSS_PATH = os.path.join('static', 'assets', 'css', 'style.css')
OUTPUT_PDF = 'diploma.pdf'


def generate_diploma():
    try:
        html_content = render_to_string(TEMPLATE_PATH, context={
            'variable': 'value'
        })

        with open(CSS_PATH, 'r', encoding='utf-8') as css_file:
            css_content = f"<style>{css_file.read()}</style>"

        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            {css_content}
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        pdfkit.from_string(full_html, OUTPUT_PDF, configuration=CONFIG)
        print(f"Диплом успешно сохранён в {OUTPUT_PDF}")

    except Exception as e:
        print(f"Ошибка генерации: {str(e)}")


if __name__ == "__main__":
    if not settings.configured:
        settings.configure()

    generate_diploma()
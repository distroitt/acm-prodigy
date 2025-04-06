import pdfkit
import os
from django.conf import settings
from django.template.loader import render_to_string

PATH_WKHTMLTOPDF = r'/usr/local/bin/wkhtmltopdf'
CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_WKHTMLTOPDF)

TEMPLATE_PATH = os.path.join('templates', 'diplom', 'diplom.html')
CSS_PATH = os.path.join('static', 'assets', 'css', 'style.css')



def generate_diploma(participants, team, coach):
    try:
        output_pdf = f'diploma{team}.pdf'
        html_content = render_to_string(TEMPLATE_PATH, context={
            'participants': participants,
            'team': team,
            'coach': coach,
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

        pdfkit.from_string(full_html, output_pdf, configuration=CONFIG)
        print(f"Диплом успешно сохранён в {output_pdf}")

    except Exception as e:
        print(f"Ошибка генерации: {str(e)}")
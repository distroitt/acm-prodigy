import os
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

TEMPLATE_PATH = os.path.join('templates', 'diplom', 'diplom.html')
CSS_PATH = os.path.join('static', 'assets', 'css', 'style.css')
OUTPUT_PDF = 'diploma.pdf'


def generate_diploma():
    try:
        html_content = render_to_string(TEMPLATE_PATH, context={
            'variable': 'value'
        })

        with open(CSS_PATH, 'r', encoding='utf-8') as css_file:
            css_content = css_file.read()

        font_config = FontConfiguration()
        html = HTML(string=html_content)
        css = CSS(string=css_content, font_config=font_config)

        html.write_pdf(
            OUTPUT_PDF,
            stylesheets=[css],
            font_config=font_config
        )

        print(f"Диплом успешно сохранён в {OUTPUT_PDF}")

    except Exception as e:
        print(f"Ошибка генерации: {str(e)}")


if __name__ == "__main__":
    if not settings.configured:
        settings.configure(
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
            }],
            STATIC_URL='/static/',
            STATICFILES_DIRS=[os.path.join(os.path.dirname(__file__), 'static')]
        )

    generate_diploma()
from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p^hlzk-*sjpul#2@-3zq9r1s7t(gtyhfo(i0g(n1+lr!sq2ktv'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

# Provide set of theme choices
# NB this method of selection may break in future versions of coderedcms
from coderedcms.settings import cr_settings
cr_settings['FRONTEND_THEME_CHOICES'] = (
        ('ceda_div/0.3.2', 'CEDA Division Bootstap4 theme based on Bootswatch Flatly'),
        ('jasmin/0.2.1', 'JASMIN Bootstap4 theme 0.2.1 based on Bootswatch Flatly'),
        ('jasmin/0.3', 'JASMIN Bootstap4 theme 0.3 blue primary'),
        ('jasmin/0.3c03', 'JASMIN Bootstap4 theme 0.3c03 cyan primary'),
        ('jasmin/0.3c04', 'JASMIN Bootstap4 theme 0.3c04 light green primary')
)

# Append to choice of page templates for specific page types
# NB this method of selection may break in future versions of coderedcms
cr_settings['FRONTEND_TEMPLATES_PAGES']["webpage"] = (
    ("apptheme_codered/webpage_custom_example.html", "webpage custom example"),
)
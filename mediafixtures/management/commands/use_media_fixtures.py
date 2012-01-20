import os

from distutils import dir_util
from django.conf import settings
from django.core.management import base as management


class Command(management.AppCommand):
    """
    Copy files from "fixtures/media/" directory of the given applications in to
    the directory specified by the settings.MEDIA_ROOT.

    Usefull alongside initial_data.* fixtures, so that you can have DB-fixtures
    and matching media-file fixtures. 
    """

    help = "TODO"

    def handle_app(self, app, **options):
        path = os.path.join(os.path.dirname(app.__file__), 'fixtures', 'media')

        if os.path.isdir(path):
            dir_util.copy_tree(path, settings.MEDIA_ROOT)

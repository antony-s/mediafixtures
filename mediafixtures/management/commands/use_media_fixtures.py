import os
import tempfile
import uuid
from distutils import dir_util
from optparse import make_option
from shutil import copytree, ignore_patterns, rmtree

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

    def __init__(self):
        super(Command, self).__init__()
        self.option_list = super(Command, self).option_list + (
            make_option('--ignore',
                help='ignore files according to a space-separeated list of patterns e.g. \'*.svn *.tmp\'',
                ),
        )

    def handle_app(self, app, **options):
        path = os.path.join(os.path.dirname(app.__file__), 'fixtures', 'media')
        ignores = options.get('ignore')
        tmp_dir = None

        if ignores:
            # Allows us to filter fixtures/media before merging into MEDIA_ROOT
            ignores_list = ignores.split()
            tmp_dir = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
            copytree(path, tmp_dir, ignore=ignore_patterns(*ignores_list))
            path = tmp_dir

        if os.path.isdir(path):
            dir_util.copy_tree(path, settings.MEDIA_ROOT)

        if tmp_dir:
            rmtree(tmp_dir)

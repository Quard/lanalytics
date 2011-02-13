import os
DIRNAME = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) +  '/../../')

COMPRESS = False
COMPRESS_VERSION = True
COMPRESS_YUI_BINARY = "%s/tools/yuicompressor-2.4.4.jar" % DIRNAME
COMPRESS_CSS_FILTERS = None

COMPRESS_CSS = {
    'main': {
        'source_filenames': ('css/reset.css', 'css/master.css',
        ),
        'output_filename': 'css/static/main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

COMPRESS_JS = {
    'main': {
        'source_filenames': (
        'js/lib/jquery-min.js',
        ),
        'output_filename': 'js/static/main.js',
    },
}
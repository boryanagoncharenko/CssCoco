# import json
# import os
# import platform
from subprocess import Popen, PIPE

COCO_PATH = 'src/gonzales_parser.js'


class ParseWrapper(object):

    @staticmethod
    def parse_css(css):
        encoded_css = css.encode('utf8')
        try:
            process = Popen(['node', COCO_PATH, encoded_css], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        except OSError:
            raise Exception('')

        out, err = process.communicate(input=encoded_css)
        if out:
            return out

        return err
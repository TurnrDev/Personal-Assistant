import os
from distutils.util import strtobool

from papy.utils import ai_ask

def shutdown():
    if strtobool(ai_ask("Are you sure you want to shutdown?")):
        os.system("shutdown /s /t 1")

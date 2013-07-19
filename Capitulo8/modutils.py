# -*- coding: latin1 -*-
"""
modutils => rotinas utilitárias para módulos
"""

import os.path
import sys
import glob

def find(txt):
    """encontra módulos que tem o nome
    contendo o parâmetro
    """

    resp = []

    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)

        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)

    return resp

#!/usr/bin/env python3

import os

# import all names from core conf:
#   sphinx injects a global named `tags` into the conf.py namespace. Therefore, simply importing all names from the core config
#   file (`from conf_core import *`) does not suffice because core_conf.py then lacks access to this global. Instead we follow a
#   similar approach to sphinx itself (although a bit simpler because we're just proxying): exec the core config file with a
#   shared globals namespace, both so conf_core.py can access the tags global and so all names from conf_core.py get get bound
#   to this module's namespace.
#   (sphinx implementation for reference: https://github.com/sphinx-doc/sphinx/blob/799385f5558a888d1a143bf703d06b66d6717fe4/sphinx/config.py#L329)
core_conf_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "conf_core.py"))
with open(core_conf_file) as f:
    code = compile(f.read(), core_conf_file, "exec")
    # share this file's globals namespace (both for reading and for writing)
    exec(code, globals())

#!/usr/bin/env python3

import os
import sys

# import all names from core conf
core_conf_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "conf_core.py"))
with open(core_conf_file, "r") as f:
    code = compile(f.read(), core_conf_file, "exec")
    # share this file's globals namespace (both for reading and for writing)
    exec(code, globals())

# override exclude patterns: don't exclude anything for product docs
exclude_patterns = []

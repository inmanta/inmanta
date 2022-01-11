#!/usr/bin/env python3

# import all names from core conf
sys.path.append(os.path.dirname(__file__))
from conf_core import *

# override exclude patterns: don't exclude anything for product docs
exclude_patterns = []

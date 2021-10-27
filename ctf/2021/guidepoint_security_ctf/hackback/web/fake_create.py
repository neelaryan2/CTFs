#!/usr/bin/env python3

import os
import sys

print(os.popen(' '.join(sys.argv[1:])).read())

#!/usr/bin/env python3

import os
import sys

start_url=sys.argv[1]
print(start_url)
os.system("wget" + " " + start_url)

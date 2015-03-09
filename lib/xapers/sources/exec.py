#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import subprocess
import shlex

description = "Launch external program to get the bibtex"

def fetch_bibtex(id):
    p = subprocess.Popen(shlex.split(id), stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read().decode("utf-8")

#!/bin/env python
# -*- coding=utf-8 -*-
import logging

API_URL = "http://127.0.0.1:8775"

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOG = {
"level" : LEVELS["debug"],
"filename" : "autosqli.log",
"format" : '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s',
"datefmt" : '%Y-%m-%d %H:%M:%S'
}

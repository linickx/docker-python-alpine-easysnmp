#!/usr/bin/env python
# coding=utf-8
"""
    easysnmp
"""

import sys
import logging

logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger("test")

try:
    from easysnmp import snmp_get
    logger.info("easysnmp Works!")
except:
    logger.critical("easysnmp Not installed")
    logger.debug("Exception: %s", sys.exc_info()[1])
    sys.exit(1)



# Grab a single piece of information using an SNMP GET
result = snmp_get('sysName.0', hostname='localhost', community='public', version=2)
print(result.value)

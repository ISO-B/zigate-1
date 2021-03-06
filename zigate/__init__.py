#!/usr/bin/env python3
#
# Copyright (c) 2018 Sébastien RAMAGE
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

from .core import (ZiGate, ZiGateWiFi)
from .const import *  # noqa
from .version import __version__  # noqa
from pydispatch import dispatcher

__all__ = ['ZiGate', 'ZiGateWiFi',
           'dispatcher']


def connect(port=None, host=None,
            path='~/.zigate.json',
            auto_start=True,
            auto_save=True):
    '''
    connect to zigate USB or WiFi
    specify USB port OR host IP
    Example :
    port='/dev/ttyS0'
    host='192.168.0.10' OR '192.168.0.10:1234'

    in both case you could set 'auto' to auto discover the zigate
    '''
    if host:
        port = None
        host = host.split(':', 1)
        if len(host) == 2:
            port = int(host[1])
        host = host[0]
        z = ZiGateWiFi(host,
                       port,
                       path=path,
                       auto_start=auto_start,
                       auto_save=auto_save)
    else:
        z = ZiGate(port,
                   path=path,
                   auto_start=auto_start,
                   auto_save=auto_save)
    return z

# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


from . import snowobs


GET_FUNCTIONS = {
    snowobs.OBSERVATION_TYPE: snowobs.get_records,
}
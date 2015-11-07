#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crc and uuid properties
"""
from __future__ import unicode_literals

import regex as re

from rebulk import Rebulk
from ..common.validators import seps_surround


def crc():
    """
    Builder for rebulk object.
    :return: Created Rebulk object
    :rtype: Rebulk
    """
    rebulk = Rebulk().regex_defaults(flags=re.IGNORECASE)
    rebulk.defaults(validator=seps_surround)

    rebulk.regex('(?:[a-fA-F]|[0-9]){8}', name='crc32')

    rebulk.functional(guess_idnumber, name='uuid')
    return rebulk


_DIGIT = 0
_LETTER = 1
_OTHER = 2

_idnum = re.compile(r'(?P<uuid>[a-zA-Z0-9-]{20,})')  # 1.0, (0, 0))


def guess_idnumber(string):
    """
    Guess id number function
    :param string:
    :type string:
    :return:
    :rtype:
    """
    # pylint:disable=invalid-name
    ret = []

    matches = list(_idnum.finditer(string))
    for match in matches:
        result = match.groupdict()
        switch_count = 0
        switch_letter_count = 0
        letter_count = 0
        last_letter = None

        last = _LETTER
        for c in result['uuid']:
            if c in '0123456789':
                ci = _DIGIT
            elif c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                ci = _LETTER
                if c != last_letter:
                    switch_letter_count += 1
                last_letter = c
                letter_count += 1
            else:
                ci = _OTHER

            if ci != last:
                switch_count += 1

            last = ci

        # only return the result as probable if we alternate often between
        # char type (more likely for hash values than for common words)
        switch_ratio = float(switch_count) / len(result['uuid'])
        letters_ratio = (float(switch_letter_count) / letter_count) if letter_count > 0 else 1

        if switch_ratio > 0.4 and letters_ratio > 0.4:
            ret.append(match.span())

    return ret

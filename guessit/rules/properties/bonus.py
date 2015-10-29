#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bonus support
"""
import regex as re
from rebulk import Rebulk, AppendMatch, Rule

from ..common.formatters import cleanup
from ..common.validators import seps_surround

BONUS = Rebulk().regex_defaults(flags=re.IGNORECASE)


BONUS.regex(r'x(\d+)', name='bonusNumber', private_parent=True, children=True, formatter=int,
            validator={'__parent__': lambda match: seps_surround},
            conflict_solver=lambda match, conflicting: match
            if conflicting.name in ['videoCodec', 'episodeNumber'] and 'bonus-conflict' not in conflicting.tags
            else '__default__')


class BonusTitleRule(Rule):
    """
    Abstract rule to validate audio profiles
    """
    priority = 250
    consequence = AppendMatch

    def when(self, matches, context):
        bonus_number = matches.named('bonusNumber', lambda match: not match.private, index=0)
        if bonus_number:
            filepath = matches.markers.at_match(bonus_number, lambda marker: marker.name == 'path', 0)
            hole = matches.holes(bonus_number.end, filepath.end + 1, formatter=cleanup, index=0)
            if hole and hole.value:
                hole.name = 'bonusTitle'
                return hole


BONUS.rules(BonusTitleRule)

# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from collections import namedtuple
from typing import Any, Dict, List, Tuple, Union

WMIMetric = namedtuple('WMIMetric', ['name', 'value', 'tags'])
WMIProperties = Tuple[Dict[str, Tuple[str, str]], List[str]]
TagQuery = List[str]
WMIObject = Dict[str, Any]
WMIFilter = Union[str, List[str]]

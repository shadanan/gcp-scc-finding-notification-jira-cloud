#!/usr/bin/env python3
from cf.main import process_notification

with open("activate_finding.dat") as fp:
    data = fp.read()
event = {"data": data}
process_notification(event, None)

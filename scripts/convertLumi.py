#!/usr/bin/env python2.6

import logging
import json
import sys, os
mask = json.loads(open(sys.argv[1],'r').read())

runs = []
lumis = []
lumicount = 0
for run in sorted(mask.keys()):
    runs.append(run)
    lumisForThisRun = []
    for lumiTuple in mask[run]:
        lumisForThisRun.append("%s,%s" % (lumiTuple[0], lumiTuple[1]))
        lumicount += lumiTuple[0] + lumiTuple[1]
    lumis.append(",".join(lumisForThisRun))

print json.dumps( { 'runs': runs, 'lumis': lumis }, indent=0,
                                                    sort_keys = True)

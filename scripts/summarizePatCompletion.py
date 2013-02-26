#!/usr/bin/env python2.6

import os
import sys
import pwd
import json
import pprint

from optparse import OptionParser
from CMSYAAT.RequestManager import RequestManager
from CMSYAAT.Utilities import Logging, CommandLineHandler
from CMSYAAT.Utilities.Table import printTable

Logging.initLogging()

# TODO: Get some common options parsing
commonArgs = ['endpoint','wmstat']
parser = CommandLineHandler.getParser(commonArgs)

(options, args) = parser.parse_args()
CommandLineHandler.validateArguments(options, args)

# should implement
# http://code.activestate.com/recipes/574459-easier-positional-arguments-for-optparse/
if len(args) == 0:
    logging.error("You must provide a request to examine")
    sys.exit(1)

reqmgr = RequestManager( endpoint = options.endpoint,
                         wmstat   = options.wmstat )
for requestName in args:
    request = reqmgr.getRequest( requestName )
    requestDocument = request.getRequestDocument()
    resultSummary = request.getJobResultsSummary()
    countSummary = request.getJobCountSummary()
    countSummaryBySite = request.getJobCountSummaryPerSite()

    inputDataset = requestDocument['inputdataset']
    if countSummary['total'] == 0 or len(countSummaryBySite) == 0:
        jobPercentage = "  0.00%"
    else:
        totalJobs = int(requestDocument['total_jobs']) or 1
        doneCount = 0
        jobStatusNames = set()
        for site in countSummaryBySite:
            jobStatusNames.update(countSummaryBySite[site].keys())
    
        #print countSummaryBySite
        statusOrder = sorted(jobStatusNames)
        statusOrder.remove('total')
        statusOrder.append('uninjected')
        statusOrder.append('total')
        # copy the header for the table
        header = statusOrder[:]
        header.insert(0,'site')
        data = []
        for site in countSummaryBySite:
            siteRow = [site]
            for state in statusOrder:
                siteRow.append("%s" % countSummaryBySite[site].get(state,'0'))
            data.append(siteRow)
        totalRow = ['Total']
        for state in ['failed', 'success']:
            stateCounter = 0
            for site in countSummaryBySite:
                stateCounter += int(countSummaryBySite[site].get(state,0))
            totalRow.append("%s" % stateCounter)
            doneCount += stateCounter
        injectedTotal = stateCounter
        #print "got %s %s " % (doneCount, totalJobs)
        jobPercentage = "%6.2f%%" % (float(doneCount)/float(totalJobs) * 50.0)
    print "%s %s" % (jobPercentage, inputDataset)

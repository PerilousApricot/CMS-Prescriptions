#!/usr/bin/env python2.6

# get weird with it
import os
import sys
import time
import json
import pprint
from CMSYAAT.RequestManager import RequestManager

if len(sys.argv) == 2:
    jenkins = sys.argv[1]
else:
    jenkins = 'testing'

# TODO: these shouldprobably be command line options

mcSamples = [
        #'/ZJetToMuMu_Pt-50to80_TuneZ2star_8TeV_pythia6/None-20130206162922/USER'        
        '/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/None-20130206162922/USER',
        '/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/None-20130206162922/USER',
        '/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/None-20130206162922/USER',
        '/T_s-channel_TuneZ2star_8TeV-powheg-tauola/None-20130206162922/USER',
        '/T_t-channel_TuneZ2star_8TeV-powheg-tauola/None-20130206162922/USER',
        '/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/jan302103tlbsm-20130130074834/USER',
        '/ZJetToMuMu_Pt-0to15_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-120to170_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-15to20_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-170to230_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-20to30_TuneZ2star_8TeV_pythia6/None-/USER',
        '/ZJetToMuMu_Pt-20to30_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-230to300_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-300_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-30to50_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-50to80_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        '/ZJetToMuMu_Pt-80to120_TuneZ2star_8TeV_pythia6/None-20130206162922/USER',
        ]

dataSamples = [ 
        '/MET/meloam_feb12_tlbsm53x2_Run2012A_13Jul2012_v1-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012A_recover_06Aug2012_v1-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012B_13Jul2012_v1-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012C_24Aug2012_v1-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012C_EcalRecover_11Dec2012_v1-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012C_PromptReco_v2-20130212222033/USER',
        '/MET/meloam_feb12_tlbsm53x2_Run2012D_PromptReco_v1-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012A_13Jul2012_v1-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012A_recover_06Aug2012_v1-20130212213007/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012B_13Jul2012_v1-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012C_24Aug2012_v1-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012C_EcalRecover_11Dec2012_v1-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012C_PromptReco_v2-20130212222033/USER',
        '/SingleMu/meloam_feb12_tlbsm53x2_Run2012D_PromptReco_v1-20130212222033/USER',
        ]

reqmgr = RequestManager( 
                    endpoint = 'https://se9.accre.vanderbilt.edu:8443/reqmgr'
                 )

allSamples = []
allSamples.extend(mcSamples)
allSamples.extend(dataSamples)

requestIDs = []

requestJSON = { "CMSSWVersion": "CMSSW_5_3_3_patch1",
            "DbsUrl" : "http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_02/servlet/DBSServlet",
            "AsyncDest": "T2_US_Vanderbilt",
            "GlobalTag": "START53_V7E::All",
            "MergedLFNBase" : "/store/user/meloam",
            "UnmergedLFNBase" : "/store/temp/user/meloam",
              "ForceUserOutput" : 1,
              "ForceUserStorage" : 1,
              "forceUserStorage" : 1,
            "RequestPriority": 10000,
            "TimePerEvent": 0.5,
            "EnableNewStageout": 1,
            "FilterEfficiency": 1,
            "ScramArch": "slc5_amd64_gcc462",
            "RequestType" : "MeloProcessing",
            "RequestNumEvents": 1,
            "inputMode": "couchDB",
            "CouchURL":"http://andrewmelo:QRz1_diQcKnH4KJh4ehse_47h-3q_SXq@andrewmelo.cloudant.com:5984",
            "CouchDBName":"wmagent_configcache",
            "ConfigCacheID": "b63b1d4634d28520e53f6b5941c7f72a",
            "EventsPerLumi": 1,
            "filterEfficiency": 1,
            "MCPileup": "",
            "FirstEvent": 1,
            "DataTier": "USER",
            "Memory": 2000000000,
            "SizePerEvent":102400000,
            "maxRSS": 4294967296,
            "maxVSize": 4294967296,
            "SoftTimeout": 36000,
            "FirstLumi": 1,
            "Requestor": "meloam",
            "Username": "meloam",
            "RequestorDN": "/DC=org/DC=doegrids/OU=People/CN=Andrew Malone Melo 788499",
            "Group": "testing",
            "TotalTime": 14400,
            "Team" : "PriorityTeam",
            "userSandbox" : "root://xrootd.unl.edu:1094//store/user/meloam/sandboxes/edmntuple-sandboxv2.tgz",
            "userFiles" : ['Jec12_V2_L1FastJet_AK5PFchs.txt','Jec12_V2_L2Relative_AK5PFchs.txt','Jec12_V2_L3Absolute_AK5PFchs.txt','Jec12_V2_L2L3Residual_AK5PFchs.txt','Jec12_V2_Uncertainty_AK5PFchs.txt'], 
            "ValidStatus" : "VALID"
}

# MC   - b63b1d4634d28520e53f6b5941d33bcb
# DATA - 025b9c1b6853f78ac3bdf7091e2bc1fd
requestList = []
now = time.strftime("%Y%m%d%H%M%S", time.gmtime())
#allSamples = [allSamples[0]]
for sample in allSamples:
    if sample in mcSamples:
        requestJSON['ConfigCacheID'] = 'c7804c963ccd1ce51cf7c42e06147c93'
        requestJSON['GlobalTag'] = 'START53_V7E::All'
        lumiFilename = ''
        #lumiFilename = 'mc_test_wmagent.json'
        acqHelper = ''
    else:
        requestJSON['ConfigCacheID'] = 'e65186f44d26fb6cb1409e8f6b5670a3'
        requestJSON['GlobalTag'] = 'GR_P_V40_AN1::All'
        lumiFilename = 'data_all_wmagent.json'
        acqHelper = sample.split('/')[2].replace('-','_')
        acqHelper = '_'  + '_'.join(sample.split('_')[3:5])

    requestJSON['StdJobSplitArgs'] = { 'events_per_job' : 75000,
                                       'max_events_per_lumi' : 100000,
                                       'splitOnRun' : False }
    if lumiFilename:
        lumiMask = json.loads(open(lumiFilename,'r').read())
        requestJSON['StdJobSplitArgs']['runs'] = lumiMask['runs']
        requestJSON['StdJobSplitArgs']['lumis'] = lumiMask['lumis']
    
    requestJSON['StdJobSplitAlgo'] = 'EventAwareLumiBased'
    requestJSON["RequestString"]  = "melo_edm_feb25v4"
    requestJSON['AcquisitionEra'] = 'meloam_feb25_edmntuple' + acqHelper
    requestJSON['ProcessingVersion'] = now
    requestJSON['InputDataset'] = sample
    newRequest = reqmgr.newRequest()
    newRequest.setRequestDict( requestJSON )
    print "Doing %s" % sample
    reqmgr.submitRequest( newRequest )
    print newRequest.getWorkflowName()
    requestList.append(newRequest)

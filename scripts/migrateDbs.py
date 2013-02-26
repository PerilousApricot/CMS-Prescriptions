#!/usr/bin/env python2.6

from DBSAPI.dbsApi import DbsApi
import sys

#blockToMigrate = '/T_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM#b6861908-0f9a-11e2-826d-00221959e72f'
blockToMigrate = sys.argv[0]

localDbs = 'https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet'
globalDbs = 'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
dbsArgs = { 'url' : localDbs,
            'level' : 'ERROR',
            'user'  : 'DEBUG',
            'version':'DBS_2_0_8' }

# /T_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM#b6861908-0f9a-11e2-826d-00221959e72f
# /MET/Run2012C-EcalRecover_11Dec2012-v1/AOD#b38eb352-4304-11e2-a593-003048f02c8a
#  /ZJetToMuMu_Pt-0to15_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM#d6a384ec-154d-11e2-a364-00221959e72f


dbsApi = DbsApi(dbsArgs)
blockList = list(set(sys.argv[1:]))
for blockToMigrate in blockList:
    print "Beginning to migrate %s" % blockToMigrate
    newBlock = dbsApi.dbsMigrateBlock(globalDbs, localDbs, blockToMigrate)
    print newBlock
print "Migration done"

cmsrel CMSSW_5_3_3
mv CMSSW_5_3_3 tlbsm_53x
cd tlbsm_53x/src
cmsenv
addpkg CommonTools/ParticleFlow V00-03-16
addpkg CommonTools/RecoUtils V00-00-09
addpkg CommonTools/RecoAlgos V00-03-23 
addpkg JetMETCorrections/Type1MET V04-06-09
addpkg PhysicsTools/PatAlgos V08-09-14-00
addpkg PhysicsTools/PatUtils V03-09-22
addpkg RecoParticleFlow/PFProducer V15-02-09  
addpkg RecoMET/METFilters V00-00-08
addpkg RecoMET/METAnalyzers V00-00-08
addpkg RecoJets/JetProducers V05-11-01
addpkg RecoJets/JetAlgorithms V04-05-00
cvs co -r tlbsm_53x TopQuarkAnalysis/TopPairBSM
cvs co -d EGamma/EGammaAnalysisTools -r V00-00-08 UserCode/EGamma/EGammaAnalysisTools
cd EGamma/EGammaAnalysisTools/data
cat download.url | xargs wget
cd -

cvs co -r V01-04-23 RecoTauTag/RecoTau #HCP + new discriminants
cvs co -r V01-04-10 RecoTauTag/Configuration
cvs co -r V00-04-00 CondFormats/EgammaObjects
#cvs up -r 1.31.6.4 PhysicsTools/PatAlgos/python/producersLayer1/tauProducer_cfi.py
#cvs up -r 1.52.10.4 PhysicsTools/PatAlgos/python/tools/tauTools.py

scram b -j 9

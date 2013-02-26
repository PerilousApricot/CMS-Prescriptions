
cmsrel CMSSW_5_3_8_patch1
cd CMSSW_5_3_8_patch1
cmsenv

# per 
#  https://twiki.cern.ch/twiki/bin/view/CMS/B2GTopLikeBSM53X#
addpkg DataFormats/PatCandidates V06-05-06-07
addpkg DataFormats/StdDictionaries V00-02-14
addpkg FWCore/GuiBrowsers V00-00-70
addpkg PhysicsTools/PatAlgos V08-09-52
addpkg RecoJets/JetProducers V05-11-01
addpkg RecoJets/JetAlgorithms V04-05-00
addpkg RecoMET/METAnalyzers V00-00-08
addpkg RecoParticleFlow/PFProducer V15-02-09
addpkg RecoTauTag/Configuration V01-04-10
addpkg RecoTauTag/RecoTau V01-04-23
cvs co -r tlbsm_53x TopQuarkAnalysis/TopPairBSM
cvs co -d EGamma/EGammaAnalysisTools -r V00-00-31 UserCode/EGamma/EGammaAnalysisTools
cd EGamma/EGammaAnalysisTools/data
cat download.url | xargs wget
cd -
addpkg RecoMET/METFilters
cvs co -d KStenson/TrackingFilters UserCode/KStenson/TrackingFilters
cp KStenson/TrackingFilters/plugins/TobTecFakesFilter.cc RecoMET/METFilters/plugins/
cp KStenson/TrackingFilters/python/tobtecfakesfilter_cfi.py RecoMET/METFilters/python
rm -r KStenson/TrackingFilters

scram b -j 9

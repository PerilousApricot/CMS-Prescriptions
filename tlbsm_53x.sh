
# note, this pulls some newer versions of packages than used to exist in the previous
# recipe. I checked https://cmstags.cern.ch/tc/#Releases and removed addpkg statements
cmsrel CMSSW_5_3_7_patch4
cd CMSSW_5_3_7_patch4/src
cmsenv
# from PAT recommendation:
#   https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X#V08_09_51
addpkg DataFormats/PatCandidates V06-05-06-05
addpkg DataFormats/StdDictionaries V00-02-14
addpkg PhysicsTools/PatAlgos V08-09-51
addpkg FWCore/GuiBrowsers V00-00-70


# Previous tlbsm packages. I culled ones that have a more recent tag in the CMSSW release
# The first line is an exception, the (more recent) PAT recipe asks for an older version than
# what we had before. Not sure what to do with that
addpkg RecoParticleFlow/PFProducer V15-02-06
addpkg RecoMET/METAnalyzers V00-00-08
addpkg RecoJets/JetProducers V05-11-01
addpkg RecoJets/JetAlgorithms V04-05-00
cvs co -r tlbsm_53x TopQuarkAnalysis/TopPairBSM
cvs co -d EGamma/EGammaAnalysisTools -r V00-00-08 UserCode/EGamma/EGammaAnalysisTools
cd EGamma/EGammaAnalysisTools/data
cat download.url | xargs -P4 wget
cd -

# Get TauID stuff
# from
#  https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATReleaseNotes52X#V08_09_51
# and
#  https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#52X_53X
cvs co -r V01-04-23 RecoTauTag/RecoTau #HCP + new discriminants
cvs co -r V01-04-10 RecoTauTag/Configuration
# unneeded (same version is in this CMSSW version, but it's still in the PAT recommendation?
#cvs co -r V00-04-00 CondFormats/EgammaObjects

# grumble...
perl -p -i -e 's!if mod.startswith\("kt6"\):!if mod.startswith("kt6") and mod.endswith("Jets"+postfix):!' PhysicsTools/PatAlgos/python/tools/pfTools.py


scram b -j 9

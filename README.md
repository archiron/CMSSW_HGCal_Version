# CMSSW_HGCal_Version
Dev version for HGCal

This can be used from RECO files with _cfg files.

I. Installation
## create release support
cmsrel CMSSW_9_3_0_pre4 [1]
cd CMSSW_9_3_0_pre4_TEST_01/src/
cmsenv

## add package
git cms-addpkg Validation/RecoEgamma [2]

git cms-addpkg DQMOffline/EGamma [3]

git cms-addpkg TrackingTools/Configuration [4]

## add HGCal updates. MUST be added AFTER the originals !
git remote add archiron https://github.com/archiron/CMSSW_HGCal_Version
git fetch archiron
git checkout archiron/master  -- Validation/RecoEgamma [2]
git checkout archiron/master  -- TrackingTools/Configuration/python [3]
git checkout archiron/master  -- DQMOffline/EGamma [4]

## compilation
scramv1 b

II. Use

RECO validations use 2 steps (analyze & finalize [5]). You can run it with :
# step 1 - analyze

cmsRun ElectronMcSignalValidation_gedGsfElectrons_cfg.py ZEE_14

# step 2 - finalize

cmsRun ElectronMcSignalPostValidation_cfg.py ZEE_14

ZEE_14 is the DataSet sample.

The step 1 produce a file named : electronHistos.ValZEE_14Startup_gedGsfE_a.root
which is used as input in step2. Step 2 provide a file named :

DQM_V0001_R000000001__electronHistos__RelValZEE_14Startup_gedGsfE__RECO3.root
wich provides the histos.

We write the GlobalTag in each _cfg file ( process.GlobalTag.globaltag = ... ).

In order to simplify most of entry values, we use an additional file : electronValidationCheck_Env.py
The choice between Phase2 (HGCal) and Run2_2017 (classical RECO) in _cfg file( process = cms.Process(...) ) is made in this additional file.
This file is used to fill some values one time only.
- beginTag : 'Phase2' or 'Run2_2017'
- dd_tier : GEN-SIM-RECO, MINIAODSIM, GEN-SIM-DIGI-RECO, ...
- tag_startup : the complete GlobalTag (for example 93X_upgrade2023_realistic_v0_D17PU200, where the GlobalTag is 93X_upgrade2023_realistic_v0).
- data_version : v1, v2.
- test_global_tag : used for compatibility with Oval. same as tag_startup
- dd_cond : same as tag_startup-data_version. You can add PU25ns_ at the beginning for PUs.

- outputFile : name of the output file for step1. 
- inputPostFile : generation of the DQM_V00X... root file at the end of step2.
- DD_RELEASE : same as CMSSW_VERSION
- DD_SOURCE : where to search root files for validation : for example : 
/eos/cms/store/relval/CMSSW_9_3_0_pre4/RelValZEE_14/GEN-SIM-RECO/PU25ns_93X_upgrade2023_realistic_v0_D17PU200-v1

BE CAREFUL : if you want to make comparison between ecalDrivenGsfElectronsFromMultiCl and ecalDrivenGsfElectrons for example,
the generated final root files are the SAME !

---- Notes

[1] or other release you want. 

[2] needed for scripts. It is here where you can modify ecalDrivenGsfElectronsFromMultiCl into ecalDrivenGsfElectrons in python/ElectronMcSignalValidator_gedGsfElectrons_cfi.py 

[3] optionnal. Used for scripts/electronDataDiscovery.py with eos path. 

[4] optionnal : used if there is some modifications with _Keep_ statements. 

[5] Harvesting step

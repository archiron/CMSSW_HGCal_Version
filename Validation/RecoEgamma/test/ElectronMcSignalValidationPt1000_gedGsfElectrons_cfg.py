
import sys
import os
import DQMOffline.EGamma.electronDataDiscovery as dd
import FWCore.ParameterSet.Config as cms

from electronValidationCheck_Env import env
cmsEnv = env() # be careful, cmsEnv != cmsenv. cmsEnv is local

cmsEnv.checkSample() # check the sample value
cmsEnv.checkValues()

from Configuration.StandardSequences.Eras import eras
if cmsEnv.beginTag() == 'Run2_2017':
    process = cms.Process("electronValidation",eras.Run2_2017)
else:
    process = cms.Process('electronValidation',eras.Phase2) 

process.DQMStore = cms.Service("DQMStore")
process.load("DQMServices.Components.DQMStoreStats_cfi")
from DQMServices.Components.DQMStoreStats_cfi import *
dqmStoreStats.runOnEndJob = cms.untracked.bool(True)

#max_skipped = 165
max_number = -1 # 10 # number of events
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(max_number))
#process.source = cms.Source ("PoolSource",skipEvents = cms.untracked.uint32(max_skipped), fileNames = cms.untracked.vstring(),secondaryFileNames = cms.untracked.vstring())

#process.source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring(),secondaryFileNames = cms.untracked.vstring()) # std value
#process.source.fileNames.extend(dd.search())  # to be commented for local run only

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring(
    [
    #'file:/eos/user/a/archiron/HGCal_Shares/step3_A8F750A4-6D87-E711-A476-0CC47A4D7600.root',
    #'file:/eos/user/a/archiron/HGCal_Shares/step3_AE79E794-7287-E711-9D2A-0CC47A78A3EE.root',
    #'file:/eos/user/a/archiron/HGCal_Shares/step3_D801BDAF-7087-E711-AEF8-0CC47A7C354A.root',
    
    #'file:/eos/user/r/rovere/www/shared/step3.root',

    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/00FF6760-F8A6-E711-AA68-0025905A60D6.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/0A26CCF0-F5A6-E711-8C50-0025905B857E.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/1AF12BCC-F8A6-E711-B089-0025905A60D0.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/2AF566EE-FAA6-E711-BA3D-0025905B860E.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/321C4442-09A7-E711-9BBD-0CC47A4C8F0A.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/3C7CDE63-F7A6-E711-A13F-0CC47A4D7618.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/4E5D5E53-08A7-E711-8FFC-003048FF9ABC.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/52B58CEB-08A7-E711-B5A3-0CC47A78A4A6.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/56D9E02B-F7A6-E711-8A07-0CC47A4C8E8A.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/56F81F93-F5A6-E711-A87D-0CC47A4C8E14.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/5E776718-06A7-E711-9EF1-0CC47A7C34E6.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/7889725A-F1A6-E711-8442-0CC47A4D7618.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/78B617CB-F4A6-E711-BA4C-0CC47A4D7690.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/9402F52F-F5A6-E711-99B9-0CC47A7C356A.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/9A702D5A-F6A6-E711-BB94-0025905A6060.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/C00FC03B-12A7-E711-A207-0CC47A4C8ECE.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/C06FD61F-FEA6-E711-AFD2-0025905B856C.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/DE1D2C3F-12A7-E711-8C9C-0025905A608E.root',
    'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_3_2/RelValQCD_Pt-15To7000_Flat_14TeV/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/EA4B5A19-F8A6-E711-86AD-0025905A60B4.root',



    ]
    )
)  # for local run only

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("Configuration.StandardSequences.EDMtoMEAtJobEnd_cff") # new 
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = os.environ['TEST_GLOBAL_TAG']#+'::All'
process.GlobalTag.globaltag = '93X_upgrade2023_realistic_v2'
#process.GlobalTag.globaltag = '93X_upgrade2023_realistic_v0'
#process.GlobalTag.globaltag = '93X_mc2017_realistic_v1'

# FOR DATA REDONE FROM RAW, ONE MUST HIDE IsoFromDeps
# CONFIGURATION
process.load("Validation.RecoEgamma.electronIsoFromDeps_cff")
process.load("Validation.RecoEgamma.ElectronMcSignalValidatorPt1000_gedGsfElectrons_cfi")

# load DQM
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.EDM = cms.OutputModule("PoolOutputModule",
outputCommands = cms.untracked.vstring('drop *',"keep *_MEtoEDMConverter_*_*"),
fileName = cms.untracked.string(os.environ['outputFile'].replace(".root", "_a.root"))
#fileName = cms.untracked.string('electronHistos.ValFullZEEStartup_13_gedGsfE_a.root') # for local run only
)

process.electronMcSignalValidatorPt1000.InputFolderName = cms.string("EgammaV/ElectronMcSignalValidatorPt1000")
process.electronMcSignalValidatorPt1000.OutputFolderName = cms.string("EgammaV/ElectronMcSignalValidatorPt1000")

process.p = cms.Path(process.electronMcSignalValidatorPt1000 * process.MEtoEDMConverter * process.dqmStoreStats)

process.outpath = cms.EndPath(
process.EDM,
)

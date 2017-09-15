
import sys
import os
import DQMOffline.EGamma.electronDataDiscovery as dd
import FWCore.ParameterSet.Config as cms

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
# first arg : cmsRun
# second arg : name of the _cfg file
# third arg : sample name (ex. ZEE_14)

from electronValidationCheck_Env import env
cmsEnv = env() # be careful, cmsEnv != cmsenv. cmsEnv is local

cmsEnv.checkSample() # check the sample value
cmsEnv.checkValues()

if cmsEnv.beginTag == 'Run2_2017':
    process = cms.Process("electronValidation",eras.Run2_2017)
else:
    from Configuration.StandardSequences.Eras import eras
    process = cms.Process('electronValidation',eras.Phase2) 

process.DQMStore = cms.Service("DQMStore")
process.load("DQMServices.Components.DQMStoreStats_cfi")
from DQMServices.Components.DQMStoreStats_cfi import *
dqmStoreStats.runOnEndJob = cms.untracked.bool(True)

#max_skipped = 165
max_number = 10 # -1 # number of events
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(max_number))
#process.source = cms.Source ("PoolSource",skipEvents = cms.untracked.uint32(max_skipped), fileNames = cms.untracked.vstring(),secondaryFileNames = cms.untracked.vstring())
process.source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring(),secondaryFileNames = cms.untracked.vstring()) # std value
#process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring("file:electronMultiCl.root"))  # for local run only
process.source.fileNames.extend(dd.search())  # to be commented for local run only

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
#process.GlobalTag.globaltag = os.environ['TEST_GLOBAL_TAG'] + '::All'
process.GlobalTag.globaltag = '93X_upgrade2023_realistic_v0'
#process.GlobalTag.globaltag = '93X_mc2017_realistic_v1'
#process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v10'

# FOR DATA REDONE FROM RAW, ONE MUST HIDE IsoFromDeps
# CONFIGURATION
process.load("Validation.RecoEgamma.electronIsoFromDeps_cff")
process.load("Validation.RecoEgamma.ElectronMcSignalValidator_gedGsfElectrons_cfi")

# load DQM
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.EDM = cms.OutputModule("PoolOutputModule",
outputCommands = cms.untracked.vstring('drop *',"keep *_MEtoEDMConverter_*_*"),
fileName = cms.untracked.string(os.environ['outputFile'].replace(".root", "_a.root"))
#fileName = cms.untracked.string('electronHistos.ValFullZEEStartup_13_gedGsfE_a.root') # for local run only
)

process.electronMcSignalValidator.InputFolderName = cms.string("EgammaV/ElectronMcSignalValidator")
process.electronMcSignalValidator.OutputFolderName = cms.string("EgammaV/ElectronMcSignalValidator")

#process.p = cms.Path(process.electronIsoFromDeps * process.electronMcSignalValidator * process.MEtoEDMConverter * process.dqmStoreStats)
process.p = cms.Path(process.electronMcSignalValidator * process.MEtoEDMConverter * process.dqmStoreStats)

process.outpath = cms.EndPath(
process.EDM,
)

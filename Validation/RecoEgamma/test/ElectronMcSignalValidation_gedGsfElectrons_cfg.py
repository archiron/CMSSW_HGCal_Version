
import sys
import os
import DQMOffline.EGamma.electronDataDiscovery as dd
import FWCore.ParameterSet.Config as cms

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
# first arg : cmsRun
# second arg : name of the _cfg file
# third arg : sample name (ex. ZEE_14)
print "os.environ['DD_SAMPLE'] :", os.environ['DD_SAMPLE']
if os.environ['DD_SAMPLE'] == '':
    if ( len(sys.argv) > 2 ):
        sampleName = str(sys.argv[2])
        os.environ['DD_SAMPLE'] = 'RelVal' + sampleName
        print 'Sample name:', sampleName, ' - ', os.environ['DD_SAMPLE']
    else:
        print '===================='
        print 'no sample name, quit'
        print '===================='
        quit()

from Configuration.StandardSequences.Eras import eras 

#process = cms.Process("electronValidation",eras.Run2_2017)
process = cms.Process('electronValidation',eras.Phase2) 

process.DQMStore = cms.Service("DQMStore")
process.load("DQMServices.Components.DQMStoreStats_cfi")
from DQMServices.Components.DQMStoreStats_cfi import *
dqmStoreStats.runOnEndJob = cms.untracked.bool(True)

outputFile = 'electronHistos.Val' + os.environ['DD_SAMPLE'] + 'Startup_gedGsfE.root'
os.environ['outputFile'] = outputFile

from ElectronMcValidation_env import env
cmsEnv = env() # be careful, cmsEnv != cmsenv. cmsEnv is local

print '-----'
print cmsEnv.dd_tier()
print cmsEnv.tag_startup()
print cmsEnv.data_version()
print cmsEnv.test_global_tag()
print cmsEnv.dd_cond()
print '-----'

if os.environ['DD_TIER'] == '':
    os.environ['DD_TIER'] = cmsEnv.dd_tier() # 'GEN-SIM-RECO'
if 'TAG_STARTUP' not in os.environ: # TAG_STARTUP from OvalFile
    os.environ['TAG_STARTUP'] = cmsEnv.tag_startup() # '93X_upgrade2023_realistic_v0_D17PU200' 
#elif os.environ['TAG_STARTUP'] == '':
#    os.environ['TAG_STARTUP'] = cmsEnv.tag_startup() # '93X_upgrade2023_realistic_v0_D17PU200'
if 'DATA_VERSION' not in os.environ: # DATA_VERSION from OvalFile
#if os.environ['DATA_VERSION'] == '':
    os.environ['DATA_VERSION'] = cmsEnv.data_version() # 'v1'
if 'TEST_GLOBAL_TAG' not in os.environ: # TEST_GLOBAL_TAG from OvalFile
#if os.environ['TEST_GLOBAL_TAG'] == '':
    os.environ['TEST_GLOBAL_TAG'] = cmsEnv.test_global_tag() # os.environ['TAG_STARTUP']
if os.environ['DD_COND'] == '':
    os.environ['DD_COND'] = cmsEnv.dd_cond() # 'PU25ns_' + os.environ['TEST_GLOBAL_TAG'] + '-' + os.environ['DATA_VERSION']

os.environ['DD_RELEASE'] = os.environ['CMSSW_VERSION']
os.environ['DD_SOURCE'] = '/eos/cms/store/relval/' + os.environ['DD_RELEASE'] + '/' + os.environ['DD_SAMPLE'] + '/' + os.environ['DD_TIER'] + '/' + os.environ['DD_COND']

print 'DD_RELEASE', os.environ['DD_RELEASE']
print 'DD_SAMPLE', os.environ['DD_SAMPLE']
print 'DD_COND', os.environ['DD_COND']
print 'DD_TIER', os.environ['DD_TIER']
print 'DD_SOURCE', os.environ['DD_SOURCE']
print 'outputFile :', os.environ['outputFile']

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

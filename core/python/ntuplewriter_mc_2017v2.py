import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts


"""NTuple config for 2017v2 MC datasets.

You should try and put any centralised changes in generate_process(), not here.
"""


process = generate_process(year="2017v2", useData=False)

# Please do not commit changes to source filenames - used for consistency testing
process.source.fileNames = cms.untracked.vstring([
    # '/store/mc/RunIIFall17MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/D221F074-FF58-E811-958D-509A4C78138B.root'
    # '/store/mc/RunIIFall17MiniAODv2/WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/F60A3903-3A94-E811-8EC2-0002C9A0C4C1.root'
    '/store/mc/RunIIFall17MiniAODv2/WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/2A589FED-6695-E811-8E18-0025905A48F0.root'
])

# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts()
parse_apply_opts(process, options)

with open('pydump_mc_2017v2.py', 'w') as f:
    f.write(process.dumpPython())

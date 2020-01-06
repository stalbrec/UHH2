import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts


"""NTuple config for 2016UL (preVFP) miniaod MC datasets.

You should try and put any centralised changes in generate_process(), not here.
"""


process = generate_process(year="2016ULPreVFP", useData=False)

# Please do not commit changes to source filenames - used for consistency testing
process.source.fileNames = cms.untracked.vstring([
    '/store/relval/CMSSW_10_6_8/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/FlatPU0to70_106X_mcRun2_asymptotic_preVFP_v3_UL16_CP5_preVFP-v1/20000/84837A6A-DA1B-5C4B-BCFB-85647C73CC68.root'
])

# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts()
parse_apply_opts(process, options)

with open('pydump_mc_2016ULPreVFP.py', 'w') as f:
    f.write(process.dumpPython())

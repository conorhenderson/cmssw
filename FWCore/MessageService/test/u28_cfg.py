# Unit test configuration file for MessageLogger service:
# distinct threshold level for linked destination.
# A destination with different PSet name uses output= to share the
# same stream as an ordinary output destination.  But their thresholds
# are different.

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

import FWCore.Framework.test.cmsExceptionsFatal_cff
process.options = FWCore.Framework.test.cmsExceptionsFatal_cff.options

process.load("FWCore.MessageService.test.Services_cff")

process.MessageLogger = cms.Service("MessageLogger",
    categories = cms.untracked.vstring('preEventProcessing'),
    destinations = cms.untracked.vstring('u28_output'),
    statistics = cms.untracked.vstring('u28_statistics'),
    u28_statistics = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('u28_output')
    ),
    u28_output = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO'),
        noTimeStamps = cms.untracked.bool(True),
        preEventProcessing = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

process.source = cms.Source("EmptySource")

process.sendSomeMessages = cms.EDAnalyzer("UnitTestClient_A")

process.p = cms.Path(process.sendSomeMessages)

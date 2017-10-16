import FWCore.ParameterSet.Config as cms


#print "Running on data or mc"

#HLTLIST = cms.VPSet(#list of HIG groups: ALL, HEXO, HGG, HWW, HTT, HBB, HZZ, HH
HLTLIST = cms.VPSet(#list of HIG groups: ALL, HEXO, HGG, HWW, HTT, HBB, HZZ, TTH
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_v"),
        HiggsGroup = cms.string("ALL"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Ele35_WPTight_Gsf_v"),
        HiggsGroup = cms.string("ALL"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v"),
        HiggsGroup = cms.string("HGG"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v"),
        HiggsGroup = cms.string("HGG"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v"),
        HiggsGroup = cms.string("HGG"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v"),
        HiggsGroup = cms.string("HZZ,HWW,TTH"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"),
        HiggsGroup = cms.string("HZZ,HWW,TTH"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Ele35_WPTight_Gsf_v"),
        HiggsGroup = cms.string("HZZ,HWW,TTH"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DoublePFJets100MaxDeta1p6_DoubleCaloBTagCSV_p33_v"),
        HiggsGroup = cms.string("HBB"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagCSV_p33_v"),
        HiggsGroup = cms.string("HBB"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v"),
        HiggsGroup = cms.string("HBB"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DiJet110_35_Mjj650_PFMET110_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFMET120_PFMHT120_IDTight_CaloBTagCSV_3p1_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFMET120_PFMHT120_IDTight_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_PFMETTypeOne120_PFMHT120_IDTight_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_TripleJet110_35_35_Mjj650_PFMET110_v"),
        HiggsGroup = cms.string("HEXO"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DoubleMediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DoubleTightChargedIsoPFTau35_Trk1_eta2p1_Reg_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET90_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v"),
        HiggsGroup = cms.string("HZZ"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v"),
        HiggsGroup = cms.string("HZZ"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"),
        HiggsGroup = cms.string("HZZ,HWW,TTH"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1_v"),
        HiggsGroup = cms.string("HTT"),
        prescale = cms.int32(1)
    ),
)

ZeroBias = cms.EDAnalyzer("ZeroBias",
    treeName = cms.string("ZeroBias"),
    L1Tau = cms.InputTag("caloStage2Digis", "Tau"),
    L1EmuTau = cms.InputTag("simCaloStage2Digis", "MP"),
    l1tJetCollection = cms.InputTag("caloStage2Digis","Jet"),
    l1tEmuJetCollection = cms.InputTag("simCaloStage2Digis","MP"),
    triggerList = HLTLIST,
    triggerSet = cms.InputTag("slimmedPatTrigger"),
    triggerResultsLabel = cms.InputTag("TriggerResults", "", "HLT"),
    #L2CaloJet_L1TauSeeded_Collection = cms.InputTag("hltL2TauJetsL1IsoTauSeeded", "", "MYHLT"),
    #L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "MYHLT"),
    #L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "MYHLT"),                      
    #L2CaloJet_IsoPix_Collection = cms.InputTag("hltL2TauJetsIso", "", "MYHLT"),
    #TrackCollection = cms.InputTag("hltPixelTracksRegForTau", "", "MYHLT"),
    #PFRegCandCollection = cms.InputTag("hltParticleFlowReg", "", "MYHLT"),
    #AK4PFRegJetCollection = cms.InputTag("hltAK4PFJetsReg", "", "MYHLT"),
    #PFTauSansRefRegCollection = cms.InputTag("hltPFTausSansRefReg", "", "MYHLT"),
    #PFJetRegionCollection = cms.InputTag("hltTauPFJets08RegionReg", "jets", "MYHLT"),
    #PFJetChargedHadronAssociation = cms.InputTag("hltTauPFJetsRecoTauChargedHadronsReg", "", "MYHLT"),
    #JetPiZeroAssociation = cms.InputTag("hltPFTauPiZerosReg", "", "MYHLT")

    #L2CaloJet_L1TauSeeded_Collection = cms.InputTag("hltL2TauJetsL1IsoTauSeeded", "", "MYHLT"),
    #L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "MYHLT"),
    #L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "MYHLT"),                      
    #L2CaloJet_IsoPix_Collection = cms.InputTag("hltL2TauJetsIso", "", "MYHLT"),
    #TrackCollection = cms.InputTag("hltPixelTracksRegForTau", "", "MYHLT"),
    #PFRegCandCollection = cms.InputTag("hltParticleFlowReg", "", "MYHLT"),
    #AK4PFRegJetCollection = cms.InputTag("hltAK4PFJetsReg", "", "MYHLT"),
    #PFTauSansRefRegCollection = cms.InputTag("hltPFTausSansRefReg", "", "MYHLT"),
    #PFJetRegionCollection = cms.InputTag("hltTauPFJets08RegionReg", "jets", "MYHLT"),
    #PFJetChargedHadronAssociation = cms.InputTag("hltTauPFJetsRecoTauChargedHadronsReg", "", "MYHLT"),
    #JetPiZeroAssociation = cms.InputTag("hltPFTauPiZerosReg", "", "MYHLT")
)


NtupleZeroBiasSeq = cms.Sequence(
    ZeroBias
)





patTriggerUnpacker = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
                                    patTriggerObjectsStandAlone = cms.InputTag("slimmedPatTrigger"),
                                    triggerResults = cms.InputTag('TriggerResults', '', "HLT"),
                                    unpackFilterLabels = cms.bool(True)
                                    )

patTriggerUnpackerSeq = cms.Sequence(
    patTriggerUnpacker
)

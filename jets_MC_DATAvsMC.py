#!/usr/bin/env python

# ******************************************
# usage: 
#    python jets_MC_DATAvsMC.py
#
# ******************************************

import json
import ROOT
from ROOT import *
import math, helper, CMSGraphics, CMS_lumi
from CMSGraphics import makeCMSCanvas, makeLegend
from helper import ReadJSON
from helper import DoSimpleFit, Result
from ROOT import TFile, TH1, TH1F, TCanvas, gSystem, TAttFill, TLegend, TRatioPlot, TPad, TStyle, THStack, TPaveText, gStyle
from ROOT import kBlue, kRed, kBlack, kWhite, kAzure, kOrange

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

# *****************************                                                                                                                       
# Data tree options                                                                                                                              
# *****************************                                                                                                                                       
CRZLLTree = False
ZTree     = True
# *****************************                                                                                                                                         
# Data periods options                                                                                                                                                    
# *****************************                                                                                                                                          
period = "data2016"                                                                                                                                                        
#period = "data2017"                                                                                                                                              
#period = "data2018"
# *****************************      

if (period == "data2016"):
        fDY = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2016_CorrectBTag/DYJetsToLL_M50/ZZ4lAnalysis.root")
        fTT = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2016_CorrectBTag/TTTo2L2Nu/ZZ4lAnalysis.root")
        fdata = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200430_LegacyRun2/Data_2016/AllData/ZZ4lAnalysis.root")
        lumi = 35.92 # /fb
        lumiText = "35.92 fb^{-1}"

        if (CRZLLTree):
                tDY = fDY.Get("CRZLLTree/candTree")
                counterDY = fDY.Get("CRZLLTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(40)
                tTT = fTT.Get("CRZLLTree/candTree")
                counterTT = fTT.Get("CRZLLTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(40)
                tdata = fdata.Get("CRZLLTree/candTree")
                treeText = "CRZLLTree"

        elif (ZTree):
                tDY = fDY.Get("ZTree/candTree")
                counterDY = fDY.Get("ZTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(1)
                tTT = fTT.Get("ZTree/candTree")
                counterTT = fTT.Get("ZTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

elif (period == "data2017"):
        fDY = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2017/DYJetsToLL_M50/ZZ4lAnalysis.root")
        fTT = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2017/TTTo2L2Nu/ZZ4lAnalysis.root")
        fdata = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200430_LegacyRun2/Data_2017/AllData/ZZ4lAnalysis.root")
        lumi = 41.53 # /fb
        lumiText = "41.53 fb^{-1}"

        if (CRZLLTree):
                tDY = fDY.Get("CRZLLTree/candTree")
                counterDY = fDY.Get("CRZLLTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(40)
                tTT = fTT.Get("CRZLLTree/candTree")
                counterTT = fTT.Get("CRZLLTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(40)
                tdata = fdata.Get("CRZLLTree/candTree")
                treeText = "CRZLLTree"

        elif (ZTree):
                tDY = fDY.Get("ZTree/candTree")
                counterDY = fDY.Get("ZTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(1)
                tTT = fTT.Get("ZTree/candTree")
                counterTT = fTT.Get("ZTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

elif (period == "data2018"):
        fDY = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2018/DYJetsToLL_M50_LO/ZZ4lAnalysis.root")
        fTT = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200205_CutBased/MC_2018/TTTo2L2Nu/ZZ4lAnalysis.root")
        fdata = TFile.Open("/eos/cms/store/group/phys_higgs/cmshzz4l/cjlst/RunIILegacy/200430_LegacyRun2/Data_2018/AllData/ZZ4lAnalysis.root")
        lumi = 59.74 # /fb
        lumiText = "59.74 fb^{-1}"

        if (CRZLLTree):
                tDY = fDY.Get("CRZLLTree/candTree")
                counterDY = fDY.Get("CRZLLTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(40)
                tTT = fTT.Get("CRZLLTree/candTree")
                counterTT = fTT.Get("CRZLLTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(40)
                tdata = fdata.Get("CRZLLTree/candTree")
                treeText = "CRZLLTree"

        elif (ZTree):
                tDY = fDY.Get("ZTree/candTree")
                counterDY = fDY.Get("ZTree/Counters")
                SumWeight_DY = counterDY.GetBinContent(1)
                tTT = fTT.Get("ZTree/candTree")
                counterTT = fTT.Get("ZTree/Counters")
                SumWeight_TT = counterTT.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

# create output directory                                                                                                                                                   
DIR = "/afs/cern.ch/work/e/elfontan/private/HZZ/HopefullyFinalProduction/CMSSW_10_2_18/src/ZZAnalysis/AnalysisStep/test/hzz4l_ValidationPlots/outputDir/"
gSystem.Exec("mkdir -p " + DIR)
print "Output directory created!"


#**************
# Define histo
#**************
leadingJet_Pt_DY       = TH1F("leadingJet_Pt_DY","leadingJet_Pt_DY",          27, 30, 300)
leadingJet_Pt_DYup     = TH1F("leadingJet_Pt_DYup","leadingJet_Pt_DYup",      27, 30, 300)
leadingJet_Pt_DYdn     = TH1F("leadingJet_Pt_DYdn","leadingJet_Pt_DYdn",      27, 30, 300)
leadingJet_Pt_TT       = TH1F("leadingJet_Pt_TT","leadingJet_Pt_TT",          27, 30, 300)
leadingJet_Pt_TTup     = TH1F("leadingJet_Pt_TTup","leadingJet_Pt_TTup",      27, 30, 300)
leadingJet_Pt_TTdn     = TH1F("leadingJet_Pt_TTdn","leadingJet_Pt_TTdn",      27, 30, 300)

leadingJet_Eta_DY      = TH1F("leadingJet_Eta_DY","leadingJet_Eta_DY",          47, -4.7, 4.7)
leadingJet_Eta_DYup    = TH1F("leadingJet_Eta_DYup","leadingJet_Eta_DYup",      47, -4.7, 4.7)
leadingJet_Eta_DYdn    = TH1F("leadingJet_Eta_DYdn","leadingJet_Eta_DYdn",      47, -4.7, 4.7)
leadingJet_Eta_TT      = TH1F("leadingJet_Eta_TT","leadingJet_Eta_TT",          47, -4.7, 4.7)
leadingJet_Eta_TTup    = TH1F("leadingJet_Eta_TTup","leadingJet_Eta_TTup",      47, -4.7, 4.7)
leadingJet_Eta_TTdn    = TH1F("leadingJet_Eta_TTdn","leadingJet_Eta_TTdn",      47, -4.7, 4.7)

nJetsPt30_DY           = TH1F("nJetsPt30_DY","nJetsPt30_DY",          6, 0, 6)
nJetsPt30_DYup         = TH1F("nJetsPt30_DYup","nJetsPt30_DYup",      6, 0, 6)
nJetsPt30_DYdn         = TH1F("nJetsPt30_DYdn","nJetsPt30_DYdn",      6, 0, 6)
nJetsPt30_TT           = TH1F("nJetsPt30_TT","nJetsPt30_TT",          6, 0, 6)
nJetsPt30_TTup         = TH1F("nJetsPt30_TTup","nJetsPt30_TTup",      6, 0, 6)
nJetsPt30_TTdn         = TH1F("nJetsPt30_TTdn","nJetsPt30_TTdn",      6, 0, 6)

print 'Reading file', fDY.GetName(),'...'
n_events = 0

for event in tDY:
        n_events+=1
	nJetsUp = 0
	nJetsDn = 0
	highest_up = 0.
	highest_dn = 0.
	i_up = 0
	i_dn = 0

        if(n_events % int((tDY.GetEntries()/50)) == 0):
                print "{} %".format(str(100*n_events/tDY.GetEntries() + 1))
        #if (n_events==100): break

        for jet in range(event.JetPt.size()):
                jet_varUp_list = []
                jet_varDn_list = []
                jet_varUp_sum = 0
                jet_varDn_sum = 0
                if (event.JetPt_JESUp.at(jet)/event.JetPt.at(jet) > 1):
                        jes_varUp = (event.JetPt_JESUp.at(jet)/event.JetPt.at(jet)-1)
                        jet_varUp_list.append(jes_varUp)
                else:
                        jes_varUp = (1 - event.JetPt_JESUp.at(jet)/event.JetPt.at(jet))
                        jet_varDn_list.append(jes_varUp)

                if (event.JetPt_JESDown.at(jet)/event.JetPt.at(jet) > 1):
                        jes_varDn = (event.JetPt_JESDown.at(jet)/event.JetPt.at(jet)-1)
                        jet_varUp_list.append(jes_varDn)
                else:
                        jes_varDn = (1 - event.JetPt_JESDown.at(jet)/event.JetPt.at(jet))
                        jet_varDn_list.append(jes_varDn)

                if (event.JetPt_JERUp.at(jet)/event.JetPt.at(jet) > 1):
                        jer_varUp = (event.JetPt_JERUp.at(jet)/event.JetPt.at(jet)-1)
                        jet_varUp_list.append(jer_varUp)
                else:
                        jer_varUp = (1 - event.JetPt_JERUp.at(jet)/event.JetPt.at(jet))
                        jet_varDn_list.append(jer_varUp)

                if (event.JetPt_JERDown.at(jet)/event.JetPt.at(jet) > 1):
                        jer_varDn = (event.JetPt_JERDown.at(jet)/event.JetPt.at(jet)-1)
                        jet_varUp_list.append(jer_varDn)
                else:
                        jer_varDn = (1 - event.JetPt_JERDown.at(jet)/event.JetPt.at(jet))
                        jet_varDn_list.append(jer_varDn)

                if len(jet_varDn_list) > 0:
                        for jvar_dn in range(len(jet_varDn_list)):
                                jet_varDn_sum += (jet_varDn_list[jvar_dn] * jet_varDn_list[jvar_dn])
                        jet_varDn = math.sqrt(jet_varDn_sum)
                if len(jet_varUp_list) > 0:
                        for jvar_up in range(len(jet_varUp_list)):
                                jet_varUp_sum += (jet_varUp_list[jvar_up] * jet_varUp_list[jvar_up])
                        jet_varUp = math.sqrt(jet_varUp_sum)


                if ( event.JetPt.at(jet)*(1+jet_varUp) > highest_up):
                        highest_up = event.JetPt.at(jet)*(1+jet_varUp)
                        i_up = jet
                if ( event.JetPt.at(jet)*(1-jet_varDn ) > highest_dn):
                        highest_dn = event.JetPt.at(jet)*(1-jet_varDn)
                        i_dn = jet
                if ( event.JetPt.at(jet)*(1+jet_varUp ) > 30.):
                        nJetsUp += 1
                if ( event.JetPt.at(jet)*(1-jet_varDn ) > 30.):
                        nJetsDn += 1

	if (event.JetPt.size() > 0 and event.JetPt.at(0) > 30.):
		leadingJet_Pt_DY.Fill(event.JetPt.at(0),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
		leadingJet_Eta_DY.Fill(event.JetEta.at(0),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
	if (event.JetPt.size() > 0 and event.JetPt.at(0)*(1+jet_varUp) > 30.):
		leadingJet_Pt_DYup.Fill(event.JetPt.at(i_up),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
		leadingJet_Eta_DYup.Fill(event.JetEta.at(i_up),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
	if (event.JetPt.size() > 0 and event.JetPt.at(0)*(1-jet_varDn) > 30.):
		leadingJet_Pt_DYdn.Fill(event.JetPt.at(i_dn),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
		leadingJet_Eta_DYdn.Fill(event.JetEta.at(i_dn),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)

	nJetsPt30_DY.Fill(event.nCleanedJetsPt30,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
	nJetsPt30_DYup.Fill(nJetsUp,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)
	nJetsPt30_DYdn.Fill(nJetsDn,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_DY)

print "Saving MC DY histos..."
outFile_DY = TFile.Open(DIR+"DYMC_Histos_"+ period + ".root", "RECREATE")
outFile_DY.cd()
leadingJet_Pt_DY.Write()
leadingJet_Pt_DYup.Write()
leadingJet_Pt_DYdn.Write()
leadingJet_Eta_DY.Write()
leadingJet_Eta_DYup.Write()
leadingJet_Eta_DYdn.Write()
nJetsPt30_DY.Write()
nJetsPt30_DYup.Write()
nJetsPt30_DYdn.Write()
outFile_DY.Close()

print 'Reading file', fTT.GetName(),'...'
n_events=0

for event in tTT:
        n_events+=1
	nJetsUp = 0
	nJetsDn = 0
	highest_up = 0.
	highest_dn = 0.
	i_up = 0
	i_dn = 0
        if(n_events % int((tTT.GetEntries()/50)) == 0):
                print "{} %".format(str(100*n_events/tTT.GetEntries() + 1))
        #if (n_events==50): break

        for jet in range(event.JetPt.size()):
                jet_varUp_list = []
                jet_varDn_list = []
                jet_varUp_sum = 0
                jet_varDn_sum = 0
                if (event.JetPt_JESUp.at(jet)/event.JetPt.at(jet) > 1):
                        jes_varUp = (event.JetPt_JESUp.at(jet)/event.JetPt.at(jet)-1)
                        jet_varUp_list.append(jes_varUp)
                else:
                        jes_varUp = (1 - event.JetPt_JESUp.at(jet)/event.JetPt.at(jet))
                        jet_varDn_list.append(jes_varUp)

               if (event.JetPt_JESDown.at(jet)/event.JetPt.at(jet) > 1):
                       jes_varDn = (event.JetPt_JESDown.at(jet)/event.JetPt.at(jet)-1)
                       jet_varUp_list.append(jes_varDn)
               else:
                       jes_varDn = (1 - event.JetPt_JESDown.at(jet)/event.JetPt.at(jet))
                       jet_varDn_list.append(jes_varDn)

               if (event.JetPt_JERUp.at(jet)/event.JetPt.at(jet) > 1):
                       jer_varUp = (event.JetPt_JERUp.at(jet)/event.JetPt.at(jet)-1)
                       jet_varUp_list.append(jer_varUp)
               else:
                       jer_varUp = (1 - event.JetPt_JERUp.at(jet)/event.JetPt.at(jet))
                       jet_varDn_list.append(jer_varUp)
                if (event.JetPt_JERDown.at(jet)/event.JetPt.at(jet) > 1):
                       jer_varDn = (event.JetPt_JERDown.at(jet)/event.JetPt.at(jet)-1)
                       jet_varUp_list.append(jer_varDn)
               else:
                       jer_varDn = (1 - event.JetPt_JERDown.at(jet)/event.JetPt.at(jet))
                       jet_varDn_list.append(jer_varDn)

                if len(jet_varDn_list) > 0:
                        for jvar_dn in range(len(jet_varDn_list)):
                                jet_varDn_sum += (jet_varDn_list[jvar_dn] * jet_varDn_list[jvar_dn])
                        jet_varDn = math.sqrt(jet_varDn_sum)
                if len(jet_varUp_list) > 0:
                        for jvar_up in range(len(jet_varUp_list)):
                               jet_varUp_sum += (jet_varUp_list[jvar_up] * jet_varUp_list[jvar_up])
                        jet_varUp = math.sqrt(jet_varUp_sum)


                if ( event.JetPt.at(jet)*(1+jet_varUp) > highest_up):
                        highest_up = event.JetPt.at(jet)*(1+jet_varUp)
                        i_up = jet
                if ( event.JetPt.at(jet)*(1-jet_varDn ) > highest_dn):
                        highest_dn = event.JetPt.at(jet)*(1-jet_varDn)
                        i_dn = jet
                if ( event.JetPt.at(jet)*(1+jet_varUp ) > 30.):
                        nJetsUp += 1
                if ( event.JetPt.at(jet)*(1-jet_varDn ) > 30.):
                        nJetsDn += 1

	if (event.JetPt.size() > 0 and event.JetPt.at(0) > 30.):
		leadingJet_Pt_TT.Fill(event.JetPt.at(0),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
		leadingJet_Eta_TT.Fill(event.JetEta.at(0),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
	if (event.JetPt.size() > 0 and event.JetPt.at(0)*(1+jet_varUp) > 30.):
		leadingJet_Pt_TTup.Fill(event.JetPt.at(i_up),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
		leadingJet_Eta_TTup.Fill(event.JetEta.at(i_up),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
	if (event.JetPt.size() > 0 and event.JetPt.at(0)*(1-jet_varDn) > 30.):
		leadingJet_Pt_TTdn.Fill(event.JetPt.at(i_dn),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
		leadingJet_Eta_TTdn.Fill(event.JetEta.at(i_dn),event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)

	nJetsPt30_TT.Fill(event.nCleanedJetsPt30,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
	nJetsPt30_TTup.Fill(nJetsUp,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)
	nJetsPt30_TTdn.Fill(nJetsDn,event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_TT)

print "Saving TT MC histos..."
outFile_TTbar = TFile.Open(DIR+"TTbarMC_Histos_"+ period + ".root", "RECREATE")
outFile_TTbar.cd()
leadingJet_Pt_TT.Write()
leadingJet_Pt_TTup.Write()
leadingJet_Pt_TTdn.Write()
leadingJet_Eta_TT.Write()
leadingJet_Eta_TTup.Write()
leadingJet_Eta_TTdn.Write()
nJetsPt30_TT.Write()
nJetsPt30_TTup.Write()
nJetsPt30_TTdn.Write()
outFile_TTbar.Close()

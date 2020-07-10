#!/usr/bin/env python

# ***************************************************
# usage: 
#    python prefiring.py
# NB: Set DIR and file names and choose period/tree
# ***************************************************

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
ZZTree  = True
ZTree     = False
# *****************************                                                                                                                                         
# Data periods options                                                                                                                                                    
# *****************************                                                                                                                                          
period = "data2016"                                                                                                                                                        
#period = "data2017"                                                                                                                                              
#period = "data2018"
# *****************************      

if (period == "data2016"):
        fdata   = TFile.Open  ("")
        fGGH    = TFile.Open  ("")
        fVBF    = TFile.Open  ("")
        lumi = 35.92 # /fb
        lumiText = "35.92 fb^{-1}"

        if (ZZTree):
                tGGH = fGGH.Get("ZZTree/candTree")
                counterGGH = fGGH.Get("ZZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(40)
                tVBF = fVBF.Get("ZZTree/candTree")
                counterVBF = fVBF.Get("ZZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(40)
                tdata = fdata.Get("ZZTree/candTree")
                treeText = "ZZTree"

        elif (ZTree):
                tGGH = fGGH.Get("ZTree/candTree")
                counterGGH = fGGH.Get("ZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(1)
                tVBF = fVBF.Get("ZTree/candTree")
                counterVBF = fVBF.Get("ZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

elif (period == "data2017"):
        fdata   = TFile.Open  ("")
        fGGH    = TFile.Open  ("")
        fVBF    = TFile.Open  ("")
        lumi = 41.53 # /fb
        lumiText = "41.53 fb^{-1}"

        if (ZZTree):
                tGGH = fGGH.Get("ZZTree/candTree")
                counterGGH = fGGH.Get("ZZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(40)
                tVBF = fVBF.Get("ZZTree/candTree")
                counterVBF = fVBF.Get("ZZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(40)
                tdata = fdata.Get("ZZTree/candTree")
                treeText = "ZZTree"

        elif (ZTree):
                tGGH = fGGH.Get("ZTree/candTree")
                counterGGH = fGGH.Get("ZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(1)
                tVBF = fVBF.Get("ZTree/candTree")
                counterVBF = fVBF.Get("ZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

elif (period == "data2018"):
        fdata   = TFile.Open  ("")
        fGGH    = TFile.Open  ("")
        fVBF    = TFile.Open  ("")
        lumi = 59.74 # /fb
        lumiText = "59.74 fb^{-1}"

        if (ZZTree):
                tGGH = fGGH.Get("ZZTree/candTree")
                counterGGH = fGGH.Get("ZZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(40)
                tVBF = fVBF.Get("ZZTree/candTree")
                counterVBF = fVBF.Get("ZZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(40)
                tdata = fdata.Get("ZZTree/candTree")
                treeText = "ZZTree"

        elif (ZTree):
                tGGH = fGGH.Get("ZTree/candTree")
                counterGGH = fGGH.Get("ZTree/Counters")
                SumWeight_GGH = counterGGH.GetBinContent(1)
                tVBF = fVBF.Get("ZTree/candTree")
                counterVBF = fVBF.Get("ZTree/Counters")
                SumWeight_VBF = counterVBF.GetBinContent(1)
                tdata = fdata.Get("ZTree/candTree")
                treeText = "ZTree"

# create output directory                                                                                                                     
DIR = ""
gSystem.Exec("mkdir -p " + DIR)
print "Output directory created: " + str(DIR)


#********************
# Define histo Z->ee
#********************
leadingJet_Eta_data     = TH1F("leadingJet_Eta_data","leadingJet_Eta_data",         45, -4.5, 4.5)

leadingJet_Eta_ggH_MC   = TH1F("leadingJet_Eta_ggH_MC","leadingJet_Eta_ggH_MC",     45, -4.5, 4.5)
leadingJet_Eta_ggH_MCup = TH1F("leadingJet_Eta_ggH_MCup","leadingJet_Eta_ggH_MCup", 45, -4.5, 4.5)
leadingJet_Eta_ggH_MCdn = TH1F("leadingJet_Eta_ggH_MCdn","leadingJet_Eta_ggH_MCdn", 45, -4.5, 4.5)
leadingJet_Eta_ggH_MC_w   = TH1F("leadingJet_Eta_ggH_MC_w","leadingJet_Eta_ggH_MC_w",     45, -4.5, 4.5)
leadingJet_Eta_ggH_MCup_w = TH1F("leadingJet_Eta_ggH_MCup_w","leadingJet_Eta_ggH_MCup_w", 45, -4.5, 4.5)
leadingJet_Eta_ggH_MCdn_w = TH1F("leadingJet_Eta_ggH_MCdn_w","leadingJet_Eta_ggH_MCdn_w", 45, -4.5, 4.5)

leadingJet_Eta_VBF_MC   = TH1F("leadingJet_Eta_VBF_MC","leadingJet_Eta_VBF_MC",     45, -4.5, 4.5)
leadingJet_Eta_VBF_MCup = TH1F("leadingJet_Eta_VBF_MCup","leadingJet_Eta_VBF_MCup", 45, -4.5, 4.5)
leadingJet_Eta_VBF_MCdn = TH1F("leadingJet_Eta_VBF_MCdn","leadingJet_Eta_VBF_MCdn", 45, -4.5, 4.5)
leadingJet_Eta_VBF_MC_w   = TH1F("leadingJet_Eta_VBF_MC_w","leadingJet_Eta_VBF_MC",     45, -4.5, 4.5)
leadingJet_Eta_VBF_MCup_w = TH1F("leadingJet_Eta_VBF_MCup_w","leadingJet_Eta_VBF_MCup_w", 45, -4.5, 4.5)
leadingJet_Eta_VBF_MCdn_w = TH1F("leadingJet_Eta_VBF_MCdn_w","leadingJet_Eta_VBF_MCdn_w", 45, -4.5, 4.5)


print 'Reading file', fGGH.GetName(),'...'
n_events = 0

for event in tGGH:
        n_events+=1
	nJetsUp = 0
	nJetsDn = 0
	highest_up = 0.
	highest_dn = 0.
	i_up = 0
	i_dn = 0
        if(n_events % int((tGGH.GetEntries()/10)) == 0):
                print "{} %".format(str(100*n_events/tGGH.GetEntries() + 1))

	for jet in range(event.JetPt.size()):
		if (event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet)) > highest_up):
			highest_up = event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet))
			i_up = jet
		if (event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet)) > highest_dn):
			highest_dn = event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet))
			i_dn = jet
		if ( event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet)) > 30.):
			nJetsUp += 1
		if ( event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet)) > 30.):
			nJetsDn += 1

	if (event.JetPt.size() > 0 and event.JetPt.at(0) > 30.):
		leadingJet_Eta_ggH_MC.Fill (event.JetEta.at(0), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_GGH)
		leadingJet_Eta_ggH_MC_w.Fill (event.JetEta.at(0), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_GGH)
	if (event.JetPt.size() > 0 and event.JetJERUp.at(i_up)*(1+event.JetSigma.at(i_up)) > 30.):
		leadingJet_Eta_ggH_MCup.Fill (event.JetEta.at(i_up), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_GGH)
		leadingJet_Eta_ggH_MCup_w.Fill (event.JetEta.at(i_up), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeightUp/SumWeight_GGH)
	if (event.JetPt.size() > 0 and event.JetJERDown.at(i_dn)*(1-event.JetSigma.at(i_up)) > 30.):
		leadingJet_Eta_ggH_MCdn.Fill (event.JetEta.at(i_dn), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_GGH)
		leadingJet_Eta_ggH_MCdn_w.Fill (event.JetEta.at(i_dn), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeightDn/SumWeight_GGH)

print 'Reading file', fVBF.GetName(),'...'
n_events=0

for event in tVBF:
        n_events+=1
	nJetsUp = 0
	nJetsDn = 0
	highest_up = 0.
	highest_dn = 0.
	i_up = 0
	i_dn = 0
        if(n_events % int((tVBF.GetEntries()/10)) == 0):
                print "{} %".format(str(100*n_events/tVBF.GetEntries() + 1))

	for jet in range(event.JetPt.size()):
		if (event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet)) > highest_up):
			highest_up = event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet))
			i_up = jet
		if (event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet)) > highest_dn):
			highest_dn = event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet))
			i_dn = jet
		if ( event.JetJERUp.at(jet)*(1+event.JetSigma.at(jet)) > 30.):
			nJetsUp += 1
		if ( event.JetJERDown.at(jet)*(1-event.JetSigma.at(jet)) > 30.):
			nJetsDn += 1

	if (event.JetPt.size() > 0 and event.JetPt.at(0) > 30.):
		leadingJet_Eta_VBF_MC.Fill (event.JetEta.at(0), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_VBF)
		leadingJet_Eta_VBF_MC_w.Fill (event.JetEta.at(0), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeight/SumWeight_VBF)
	if (event.JetPt.size() > 0 and event.JetJERUp.at(i_up)*(1+event.JetSigma.at(i_up)) > 30.):
		leadingJet_Eta_VBF_MCup.Fill (event.JetEta.at(i_up), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_VBF)
		leadingJet_Eta_VBF_MCup_w.Fill (event.JetEta.at(i_up), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeightUp/SumWeight_VBF)
	if (event.JetPt.size() > 0 and event.JetJERDown.at(i_dn)*(1-event.JetSigma.at(i_up)) > 30.):
		leadingJet_Eta_VBF_MCdn.Fill (event.JetEta.at(i_dn), event.overallEventWeight*event.xsec*1000*lumi/SumWeight_VBF)
		leadingJet_Eta_VBF_MCdn_w.Fill (event.JetEta.at(i_dn), event.overallEventWeight*event.xsec*1000*lumi*event.L1prefiringWeightDn/SumWeight_VBF)


print 'Reading file', fdata.GetName(),'...'

for event in tdata:
        if (event.JetPt.size() > 0 and event.JetPt.at(0) > 30.):
                leadingJet_Eta_data.Fill (event.JetEta.at(0))


outFile = TFile.Open(DIR+"OK_JetEta_" + period + "_" + treeText + ".root", "RECREATE")
print "Saving histos into root file " + outFile.GetName() + "..."
outFile.cd()
leadingJet_Eta_data.Write()
leadingJet_Eta_ggH_MC.Write()
leadingJet_Eta_ggH_MCup.Write()
leadingJet_Eta_ggH_MCdn.Write()
leadingJet_Eta_ggH_MC_w.Write()
leadingJet_Eta_ggH_MCup_w.Write()
leadingJet_Eta_ggH_MCdn_w.Write()
leadingJet_Eta_VBF_MC.Write()
leadingJet_Eta_VBF_MCup.Write()
leadingJet_Eta_VBF_MCdn.Write()
leadingJet_Eta_VBF_MC_w.Write()
leadingJet_Eta_VBF_MCup_w.Write()
leadingJet_Eta_VBF_MCdn_w.Write()
outFile.Close()

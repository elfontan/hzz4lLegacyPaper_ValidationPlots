#!/usr/bin/env python

# ******************************************
# usage: 
#    python jetMET_ratioPlots_DATAvsMC.py
# NB: Set DIR and choose period/tree  
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
CRZLTree  = False
ZTree     = True
# *****************************                                                                                                                                         
# Data periods options                                                                                                                                                    
# *****************************                                                                                                                                          
#period = "data2016"                                                                                                                                                        
#period = "data2017"                                                                                                                                              
period = "data2018"
# *****************************      

def DrawRatioPlot(name, xaxis_title, yaxis_title, c, data, MCDY, MCDYUp, MCDYDn, MCTT, MCTTUp, MCTTDn, logscale):
        c.Divide(0,2,0,0)
        pad1 = c.cd(1)
        pad1.SetBottomMargin(0.02)
        pad1.SetTopMargin(0.18)
        pad1.SetLeftMargin(0.10)
    
        if logscale:
                pad1.SetLogy()

        hs = THStack("hs","")
        norm = 1                                                      # Normalize to MC cross section 
        #norm = data.Integral() / (MCDY.Integral() + MCTT.Integral()) # Normalize MC to data   

        #MC TTbar hist
        MCTT.Scale(norm) # MC normalization
        MCTT.SetFillColor(kBlue-4)
        MCTT.SetLineColor(kBlack)
        hs.Add(MCTT)

        #MC DY hist
        MCDY.Scale(norm) # MC normalization
        MCDY.SetFillColor(kOrange+1)
        MCDY.SetLineColor(kBlack)
        hs.Add(MCDY)

        #hs.SetMaximum(1100000)
        hs.SetMaximum(1.9*max(hs.GetMaximum(), data.GetMaximum()))
        hs.Draw("histo")
        
        data.SetLineColor(ROOT.kBlack)
        data.SetMarkerStyle(20)
        data.SetMarkerSize(0.6)
        data.Draw("p E1 X0 SAME")

        hs.GetYaxis().SetTitle(yaxis_title)
        hs.GetXaxis().SetLabelSize(0)
        hs.GetYaxis().SetTitleSize(0.07)
        hs.GetYaxis().SetLabelSize(0.07)
        hs.GetYaxis().SetTitleOffset(0.7)

        pad2 = c.cd(2)

        pad2.SetBottomMargin(0.20)
        pad2.SetTopMargin(0.02)
        pad2.SetLeftMargin(0.10)
    
        MC = MCDY.Clone("MC")
        MC.Add(MCTT)
        MCUp = MCDYUp.Clone("MCUp")
        MCUp.Add(MCTTUp)
        MCDn = MCDYDn.Clone("MCDn")
        MCDn.Add(MCTTDn)

        Ratio    = TH1F("Ratio","Ratio",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())
        sigma_up = TH1F("sigma_up","sigma_up",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())
        sigma_dn = TH1F("sigma_dn","sigma_dn",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())

        for bin in range (MC.GetSize() - 2):
                if (MC.GetBinContent(bin + 1) == 0):
                        Ratio   .SetBinContent(bin + 1, 0)
                        Ratio   .SetBinError(bin + 1, 0)
                        sigma_up.SetBinContent(bin + 1, 0)
                        sigma_dn.SetBinContent(bin + 1, 0)
                else:
                        Ratio   .SetBinContent(bin + 1, float(data.GetBinContent(bin + 1))/MC.GetBinContent(bin + 1))
                        Ratio   .SetBinError  (bin + 1, 1./(data.GetBinContent(bin + 1))**0.5)
                        sigma_up.SetBinContent(bin + 1, float(MCUp.GetBinContent(bin + 1))/MC.GetBinContent(bin + 1))
                        sigma_dn.SetBinContent(bin + 1, float(MCDn.GetBinContent(bin + 1))/MC.GetBinContent(bin + 1))

        for bin in range (Ratio.GetSize() - 2):
                temp = Ratio.GetBinContent(bin + 1)
                Ratio.SetBinContent( bin + 1, temp - 1)

        for bin in range (sigma_up.GetSize() - 2):
                temp = sigma_up.GetBinContent(bin + 1)
                sigma_up.SetBinContent( bin + 1, temp - 1)

        for bin in range (sigma_dn.GetSize() - 2):
                temp = sigma_dn.GetBinContent(bin + 1)
                sigma_dn.SetBinContent( bin + 1, temp - 1)

        sigma_up.SetFillColor(ROOT.kGray)
        sigma_up.SetLineColor(ROOT.kGray)
        sigma_up.SetMaximum(1.0)
        sigma_up.SetMinimum(-1.0)
        sigma_up.GetXaxis().SetTitle(xaxis_title)
        sigma_up.GetYaxis().SetTitle("(Data/MC)-1")
        sigma_up.GetYaxis().SetTitleOffset(0.6)
        sigma_up.Draw("HIST")
        sigma_up.GetXaxis().SetLabelSize(0.07)
        sigma_up.GetXaxis().SetTitleSize(0.07)
        sigma_up.GetYaxis().SetLabelSize(0.07)
        sigma_up.GetYaxis().SetTitleSize(0.07)
        
        sigma_dn.SetFillColor(ROOT.kGray)
        sigma_dn.SetLineColor(ROOT.kGray)
        sigma_dn.Draw("HIST SAME")
        
        gPad.RedrawAxis()
        
        Ratio.SetMarkerStyle(20)
        Ratio.SetMarkerSize(0.6)
        Ratio.Draw("p E1 X0 SAME")
        
        pad1.cd()
        leg = TLegend(.75,.45,.95,.75)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetTextFont(42)
        leg.SetTextSize(0.07)
        #leg.AddEntry(MC, "DY + t#bar{t}  MC", "f" )
        leg.AddEntry(MCDY, "DY MC", "f" )
        leg.AddEntry(MCTT, "t#bar{t}  MC", "f" )
        leg.AddEntry(data, "Data", "p")
        leg.AddEntry(sigma_up, "JEC Uncertainty", "f")
        leg.Draw()

        #draw CMS and lumi text                                                                                                                                                          
        CMS_lumi.writeExtraText = True
        CMS_lumi.extraText      = "Preliminary"
        CMS_lumi.lumi_sqrtS     = lumiText + " (13 TeV)"
        CMS_lumi.cmsTextSize    = 0.6
        CMS_lumi.lumiTextSize   = 0.46
        CMS_lumi.extraOverCmsTextSize = 0.75
        CMS_lumi.relPosX = 0.12
        CMS_lumi.CMS_lumi(pad1, 0, 0)
        c.Update()

        c.SaveAs(name+".pdf")
        c.SaveAs(name+".png")
        
        c.Clear()


if (period == "data2016"):
        lumi = 35.92 # /fb
        lumiText = "35.92 fb^{-1}"

        if (CRZLLTree):
                treeText = "CRZLL"
        if (CRZLTree):
                treeText = "CRZL"
        elif (ZTree):
                treeText = "ZTree"

elif (period == "data2017"):
        lumi = 41.53 # /fb
        lumiText = "41.53 fb^{-1}"

        if (CRZLLTree):
                treeText = "CRZLL"
        elif (CRZLTree):
                treeText = "CRZL"
        elif (ZTree):
                treeText = "ZTree"

elif (period == "data2018"):
        lumi = 59.74 # /fb
        lumiText = "59.74 fb^{-1}"

        if (CRZLLTree):
                treeText = "CRZLL"
        elif (CRZLTree):
                treeText = "CRZL"
        elif (ZTree):
                treeText = "ZTree"

# create output directory                                                                                                                                                   
DIR = ""

print "Reading histos..."  
inFile_DY = TFile.Open(DIR+"DYMC_Histos_" + period + ".root")
inFile_TT = TFile.Open(DIR+"TTbarMC_Histos_" + period + ".root")
inFile_Data = TFile.Open(DIR+"Data_Histos_" + period + ".root")

h_leadingJet_Pt_data  = inFile_Data.Get("leadingJet_Pt_data")
h_leadingJet_Eta_data = inFile_Data.Get("leadingJet_Eta_data")
h_nJetsPt30_data      = inFile_Data.Get("nJetsPt30_data")

h_leadingJet_Pt_DY    = inFile_DY.Get("leadingJet_Pt_DY")
h_leadingJet_Eta_DY   = inFile_DY.Get("leadingJet_Eta_DY")
h_nJetsPt30_DY        = inFile_DY.Get("nJetsPt30_DY")
h_leadingJet_Pt_DYup  = inFile_DY.Get("leadingJet_Pt_DYup")
h_leadingJet_Eta_DYup = inFile_DY.Get("leadingJet_Eta_DYup")
h_nJetsPt30_DYup      = inFile_DY.Get("nJetsPt30_DYup")
h_leadingJet_Pt_DYdn  = inFile_DY.Get("leadingJet_Pt_DYdn")
h_leadingJet_Eta_DYdn = inFile_DY.Get("leadingJet_Eta_DYdn")
h_nJetsPt30_DYdn      = inFile_DY.Get("nJetsPt30_DYdn")

h_leadingJet_Pt_TT    = inFile_TT.Get("leadingJet_Pt_TT")
h_leadingJet_Eta_TT   = inFile_TT.Get("leadingJet_Eta_TT")
h_nJetsPt30_TT        = inFile_TT.Get("nJetsPt30_TT")
h_leadingJet_Pt_TTup  = inFile_TT.Get("leadingJet_Pt_TTup")
h_leadingJet_Eta_TTup = inFile_TT.Get("leadingJet_Eta_TTup")
h_nJetsPt30_TTup      = inFile_TT.Get("nJetsPt30_TTup")
h_leadingJet_Pt_TTdn  = inFile_TT.Get("leadingJet_Pt_TTdn")
h_leadingJet_Eta_TTdn = inFile_TT.Get("leadingJet_Eta_TTdn")
h_nJetsPt30_TTdn      = inFile_TT.Get("nJetsPt30_TTdn")

c = ROOT.TCanvas()
DrawRatioPlot(DIR+"leadingJet_Pt_"+treeText+"_"+period+"_STACKED", "Leading jet p_{T}", "Events/10 GeV", c, h_leadingJet_Pt_data, h_leadingJet_Pt_DY, h_leadingJet_Pt_DYup, h_leadingJet_Pt_DYdn, h_leadingJet_Pt_TT, h_leadingJet_Pt_TTup, h_leadingJet_Pt_TTdn, True)
DrawRatioPlot(DIR+"leadingJet_Eta_"+treeText+"_"+period+"_STACKED", "Leading jet #eta", "Events/0.2", c, h_leadingJet_Eta_data, h_leadingJet_Eta_DY, h_leadingJet_Eta_DYup, h_leadingJet_Eta_DYdn, h_leadingJet_Eta_TT, h_leadingJet_Eta_TTup, h_leadingJet_Eta_TTdn,False)
DrawRatioPlot(DIR+"nCleanedJetsPt30_"+treeText+"_"+period+"_STACKED", "# Jets Pt > 30 GeV", "Events", c, h_nJetsPt30_data, h_nJetsPt30_DY, h_nJetsPt30_DYup, h_nJetsPt30_DYdn, h_nJetsPt30_TT, h_nJetsPt30_TTup, h_nJetsPt30_TTdn,True)




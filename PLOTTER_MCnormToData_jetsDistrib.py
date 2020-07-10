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
period = "data2017"                                                                                                                                              
#period = "data2018"
# *****************************      

def DrawRatioPlot(name, xaxis_title, yaxis_title, c, data, MC, MCUp, MCDn, logscale):
        c.Divide(0,2,0,0)
        pad1 = c.cd(1)

        pad1.SetBottomMargin(0.02)
        pad1.SetTopMargin(0.18)
        pad1.SetLeftMargin(0.10)
    
        if logscale:
                pad1.SetLogy()

        MCnorm = MC.Clone("MCnorm");
        MCnormUp = MCUp.Clone("MCnormUp");
        MCnormDn = MCDn.Clone("MCnormDn");
        norm = data.Integral()/MCnorm.Integral() 

        MCnorm.Scale(norm)
        MCnormUp.Scale(norm)
        MCnormDn.Scale(norm)

        max = 0.
        for bin in range (MCnorm.GetSize() - 2):
                if ( MCnorm.GetBinContent(bin + 1) > max):
                        max = MCnorm.GetBinContent(bin + 1)

        MCnorm.SetMaximum(1.4*max)        
        MCnorm.SetFillColor(kOrange + 1)
        MCnorm.GetYaxis().SetTitle(yaxis_title)
        MCnorm.Draw("HIST")
        MCnorm.GetXaxis().SetLabelSize(0)
        MCnorm.GetYaxis().SetTitleSize(0.07)
        MCnorm.GetYaxis().SetLabelSize(0.07)
        MCnorm.GetYaxis().SetTitleOffset(0.7)
        data.SetLineColor(ROOT.kBlack)
        data.SetMarkerStyle(20)
        data.SetMarkerSize(0.6)
        data.Draw("p E1 X0 SAME")

        pad2 = c.cd(2)

        pad2.SetBottomMargin(0.20)
        pad2.SetTopMargin(0.02)
        pad2.SetLeftMargin(0.10)

        Ratio    = TH1F("Ratio","Ratio",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())
        sigma_up = TH1F("sigma_up","sigma_up",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())
        sigma_dn = TH1F("sigma_dn","sigma_dn",MC.GetSize() - 2, MC.GetXaxis().GetXmin(),MC.GetXaxis().GetXmax())

        for bin in range (MCnorm.GetSize() - 2):
                if (MCnorm.GetBinContent(bin + 1) == 0):
                        Ratio   .SetBinContent(bin + 1, 0)
                        Ratio   .SetBinError(bin + 1, 0)
                        sigma_up.SetBinContent(bin + 1, 0)
                        sigma_dn.SetBinContent(bin + 1, 0)
                else:
                        Ratio   .SetBinContent(bin + 1, float(data.GetBinContent(bin + 1))/MCnorm.GetBinContent(bin + 1))
                        Ratio   .SetBinError  (bin + 1, 1./(data.GetBinContent(bin + 1))**0.5)
                        sigma_up.SetBinContent(bin + 1, float(MCnormUp.GetBinContent(bin + 1))/MCnorm.GetBinContent(bin + 1))
                        sigma_dn.SetBinContent(bin + 1, float(MCnormDn.GetBinContent(bin + 1))/MCnorm.GetBinContent(bin + 1))


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
        #leg = TLegend(.45,.45,.75,.75)
        leg = TLegend(.75,.45,.95,.75)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetTextFont(42)
        leg.SetTextSize(0.07)
        #leg.AddEntry(MC, "Z/t#bar{t} + jets", "f" )
        leg.AddEntry(MCnorm, "DY + t#bar{t}  MC", "f" )
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
if (ZTree):
        inFile_MC = TFile.Open(DIR+"MC_Histos_2017_" + treeText + "_Zmumu.root")
        inFile_Data = TFile.Open(DIR+"Data_Histos_2017_" + treeText + "_Zmumu.root")
        h_leadingJet_Pt_data = inFile_Data.Get("leadingJet_Pt_data")
        h_leadingJet_Eta_data = inFile_Data.Get("leadingJet_Eta_data")
        h_nJetsPt30_data = inFile_Data.Get("nJetsPt30_data")
        h_leadingJet_Pt_MC = inFile_MC.Get("leadingJet_Pt_MC")
        h_leadingJet_Eta_MC = inFile_MC.Get("leadingJet_Eta_MC")
        h_nJetsPt30_MC = inFile_MC.Get("nJetsPt30_MC")
        h_leadingJet_Pt_MCup = inFile_MC.Get("leadingJet_Pt_MCup")
        h_leadingJet_Eta_MCup = inFile_MC.Get("leadingJet_Eta_MCup")
        h_nJetsPt30_MCup = inFile_MC.Get("nJetsPt30_MCup")
        h_leadingJet_Pt_MCdn = inFile_MC.Get("leadingJet_Pt_MCdn")
        h_leadingJet_Eta_MCdn = inFile_MC.Get("leadingJet_Eta_MCdn")
        h_nJetsPt30_MCdn = inFile_MC.Get("nJetsPt30_MCdn")
else:
        inFile = TFile.Open(DIR+"Histos_2017_" + treeText + "_Zmumu.root")
        h_leadingJet_Pt_data = inFile.Get("leadingJet_Pt_data")
        h_leadingJet_Eta_data = inFile.Get("leadingJet_Eta_data")
        h_nJetsPt30_data = inFile.Get("nJetsPt30_data")
        h_leadingJet_Pt_MC = inFile.Get("leadingJet_Pt_MC")
        h_leadingJet_Eta_MC = inFile.Get("leadingJet_Eta_MC")
        h_nJetsPt30_MC = inFile.Get("nJetsPt30_MC")
        h_leadingJet_Pt_MCup = inFile.Get("leadingJet_Pt_MCup")
        h_leadingJet_Eta_MCup = inFile.Get("leadingJet_Eta_MCup")
        h_nJetsPt30_MCup = inFile.Get("nJetsPt30_MCup")
        h_leadingJet_Pt_MCdn = inFile.Get("leadingJet_Pt_MCdn")
        h_leadingJet_Eta_MCdn = inFile.Get("leadingJet_Eta_MCdn")
        h_nJetsPt30_MCdn = inFile.Get("nJetsPt30_MCdn")

c = ROOT.TCanvas()
DrawRatioPlot(DIR+"leadingJet_Pt_"+treeText+"_MCnormToData_Zmumu", "Leading jet p_{T}", "Events/10 GeV", c, h_leadingJet_Pt_data, h_leadingJet_Pt_MC, h_leadingJet_Pt_MCup, h_leadingJet_Pt_MCdn, True)
DrawRatioPlot(DIR+"leadingJet_Eta_2017_"+treeText+"_MCnormToData_Zmumu", "Leading jet #eta", "Events/0.2", c, h_leadingJet_Eta_data, h_leadingJet_Eta_MC, h_leadingJet_Eta_MCup, h_leadingJet_Eta_MCdn, False)
DrawRatioPlot(DIR+"nCleanedJetsPt30_"+treeText+"_MCnormToData_Zmumu", "# Jets Pt > 30 GeV", "Events", c, h_nJetsPt30_data, h_nJetsPt30_MC, h_nJetsPt30_MCup, h_nJetsPt30_MCdn, True)




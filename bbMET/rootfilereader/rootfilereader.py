#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D,TH2D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import ROOT as ROOT
import os
import sys, optparse



gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(0)
#gStyle.SetPadColor(1)
legend=TLegend(.63,.69,.87,.89)
canvas = ROOT.TCanvas()
canvas.SetLogy()
f1 = ROOT.TFile.Open('LO_bbDM_ntupleHistos.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")



hist_genMET_bbDM_LO = f1.Get('genMET')
hist_genMET_bbDM_LO.Rebin(10)
hist_genMET_bbDM_LO.SetLineColor(2)
hist_genMET_bbDM_LO.SetXTitle("genMET[GeV]")
hist_genMET_bbDM_LO.SetYTitle("Events")
hist_genMET_bbDM_LO.Scale(1/hist_genMET_bbDM_LO.Integral())

hist_pfMET_bbDM_LO = f1.Get('h_met_')
hist_pfMET_bbDM_LO.SetLineColor(2)
hist_pfMET_bbDM_LO.Rebin(10)
hist_pfMET_bbDM_LO.Scale(1/hist_pfMET_bbDM_LO.Integral())
#hist_genMET_bbDM_LO.Draw()
hist_pfMET_bbDM_LO.Draw()

#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
legend.AddEntry(hist_pfMET_bbDM_LO,"pfMET_LO_bbDM","L")


f2 = ROOT.TFile.Open('NLO_bbDM_ntupleHistos.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

hist_genMET_bbDM_NLO = f2.Get('genMET')
hist_genMET_bbDM_NLO.SetLineColor(4)
hist_genMET_bbDM_NLO.Rebin(10)
hist_genMET_bbDM_NLO.Scale(1/hist_genMET_bbDM_NLO.Integral())
#legend.AddEntry(hist_genMET_bbDM_NLO,"genMET_NLO_bbDM","L")


hist_pfMET_bbDM_NLO = f2.Get('h_met_')
hist_pfMET_bbDM_NLO.SetLineColor(4)
hist_pfMET_bbDM_NLO.Rebin(10)
hist_pfMET_bbDM_NLO.Scale(1/hist_pfMET_bbDM_NLO.Integral())
legend.AddEntry(hist_pfMET_bbDM_NLO,"pfMET_NLO_bbDM","L")

#hist_genMET_bbDM_NLO.Draw('same')
hist_pfMET_bbDM_NLO.Draw('same')


f3 = ROOT.TFile.Open('LO_ttDM_ntupleHistos.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

hist_genMET_ttDM_LO = f3.Get('genMET')
hist_genMET_ttDM_LO.Rebin(10)
hist_genMET_ttDM_LO.SetLineColor(3)
hist_genMET_ttDM_LO.Scale(1/hist_genMET_ttDM_LO.Integral())

hist_pfMET_ttDM_LO = f3.Get('h_met_')
hist_pfMET_ttDM_LO.Rebin(10)
hist_pfMET_ttDM_LO.SetLineColor(3)
hist_pfMET_ttDM_LO.Scale(1/hist_pfMET_ttDM_LO.Integral())

#hist_genMET_ttDM_LO.Draw('same')
hist_pfMET_ttDM_LO.Draw('same')

#legend.AddEntry(hist_genMET_ttDM_LO,"genMET_LO_ttDM","L")
legend.AddEntry(hist_pfMET_ttDM_LO,"pfMET_LO_ttDM","L")

#canvas.BuildLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
legend.Draw()
canvas.SaveAs('pfMET.png')

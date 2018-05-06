#!/usr/bin/env python
from ROOT import TFile, TStyle,TTree,TLatex, TH1F, TH1D,TH2D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import ROOT as ROOT
import os
import sys, optparse


#gROOT.ForceStyle()

#gStyle.SetHistFillColor(kWhite);
gStyle.SetHistFillStyle(0)
#gStyle->SetHistLineColor(kBlack);
gStyle.SetHistLineStyle(1)
gStyle.SetHistLineWidth(1)
gStyle.SetEndErrorSize(0)

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(0)
#gStyle.SetPadColor(1)
tdrstyle=TStyle()
#gStyle.SetHistFillStyle(1)

cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary  ')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

legend=TLegend(.63,.69,.87,.89)
canvas = ROOT.TCanvas()
canvas.SetLogy()
f1 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/ntupleout/BROutputs/Filelist_05052018_signal_ntuple/Output_pseudo_NLO_Mchi-1_Mphi-50.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")



hist_50 = f1.Get('genMET')
hist_50.Rebin(4)
hist_50.SetLineColor(2)
hist_50.SetXTitle("genMET[GeV]")
hist_50.SetYTitle("Events")
#hist_50.SetMaximum(2)
#hist_50.SetHistFillStyle(0)
hist_50.Scale(3.769e-02/hist_50.Integral())
hist_50.SetMaximum(10000)
#hist_50.SetFillStyle(4050)
#hist_50.SetOption("L")
#hist_50.GetOption()
#hist_50.SetFillStyle(4050)
#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
legend.AddEntry(hist_50,"Mphi=50,Mchi=1","L")
hist_50.Draw('HIST')

f2 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/ntupleout/BROutputs/Filelist_05052018_signal_ntuple/Output_pseudo_NLO_Mchi-1_Mphi-100.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

hist_100 = f2.Get('genMET')
hist_100.SetLineColor(3)
hist_100.Rebin(4)
hist_100.Scale(2.072e-02/hist_100.Integral())
legend.AddEntry(hist_100,"Mphi=100,Mchi=1","L")
#hist_100.SetFillStyle(3001)

#hist_genMET_bbDM_NLO.Draw('same')
hist_100.Draw('HIST' 'same')


f3 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/ntupleout/BROutputs/Filelist_05052018_signal_ntuple/Output_pseudo_NLO_Mchi-1_Mphi-350.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

hist_350 = f3.Get('genMET')
hist_350.Rebin(4)
hist_350.SetLineColor(4)
hist_350.Scale(1.237e-03/hist_350.Integral())
legend.AddEntry(hist_350,"Mphi=350,Mchi=1","L")

#hist_genMET_ttDM_LO.Draw('same')
hist_350.Draw('HIST' 'same')


f4=ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/ntupleout/BROutputs/Filelist_05052018_signal_ntuple/Output_pseudo_NLO_Mchi-1_Mphi-400.root','read')
hist_400 = f4.Get('genMET')
hist_400.Rebin(4)
hist_400.SetLineColor(5)
hist_400.Scale(5.773e-04/hist_400.Integral())
legend.AddEntry(hist_400,"Mphi=400,Mchi=1","L")
hist_400.Draw('HIST' 'same')

f5=ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/ntupleout/BROutputs/Filelist_05052018_signal_ntuple/Output_pseudo_NLO_Mchi-1_Mphi-500.root','read')
hist_500 = f5.Get('genMET')
hist_500.Rebin(4)
hist_500.SetLineColor(6)
hist_500.Scale(2.802e-04/hist_500.Integral())
legend.AddEntry(hist_500,"Mphi=500,Mchi=1","L")
#canvas.BuildLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
hist_500.Draw('HIST' 'same')
legend.Draw()
cmsname.Draw()
canvas.SaveAs('CSgenMET.pdf')

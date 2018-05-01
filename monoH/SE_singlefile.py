#!/usr/bin/env python
from ROOT import TFile, TLatex, TTree, TH1F, TH1D,TH2D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import ROOT as ROOT
import os
import sys, optparse,math,argparse


dirpath="signal/"

chilist=[1,10,50,100,350,450]
philist=[10,50,100,200,300,350,400,500,750,1000]

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
#gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","brNDC")
c = ROOT.TCanvas()

cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary  ')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)



#cs.SetLogy()
#f1 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/1000_500_testeff/CMSSW_8_0_26_patch1/src/bbMET/bbMET/bbMET/Output_testSkimmedTree.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.
#f1=ROOT.TFile.Open(args.file,'read')

parser = argparse.ArgumentParser()
parser.add_argument("--file","-f", type=str, required=True)
args = parser.parse_args()
print "file name:",format(args.file)
#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
#f1=args.filei
f1=ROOT.TFile.Open(args.file,'read')
total = f1.Get('h_total')
total.Draw()
print "Total events",total.Integral()

totalweight = f1.Get('h_total_weight')
totalweight.Draw()

print "totalweighted events", totalweight.Integral()

nak8=f1.Get('h_nak8jet_sr2_')
nca15=f1.Get('h_nca15jet_sr2_')

firstbin_nak8=nak8.GetBinContent(1)
firstbin_ca15=nca15.GetBinContent(1)

print "events in first bin_ak8",nak8.GetBinContent(1)
print "events in first bin_ca15",nca15.GetBinContent(1)
print "Total integral of ak8",nak8.Integral()
print "Total integral of CA15jets", nca15.Integral()

print "Efficiency_ak8 for first bin ", nak8.GetBinContent(1)/total.Integral()
print "Efficiency_ca15 for first bin ", nca15.GetBinContent(1)/total.Integral()

legend.SetTextSize(0.0246)
legend.SetBorderSize(0)
legend.SetLineColor(1)
legend.SetLineStyle(1)
legend.SetLineWidth(1)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetNColumns(2)
#legend.AddEntry(nak8,"Mass point (1000,1)","f")


nak8.SetXTitle("Number of AK8jets")
nak8.SetYTitle("Events")
nak8.SetFillColor(2)
nak8.Draw('bar0')
legend.AddEntry(nak8,"MH3_600_MH4_100_MH2_600_MHC_600","f")
#legend.Draw()
cmsname.Draw("same")
c.SaveAs("AK8jets.png")


nca15.SetXTitle("Number of CA15jets")
nca15.SetYTitle("Events")
nca15.SetFillColor(2)
nca15.Draw('bar0')
#legend.AddEntry(nak8,"MH3_600_MH4_100_MH2_600_MHC_600","f")
#legend.Draw()
cmsname.Draw("same")
c.SaveAs("CA15jets.png")

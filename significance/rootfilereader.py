#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D,TH2D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import ROOT as ROOT
import os
import sys, optparse,math



gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(0)
#gStyle.SetPadColor(1)
legend=TLegend(.63,.69,.87,.89)
canvas = ROOT.TCanvas()
canvas.SetLogy()
f1 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/files_jetpt30/Output_bbDM_SkimmedTrees_signal_180306_scalar_LO_Mchi-1_Mphi-200.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")

hist_totalevents1 = f1.Get('h_total')
hist_totalevents1.Draw()
totalevents1 = hist_totalevents1.Integral()

hist_ptcuts_events1=f1.Get('h_jet1_pT_sr2_')
hist_ptcuts_events1.Draw()
ptcuts_events1=hist_ptcuts_events1.Integral()

#hist_genMET_bbDM1_LO = f1.Get('h_total')

#hist_genMET_bbDM2_LO = f1.Get('h_jet1_pT_sr1_')


#hist_genMET_bbDM_LO.Rebin(10)
#hist_genMET_bbDM_LO.SetLineColor(2)
#hist_genMET_bbDM_LO.SetXTitle("genMET[GeV]")
#hist_genMET_bbDM_LO.SetYTitle("Events")
#hist_genMET_bbDM_LO.Scale(1/hist_genMET_bbDM_LO.Integral())
#hist_genMET_bbDM1_LO.Draw()

#print "sr2_jet1: ", hist_jet1_sr2_LO.Integral(10,50)
#print "sr2_jet2: ", hist_jet2_sr2_LO.Integral()

#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
#legend.AddEntry(hist_pfMET_bbDM_LO,"pfMET_LO_bbDM","L")

###########################################################################################

f2 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/files_jetpt30/Output_bbDM_SkimmedTrees_signal_180306_scalar_LO_Mchi-1_Mphi-350.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
hist_totalevents2 = f2.Get('h_total')
hist_totalevents2.Draw()
totalevents2 = hist_totalevents2.Integral()

hist_ptcuts_events2=f2.Get('h_jet1_pT_sr2_')
hist_ptcuts_events2.Draw()
ptcuts_events2=hist_ptcuts_events2.Integral()
#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
#legend.AddEntry(hist_pfMET_bbDM_LO,"pfMET_LO_bbDM","L")

##################################################################################

f3 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/files_jetpt30/Output_bbDM_SkimmedTrees_signal_180306_scalar_LO_Mchi-1_Mphi-500.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
hist_totalevents3 = f3.Get('h_total')
hist_totalevents3.Draw()
totalevents3 = hist_totalevents3.Integral()

hist_ptcuts_events3=f3.Get('h_jet1_pT_sr2_')
hist_ptcuts_events3.Draw()
ptcuts_events3=hist_ptcuts_events3.Integral()

#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
#legend.AddEntry(hist_pfMET_bbDM_LO,"pfMET_LO_bbDM","L")

##############################################################################

f4 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/files_jetpt30/Output_bbDM_SkimmedTrees_signal_180306_scalar_LO_Mchi-1_Mphi-1000.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")

hist_totalevents4 = f4.Get('h_total')
hist_totalevents4.Draw()
totalevents4 = hist_totalevents4.Integral()

hist_ptcuts_events4=f4.Get('h_jet1_pT_sr2_')
hist_ptcuts_events4.Draw()
ptcuts_events4=hist_ptcuts_events4.Integral()

#legend.AddEntry(hist_genMET_bbDM_LO,"genMET_LO_bbDM","L")
#legend.AddEntry(hist_pfMET_bbDM_LO,"pfMET_LO_bbDM","L")


print "pt>50 cut for all masspoint(mchi=1,mphi=....)"

print "TotalEvents",hist_totalevents1.Integral(), "Events_cut50: ",hist_ptcuts_events1.Integral(6,100),"mass: 200", "ratio: ", (hist_ptcuts_events1.Integral(6,100)/hist_totalevents1.Integral())
print "TotalEvents",hist_totalevents2.Integral(), "Events_cut50: ",hist_ptcuts_events2.Integral(6,100),"mass: 350","ratio: ", (hist_ptcuts_events2.Integral(6,100)/hist_totalevents2.Integral())
print "TotalEvents",hist_totalevents3.Integral(), "Events_cut50: ",hist_ptcuts_events3.Integral(6,100),"mass: 500","ratio: ", (hist_ptcuts_events3.Integral(6,100)/hist_totalevents3.Integral())
print "TotalEvents",hist_totalevents4.Integral(), "Events_cut50: ",hist_ptcuts_events4.Integral(6,100),"mass: 1000","ratio: ", (hist_ptcuts_events4.Integral(6,100)/hist_totalevents4.Integral())


print "pt>60 cut for all masspoint(mchi=1,mphi=....)"

print "TotalEvents",hist_totalevents1.Integral(), "Events_cut60: ",hist_ptcuts_events1.Integral(7,100),"mass: 200", "ratio: ", (hist_ptcuts_events1.Integral(7,100)/hist_totalevents1.Integral())
print "TotalEvents",hist_totalevents2.Integral(), "Events_cut60: ",hist_ptcuts_events2.Integral(7,100),"mass: 350","ratio: ", (hist_ptcuts_events2.Integral(7,100)/hist_totalevents2.Integral())
print "TotalEvents",hist_totalevents3.Integral(), "Events_cut60: ",hist_ptcuts_events3.Integral(7,100),"mass: 500","ratio: ", (hist_ptcuts_events3.Integral(7,100)/hist_totalevents3.Integral())
print "TotalEvents",hist_totalevents4.Integral(), "Events_cut60: ",hist_ptcuts_events4.Integral(7,100),"mass: 1000","ratio: ", (hist_ptcuts_events4.Integral(7,100)/hist_totalevents4.Integral())


print "pt>70 cut for all masspoint(mchi=1,mphi=....)"

print "TotalEvents",hist_totalevents1.Integral(), "Events_cut70: ",hist_ptcuts_events1.Integral(8,100),"mass: 200", "ratio: ", (hist_ptcuts_events1.Integral(8,100)/hist_totalevents1.Integral())
print "TotalEvents",hist_totalevents2.Integral(), "Events_cut70: ",hist_ptcuts_events2.Integral(8,100),"mass: 350","ratio: ", (hist_ptcuts_events2.Integral(8,100)/hist_totalevents2.Integral())
print "TotalEvents",hist_totalevents3.Integral(), "Events_cut70: ",hist_ptcuts_events3.Integral(8,100),"mass: 500","ratio: ", (hist_ptcuts_events3.Integral(8,100)/hist_totalevents3.Integral())
print "TotalEvents",hist_totalevents4.Integral(), "Events_cut70: ",hist_ptcuts_events4.Integral(8,100),"mass: 1000","ratio: ", (hist_ptcuts_events4.Integral(8,100)/hist_totalevents4.Integral())


print "pt>80 cut for all masspoint(mchi=1,mphi=....)"

print "TotalEvents",hist_totalevents1.Integral(), "Events_cut80: ",hist_ptcuts_events1.Integral(9,100),"mass: 200", "ratio: ", (hist_ptcuts_events1.Integral(9,100)/hist_totalevents1.Integral())
print "TotalEvents",hist_totalevents2.Integral(), "Events_cut80: ",hist_ptcuts_events2.Integral(9,100),"mass: 350","ratio: ", (hist_ptcuts_events2.Integral(9,100)/hist_totalevents2.Integral())
print "TotalEvents",hist_totalevents3.Integral(), "Events_cut80: ",hist_ptcuts_events3.Integral(9,100),"mass: 500","ratio: ", (hist_ptcuts_events3.Integral(9,100)/hist_totalevents3.Integral())
print "TotalEvents",hist_totalevents4.Integral(), "Events_cut80: ",hist_ptcuts_events4.Integral(9,100),"mass: 1000","ratio: ", (hist_ptcuts_events4.Integral(9,100)/hist_totalevents4.Integral())


print "pt>90 cut for all masspoint(mchi=1,mphi=....)"

print "TotalEvents",hist_totalevents1.Integral(), "Events_cut90: ",hist_ptcuts_events1.Integral(10,100),"mass: 200", "ratio: ", (hist_ptcuts_events1.Integral(10,100)/hist_totalevents1.Integral())
print "TotalEvents",hist_totalevents2.Integral(), "Events_cut90: ",hist_ptcuts_events2.Integral(10,100),"mass: 350", "ratio: ", (hist_ptcuts_events2.Integral(10,100)/hist_totalevents2.Integral())
print "TotalEvents",hist_totalevents3.Integral(), "Events_cut90: ",hist_ptcuts_events3.Integral(10,100),"mass: 500","ratio: ", (hist_ptcuts_events3.Integral(10,100)/hist_totalevents3.Integral())
print "TotalEvents",hist_totalevents4.Integral(), "Events_cut90: ",hist_ptcuts_events4.Integral(10,100),"mass: 1000","ratio: ", (hist_ptcuts_events4.Integral(10,100)/hist_totalevents4.Integral())

#canvas.BuildLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")
#legend.Draw()


g1 = ROOT.TFile.Open('/afs/cern.ch/work/d/dekumar/punzi_significance/files_jetpt30/jet2_pT_sr2.root', 'read')
# Setup a canvas for plotting. The arguments are a name, an optional title, and the width and height in pixels.

#legend=TLegend(0.2,0.7,0.48,0.9,"(M_{#chi}=1, M_{#phi}=500)")

hist_jet2pt = g1.Get('bkgSum')
hist_jet2pt.Draw()
_1e2b_events = hist_jet2pt.Integral()



print "total events: ",hist_jet2pt.Integral()
print "total events at cut30: ",hist_jet2pt.Integral(6+2,200)
print "total events at cut35: ",hist_jet2pt.Integral(7+2,200)
print "total events at cut40: ",hist_jet2pt.Integral(8+2,200)
print "total events at cut45: ",hist_jet2pt.Integral(9+2,200)
print "total events at cut50: ",hist_jet2pt.Integral(10+2,200)



print "total events at cut55: ",hist_jet2pt.Integral(11+2,200)
print "total events at cut60: ",hist_jet2pt.Integral(12+2,200)
print "total events at cut65: ",hist_jet2pt.Integral(13+2,200)
print "total events at cut70: ",hist_jet2pt.Integral(14+2,200)
print "total events at cut75: ",hist_jet2pt.Integral(15+2,200)
print "total events at cut80: ",hist_jet2pt.Integral(16+2,200)



print "Significance calculation at pt 50"
#print "n"
eff50_200=(hist_ptcuts_events1.Integral(6,100)/hist_totalevents1.Integral())
eff50_350=(hist_ptcuts_events2.Integral(6,100)/hist_totalevents2.Integral())
eff50_500=(hist_ptcuts_events3.Integral(6,100)/hist_totalevents3.Integral())
eff50_1000=(hist_ptcuts_events4.Integral(6,100)/hist_totalevents4.Integral())

eff50_200=(hist_ptcuts_events1.Integral(6,100)/hist_totalevents1.Integral())
eff50_350=(hist_ptcuts_events2.Integral(6,100)/hist_totalevents2.Integral())
eff50_500=(hist_ptcuts_events3.Integral(6,100)/hist_totalevents3.Integral())
eff50_1000=(hist_ptcuts_events4.Integral(6,100)/hist_totalevents4.Integral())

sig50_200=eff50_200/math.sqrt(hist_jet2pt.Integral(6,100))
sig50_350=eff50_350/math.sqrt(hist_jet2pt.Integral(6,100))
sig50_500=eff50_500/math.sqrt(hist_jet2pt.Integral(6,100))
sig50_1000=eff50_1000/math.sqrt(hist_jet2pt.Integral(6,100))

print "200  ",sig50_200
print "350 ",sig50_350
print "500",sig50_500
print "1000",sig50_1000


print "Significance calculation at pt 60"
#

eff60_200=(hist_ptcuts_events1.Integral(7,100)/hist_totalevents1.Integral())
eff60_350=(hist_ptcuts_events2.Integral(7,100)/hist_totalevents2.Integral())
eff60_500=(hist_ptcuts_events3.Integral(7,100)/hist_totalevents3.Integral())
eff60_1000=(hist_ptcuts_events4.Integral(7,100)/hist_totalevents4.Integral())

sig60_200=eff60_200/math.sqrt(hist_jet2pt.Integral(7,100))
sig60_350=eff60_350/math.sqrt(hist_jet2pt.Integral(7,100))
sig60_500=eff60_500/math.sqrt(hist_jet2pt.Integral(7,100))
sig60_1000=eff60_1000/math.sqrt(hist_jet2pt.Integral(7,100))

print "200  ",sig60_200
print "350 ",sig60_350
print "500",sig60_500
print "1000",sig60_1000


print "Significance calculation at pt  70"

eff70_200=(hist_ptcuts_events1.Integral(8,100)/hist_totalevents1.Integral())
eff70_350=(hist_ptcuts_events2.Integral(8,100)/hist_totalevents2.Integral())
eff70_500=(hist_ptcuts_events3.Integral(8,100)/hist_totalevents3.Integral())
eff70_1000=(hist_ptcuts_events4.Integral(8,100)/hist_totalevents4.Integral())


sig70_200=eff70_200/math.sqrt(hist_jet2pt.Integral(8,100))
sig70_350=eff70_350/math.sqrt(hist_jet2pt.Integral(8,100))
sig70_500=eff70_500/math.sqrt(hist_jet2pt.Integral(8,100))
sig70_1000=eff70_1000/math.sqrt(hist_jet2pt.Integral(8,100))



print "200  ",sig70_200
print "350 ",sig70_350
print "500",sig70_500
print "1000",sig70_1000

print "Significance calculation at pt  80"

eff80_200=(hist_ptcuts_events1.Integral(9,100)/hist_totalevents1.Integral())
eff80_350=(hist_ptcuts_events2.Integral(9,100)/hist_totalevents2.Integral())
eff80_500=(hist_ptcuts_events3.Integral(9,100)/hist_totalevents3.Integral())
eff80_1000=(hist_ptcuts_events4.Integral(9,100)/hist_totalevents4.Integral())


sig80_200=eff80_200/math.sqrt(hist_jet2pt.Integral(9,100))
sig80_350=eff80_350/math.sqrt(hist_jet2pt.Integral(9,100))
sig80_500=eff80_500/math.sqrt(hist_jet2pt.Integral(9,100))
sig80_1000=eff80_1000/math.sqrt(hist_jet2pt.Integral(9,100))

print "200  ",sig80_200
print "350 ",sig80_350
print "500",sig80_500
print "1000",sig80_1000


print "Significance calculation at pt  90"

eff90_200=(hist_ptcuts_events1.Integral(10,100)/hist_totalevents1.Integral())
eff90_350=(hist_ptcuts_events2.Integral(10,100)/hist_totalevents2.Integral())
eff90_500=(hist_ptcuts_events3.Integral(10,100)/hist_totalevents3.Integral())
eff90_1000=(hist_ptcuts_events4.Integral(10,100)/hist_totalevents4.Integral())


sig90_200=eff90_200/math.sqrt(hist_jet2pt.Integral(10,100))
sig90_350=eff90_350/math.sqrt(hist_jet2pt.Integral(10,100))
sig90_500=eff90_500/math.sqrt(hist_jet2pt.Integral(10,100))
sig90_1000=eff90_1000/math.sqrt(hist_jet2pt.Integral(10,100))


print "200  ",sig90_200
print "350 ",sig90_350
print "500",sig90_500
print "1000",sig90_1000





canvas.SaveAs('test.png')

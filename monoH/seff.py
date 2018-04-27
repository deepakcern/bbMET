from ROOT import TFile, TLatex, TGraph, TTree, TH1F,  TCanvas, TChain, TMath, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import os
import glob
from array import array

path = '/afs/cern.ch/work/d/dekumar/public/monoH/ST_BR_test/CMSSW_8_0_26_patch1/src/bbMET/bbMET/bbMET/BROutput/*.root'

MH4=['100','150','200','250','300','350','400','500']

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)

eff=[]
mass=[]

cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

c=TCanvas()
files = glob.glob(path)
print "files",files
for file in files:
    f=TFile.Open(file,'read')
    print "file",f
    hist_total=f.Get('h_total')
    total_events=hist_total.Integral()
    hist_sel=f.Get('h_nca15jet_sr2_')
    hist_sel.Draw()
    bin_events=hist_sel.GetBinContent(1)
    seff=(bin_events)/(total_events)
    print "se",seff
    for i in MH4:
        print i
        if i in file.strip():
            mass.append(int(i))
            eff.append(seff)
            print "mass", i
            print "eff", seff
x=array("d",mass)
y=array("d",eff)
n=len(mass)
gr = TGraph( n, x, y )
gr.SetTitle("Signal Efficiency Vs MH4")
gr.GetXaxis().SetTitle("Mass(MH4)")
gr.GetYaxis().SetTitle("Efficiency")
gr.SetLineColor(2)
gr.Draw("AC*")
cmsname.Draw()
c.SaveAs("efficiency.pdf")

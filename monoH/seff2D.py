from ROOT import TFile, TLatex, TGraph, TTree, TH1F, TH2F, TCanvas, TChain, TMath, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import os
import glob,math
from array import array

path = '/afs/cern.ch/work/d/dekumar/public/monoH/bbMETSamples/CA15BRoutput/Filelist_180422_mc_skimmed/*'

Mzp=['10','15','20','50','100','200','300','500','1000','2000','10000']
mchi=['1','10','50','150','500','1000']

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)

eff=[]
mass=[]
print '#sqrt{10}'
cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

c=TCanvas()
c.SetLogz()
hist2=TH2F("hist2","",len(Mzp),0,len(Mzp),len(mchi),0,len(mchi))
hist2.GetYaxis().SetTitle("#chi Mass (GeV)")
hist2.GetXaxis().SetTitle("M_{ZP} (GeV)")
hist2.SetStats(0)
hist2.SetMaximum(0.05)
hist2.SetMinimum(2e-3)

files = sorted(glob.glob(path))
print "total files",files
for file in files:
    f=TFile.Open(file,'read')
    print "selected file",f
    hist_total=f.Get('h_total')
    total_events=hist_total.Integral()
    hist_sel=f.Get('h_nak8jet_sr2_')
    hist_sel.Draw()
    bin_events=hist_sel.GetBinContent(1)
    seff=(bin_events)/(total_events)
    print "se",seff
    for i in Mzp:
        print "points of Mzp",i
        if 'MZp-'+i+'_' in file.split('/')[-1].strip('MC25ns_LegacyMC_20170328.root'):
            print '#sqrt{10}'
            for j in mchi:
                print "mass points of Mchi",j
                if 'MChi-'+j+'_' in file.split('/')[-1].strip('MC25ns_LegacyMC_20170328.root'):
                    for numx in range(len(Mzp)):
                        for numy in range(len(mchi)):
                            if i==Mzp[numx] and j==mchi[numy]:
                                print "selected Mzp: ", Mzp[numx]
                                print "selected mchi: ", mchi[numy]
                                hist2.GetXaxis().SetBinLabel(numx+1,i)
                                hist2.GetYaxis().SetBinLabel(numy+1,j)
                                hist2.SetBinContent(numx+1,numy+1,seff)


hist2.Draw("COLZ TEXT")
cmsname.Draw()
c.SaveAs("efficiencyak8.pdf")

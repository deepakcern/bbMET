
import elementtree.ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex


pt_phi1=[]
pt_b=[]
pt_bbar=[]
eta_b=[]
eta_bbar=[]
met1=[]
met2=[]
met3=[]
met4=[]
DR=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","brNDC")
c = TCanvas()
legend=TLegend(.63,.69,.87,.89)
cmsname=TLatex(0.15,0.95,'CMS Simulation Preliminary  ')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
#lhefdata=LHEFData(float(root.attrib['version']))
tree1 = ET.parse('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/lhefiles/run01/events.lhe')
root1=tree1.getroot()
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())



       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='52']
       chibar=[s for s in lines if s.split()[0]=='-52']
       b=[s for s in lines if s.split()[0]=='5']
       bbar=[s for s in lines if s.split()[0]=='-5']


       if phi:

           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)
           #pt_phi1.append(p.Pt())


       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       pi=p1+p2

       met1.append(pi.Pt())

       px3=float (b[0].split()[6])
       py3=float (b[0].split()[7])
       pz3=float (b[0].split()[8])
       e3=float (b[0].split()[9])

       px4=float (bbar[0].split()[6])
       py4=float (bbar[0].split()[7])
       pz4=float (bbar[0].split()[8])
       e4=float (bbar[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       pb=p3+p4
       pt_b.append(p3.Pt())
       eta_b.append(p3.Eta())
       pt_bbar.append(p4.Pt())
       eta_bbar.append(p4.Eta())
       DR.append(abs(p3.DeltaR(p4)))



h1_met=TH1F("genMET","",100,0,1000)
for i in met1:
        h1_met.Fill(i)

h1_DR=TH1F("DR(b,bbar)","",5,0,5)
for i in DR:
        h1_DR.Fill(i)

h_ptb=TH1F("pT of b","",100,0,1000)
for i in pt_b:
        h_ptb.Fill(i)

h_etab=TH1F("Eta of b","",10,-5,5)
for i in eta_b:
        h_etab.Fill(i)

h_ptbbar=TH1F("pT of bbar","",100,0,1000)
for i in pt_bbar:
        h_ptbbar.Fill(i)

h_etabbar=TH1F("Eta of bbar","",10,-5,5)
for i in eta_bbar:
        h_etabbar.Fill(i)

#------------------------------------------------------------------------
tree2 = ET.parse('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/lhefiles/run02/events.lhe')
root2=tree2.getroot()
for child in root2:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())



       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='52']
       chibar=[s for s in lines if s.split()[0]=='-52']
       b=[s for s in lines if s.split()[0]=='5']
       bbar=[s for s in lines if s.split()[0]=='-5']


       if phi:

           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)
           #pt_phi1.append(p.Pt())


       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       pi=p1+p2

       met2.append(pi.Pt())

       px3=float (b[0].split()[6])
       py3=float (b[0].split()[7])
       pz3=float (b[0].split()[8])
       e3=float (b[0].split()[9])

       px4=float (bbar[0].split()[6])
       py4=float (bbar[0].split()[7])
       pz4=float (bbar[0].split()[8])
       e4=float (bbar[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       pb=p3+p4
       #pt_b.append(p3.Pt())
       #eta_b.append(p3.Eta())
       #pt_bbar.append(p4.Pt())
       #eta_bbar.append(p4.Eta())
       #DR.append(abs(p3.DeltaR(p4)))



h2_met=TH1F("genMET","",100,0,1000)
for i in met2:
        h2_met.Fill(i)


#----------------------------------------------------------------
tree3 = ET.parse('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/lhefiles/run03/events.lhe')
root3=tree3.getroot()
for child in root3:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())



       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='52']
       chibar=[s for s in lines if s.split()[0]=='-52']
       b=[s for s in lines if s.split()[0]=='5']
       bbar=[s for s in lines if s.split()[0]=='-5']


       if phi:

           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)
           #pt_phi1.append(p.Pt())


       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       pi=p1+p2

       met3.append(pi.Pt())

       px3=float (b[0].split()[6])
       py3=float (b[0].split()[7])
       pz3=float (b[0].split()[8])
       e3=float (b[0].split()[9])

       px4=float (bbar[0].split()[6])
       py4=float (bbar[0].split()[7])
       pz4=float (bbar[0].split()[8])
       e4=float (bbar[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       pb=p3+p4
       #pt_b.append(p3.Pt())
       #eta_b.append(p3.Eta())
       #pt_bbar.append(p4.Pt())
       #eta_bbar.append(p4.Eta())
       #DR.append(abs(p3.DeltaR(p4)))



h3_met=TH1F("genMET","",100,0,1000)
for i in met3:
        h3_met.Fill(i)


#---------------------------------------------------------------
tree4 = ET.parse('/afs/cern.ch/work/d/dekumar/punzi_significance/scalar_signalfiles/SRs/lhefiles/run04/events.lhe')
root4=tree4.getroot()
for child in root4:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())



       phi=[s for s in lines if s.split()[0]=='55']
       chi=[s for s in lines if s.split()[0]=='52']
       chibar=[s for s in lines if s.split()[0]=='-52']
       b=[s for s in lines if s.split()[0]=='5']
       bbar=[s for s in lines if s.split()[0]=='-5']


       if phi:

           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)
           #pt_phi1.append(p.Pt())


       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       pi=p1+p2

       met4.append(pi.Pt())

       px3=float (b[0].split()[6])
       py3=float (b[0].split()[7])
       pz3=float (b[0].split()[8])
       e3=float (b[0].split()[9])

       px4=float (bbar[0].split()[6])
       py4=float (bbar[0].split()[7])
       pz4=float (bbar[0].split()[8])
       e4=float (bbar[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       pb=p3+p4
       #pt_b.append(p3.Pt())
       #eta_b.append(p3.Eta())
       #pt_bbar.append(p4.Pt())
       #eta_bbar.append(p4.Eta())
       #DR.append(abs(p3.DeltaR(p4)))



h4_met=TH1F("genMET","",100,0,1000)
for i in met4:
        h4_met.Fill(i)


#-----------------------------------------------------------------

#c=TCanvas()
c.SetLogy()

h1_met.SetXTitle("genMET[GeV]")
h1_met.SetYTitle("Events")
h1_met.SetLineColor(1)
h1_met.Rebin(5)
h1_met.Scale(13.47/h1_met.Integral())
h1_met.SetMaximum(1500)
legend.AddEntry(h1_met,"tan #beta =5","L")
h1_met.Draw()

h2_met.SetLineColor(2)
h2_met.Rebin(5)
h2_met.Scale(58.05/h2_met.Integral())
legend.AddEntry(h2_met,"tan #beta =10","L")
h2_met.Draw('same')

#legend.AddEntry(h3_met,"tan #beta =35","L")
h3_met.SetLineColor(3)
h3_met.Rebin(5)
h3_met.Scale(666.5/h3_met.Integral())
legend.AddEntry(h3_met,"tan #beta =35","L")
h3_met.Draw('same')

#legend.AddEntry(h4_met,"tan #beta =50","L")
#h4_met.Scale(1460/h4_met.Integral())
h4_met.Rebin(5)
h4_met.SetLineColor(4)
h4_met.Scale(1460/h4_met.Integral())
legend.AddEntry(h4_met,"tan #beta =50","L")
h4_met.Draw('same')

cmsname.Draw()
legend.Draw()
c.SaveAs("met.pdf")

h1_DR.SetXTitle("#DeltaR(b,bbar)")
h1_DR.SetYTitle("Events")
h1_DR.Draw()
cmsname.Draw()
c.SaveAs("DR.pdf")

h_ptb.SetXTitle("pT of b")
h_ptb.SetYTitle("Events")
h_ptb.Draw()
cmsname.Draw()
c.SaveAs("ptb.pdf")

h_etab.SetXTitle("Eta of b")
h_etab.SetYTitle("Events")
h_etab.Draw()
cmsname.Draw()
c.SaveAs("etab.pdf")

h_ptbbar.SetXTitle("pT of bbar")
h_ptbbar.SetYTitle("Events")
h_ptbbar.Draw()
cmsname.Draw()
c.SaveAs("ptbbar.pdf")

h_etabbar.SetXTitle("Eta of bbar")
h_etabbar.SetYTitle("Events")
h_etabbar.Draw()
cmsname.Draw()
c.SaveAs("etabbar.pdf")

#c.BuildLegend(0.3,0.7,0.58,0.9,"(M_{#chi}=1, M_{#phi}=1000)")

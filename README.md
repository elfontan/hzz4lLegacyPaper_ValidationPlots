# Scripts for HZZ4l validation

*******************************
 **To perform Data vs Lumi study**
---

-  enter in JSONCalc/ directory and set 
   ```
   export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
   ```

   If you never used brilcalc you should also do:
   ```
   pip install --install-option="--prefix=$HOME/.local" brilws
   ```

-  then run the scripts:

   -   ./CalcJSON.sh                       to convert JSON file in txt
   -   python SplitPerLumi.py              to divide JSON into lumi block 

-  exit from the JSONCalc/ directory and run the scripts:

   -   python ExtractHistos.py             to store data into histo for each lumi block (needs some time)
   -   python FitDATA.py
   -   python FitMC.py
   -   python DataVsLumi.py                to plot Data vs Lumi


Then you can use:

-  python yellowPlots.py           to plot Data vs MC histos (DATA/MC comparison on the Z peak)


************************
To compare Iso DATA/MC distributions:

   -   python IsoDistrib_DATA.py 
   -   python IsoDistrib_MC.py
   -   python IsoDistrib_DATAvsMC.py 


To compare SIP DATA/MC distributions:
 
   -   python SipDistrib_DATA.py 
   -   python SipDistrib_MC.py 
   -   python SipDistrib_DATAvsMC.py


To compare LepBDT DATA/MC distributions:

   -   python LepBDTdistrib_DATA.py 
   -   python LepBDTdistrib_MC.py 
   -   python LepBDTdistrib_DATAvsMC.py 


To compare Lepton pT eta phi DATA/MC distributions:

   -   python LepPtEtaPhiDistrib_DATAvsMC.py


To study jets DATA/MC distributions:

   -   python jetsDistrib_DATAvsMC.py


************************	

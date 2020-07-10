#!/bin/bash

# *******************
# usage: 
#    - choose the period of your dataset
#    - ./CalcJSON.sh 
#
# structure:
#    - read file JSON
#    - convert JSON file in txt and compute luminosity
# ********************



# **********************
# Golden Json 2018 data 
# **********************

#2016
#JSON_path=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt
#2017
#JSON_path=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt
#2018
JSON_path=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt #Nov 24, 2018; 58.83/fb; https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/3259.html


#JSON_localName=GoldenJSON_2016data.txt
#Output=LumiCalc_2016data.txt
#JSON_localName=GoldenJSON_2017data.txt
#Output=LumiCalc_2017data.txt
JSON_localName=GoldenJSON_2018data.txt
Output=LumiCalc_2018data.txt


cp $JSON_path $JSON_localName

# normtag file is not available yet
brilcalc lumi -b "STABLE BEAMS" -u /fb -i $JSON_path -o $Output

# norm tag now available 
# brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i $JSON_path -u /fb -o $Output




echo DONE

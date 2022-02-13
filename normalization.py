# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:03:25 2022

@author: marco
"""
import sys
import requests
import pandas as pd
 

def main(compoundName):
    
    normalizedCompoound = []
    for compound in compoundName:
        response = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"+compound+"/synonyms/JSON")
        if response.status_code==200:
            normalizedCompoound.append(response.json().get("InformationList").get("Information")[0]["Synonym"][0].upper())
        else:
            normalizedCompoound.append("Synonym not found")
        
    data = {'org_form':compoundName,
            'normed_form':normalizedCompoound}
     
    df = pd.DataFrame(data)
    print(df)
    
    
    
if __name__ == '__main__':
    #compoundName = ["Adenosine","Adenocard","BG8967","Bivalirudin","BAYT006267","diflucan","ibrutinib","PC-32765"]
    compoundName = sys.argv
    del compoundName[0]
    main(compoundName)





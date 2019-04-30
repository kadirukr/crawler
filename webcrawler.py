import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

class WebScrapper:

    def lessorNamesArray(self, docArray):
        self.docArray = docArray
        arr_names = []
        for link in docArray:
            r = requests.get(link, verify=False)
            doc = BeautifulSoup(r.text,"html.parser")
            lessorNames = doc.find_all("h2",class_='lead page-header')
            
            for i in lessorNames:
                arr_names = np.append(arr_names, i.get_text())
    
        return arr_names

    def lessorPLZArray(self, docArray):
        self.docArray = docArray
        arr_plz = []
        for link in docArray:
            r = requests.get(link, verify=False)
            doc = BeautifulSoup(r.text,"html.parser")    
            lessor_plz = doc.find_all("div",class_='spField field_plz')
            
            for i in lessor_plz:    
                arr_plz = np.append(arr_plz, i.get_text()[4:])

        return arr_plz

    def lessorOrtArray(self, docArray):
        self.docArray = docArray
        arr_ort = []
        for link in docArray:
            r = requests.get(link, verify=False)
            doc = BeautifulSoup(r.text,"html.parser")
            lessor_ort = doc.find_all("div",class_='spField field_ort')
           
            for i in lessor_ort:
                arr_ort = np.append(arr_ort,i.get_text()[5:])
        
        return arr_ort
    
class xyz:

    def getPages(self):
        r = requests.get("https://www.bagger.de/haendler/baumaschinen-haendler/590-baumaschinen-geraete.html?site=1", verify=False)
        doc = BeautifulSoup(r.text,"html.parser")
        page_links = doc.find_all("div", class_ = "pagination pagination-centered")

        links = []
        for i in page_links:
            links = i.find_all("a")
            print (i)
        
        docArray = []
        for i in links:
            try:
                int(i.text)
                docArray = np.append(docArray, 'http://www.bagger.de' + i.get('href'))
            
            except:
                continue
        
        return docArray


 
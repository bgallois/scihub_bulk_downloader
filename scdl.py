#!/usr/bin/env python

import requests
import re
import os
import argparse


def checkBaseUrl(baseUrl):
    """Check the Scihub url to determinate if the website is reachable."""
    headers = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    r = requests.get(baseUrl, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False


def checkDoi(doiList):
    """Format the doi in a list of doi from a text file."""
    if len(doiList) == 1 and os.path.isfile(os.path.abspath(doiList[0])):
       with open(os.path.abspath(doiList[0])) as f:
           doiList = f.readlines()
       doiList = [i.strip() for i in doiList] 
    return doiList
    

def getPdf(baseUrl, doiUrl, outPath):
    """Download the pdf file from the Scihub adress and a doi."""
    headers = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    r = requests.get(baseUrl + doiUrl, headers=headers, allow_redirects=True)
    text = r.text
    pdfUrl = re.findall(r"https?://.*\.pdf", text)
    if pdfUrl:
        pdfName = pdfUrl[0].split('/')[-1]
        if outPath:
            savingPath = os.path.join(os.path.abspath(outPath), pdfName)
        else:
            savingPath = pdfName
        with open(savingPath, 'wb') as pdfFile:
            pdfFile.write(requests.get(pdfUrl[0]).content)
        return True
    else:
        return False



parser = argparse.ArgumentParser(description="Download articles from a list of DOI and a scihub mirror. The list of doi can be entered as a list or arguments or in a text file with one doi by line.") 
parser.add_argument("doi", nargs='+', help="List of DOI or files containing a list of DOI.")
parser.add_argument("--mirror", dest="scihubMirror", help="An url to a reachable Scihub mirror.", required=True)
parser.add_argument("--dest", dest="destination", help="Optional: A folder where to saved the papers. Default in the current directory.", required=False)

args = parser.parse_args()
if args.scihubMirror[-1] != "/":
    args.scihubMirror += "/"
if not checkBaseUrl(args.scihubMirror):
     raise Exception("Scihub mirror is not valid")
doi = checkDoi(args.doi)
for i in doi:
    if getPdf(args.scihubMirror, i, args.destination):
        print("Article " + i + " successfully downloaded :)")
    else:
        print("Article " + i + " NOT downloaded :( Check the DOI!")

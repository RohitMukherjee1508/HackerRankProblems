#!/usr/bin/env python
import sys, getopt
import csv
import json

#usage
if ((len(sys.argv) < 3)):
    print """\
        USAGE: csv2json -i users.csv -o users.json -f pretty
    """
    sys.exit(1)
#Get Command Line Arguments
def main(argv):
    csvFilename = r'csvFile.csv'
    jsonFilename = r'mydatalist.json'
    mydata = {}
    mykey = ""
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
   convjson(csvFilename, jsonFilename)

def convjson(csvFilename, jsonFilename):
    
    with open(csvFilename, encoding='utf-8') as csvfile:
        
        csvRead = csv.DictReader(csvfile)
        for rows in csvRead:
          mykey = rows['Route TableName']
          # print(rows)                    
          addressPrefix =rows["addressPrefix"] 
          nextHopType = rows["nextHopType"]
          nextHopIpAddress =  rows["nextHopIpAddress"]
          hasBgpOverride =  rows["hasBgpOverride"]
          string = {
          "type": "Microsoft.Network/routeTables/routes",
          "apiVersion": "2020-11-01",
          "name": mykey,
          "dependsOn": [
              "[resourceId('Microsoft.Network/routeTables', parameters('routeTables_rt_coreservices_prd_use_priv_udns_name'))]"
          ],
          "properties": {
              "addressPrefix": addressPrefix,
              "nextHopType": nextHopType,
              "nextHopIpAddress": nextHopIpAddress,
              "hasBgpOverride": hasBgpOverride
          }}
    with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
              jsonfile.write(json.dumps(string,indent = 4))

if __name__ == "__main__":
   main(sys.argv[1:])


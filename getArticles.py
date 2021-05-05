#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'getArticleTitles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
# 
# URL for cut and paste: 
# https://jsonmock.hackerrank.com/api/articles?author=<authorName>&page=<num>
# 
#

def getArticleTitles(author):

    if not author:  return []       #return if no author
    titles = []
    pageNum, total = 1, float('inf')             # large value store
    while pageNum <= total:
        url = "https://jsonmock.hackerrank.com/api/articles?author={0}&page={1}".format(author, pageNum)
        response = requests.get(url)
        res = json.loads(response.content)
        total = res['total_pages']

        for t in res['data']:
            if not t['title'] and not t['story_title']:
                continue
            elif not t['title']:
                titles += [t['story_title']]
            else:
                titles += [t['title']]
        pageNum += 1
    return titles
  
  
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    author = input()

    result = getArticleTitles(author)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

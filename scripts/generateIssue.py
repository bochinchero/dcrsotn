import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import os
import markdown
import re

# evaluation period
issue_start = dt.date(int(2023),int(12),int(1))
issue_end   = dt.date(int(2024),int(1),int(1))

issue_month = issue_start.strftime('%m')
issue_year = issue_start.strftime('%Y')
issue_monthStr = 'December'
issue_prevMonthStr = 'November'
# grab the csv file for the desired date
yearMonthStr = issue_year + '-' + issue_month
# concat date into base url
url = 'https://raw.githubusercontent.com/bochinchero/dcrsnapshots/main/' + yearMonthStr + '/monthlyStats.csv'
print(url)
# create pd dataframe with raw csv data
data = pd.read_csv(url)
# set id as the index
data = data.set_index('id')
# convert to lookup dictionary
dataDict = data.to_dict('index')
# updates the dictionary with the issue information
dataDict['Issue'] = {'Month':issue_month,'Year':issue_year,'PrevMonthStr':issue_prevMonthStr,'MonthStr':issue_monthStr}

# open the template markdown file
f = open('../template/Template.md', 'r')
htmlmd = markdown.markdown( f.read() )
# find a list of all variables - those tagged in curly brackets {}
res = re.findall(r'\{.*?\}', htmlmd)
# replace variables with values from the lookup dictionary
text_out = htmlmd
for i in res:
    x = re.search('\{.*?\.', i)
    id = x[0][1:-1]
    y = re.search('\..*?\}', i)
    key = y[0][1:-1]
    try:
        val = dataDict[id][key]
        text_out = text_out.replace(i,str(val))
    except:
        print("value not found for "+id+'.'+key)

# save to file
basePathStr = "../content/" + issue_year +'/'
pathStr = basePathStr
if not os.path.exists(pathStr):
    os.makedirs(pathStr)
filename = pathStr + yearMonthStr + '.md'
# remove file if it exists
if os.path.isfile(filename):
    os.remove(filename)
# save to file
text_file = open(filename, "w")
text_file.write(text_out)
text_file.close()

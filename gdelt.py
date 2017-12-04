import gdelt
import time
import pandas as pd
pd.set_option('display.max_colwidth', -1)
url_list = []
results_list = []
# Version 1 queries
gd1 = gdelt.gdelt(version=1)
dates =['2017 May 22','2017 May 23','2017 May 24','2017 May 25','2017 May 26','2017 May 27','2017 May 28','2017 May 29']
# pull all days mentioned in dates, events table
for day in dates:
    results= gd1.Search(day,table='events')
    results_list.append(len(results))
    #uk = results['ActionGeo_CountryCode'] == "UK"
    #uk_df = results[uk]
    uk_df1 = results[results['SOURCEURL'].str.contains("manchester|Manchester")]
    uk_df2 = uk_df1[uk_df1['SOURCEURL'].str.contains("fake|false|Fake|False|fraud|Fraud|malicious|Malicious|hoax|Hoax|untrue|Untrue|unreal|Unreal" )]
    uk_df2 = uk_df2.drop_duplicates(subset = ['SOURCEURL'], keep = 'first')
    listval = uk_df2['SOURCEURL'].tolist()
    url_list.append(listval)
    time.sleep(2)
print url_list

import config
import requests
import urllib.request as request
import json

# # https://www.glassdoor.com/developer/index.htm
# # https://www.glassdoor.com/developer/jobsApiActions.htm
# https://www.glassdoor.com/job-listing/details.htm?pos=101&ao=102921&s=58&guid=0000015ddcac31b880df8f909214a408&src=GD_JOB_AD&t=SR&extid=1&exst=OL&ist=&ast=OL&vt=w&slr=true&rtp=0&cb=1502645859672&jobListingId=2482350711
# https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=software+engineer&sc.keyword=software+engineer&locT=C&locId=2296722&jobType=

GLASSDOOR_PARTNER_ID = 180312
GLASSDOOR_KEY = 'kOBfBy2ph7I'
USERAGENT = "Mozilla/5.0"
location = "Montreal"
MY_IP = json.loads(request.urlopen("http://ip.jsontest.com/").read().decode('utf-8'))['ip'] # From the stackoverflow answer
url = 'http://api.glassdoor.com/api/api.htm'


payload1 = {'v':'1',
            'format':'json',
            't.p':GLASSDOOR_PARTNER_ID,
            't.k':GLASSDOOR_KEY,
            'userip':MY_IP,
            'useragent': USERAGENT,
            'action':'jobs-prog',
            'jobTitle': 'Software Engineer',
            'countryId': '1'
            }

payload = {'v':'1',
            'format':'json',
            't.p':GLASSDOOR_PARTNER_ID,
            't.k':GLASSDOOR_KEY,
            'userip':MY_IP,
            'useragent': USERAGENT,
            'action':'jobs-stats',
            'l': 'seattle',
            'q': 'software engineer',
            'jobType': 'fulltime',
            'returnJobTitles': 'True',
            "admLevelRequested": 1,
            "jc": 29
            }
hdr = {'User-Agent': USERAGENT}

r = requests.get(url, params=payload, headers=hdr)


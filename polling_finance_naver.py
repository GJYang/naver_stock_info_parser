from time import sleep
import json
import requests

# Silicon Works: 108320
sw='108320'
kakao='035720'
innotech='011070'
hdfeed='016790'
lge='066570'
sse='005930'
hynix='000660'
dstrobot='090710'
seoulsemi='046890'

kospi      = 'http://polling.finance.naver.com/api/realtime.nhn?query=SERVICE_INDEX:KOSPI'
naver_poll = 'http://polling.finance.naver.com/api/realtime.nhn?query=SERVICE_ITEM:'
url = naver_poll + hdfeed

CBLU = '\033[94m'
CGRE = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'

def queryKospi():
	r = requests.get(kospi)
	datas = r.json()['result']['areas'][0]['datas'][0]
	nv = datas['nv'] # now
	cv = datas['cv'] # current value
	ms = datas['ms'] # market status
	# aq
	# aa
	cr = datas['cr'] # curent raito
	hv = datas['hv'] # high
	lv = datas['lv'] # low
	# bs
	cd = datas['cd'] 
	if cr > 0:
		print ("%s(%s): %s, %s, %s%s%%%s" %(str(cd), str(ms), str(nv/100), str(cv/100), CRED, str(cr), CEND))
	else :
		print ("%s(%s): %s, %s, %s%s%%%s" %(str(cd), str(ms), str(nv/100), str(cv/100), CBLU, str(cr), CEND))
	return;


def queryStock(KRX_ID):
	r = requests.get(naver_poll + KRX_ID)
	datas = r.json()['result']['areas'][0]['datas'][0]
	sv = datas['sv'] # start 
	ov = datas['ov'] # open
	nv = datas['nv'] # now
	hv = datas['hv'] # high
	lv = datas['lv'] # low
	ul = datas['ul'] # up limit
	cr = datas['cr'] # curent raito
	cv = datas['cv'] # current value
	ms = datas['ms'] # market status
	pcv = datas['pcv'] # prev close value
	nm = datas['nm'] # name

	if nv > sv:
		print ("%s: %s, %s, %s, %s+%s%% %s" % (str(nm), str(ov), str(nv), str(hv), CRED, str(cr), CEND))
	else :
		print ("%s: %s, %s, %s, %s-%s%% %s" % (str(nm), str(ov), str(nv), str(hv), CBLU, str(cr), CEND))
	return;

while 1 :
	queryKospi()
	queryStock(lge)
	queryStock(sse)
	queryStock(hynix)
	queryStock(sw)
	queryStock(dstrobot)
	queryStock(seoulsemi)
	sleep(2)

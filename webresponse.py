import os
import datetime


def runOsCmd():

	os.system('cmd /c echo | set /p dummyName="Google, " >> google.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> google.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.google.com/" >> google.csv')

	os.system('cmd /c echo | set /p dummyName="Youtube, " >> youtube.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> youtube.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.youtube.com/" >> youtube.csv')

	os.system('cmd /c echo | set /p dummyName="HKYahoo, " >> hkyahoo.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> hkyahoo.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://hk.yahoo.com/" >> hkyahoo.csv')

	os.system('cmd /c echo | set /p dummyName="Wikipedia, " >> wikipedia.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> wikipedia.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.wikipedia.org/" >> wikipedia.csv')

	os.system('cmd /c echo | set /p dummyName="Lihkg, " >> lihkg.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> lihkg.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://lihkg.com/" >> lihkg.csv')

	os.system('cmd /c echo | set /p dummyName="Oncc, " >> oncc.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> oncc.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://hk.on.cc/" >> oncc.csv')

	os.system('cmd /c echo | set /p dummyName="HKJC, " >> hkjc.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> hkjc.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.hkjc.com/" >> hkjc.csv')

	os.system('cmd /c echo | set /p dummyName="HK01, " >> hk01.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> hk01.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.hk01.com/" >> hk01.csv')

	os.system('cmd /c echo | set /p dummyName="Taobao, " >> taobao.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> taobao.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.taobao.com" >> taobao.csv')

	os.system('cmd /c echo | set /p dummyName="Bilibili, " >> bilibili.csv')
	datetime_object = datetime.datetime.now()
	os.system('cmd /c echo | set /p dummyName="{}, " >> bilibili.csv'.format(datetime_object))
	os.system('cmd /c curl -w "@curl-format2.txt" -o NUL -s "https://www.bilibili.com/" >> bilibili.csv')


if __name__ == '__main__':
	try:
		datetime_prg = datetime.datetime.now()
		print("The program started:", datetime_prg)
		runOsCmd()
		datetime_prg = datetime.datetime.now()
		print("The program ended:", datetime_prg)

	except:
		print("Unexpected error:")
		raise
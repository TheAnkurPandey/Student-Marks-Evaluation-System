import requests, pprint

def ocr_space_file(filename='text.png', overlay=False, api_key='725dea855d88957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='725dea855d88957', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

	
def Search(pat, txt):
	M = len(pat)
	N = len(txt)
	lps = [0]*M
	j = 0
	computeLps(pat, M, lps)
	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			return 1
			j = lps[j-1]

		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
	return 0

def computeLps(pat, M, lps):
	len = 0
	lps[0]
	i = 1
	while i < M:
		if pat[i]==pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1


txt=[]
choice = input("Enter \'y' to enter answer manually, otherwise \'n' to upload images of answer.")
if choice == 'y':
	a = input("Name the petroleum product used for surfacing of road? \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("What are the advantages of using CNG and LPG? \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("Fossils fuels are ___ , ___ , ___. \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("Why fossils fuels are exhaustible natural resources? \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("kerosene is not a fossils fuels (T/F) \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("Least polluting fuel for vehicle is____. \nAnswer-->\t")
	txt.append(a)
	print("\n")
	a = input("How coal is formed from dead vegetation? \nAnswer-->\t")
	txt.append(a)
	print("\n")
else:
	test_file = ocr_space_file(filename='text.png', language='eng')
	txt = test_file[164:-237].replace(r"\r\n","")
	print(txt)
	
pat =[ ["bitumen"] ,
	   ["burnt directly" , "transport easily" , "no smoke" , "lot of heat energy"] ,
	   ["coal", "petroleum","natural gas"] ,
	   ["limited", "long formation"],
	   ["f"] ,
	   ["CNG"],
	   ["buried","compressed","high temperature", "high pressure"]]

print("\n\n")
print("---------Report Card---------\n")
i=0
while i<len(pat):
	count=0
	j=0
	while j<len(pat[i]):
		if Search(pat[i][j].lower(), txt[i].lower()):
			count=count+1
		j=j+1
	print("Probability for answer "+str(i)+": "+str( count/len(pat[i]) ) )
	i=i+1

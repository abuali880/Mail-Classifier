import operator
import numpy as np

TotalNumber = 0
SpamNumber = 0
HamNumber = 0
TotalSpamWords = 0
TotalHamWords = 0
SpamMap = {}
HamMap = {}
AllMap = {}
PropSpamMap = {}
PropHamMap = {}
TrainFile = open("train","r")
for line in TrainFile:
	TotalNumber=TotalNumber+1
	words = line.split()
	if words[1]=="spam":
		SpamNumber=SpamNumber+1
		for i in range(2,len(words),2):
			if words[i] in SpamMap:
				SpamMap[words[i]] = int(words[i+1]) + SpamMap[words[i]]
				pass
			else :
				SpamMap[words[i]] = int(words[i+1])
				pass
			pass
		pass
	elif words[1]=="ham":
		HamNumber=HamNumber+1
		for i in range(2,len(words),2):
			if words[i] in HamMap:
				HamMap[words[i]] = int(words[i+1]) + HamMap[words[i]]
				pass
			else :
				HamMap[words[i]] = int(words[i+1])
				pass
			pass
		pass
	pass

SpamPrior = float(SpamNumber)/float(TotalNumber)
HamPrior = float(HamNumber)/float(TotalNumber)
DistinctSpamWords = len(SpamMap)
DistictHamWords = len(HamMap)
#print(SpamPrior,HamPrior)

for v in SpamMap.values():
	TotalSpamWords = TotalSpamWords + v
	pass

for v in HamMap.values():
	TotalHamWords = TotalHamWords + v
	pass

for k,v in SpamMap.items():
	PropSpamMap[k] =  float(v + 1)/float(TotalSpamWords+1000)
	pass

for k,v in HamMap.items():
	PropHamMap[k] = float(v + 1)/float(TotalHamWords+1000)
	pass

SortedPropHamMap = sorted(PropHamMap.items(), key=operator.itemgetter(1),reverse=True)
SortedPropSpamMap = sorted(PropSpamMap.items(), key=operator.itemgetter(1),reverse=True)
for v in SortedPropSpamMap:
#	print(v)
	pass
#print(PropSpamMap)
#print(TotalSpamWords)
#print(TotalHamWords)

TrainFile.close()
TotalEmails = 0
CorrectClassifiedMails = 0
flag2 = True
TestFile = open("test","r")
for line in TestFile:
	TotalEmails = TotalEmails + 1
	SpamMail = 1.0
	HamMail = 1.0
	words = line.split()
	for i in range(2,len(words),2):
		if words[i] in PropSpamMap:
			SpamMail =  1000 * float(SpamMail) * float(PropSpamMap[words[i]]) * float(words[i+1])
			pass
		else:
			SpamMail = 1000 * float(SpamMail) * float(1.0/(1000+TotalSpamWords)) *float(words[i+1])
			pass
		pass
		if words[i] in PropHamMap:
			HamMail =  1000 * float(HamMail) * float(PropHamMap[words[i]])*float(words[i+1])
			pass
		else:
			HamMail = 1000 * float(HamMail) * float(1.0/(1000+TotalHamWords)) *float(words[i+1])
			pass
		pass
	SpamMail = SpamMail * SpamPrior
	HamMail = HamMail * HamPrior
	#print(SpamMail,HamMail)
	if HamMail > SpamMail:
		indi  = "ham"
	else:
		indi = "spam"
	if words[1] == indi:
		CorrectClassifiedMails = CorrectClassifiedMails + 1
		pass
Accuracy = (float(CorrectClassifiedMails) / float(TotalEmails))*100.0
print(Accuracy)
#print(CorrectClassifiedMails,TotalEmails)


#Implement the naive -bayes learning algorithm for restaurant waiting porblem
rwp_examples=dict(
 x1=dict(Alt='Y', Bar='N',Fri='N', Hun='Y',Pat='S',Price='$$$',Rain='N',Res='Y',Type='F',Est='0-10',ans='Y'),
 X2=dict(Alt='Y', Bar='N',Fri='N', Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='T',Est='30-60',ans='N'),
 x3=dict(Alt='N', Bar='Y',Fri='N', Hun='N',Pat= 'S',Price='$',Rain='N',Res='N',Type='N',Est='0-10',ans='Y'),
 x4=dict(Alt='Y', Bar='N',Fri='Y', Hun='Y',Pat='F',Price='$',Rain='Y',Res='N',Type='T',Est='10-30',ans='Y'),
 x5=dict(Alt='Y', Bar='N',Fri='Y', Hun='Y',Pat='F',Price='$$$',Rain='N',Res='Y',Type='F',Est='>60',ans='N'),
 x6=dict(Alt='N', Bar='Y',Fri='N', Hun='Y',Pat='S',Price='$$',Rain='Y',Res='N',Type='I',Est='0-10',ans='Y'),
 x7=dict(Alt='N', Bar='Y',Fri='N', Hun='N',Pat='N',Price='$',Rain='Y',Res='Y',Type='B',Est='0-10',ans='N'),
 x8=dict(Alt='N', Bar='N',Fri='N', Hun='Y',Pat='S',Price='$$',Rain='Y',Res='Y',Type='T',Est='0-10',ans='Y'),
 x9=dict(Alt='N', Bar='Y',Fri='Y', Hun='N',Pat='F',Price='$',Rain='Y',Res='N',Type='B',Est='>60',ans='N'),
 x10=dict(Alt='Y', Bar='Y',Fri='Y', Hun='Y',Pat='F',Price='$$$',Rain='N',Res='Y',Type='I',Est='10-30',ans='N'),
 x11=dict(Alt='N', Bar='N',Fri='N', Hun='N',Pat='N',Price='$',Rain='N',Res='N',Type='T',Est='0-10',ans='N'),
 x12=dict(Alt='Y', Bar='Y',Fri='Y', Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y'))
total_exp=12
def tot(attribute,value):
	count=0
	for key,val in rwp_examples.items():
		for key1,val1 in val.items():
			if key1==attribute:
				if val1==value:
					count+=1
	return count
def getProbab(attribute,attrival,value):
	count=0
	for key,val in rwp_examples.items():
		val1=rwp_examples[key][attribute]
		val2=rwp_examples[key]['ans']
		if val1==attrival and val2==value:
			count+=1
	probab=count/tot('ans',value)
	return probab

def main():
	PAltYes=tot('Alt','Y')/total_exp
	PAltNo=tot('Alt','N')/total_exp
	PBarYes=tot('Bar','Y')/total_exp
	PBarNo=tot('Bar','N')/total_exp
	PFriYes=tot('Fri','Y')/total_exp
	PFriNo=tot('Fri','N')/total_exp
	PHunYes=tot('Hun','Y')/total_exp
	PHunNo=tot('Hun','N')/total_exp
	PPatSome=tot('Pat','S')/total_exp
	PPatFull=tot('Pat','F')/total_exp
	PPatNone=tot('Pat','N')/total_exp
	PPriceCheap=tot('Price','$')/total_exp
	PPriceAvg=tot('Price','$$')/total_exp
	PPriceExp=tot('Price','$$$')/total_exp
	PRainYes=tot('Rain','Yes')/total_exp
	PRainNo=tot('Rain','No')/total_exp
	PResYes=tot('Res','Yes')/total_exp
	PResNo=tot('Res','No')/total_exp
	PTypeFrench=tot('Type','F')/total_exp
	PTypeThai=tot('Type','T')/total_exp
	PTypeBurger=tot('Type','B')/total_exp
	PTypeItalian=tot('Type','I')/total_exp
	PEstFew=tot('Est','0-10')/total_exp
	PEstMore=tot('Est','10-30')/total_exp
	PEstStillMore=tot('Est','30-60')/total_exp
	PEstTooMuch=tot('Est','>60')/total_exp
	PAnsYes=tot('ans','Y')/total_exp
	PAnsNo=tot('ans','N')/total_exp
	print("Probability for people will wait if there is an alternate restaurant : ")
	print("Yes: Will wait: ",(getProbab('Alt','Y','Y')*PAnsYes/PAltYes)*100,"%")
	print("No : Will wait: ",(getProbab('Alt','Y','N')*PAnsNo/PAltYes)*100,"%") 
	print("Probability for people will wait if there is no alternate restaurant : ")
	print("Yes : Will wait: ",(getProbab('Alt','N','Y')*PAnsYes/PAltNo)*100,"%")
	print("No : Will wait: ",(getProbab('Alt','N','N')*PAnsNo/PAltNo)*100,"%")
	print("Probability for people  will wait sif the Estimated Wait Time is 0-10 mins :")
	print("Yes : Will Wait : ",(getProbab('Est','0-10','Y')*PAnsYes/PEstFew)*100,"%")
	print("No : Will Wait : ",(getProbab('Est','0-10','N')*PAnsNo/PEstFew)*100,"%")
	print("Probability for people will Wait if the EstimatedWait Time is 10-30 mins: ")
	print("Yes: Will Wait : ",(getProbab('Est','10-30','Y')*PAnsYes/PEstMore)*100,"%")
	print("No: Will Wait: ",(getProbab('Est','10-30','N')*PAnsNo/PEstMore)*100,"%")
	print("Probability for people will Wait if the EstimatedWait Time is 30-60 mins: ")
	print("Yes: Will Wait : ",(getProbab('Est','30-60','Y')*PAnsYes/PEstStillMore)*100,"%")
	print("No: Will Wait : ",(getProbab('Est','30-60','N')*PAnsNo/PEstStillMore)*100,"%")
	print("Probability for people will Wait if the EstimatedWait Time is >60 mins: ")
	print("Yes: Will Wait: ",(getProbab('Est','>60','Y')*PAnsYes/PEstTooMuch)*100,"%")
	print("No: Will Wait: ",(getProbab('Est','>60','N')*PAnsNo/PEstTooMuch)*100,"%")
	print("Probability for people will Wait if there are somePatrons: ")
	print("Yes: Will Wait: ",(getProbab('Pat','S','Y')*PAnsYes/PPatSome)*100,"%")
	print("No: Will Wait: ",(getProbab('Pat','S','N')*PAnsNo/PPatSome)*100,"%")
	print("Probability for people will Wait if there are NonePatrons: ")
	print("Yes: Will Wait: ",(getProbab('Pat','N','Y')*PAnsYes/PPatNone)*100,"%")
	print("No: Will Wait: ",(getProbab('Pat','N','N')*PAnsNo/PPatNone)*100,"%")
	print("Probability for people will Wait if there are FullPatrons: ")
	print("Yes: Will Wait: ",(getProbab('Pat','F','Y')*PAnsYes/PPatFull)*100,"%")
	print("No: Will Wait: ",(getProbab('Pat','F','N')*PAnsNo/PPatFull)*100,"%")
	print("Probability for people will Wait if food is Thai: ")
	print("Yes: Will Wait: ",(getProbab('Type','T','Y')*PAnsYes/PTypeThai)*100,"%")
	print("No: Will Wait: ",(getProbab('Type','T','N')*PAnsNo/PTypeThai)*100,"%")
main()

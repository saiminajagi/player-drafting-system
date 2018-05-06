t1=[["Sam Billings","KL Rahul","Parthiv Patel","De Kock","B McCullum","W Saha","J Butler","H Klaasen","R Uthappa","D Kartik","A Tare","Ishan Kishan","MS Dhoni","N Jagadeesan","Rishabh Pant","Naman Ojha"],
["P Negi","Bipul Sharma","D Hooda","S Gopal","K Gowtham","S Binny","S Gill","N Rana","K Pandya","Rahul Tewatia","Vijay Shankar","Gurkeerat Singh","M Kalra","I Jaggi","M Lormor","A Singh"],
["M Ashwin","K Kejrolia","Sandeep Sharma","B Thampi","S Kaul","Sran","J Unadkat","D Kulkarni","K Nagarkoti","S Mavi","V Kumar","M Markande","P Sangwan","R Chahar","KM Asif","Harshal Patel","Avesh Khan","Shahbaz Nadeem"],
["T Southee","B Stanlake","C Jordan","M Nabi","Rashid Khan","A Tye","Mujeeb Z","B Laughlin","J Archer","M Johnson","T Curran","M Mcleanaghan","Pat Cummins","M Rahman","Imran Tahir","Santner","Mark Wood","Kagiso Rabada","Trent Boult"],
["M Ali","C Grandhomme","C Woakes","C Brathwaite","Shakib Al Hasan","M Stoinis","Ben Stokes","S Narine","A Russell","JP Duminy","B Cutting","K Pollard","Dwayne Bravo","Shane Watson","Chris Morris","Glenn Maxwell","Dan Christian"]]
N=8

import random
from functools import partial
for i in range(5):
	P=len(t1[i])
	for j in range(len(t1[i])):		
		#print("1")
		m=partial(random.sample,range(N),N)
		player=[m() for i in range(P)]
		m=partial(random.sample,range(P),P)
		pref_team=[m() for i in range(N)]
		team=[0,1,2,3,4,5,6,7]
		teamFree=[False for i in range(N)]
		playerList=[-1 for i in range(P)]
		def teamCount(a):
			count=0
			for i in range(P):
				if playerList[i]==a:
					count+=1
			return count
		def preference(a,b,c):
			if player[a][b]<player[a][c]:
				return True 
			else:
				return False
		while (len(team)!=0):
			q=team.pop(0)
			team.insert(0,q)
			for j in range(P):
				z=pref_team[q][j]
				if playerList[z]==-1:
					playerList[z]=q
					if teamCount(q)==2:
						team.pop(0)
						teamFree[q]=True
						break

		team_List=["DD","RCB","KXIP","CSK","KKR","MI","RR","SRH"]
	for x in range(P):
		#if playerList[x]==0 :
		#	print(t1[i][x])
		if playerList[x]==-1:
			print(t1[i][x],"-","None")	
		else:
			print(t1[i][x],"-",team_List[playerList[x]])
	print("\n")
t=[["V Kohli","M Pandey","S Dhawan","K Nair","S Samson","A Rahane","Rohit Sharma","Suresh Raina","Kedar Jadhav","Ambati Rayudu","Shreyas Iyer","Gautam Gambhir"],
["M Siraj","U Yadav","Y Chahal","B Kumar","M Sharma","K Yadav","P Chawla","Jasprit Bumrah","Harbhajan Singh","Shardul Thakur","Deepak Chahar","Mohamed Shami","Amit Mishra"],
["Anirudha Joshi","Pavan DP","W Sundar","Y Pathan","Yuvraj Singh","R Ashwin","Axar Patel","Hardik Pandya","Ravindra Jadeja","Karn Sharma","Jayant Yadav"],
["Mandeep Singh","M Vohra","Sarfaraz K","S Baby","M Tiwary","M Agarwal","R Tripathi","S Lad","S Tiwary","S Yadav","Kshitiz Sharma","Prithvi Shaw"],
["C Anderson","De Villiers","K Williamson","A Hales","A Finch","D Miller","C Gayle","D Short","C Lynn","E Lewis","Faf du Plessis","Jason Roy","Colin Munro"]]

N=8

import random
from functools import partial
for i in range(5):
	P=len(t[i])
	for j in range(len(t[i])):
		m=partial(random.sample,range(N),N)
		player=[m() for i in range(P)]
		m=partial(random.sample,range(P),P)
		pref_team=[m() for i in range(N)]
		team=[0,1,2,3,4,5,6,7]
		teamFree=[False for i in range(N)]
		playerList=[-1 for i in range(P)]
		def preference(a,b,c):
			if player[a][b]<player[a][c]:
				return False 
			else:
				return True
		while (len(team)!=0):
			q=team.pop(0)
			for j in range(P):
				z=pref_team[q][j]
				if playerList[z]==-1:
					teamFree[q]=True
					playerList[z]=q
					break
				else:
					y=playerList[z]
					if preference(z,q,y)==True:
						team.append(y)
						teamFree[y]=False
						playerList[z]=q
						teamFree[q]=True
						break
		team_List=["DD","RCB","KXIP","CSK","KKR","MI","RR","SRH"]
	for x in range(P):		
		#if playerList[x]==1:
		#	print(t[i][x])
		if playerList[x]==-1:
			print(t[i][x],"-","None")	
		else:
			print(t[i][x],"-",team_List[playerList[x]])
	print("\n")
		
	#print(pref_team)	
	#print(player)

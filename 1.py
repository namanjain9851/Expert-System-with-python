from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from experta import *
from facts import fact

gui = Tk()
gui.title("JEE college predictor")
gui.config(bg = 'pink')
gui.geometry('800x800')

l1 = Label(gui,text = 'JEE Mains college predictor',font  = ("bold",16))
l1.place(x = 200, y = 50)
cate = [
    "OPEN",
    "OPEN (PwD)",
    "OBC-NCL",
    "OBC-NCL (PwD)",
    "SC",
    "SC (PwD)",
    "ST",
    "ST (Pwd)"
]
states = [
"Andhra Pradesh",
"Arunachal Pradesh",
"Assam",
"Bihar",
"Chhattisgarh",
"Delhi",
"Goa",
"Gujarat",
"Haryana",
"Himachal Pradesh",
"Jammu and Kashmir",
"Jharkhand",
"Karnataka",
"Kerala",
"Madhya Pradesh",
"Maharashtra",
"Manipur",
"Meghalaya",
"Mizoram",
"Nagaland",
"Odisha",
"Puducherry",
"Punjab",
"Rajasthan",
"Sikkim",
"Tamil Nadu",
"Telangana",
"Tripura",
"Uttar Pradesh",
"Uttarakhand",
"West Bengal"
]
a = StringVar()
b = StringVar()
c = StringVar()

ans =[]



class student:
	JEE_rank=0
	state=0
	student_category=0
	def __init__(self,JEE_rank,state,student_category):
		self.JEE_rank=JEE_rank
		self.state=state
		self.student_category=student_category
ff = "Institute$Degree$Quota$OS$category$OR$CR"
ft="Institute$State$NIRF Ranking$India Today$Outlook India Ranking$Placement Statistics $Research Statistics$Alumni Statistics"
class Ranks:
	Institute=""
	State=""
	NIRF=""
	India_today=""
	Outlook_India=""
	Placement=""
	Research=""
	Alumni=""
	def __init__(self,Institute,State,NIRF,India_today,Outlook_India,Placement,Research,Alumni):
		self.Institute=Institute
		self.State=State
		self.NIRF=NIRF
		self.India_today=India_today
		self.Outlook_India=Outlook_India
		self.Placement=Placement
		self.Research=Research
		self.Alumni=Alumni
	def withname(self):
		return self.Institute+'\t'+'$'+self.State+'\t'+'$'+self.NIRF+'\t'+'$'+self.India_today+'\t'+'$'+self.Outlook_India+'\t'+'$'+self.Placement+'\t'+'$'+self.Research+'\t'+'$'+self.Alumni
def Input():
    print(a)
    print(b)
    print(c)
    rank=int(b)
    if(rank<=0):
        print("you entered wrong rank")
    cat=str(a)		
    state=str(c)
    return student(rank,state,cat)
	
def extract_data(file,college_names):
	reader=open(file)
	input_file=csv.DictReader(reader,college_names)
	#data={}
	data = defaultdict(list)
	#for k in college_names:
	#	data[k]=[]
	flag=0
	for row in input_file:
		if(flag==0):
			flag=1
			continue;
		for k in college_names:
				data[k].append(row[k])
	reader.close()
	return data


def filter_data(data):
	print(0.5*float(data[2]['Opening Rank'][1]))
	filtered_data1=[(0.5*float(data[2]['Opening Rank'][i])+0.3*float(data[1]['Opening Rank'][i])+0.2*float(data[0]['Opening Rank'][i])) for i in range(len(data[1]['Opening Rank']))]
	filtered_data2=[(0.5*float(data[2]['Closing Rank'][i])+0.3*float(data[1]['Closing Rank'][i])+0.2*float(data[0]['Closing Rank'][i])) for i in range(len(data[1]['Closing Rank']))]

	opening_filtered_data=[int(i) for i in filtered_data1]
	closing_filtered_data=[int(i) for i in filtered_data2]
	final_data=data[0]
	final_data['Opening Rank']=opening_filtered_data
	final_data['closing_rank']=closing_filtered_data
	return final_data


def suitable_college(user,process_data):
	ranking_data=extract_data("ranking.csv",["Ranking","Institute","State"])
	size=len(ranking_data['Ranking'])
	data={}
	k=0
	for (i,j) in process_data.items():
		#print(i,j.withname())
		#print(j.closing_rank,user.JEE_rank,j.Seat_Type,user.student_category)
		flag=0
		if(int(j.closing_rank)>=int(user.JEE_rank) and j.Seat_Type==user.student_category):
			for it in range(size):
				if(j.name==ranking_data['Institute'][it] and ranking_data['State'][it]==user.state):
					flag=1
					if(j.Quota=="HS"):
						data[k]=j
						#print("hello",data[k].withname())		
						k=k+1
						
						break
			if(flag==0):
				if(j.Quota=="OS"):
					data[k]=j
					k=k+1	
	return data

"""def preprocess(final_data):
	size=len(final_data['Institute'])
	ranking_data=extract_data("ranking.csv",["Ranking","Institute","State"])
	size_r=len(ranking_data['Ranking'])
	branch_data=extract_data("branch_ranking.csv",["Program","Priority"])
	size_a=len(branch_data['Program'])
	data={}
	j=0
	for i in range(size):
		name=final_data['Institute'][i]
		program=final_data['Academic Program Name'][i]
		Quota=final_data['Quota'][i]
		Seat_Type=final_data['Seat Type'][i]
		opening_rank=int(final_data['Opening Rank'][i])
		closing_rank=int(final_data['closing_rank'][i])
		rank=100
		for r in range(size_r):
			if(name==ranking_data['Institute'][r]):
				rank=int(ranking_data['Ranking'][r])
		branch_p=100
		for r in range(size_a):
			if(program==branch_data['Program'][r]):
				branch_p=int(branch_data['Priority'][r])
		data[j]=college(name,program,Quota,Seat_Type,opening_rank,closing_rank,rank,branch_p)
		#print('fact['+str(j)+']='+'college('+ '\'' +name+ '\''','+'\''+program+'\''+','+ '\''+Quota+ '\''+','+ '\''+Seat_Type+ '\''+','+ '\''+str(opening_rank)+ '\''+','+ '\''+str(closing_rank)+ '\''+','+ '\''+str(rank)+ '\''+','+ '\''+str(branch_p)+ '\''+')')
		#print(data[j].withname())
		j=j+1
		data=fact
	return data
"""
def gettopN(list1,n):
	if(len(list1)==0):
		print("no college is found")
	elif(len(list1)>=n):
		for i in range(n):
			print(list1[i].withname())
	else:
		for i in range(len(list1)):
			print(list1[i].withname())
def sort_college(final_college):
	size=len(final_college)
	list1=[]
	for i in range(size):
		list1.append(final_college[i])
		#print("Hello",list1[i].withname())
	list1.sort(key=lambda x:(int(x.rank)*int(x.opening_rank)*int(x.branch_priority)),reverse=False)
	return list1



class expert_system(KnowledgeEngine):
  
  @Rule(Fact(x=MATCH.y,n=MATCH.n))
  def is_suitable(self,y,n):
  	if(len(y)==0):
  		print("no college is found")
  	elif(len(y)>=n):
  		for i in range(n): 
  			print(y[i].withname())
  			ans.append(y[i].withname())
  	else:
  		for i in range(len(y)):
  			print(y[i].withname())
  			ans.append(y[i].withname())  
def main():
	print(a + " " + b + " " + c)
	n=3
	j=2016
	data={}
	for i in range(n):
		print("loading data of year "+str(j))
		data[i]=extract_data(str(j)+'.csv',['Institute','Academic Program Name','Quota','Seat Type','Opening Rank','Closing Rank'])
		#print(data[i])
		#data[i]=str(j)+'.csv)
		j=j+1 
	#list1 = [0.5*float(i) for i in data[2]['Opening Rank']]
	final_data=filter_data(data)
	#print(final_data)
	user=Input()
	#processed_data=preprocess(final_data)
	processed_data=fact
	final_college=suitable_college(user,processed_data)
	result=sort_college(final_college)


	engine=expert_system()
	engine.reset()
	engine.declare(Fact(x=result,n=20))
	engine.run()

	#print(ab)

def submit():
	global a,b,c
	a = (V1.get())
	b = (e1.get())
	c = (ss.get())
	ans.append(ff)
	main()
	asd = Tk()
	asd.title("Suggested Colleges")
	h = 20	
	w=6
	p = "asdfffffffffffffffffff"
	asd.geometry('1650x530')    
	asd.bind("<Escape>",lambda q:asd.destroy())
	for i in range(h):
		x = ans[i].split('$')
		for j in range(w):
			c = Label(asd , text = x[j])
			c.grid(row = i,column = j)
	Button(gui, text='Exit', command=gui.destroy()).pack()
	mainloop()

	
def submit2():
	final_data=extract_data("ranking2.csv",["Institute","State","NIRF Ranking","India Today","Outlook India Ranking","Placement Statistics","Research Statistics","Alumni Statistics"])
	size=len(final_data['Institute'])
	ans2=[]
	ans2.append(ft)
	j=0
	data={}
	for i in range(size):
		Institute=final_data['Institute'][i]
		State=final_data['State'][i]
		NIRF=final_data['NIRF Ranking'][i]
		India_today=final_data['India Today'][i]
		Outlook_today=final_data['Outlook India Ranking'][i]
		Placement=final_data['Placement Statistics'][i]
		Research=final_data['Research Statistics'][i]
		Alumni=final_data['Alumni Statistics'][i]
		data[j]=Ranks(Institute,State,NIRF,India_today,Outlook_today,Placement,Research,Alumni)
		ans2.append(data[j].withname())
		print(data[j].withname())
		j=j+1
	

	asd = Tk()
	asd.title("Statistics")
	h = 32	
	w=8
	d={}
	p = "asdfffffffffffffffffff"
	asd.geometry('1650x830')    
	asd.bind("<Escape>",lambda q:asd.destroy())
	for i in range(h):
		x = ans2[i].split('$')
		for j in range(w):
			if j==0:
				d[i+j] = Label(asd , text = x[j])
				d[i+j].grid(row = i,column = j)
			else:
				d[i+j] = Label(asd , text = x[j])
				d[i+j].grid(row = i,column = j)

	Button(gui, text='Exit', command=gui.destroy()).pack()
	mainloop()


gui.bind("<Escape>",lambda q:gui.destroy())
# labels
cat = Label(gui,text = 'Category', font = ("bold",10))
cat.place(x = 200, y = 150)

catRank = Label(gui,text = 'Category Rank', font = ("bold",10))
catRank.place(x = 200, y = 200)

Hstate = Label(gui, text = 'Home state', font = ("bold",10))
Hstate.place(x = 200,y = 250)
# entry options and drop down menu

# 1
V1 = StringVar(gui)
V1.set(cate[0])
cc = OptionMenu(gui,V1,*cate)
cc.place(x = 500, y = 150)
# 2
e1 = Entry(gui)
e1.place(x = 500,y = 200)
# 3
V2 = StringVar(gui)
V2.set(states[0])
ss = ttk.Combobox(gui,values = states, state = "readonly", height = 8)
# ss.set(states[0])
ss.place(x = 500, y = 250)




# button

b1 = Button(gui,text = "submit", font = ("bold",14),command = submit)
b1.place(x = 350, y = 350)

b2 = Button(gui,text = "College Statistics", font = ("bold",14),command = submit2)
b2.place(x = 294, y = 450)
gui.mainloop()

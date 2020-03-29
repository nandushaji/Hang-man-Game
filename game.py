import random
from words import word_list
word = random.choice(word_list)
#word='nandu'
word.upper()
no_ch=6
d={}
dis=["_"]*len(word)
def complete():
	for i in dis:
		if(i=='_'):
			return 1
	return 0
def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def display(index,letter):
	flag=0
	
	if(len(letter)==1 and dis[index]=='_'):
		dis[index]=letter.upper()
		global no_ch
	
		
	elif(len(letter)==len(word)):
		for i in range(len(word)):
			if(word[i].upper()!=letter[i].upper()):
				flag=1
				break

		if(flag==0):
			for i in range(len(word)):
				dis[i]=word[i].upper()

			
		else:
			pass
			
	else:
		print("Inavlid Move")		
def game():
	l=[]
	print("                               *Welcome to  Hang-man*")
	print("                     *Rules:Guess Either a Letter or the Word*")
	print("                            *Hope you will enjoy the game*")
	global no_ch
	while(no_ch>0):
		count=0
		print(dis)
		f=complete()
		if(f==0):
			print("Congrats your guess is right")
			break
		print(no_ch,":Chances left")
		inp=input().upper()
		if(len(inp)>1):
			display(0,inp)
		else:
			for i in range(len(word)):
				if(inp.upper()==word[i].upper()):
					if(dis[i]!='_'):
						continue
					display(i,inp)
					count=1
					break
			if(count==0):
				print(display_hangman(no_ch))
				no_ch-=1
	else:
		print("Sorry the word was:",word.upper())
		
game()
y=input("Do you want to continue[Y/N]:").upper()
while(y=='Y'):
	word = random.choice(word_list)
	word.upper()
	no_ch=6
	dis=["_"]*len(word)
	game()
	y=input("Do you want to continue[Y/N]:").upper()


				
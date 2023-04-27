#gmae khelne wala funtion
def game(answer, guessword):
        feedback = []
        for i,letter in enumerate(guessword):
            if letter not in answer:
                feedback.append(0)
            else:
                if letter == answer[i]:
                    feedback.append(2)
                else:
                    feedback.append(1)
        
    
        return feedback

master_list=['happy','smile','arise','arose','lizht','ariae','wzazr']
alphabet="abcdefghigklmnopqrstuvwxyz"
frq={}
result=game("games","salet")

#list ko short karne wala funtion
def sortinglist(master_list,guess,result):
    n=0
    for i in range(5):
        for word in master_list:
            if result[i]==0:
                if guess[i] in word[i]:
                    master_list.remove(word)                                    
            elif result[i]==1:
               if guess[i] != word[i]:
                    master_list.remove(word)                                                   
            elif result[i]==2:
               if guess[i] not in word:
                    master_list.remove(word)

    n+=1                
    return master_list

# letters frequeny batane wala funtion 
def frequency(alphabet,master_list):
    
    for j in alphabet:
        x=0
        for word in master_list:
            for i in range(5):
                if word[i]==j:
                    x+=1
        frq.update({j: x })    
    return 0 
#guess karne wala 
def guesser(n):
    if n==0:
        guess="salet"
    else:
       guess= mainguesser()
    
    return guess

#second guess kya karna he ye batane wala
def mainguesser():
    




frequency(alphabet,master_list)
#print(frq)

sortinglist(master_list,"salet",result)
print(master_list)
print (result)

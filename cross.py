class Main():

    with open ("dictionary.txt") as f:
        words = f.readlines()

    def checkFor(listt,x,y,words,ans):
        word=""
        for i in range(y,len(listt[x])):
            word+=listt[x][i]
            for j in words:
                if word==j.lower().strip():
                    ans.append(word)
                    break
        
    def checkBack(listt,x,y,words,ans):
        word=""
        for i in range(len(listt[x])-1,y-1,-1):
            word+=listt[x][i]
            for j in words:
                if word==j.lower().strip():
                    ans.append(word)
                    break
    def checkUp(listt,x,y,words,ans):
        word=""
        for i in range(len(listt)-1,x-1,-1):
            word+=listt[i][y]
            for j in words:
                if word==j.lower().strip():
                    ans.append(word)
                    break
    def checkDown(listt,x,y,words,ans):
        word=""
        for i in range(x,len(listt)):
            word+=listt[i][y]
            for j in words:
                if word==j.lower().strip():
                    ans.append(word)
                    break

    def checkDidownright(listt,x,y,words,ans):
        word=""
        row=x
        col=y
        while(row!=len(listt) and col!=len(listt[x])):
            word+=listt[row][col]
            row+=1
            col+=1
            for i in words:
                if word==i.lower().strip():
                    ans.append(word)
                    break

    def checkDiupleft(listt,x,y,words,ans):
        word=""
        row=x
        col=y
        while(row!=-1 and col!=-1):
            word+=listt[row][col]
            row-=1
            col-=1
            for i in words:
                if word==i.lower().strip():
                    ans.append(word)
                    break
    def checkDidownleft(listt,x,y,words,ans):
        word=""
        row=x
        col=y
        while(row!=len(listt) and col!=-1):
            word+=listt[row][col]
            row+=1
            col-=1
            for i in words:
                if word==i.lower().strip():
                    ans.append(word)
                    break
    def checkDiupright(listt,x,y,words,ans):
        word=""
        row=x
        col=y
        while(row!=-1 and col!=len(listt[0])):
            word+=listt[row][col]
            row-=1
            col+=1
            for i in words:
                if word==i.lower().strip():
                    ans.append(word)
                    break
    cases=input("How many word searches? ")
    for i in range(int(cases)):
        ans=[]
        crossword=[]
        r,c = input("Enter r and c: ").split()
        for i in range(int(r)):
            row=""
            row=input("enter row ")
            assert(len(row)==int(c))
            crossword.append(row)
        print(crossword)
        for i in range(len(crossword)):
            for j in range(int(c)):
                checkFor(crossword,i,j,words,ans)
                checkBack(crossword,i,j,words,ans)
                checkUp(crossword,i,j,words,ans)
                checkDown(crossword,i,j,words,ans)
                checkDiupleft(crossword,i,j,words,ans)
                checkDidownright(crossword,i,j,words,ans)
                checkDiupright(crossword,i,j,words,ans)
                checkDidownleft(crossword,i,j,words,ans)

    print(ans)

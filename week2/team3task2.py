
def sort(srt) :
    temp =0
    c = 0
    for index in srt :
        if srt[index] > srt[index+1] and c==3 :
            temp = srt[index]
            srt[index] = srt[index +1]
            srt[index + 1] = temp
            c = c+1
                
        
    print(srt)
    
lst=[1,53,34,34]  
sort(lst)

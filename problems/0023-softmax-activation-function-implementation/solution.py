import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    sum=0
    maxVal=0
    for num in scores:
        maxVal=max(maxVal,num)
    for num in scores:
        sum=sum+(math.e**(num-maxVal))
    answer=[]
    for num in scores:
        answer.append((math.e**(num-maxVal))/sum)
    return answer
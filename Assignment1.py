import numpy as np
import logging

class SumOfElements:
    
    def __init__(self):
        pass

    def subArray(self,arr, m):
        flag=-1
        result=[]
        for i in range(0, len(arr)):
            if(isinstance(arr[i], int)):
                continue
            else:
                raise ValueError("Array elements should be only integers")
        if(len(arr)==0):
            raise Exception("Array should not be empty")
        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if(arr[i]+arr[j]==m):
                    result.append([arr[i], arr[j]])
                    flag=1
                for k in range(j+1, len(arr)):
                    if(arr[i]+arr[j]+arr[k]==m):
                        result.append([arr[i], arr[j], arr[k]])
                        flag=1
        return result, flag
    
logging.basicConfig(level=logging.DEBUG)                        
arr=[1,2,1,2]
logging.debug(arr)
m=int(input("Enter the sum\n"))
arrayElements=SumOfElements()
result, flag=arrayElements.subArray(arr, m)

for i in range(0, len(result)):
    logging.debug(result[i])
    


    

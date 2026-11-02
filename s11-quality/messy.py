import os
import json
def total(prices:list[float])->float:
    result=0.0
    for p in prices :
        result+=p
    return result
print( total([4.50,3.25 ,1.99]) )

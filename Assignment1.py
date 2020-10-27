

def counts(*args):
    freq= {}
    for item in args:
        if (item in freq):
            freq [item] += 1
        else:
            freq [item] = 1

    for key, value in freq.items():
        print (key, ":" ,value)
        


counts(1,2,1,2,1,2,1,2,'a','a','e','e','f','f','iou','iou')                   

    
    
        
    
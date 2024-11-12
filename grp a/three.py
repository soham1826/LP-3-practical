class Item:  
    def __init__(self, value, weight):  
        self.value = value  
        self.weight = weight  

def fractionalKnapsack(W, arr): 
    # Sort items by value-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)  
    
    # Result (value in Knapsack)
    finalvalue = 0.0  
    
    # Looping through all items
    for item in arr:  
        # If adding item won't exceed the capacity, add it completely
        if item.weight <= W:  
            W -= item.weight  
            finalvalue += item.value  
        # If we can't add the current item, add fractional part of it
        else:  
            finalvalue += item.value * W / item.weight  
            break  
    
    # Returning final value
    return finalvalue 

# Driver Code
if __name__ == "__main__":  
    W = 50  # Knapsack capacity
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]  # Items: value, weight
    
    # Function call
    max_val = fractionalKnapsack(W, arr)  
    print(max_val)

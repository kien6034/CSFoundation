#SORT STACK
"""
    Write a program to sort stack such that the smallest items are on the top. You can use an additional temporary stack,
    but you may not copy the elements into another data structure (array for exp). The stack supports the following 
    operations: push, pop, peeks and isEmpty 

    #hints: 
        - One way of sorting an array is to iterate through the array and insert each element into a new array in sorted order 
        - imagine your secondary stack is sorted. Can you insert elemnents into it in sorted order. You might need some extra storage 
        - keep the secondary stack in sorted order, with the biggest elements on the top. Use the primary stack for additional storage
"""
import sys


def sum_in_set( arr1_set , n):
    file = open("test.txt","r") 
    for line in file: 
        print(line)
    data = sys.stdin.readlines()
    print("Counted", len(data), "lines.")
    print(arr1_set)


# sum_in_set([2,3,5,6], 5)

def minsweeper():
    sweep_array = []
    file = open("test.txt","r")
    for line in file:
        temp_array = []
        for val in line.split():
            temp_array.append(val)
        sweep_array.append(temp_array)
    
    print(sweep_array)

    explored_array = []

    for i in range(0, len(sweep_array)):
        temp_array=[]
        for j in range(0, len(sweep_array)):
            temp_array.append("#")
        explored_array.append(temp_array)
    

    (status, array_after_game) = play_game( sweep_array, explored_array,"undecided")
    print("\n \n \n")
    for list1 in array_after_game:
            str1 = ""
            for vals in list1:
                str1 += str(vals)+" "
            print(str1)

    print("\nYou ",status," the game")

def play_game( minesweeper_array, explored_array, status):

    while( status=="undecided"):
       
        
        for list1 in explored_array:
            str1 = ""
            for vals in list1:
                str1 += str(vals)+" "
            print(str1)
        user_val = input("Enter position to play   ")
        user_arr = user_val.split()
        row_val =int(user_arr[0])-1
        col_val =int(user_arr[1])-1

        if row_val<0 or row_val>=len(minesweeper_array):
            print("Enter appropriate row value")
            continue
        
        if col_val<0 or col_val>=len(minesweeper_array):
            print("Enter appropriate column value")
            continue
        
        if explored_array[row_val][col_val] != "#":
            print("Enter undiscovered location")
            continue

        
        if minesweeper_array[row_val][col_val]=="1":
            explored_array[row_val][col_val] ="X"
            status="lost"
        else:
            
            hash_count = 0
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val , col_val)         
          
            for list1 in explored_array:
                for vals in list1:
                    if vals =="#":
                        hash_count+=1
            
            if hash_count == 10:
                status = "won"
            
            
            print("not a mine")


    return (status,explored_array)


def is_adjacent_not_mine( minesweeper_array, explored_array ,  row_val , col_val):
    mine_count = 0
    if col_val-1>=0:        
        if int(minesweeper_array[row_val][col_val-1])==1:            
            mine_count+=1            
    
    if col_val-1>=0 and row_val-1>=0:
        if int(minesweeper_array[row_val-1][col_val-1])==1:            
            mine_count+=1

    if row_val-1>=0:
        if int(minesweeper_array[row_val-1][col_val])==1:            
            mine_count+=1

    if col_val+1<len(minesweeper_array) and row_val-1>=0:
        if int(minesweeper_array[row_val-1][col_val+1])==1:            
            mine_count+=1

    if col_val+1<len(minesweeper_array):
        if int(minesweeper_array[row_val][col_val+1])==1:           
            mine_count+=1

    if col_val+1<len(minesweeper_array) and row_val+1<len(minesweeper_array):
        if int(minesweeper_array[row_val+1][col_val+1])==1:            
            mine_count+=1

    if row_val+1<len(minesweeper_array):
        if int(minesweeper_array[row_val+1][col_val])==1:            
            mine_count+=1

    if col_val-1 >= 0 and row_val+1<len(minesweeper_array):
        if int(minesweeper_array[row_val+1][col_val-1])==1:            
            mine_count+=1

    
    
    if mine_count == 0:
        explored_array[row_val][col_val]= " "

        if col_val-1>=0 and explored_array[row_val][col_val-1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val , col_val-1)            
        
        if col_val-1>=0 and row_val-1>=0 and explored_array[row_val-1][col_val-1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val-1 , col_val-1)            

        if row_val-1>=0 and explored_array[row_val-1][col_val]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val-1 , col_val)            

        if col_val+1<len(minesweeper_array) and row_val-1>=0 and explored_array[row_val-1][col_val+1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val-1 , col_val+1)            

        if col_val+1<len(minesweeper_array) and explored_array[row_val][col_val+1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val , col_val+1)           

        if col_val+1<len(minesweeper_array) and row_val+1<len(minesweeper_array) and explored_array[row_val+1][col_val+1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val+1 , col_val+1)

        if row_val+1<len(minesweeper_array) and explored_array[row_val+1][col_val]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val+1 , col_val)            

        if col_val-1 >= 0 and row_val+1<len(minesweeper_array) and explored_array[row_val+1][col_val-1]=="#":
            explored_array = is_adjacent_not_mine( minesweeper_array , explored_array , row_val+1 , col_val-1)
                    

    
    else:
        print("mine count is ",mine_count)
        explored_array[row_val][col_val] = mine_count
    
    
    return explored_array



minsweeper()
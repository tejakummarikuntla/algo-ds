def timeConversion(tw_time):
    tw_lst = tw_time.split(':')
    if tw_lst[-1][2:] == 'PM':
        if tw_lst[0] == '12':
            print("12:{t}".format(t=tw_time[3:8]))
        else:
            point = 12
            tw_hour = int(tw_lst[0])
            print(str(point+tw_hour)+"{t}".format(t=str(tw_time[2:8])))

    if tw_lst[-1][2:] == 'AM':
        if tw_lst[0] == '12':
            print("00:{t}".format(t=tw_time[3:8]))
        else:
            print(tw_time[:8])

if __name__ == '__main__':
    input_time = input()
    timeConversion(input_time)

    
    #################################################################
    
    
# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM")) 

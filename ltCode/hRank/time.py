tw_time = "12:05:45AM"
tw_lst = tw_time.split(':')
if tw_lst[-1][2:] == 'PM':
    point = 12
    tw_hour = int(tw_lst[0])
    print(point+tw_hour)
    
if tw_lst[-1][2:] == 'AM':
    if tw_lst[0] == '12':
        print("00:{t}".format(t=tw_time[3:8]))
    else:
        print(tw_time[:8])

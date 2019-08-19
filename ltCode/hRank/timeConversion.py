def timeConversion(tw_time):
    tw_lst = tw_time.split(':')
    if tw_lst[-1][2:] == 'PM':
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

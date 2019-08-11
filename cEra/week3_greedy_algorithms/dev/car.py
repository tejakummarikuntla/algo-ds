def stations(arr, n, L):
    stationCount = 0
    start = 0

    for i in range(n+1):
        if ( L - (arr[i]-start) < 0):
            G = arr[i-1]
            start = G
            stationCount = stationCount + 1
    return stationCount

if __name__ == '__main__':
    station_arr = [int(x) for x in input().split()]
    nof_stations = int(input())
    car_max_travel = int(input())

    print(stations(station_arr, nof_stations, car_max_travel))

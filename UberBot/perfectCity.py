import math
def perfectCity(departure, destination):
    if departure[0] == destination[0]:
        return abs(departure[1]-destination[1])
    elif departure[1] == destination[1]:
        return abs(departure[0]-destination[0])    
    if departure[0]!=int(departure[0]) or destination[0]!=int(destination[0]):
        print("X")
        total_ceil = 0
        x_pos_right = math.ceil(departure[0])
        total_ceil+=abs(x_pos_right-departure[0])
        total_ceil+=abs(x_pos_right-destination[0])
    
        total_floor = 0
        x_pos_left = math.floor(departure[0])
        total_floor+=abs(x_pos_left-departure[0])
        total_floor+=abs(x_pos_left-destination[0])
    
        x = min(total_ceil,total_floor)
        return x+abs(departure[1]-destination[1])
    else:
        print("Y")
        total_ceil = 0
        y_pos_right = math.ceil(departure[1])
        total_ceil+=abs(y_pos_right-departure[1])
        total_ceil+=abs(y_pos_right-destination[1])
    
        total_floor = 0
        y_pos_left = math.floor(departure[1])
        total_floor+=abs(y_pos_left-departure[1])
        total_floor+=abs(y_pos_left-destination[1])
    
        y = min(total_ceil,total_floor)
        return y+abs(departure[0]-destination[0])    
# Creating the variables
distance_mi = 5
is_raining =True
has_bike =True
has_car = False
has_ride_share_app = False
#Now the conditions
if not distance_mi:
    print(False)
elif distance_mi <=1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <=6:
    if not is_raining and has_bike:
        print(True)
    else:
        print(False)
elif distance_mi >6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
        


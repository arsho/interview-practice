def deliveryFee(intervals, fees, deliveries):
    my_intervals = []
    for i in range(1,len(intervals)):
        x= (intervals[i]*60)-1
        my_intervals.append(x)
    my_intervals.append((24*60)-1)
    ar = [0 for i in range(len(fees))]
    for i in deliveries:
        x = (i[0]*60) + i[1]
        for j in range(len(my_intervals)):
            if x<=my_intervals[j]:
                ar[j]+=1
                break
    final_ar = [0 for i in range(len(fees))]
    for i in range(len(fees)):
        if ar[i]==0:
            final_ar[i] = 0
        else:
            final_ar[i] = fees[i]/ar[i]
    return len(set(final_ar))==1
                
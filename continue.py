i = 0
while i<=5:
    if(i == 3):
        i+= 1
        continue # when if condition will become true, steps after
                #continue will be skipped and iteration will start again.
    print(i)
    i += 1 
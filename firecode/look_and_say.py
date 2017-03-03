def look_and_say(sequence_number):
    if sequence_number == None or sequence_number == 0:
        return None
    if sequence_number == 1:
        return 1
    if sequence_number == 2:
        return 11
    n = 3
    x = 11
    while n <= sequence_number:
        x_str = str(x)
        r_list = []
        i = 0
        
        while i < len(x_str):
            count = 1
            while i < len(x_str)-1 and x_str[i+1] == x_str[i]:
                count += 1
                i += 1

            r_list.append(str(count))
            r_list.append(x_str[i])
            i += 1
        
        x = int(''.join(r_list))

        n += 1
        
    return x

print(look_and_say(1))
print(look_and_say(3))
print(look_and_say(5))
print(look_and_say(7))

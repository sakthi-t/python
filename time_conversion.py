def timeConversion(s):
    # Write your code here
    """ splitting the string to text 
    separating AM and PM
    If it is 12:00:00AM change the 12 to '00'
    If it is 12:00:00PM keep the 12. But for anytime between 1 PM to 11 PM add 12 
    """
    text = s.split(':')
    
    if 'PM' in text[2]:
        text[2] = text[2][0:2]
        
        if int(text[0]) < 12:
            text[0] = int(text[0]) + 12
            text[0] = str(text[0])
        
        text[1] = str(text[1])
        text[2] = str(text[2])
        
    elif 'AM' in text[2]:
        text[2] = text[2][0:2]
        # print(text[0])
        
        if int(text[0]) == 12:
            # print('yes')
            text[0] = '00'
            # print(text[0])
        text[1] = str(text[1])
        text[2] = str(text[2])
    
    # print(text)    
    str1 = ':'
    
    return str1.join(text) 


print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))
print(timeConversion('07:05:45AM'))
print(timeConversion('07:05:45PM'))

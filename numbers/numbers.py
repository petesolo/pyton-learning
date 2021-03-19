largeNum = None
smallNum = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        value = int(num)
    except:
        print('Invalid input')
        continue
    if largeNum is None and smallNum is None:
        largeNum = value
        smallNum = value
    elif value > largeNum:
        largeNum = value
    elif value < smallNum:
        smallNum = value

print('Maximum is',largeNum)
print('Minimum is',smallNum)

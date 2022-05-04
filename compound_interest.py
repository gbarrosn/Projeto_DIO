import csv

def yn_choice(message, default='y'):
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice = input("%s (%s) " % (message, choices))
    values = ('y', 'yes', '') if choices == 'Y/n' else ('y', 'yes')
    return choice.strip().lower() in values

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def get_int(message, error):
    while True:
        try:
            value = int(input(f"{message}: "))
        except ValueError:
            print(f"{error}")
            continue
        else:
            return value
            break

def get_float(message, error):
    while True:
        try:
            value = float(input(f"{message}: "))
        except ValueError:
            print(f"{error}")
            continue
        else:
            return value
            break

print("Welcome to my Compound interest calculator. \nHere you will be able to calculate your investments and debts.")

value = get_int('First, input the initial value', 'Please insert an integer number, representing the currency you want to calculate')


tax = get_float("Now, insert the interest per period, in decimal, without any signs. (example: 2.5): ", "Please insert the interest per period, in decimal, without any signs. (example: 2.5): ")

periods = get_int('Now enter the number of periods to calculate', "Please insert just the number of periods, no matter if it's months, days, or whatever.")

total = 0
header = ['period', 'account balance', 'interest']

if yn_choice("Do you want to export the data to a csv file? "):
    filename = input("Name of csv file: ")
    file = open(filename + '.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(header)
    
    if yn_choice('Will you invest every month?'): 
        
        if not yn_choice("Will it be the same value every month?"):
            newvalue = value
            for i in range(periods + 1):
                investment = int(input("Month deposit: "))
                newvalue += investment
                interest = (newvalue / 100) * tax
                newvalue = newvalue + investment + (newvalue / 100) * tax

                print(f"period: {i}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
                total += interest
                line = [truncate(i + 1, 2), truncate(newvalue, 2), truncate(interest, 2)]
                writer.writerow(line)
        else:
            investment = int(input("Insert the value: "))
            newvalue = value
            for i in range(periods + 1):
                interest = (newvalue / 100) * tax
                newvalue = newvalue + investment + (newvalue / 100) * tax
                print(f"period: {i}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
                total += interest
                line = [truncate(i + 1, 2), truncate(newvalue, 2), truncate(interest, 2)]
                writer.writerow(line)
    else:
        investment = 0
        newvalue = value
        for i in range(periods):
            interest = (newvalue / 100) * tax
            newvalue = newvalue + investment + (newvalue / 100) * tax
            print(f"period: {i + 1}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
            total += interest
            line = [truncate(i + 1, 2), truncate(newvalue, 2), truncate(interest, 2)]
            writer.writerow(line)
 
    file.close()
    #else do csv
else:

    if yn_choice('Will you invest every month?'):
        if not yn_choice("Will it be the same value every month?"):
            newvalue = value
            for i in range(periods + 1):
                investment = int(input("Month deposit: "))
                newvalue += investment
                interest = (newvalue / 100) * tax
                newvalue = newvalue + investment + (newvalue / 100) * tax
                print(f"period: {i}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
                total += interest
        else:
            investment = int(input("Insert the value: "))
            newvalue = value
            for i in range(periods + 1):
                interest = (newvalue / 100) * tax
                newvalue = newvalue + investment + (newvalue / 100) * tax
                print(f"period: {i}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
                total += interest 
    else:
        investment = 0
        newvalue = value
        for i in range(periods):
            interest = (newvalue / 100) * tax
            newvalue = newvalue + investment + (newvalue / 100) * tax
            print(f"period: {i + 1}, total value: {truncate(newvalue, 2)}, interest: {truncate(interest, 2)}")
            total += interest
            line = [truncate(i + 1, 2), truncate(newvalue, 2), truncate(interest, 2)]

print(f"initial value: {value}  profit: {truncate(total, 2)}")

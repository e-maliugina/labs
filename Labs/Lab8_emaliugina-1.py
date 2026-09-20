upc = str(input("Enter a 12-digit UPC:"))

print(f"The first 11 digits are '{upc[0:11]}'.")
print(f"The provided check digit is {upc[11]}.")
print("Calculating...")

chars = list(upc[0:12])

def find_upc(chars):
    """ Finds the expected check digit for the entered UPC """
    add = int(chars[0]) + int(chars[2]) + int(chars[4]) + int(chars[6]) + int(chars[8]) + int(chars[10])
    product = add * 3
    result = product + int(chars[1]) + int(chars[3]) + int(chars[5]) + int(chars[7]) + int(chars[9])
    m = result % 10
    if m==0:
        check_digit = 0
        return check_digit
    else:
        check_digit = 10 - m
        return check_digit

check_digit = find_upc(chars)

print(f"The expected check digit is {check_digit}.")

if int(upc[11]) == check_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")

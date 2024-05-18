def find_final_price(purchase_amount,discount_percentage):
    discount_in_string = purchase_amount * (discount_percentage/100)
    final_price = purchase_amount - discount_in_string
    

    
    find_final_price = 200,5
    print(final_price)


def LongestWordLength(s):
    words = s.split()
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    return length

s = "I love AkiraChix"
print(f"Longest word's length = {LongestWordLength(s)}")


def LongestWordLength(s):
    words = s.split()
    length = " "
    for word in words:
        if len(word[]) > length:
            length = len(word)
    return length

s = "I love AkiraChix"
print(f"Longest word's length = {LongestWordLength(s)}")
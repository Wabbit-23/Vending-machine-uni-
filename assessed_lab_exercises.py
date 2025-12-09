def add_two_numbers(a, b):
    return a + b

# print(add_two_numbers(3, 5))
# print(add_two_numbers(-5, 5))


def rectangle_area(width, length):
    return width * length

# print(rectangle_area(5, 10))
# print(rectangle_area(0, 10))


def winning_numbers(winning_list,guessed_list):
    matches = 0

    # Checks every number manually without using a loop
    if guessed_list[0] in winning_list:
        matches += 1
    if guessed_list[1] in winning_list:
        matches += 1
    if guessed_list[2] in winning_list:
        matches += 1

    # Returns the output based on numbers input
    if matches == 3:
        return "First"
    elif matches == 2:
        return "Second"
    elif matches == 1:
        return "Third"
    else:
        return "No"
    
# g1 = int(input("1st number:"))
# g2 = int(input("2nd number:"))
# g3 = int(input("3rd number:"))

# guessed_list = [g1, g2, g3]
# winning_list = [5, 17, 14]
# result = winning_numbers(winning_list, guessed_list)
# print(result)


def sum_of_evens(min_num, max_num):
    total = 0

    # Start count from minimum
    current = min_num

    # Loop through numbers untill the maximum
    while current <= max_num:
        # Add number if its even
        if current % 2 == 0:
            total += current
        
        # Carry onto the next number
        current += 1

    return total

# min_num = int(input("Enter minimum number:"))
# max_num = int(input("Enter maximum number:"))

# result = sum_of_evens(min_num, max_num)
# print("Sum of all numbers is: ",result)


def calculate_average(num_list):
    total = 0
    count = 0

    for num in num_list:
        total += num
        count += 1

    average = total //count

    return average

# print(calculate_average([1, 4, 5, 6]))
# print(calculate_average([1, 8, 9]))


def calculate_weekly_pay(hours_worked):
    normal_rate = 12
    overtime_rate = 18 

    if hours_worked <= 35:
        total_pay = hours_worked * normal_rate
    else:
        overtime_hours = hours_worked - 35
        normal_pay = 35 * normal_rate
        overtime_pay = overtime_hours * overtime_rate
        total_pay = normal_pay + overtime_pay
    return total_pay

# print(calculate_weekly_pay(30))
# print(calculate_weekly_pay(36))


def is_prime(num):
    if num == 1:
        return False
    
    divisor = 2 

    while divisor < num: 
        if num % divisor == 0:
            return False
        divisor += 1

    return True

# print(is_prime(21))
# print(is_prime(10))
# print(is_prime(1))
# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(41))


def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return False
    
    for char in word1:
        count1 = 0
        count2 = 0

        for c in word1:
            if c == char:
                count1 =+ 1
            
        for c in word2:
            if c == char:
                count2 =+ 1

        if count1 != count2:
            return False
    return True

# print(are_anagrams("HEART", "EARTH"))
# print(are_anagrams("HELP", "SELF"))
# print(are_anagrams("LITTLE", "LITLE"))


def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    total = 0

    for char in text:
        if char in vowels:
            total += 1
    return total

# print(count_vowels("Hello Wrold"))
# print(count_vowels("Programming is interesting"))
# print(count_vowels("Are you okay?"))


def sort_list(num_list):
    sorted_list = num_list[:]
    n = len(sorted_list)
    
    for i in range(n):
        for j in range(0, n - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    return sorted_list

print(sort_list([5, 6, 9, 0]))
print(sort_list([1, 2, 1]))
print(sort_list([-1, 9, -10]))


def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

# print(sum_of_digits(123))
# print(sum_of_digits(4567))


def is_palindrome(text):
    text = text.lower()

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1
    return True

# print(is_palindrome("radar"))
# print(is_palindrome("level"))
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))


def password_strength(password):
    has_upper = False
    has_special = False
    
    specials = "@$£"

    for char in password:
        if char.isupper():
            has_upper = True
        if char in specials:
            has_special = True
        
    length = len(password)

    if length < 6:
        return "Weak"

    if not has_upper or not has_special:
        return "Weak"
    
    if length <= 10:
        return "Medium"
    
    return "Strong"

# print(password_strength("abc"))
# print(password_strength("Abc@12"))
# print(password_strength("MyPass2025$"))


def letter_grade(list_of_dictionary):
    total_weight = 0
    total_credits = 0

    for course in list_of_dictionary:
        grade = course["score"]
        credits = course["credits"]

        total_weight += grade * credits
        total_credits += credits

    average = total_weight / total_credits

    if average < 50:
        letter = "F"
    elif average < 60:
        letter = "D"
    elif average < 70:
        letter = "C"
    elif average < 90:
        letter = "B"
    else:
        letter = "A"
    
    return(average, letter)

# # Testing example
# data_input = [
# {"subject": "Math", "score": 90, "credits": 40},
# {"subject": "History", "score": 75, "credits": 20},
# {"subject": "English", "score": 60, "credits": 20},
# {"subject": "Science", "score": 85, "credits": 40},
# {"subject": "Art", "score": 50, "credits": 40}
# ]
# average, grade = letter_grade(data_input)
# print("Average:", average) # Expected output: Average: 73.125
# print("Grade:", grade) # Expected output: Grade: B


def maximum_gap(list1, list2):
    max1 = list1[0]
    min1 = list1[0]
    max2 = list2[0]
    min2 = list2[0]

    for num in list1:
        if num > max1:
            max1 = num
        if num < min1:
            min1 = num

    for num in list2:
        if num > max2:
            max2 = num
        if num < min2:
            min2 = num

    gap1 = max1 - min2
    gap2 = max2 - min1

    if gap1 > gap2:
        return gap1
    else:
        return gap2
    
# print(maximum_gap([1, 5, 600], [100, 7, 3, 29, 39]))
# print(maximum_gap([1, 5, 600], [100, 7, 3, 602, 39]))


def cipher_text(input_text, key):
    result = ""

    for char in input_text:
        ascii_value = ord(char)
        new_value = ascii_value - key
        new_value = new_value % 256
        result += chr(new_value)
    return result

# text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhors$"
# key = 3
# print(cipher_text(text, key))


def net_annual_income(gross_salary):
    tax = 0

    if gross_salary > 12570:
        basic_taxable = min(gross_salary, 50270) - 12570
        tax += basic_taxable * 0.2

    if gross_salary > 50270:
        higher_taxable = min(gross_salary, 125140) - 50270
        tax += higher_taxable * 0.4

    if gross_salary > 125140:
        additional_taxable = gross_salary - 125140
        tax += additional_taxable * 0.45

    return gross_salary - tax

# print(net_annual_income(60000))


def my_split(my_str, sep):
    result = []
    current = ""

    for char in my_str:
        if char == sep:
            result.append(current)
            current = ""
        else:
            current += char
        
    result.append(current)
    return result

# print(my_split("apple,banana,orange", ","))


def longest_repetition(text):
    longest_char = text[0]
    longest_count = 1

    current_char = text[0]
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            current_count += 1
        else:
            if current_count > longest_count:
                longest_char = current_char
                longest_count = current_count
            
            current_char = text[i]
            current_count = 1
        
    if current_count > longest_count:
        longest_char = current_char
        longest_count = current_count

    return(longest_char, longest_count)

# print(longest_repetition("aabbcaa"))
# print(longest_repetition("aaabbcaaa"))
# print(longest_repetition("hellooooo"))
# print(longest_repetition("banana"))
# print(longest_repetition("abc"))


def closest_pair_under_budget(prices, budget):
    best_pair = None
    best_sum = -1

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            item1, price1 = prices[i]
            item2, price2 = prices[j]

            total = price1 + price2

            if total <= budget:
                if total > best_sum:
                    best_sum = total
                    best_pair = [item1, item2]
    return best_pair

# items = [("tv", 300), ("mobile phone", 800), ("laptop", 600), ("headphones", 200)]
# budget1 = 1000
# print(closest_pair_under_budget(items, budget1))
#Task 1: Hello
def x():
    return("Hello")
print(x())

#Task 2: Greet with a Formatted String
def greet(name):
    return (f"Hello {name}!")
print(greet("Name"))

# Task 3: Calculator

def calc(x, y, z="multiply"):
# 
    try:
        match z:
            case "add":
                return x + y
            case "subtract":
                return x - y
            case "multiply":
                return x * y
            case "divide":
                return x/y
            case "modulo":
                return x%y
            case "int_divide":
                return x// y
            case "power":
                return x**y
            # one case per operation, 7 total
    except ZeroDivisionError:
            return("You can't divide by 0!")
    except TypeError:
            return("You can't multiply those values!")

print(calc(10,0,"divide"))
print(calc("10","0","multiply"))

# Task 4: Data Type Conversion

def data_type_conversion(value,type):
    try: 
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
     
    except ValueError:
         return f"You can't convert {value} into a {type}."

print(data_type_conversion("nonsense","float"))    
print(data_type_conversion(1, "str"))  
print(data_type_conversion(3.1,"int"))    

# Task 5: Grading System, Using *args

def grade(*args):

    try:
        average = sum(args)/len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"           
        elif average >= 70:
            return "C" 
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError :
       return "Invalid data was provided."
       
print(grade("hey",74))

# Task 6: Use a For Loop with a Range
def repeat(x, y):
    string = ""
    for g in range(y):       
        string = string + x  
    return string            

print(repeat("hey", 5))       
# Task 7: Student Scores, Using **kwargs

def student_scores(score, **kwargs):
    if score == "mean":
        return sum(kwargs.values()) / len(kwargs.values())
    elif score == "best":
        best_name = ""
        best_score = 0
        for key, value in kwargs.items():
            if value > best_score:
                best_score = value
                best_name = key
        return best_name

print(student_scores("best", Gabe=71, Ben=88, Mike=63))  
print(student_scores("mean", Gio=61, Lee=45, Tom=81))  
# 
# Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word == words[-1] or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)

print(titleize("the alchemist"))   
# Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"
    return result

print(hangman("alphabet", "ab"))   

# Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(sentence):
    vowels = "aeiou"
    result = []
    for word in sentence.split():
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels:
                    if word[i] == "u" and word[i - 1] == "q":
                        i = i + 1
                        continue
                    break
                i = i + 1
            result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)

print(pig_latin("bacon cheeseburger"))   
print(pig_latin("apple pie"))            
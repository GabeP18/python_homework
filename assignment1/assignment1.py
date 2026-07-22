# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(Name):
    return f"Hello, {Name}!"

# Task 3: Calculator
def calc(x,y,op="multiply"):
    try:  
        match op:

            case "add":
                return x+y
            case "multiply":
                return x*y
            case "subtract":
                return x-y
            case "divide":
                return x/y
            case "modulo":
                return x%y
            case "int_divide":
                return x//y
            case "power":
                return x**y
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(2,0, "divide"))
print(calc("2","0", "multiply"))

# Task 4: Data Type Conversion
def data_type_conversion(value,data_type):

    try:
        match data_type:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
            
    except ValueError:
           return f"You can't convert {value} into a {data_type}."
                     
print(data_type_conversion("nonsense", "float")) 

# Task 5: Grading System, Using *args

def grade(*args):
  try: 
     avg = sum(args)/len(args)

     if avg >= 90:
        return("A")
     elif avg >= 80:
        return("B")  
     elif avg >= 70:
        return("C") 
     elif avg >= 60:
        return("D")      
     else:
        return("F")          
  except Exception:
    return "Invalid data was provided."

print(grade("hi"))

# Task 6: Use a For Loop with a Range
def repeat(string,count):
    result = ""
    for x in range(count):
        result += string
    return result   
print(repeat("google",10))  

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

print(student_scores("best", Gabe=71))  
print(student_scores("mean", Gio=61))  

# Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
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
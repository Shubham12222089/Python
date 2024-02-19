
try:
    numerator = int(input("Enter a number: "))
    deno = int(input("Enter the number: "))
    result = numerator/deno
    

except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
# except Exception:
#     print("Something went wrong")6
else:
    print(result)
finally:
    print("This will always execute")
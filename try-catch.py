try:
    # Code that might raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You cannot divide by zero!")
except Exception as e:
    # Handle any other exception
    print("An error occurred:", e)
else:
    # Runs if no exception occurred
    print("Everything went fine!")
finally:
    # Always runs, whether there was an exception or not
    print("This will always run.")
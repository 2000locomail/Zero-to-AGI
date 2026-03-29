def repeat_message(message, times):
    # Base Case: If times is 0 or less, we stop.
    if times <= 0:
        return
    
    print(message)
    
    # Recursive Step: Print it again, but with (times - 1)
    repeat_message(message, times - 1)

repeat_message("Hello Recursion!", 5)
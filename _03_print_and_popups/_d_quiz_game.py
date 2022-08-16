from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    userinput = simpledialog.askstring(title='quiz_game', prompt="Who is the best at connect 4?")
    #      // 3.  Use an if statement to check if their answer is correct
    if userinput == "Ryan":
        #      // 4.  if the user's answer was correct, add one to their score
        score =+ 1
    else:
        score =- 1

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    userinput = simpledialog.askstring(title='quiz_game', prompt="How many states are in the U.S.")

    if userinput == "50":
        score =+ 1
    else:
        score =- 1
    #      // Option: Subtract a point from their score for a wrong answer
    #messagebox.showinfo(message="Final Score: 0")
    #messagebox.showinfo(message="Final Score: 1")
    messagebox.showinfo(message="Final Score: 2")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()

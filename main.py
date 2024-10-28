# Existing imports and class declarations remain unchanged
from tkinter import *  
from tkinter import messagebox  
import random  
import copy


# The WordList class encapsulates word lists for a game with different levels containing words of
# varying lengths.
class WordList:
    """Encapsulates the word lists for the game."""  
    # Define word lists for different levels
    # Level 1 to Level 4: 3 words, each with 3 letters
    level1_words = ['pet', 'top', 'toe']  # Using 'p', 't', 'o', 'e'
    level2_words = ['set', 'bed', 'bet']  # Using 's', 'e', 't', 'b'
    level3_words = ['dog', 'god', 'dos']  # Using 'd', 'o', 'g'
    level4_words = ['sun', 'nut', 'tun']  # Using 's', 'u', 'n', 't'

    # Level 5 to Level 10: 2 words with 3 letters and 2 words with 4 letters
    level5_words = ['dog', 'god', 'good', 'goad']  # Using 'd', 'o', 'g'
    level6_words = ['bes', 'set', 'best', 'test']  # Using 'b', 'e', 's', 't'
    level7_words = ['sun', 'nut', 'tuns', 'nuts']  # Using 's', 'u', 'n', 't'
    level8_words = ['top', 'pot', 'stop', 'opts']  # Using 't', 'o', 'p', 's'
    level9_words = ['tap', 'pas', 'pats', 'past']  # Using 'p', 'a', 't', 's'
    level10_words = ['sit', 'its', 'leap', 'pale']  
    
    

# The `Game` class in Python creates a word finder game with multiple levels, allowing players to form
# words from shuffled letters and progress through levels by submitting correct words.
class Game(Tk):
    """Main class to create the word finder game"""
    
    def __init__(self):
        super().__init__()  
        self.title("Game")  
        self.geometry("400x300")  
        self.resizable(False, False)  
        
        self.start_Button = Button(self, text="start game", command=lambda: self.levels())
        self.start_Button.place(x=150, y=100, width=100, height=50)  
        
        self.current_level = 1  
        self.current_word = ""  
        self.score = 0  
        self.correct_words = 0  
        self.correct_words_list = []  
        # Deep copy of the word lists
        self.words_list = copy.deepcopy({
            1: WordList.level1_words,
            2: WordList.level2_words,
            3: WordList.level3_words,
            4: WordList.level4_words,
            5: WordList.level5_words,
            6: WordList.level6_words,
            7: WordList.level7_words,
            8: WordList.level8_words,
            9: WordList.level9_words,
            10: WordList.level10_words,
        })
        
    def levels(self):
        """Function to create and display the game levels"""
        self.level = Toplevel(self)  
        self.level.title(f"Level {self.current_level}")  
        self.level.geometry("400x400")  
        self.level.resizable(False, False)  
        self.level.configure(bg='lightgray')  
        
        self.text_variable = StringVar()
        self.entry_grid = []
        self.create_letters_button()  
         # Create a frame to hold the entries
        self.for_entries = Frame(self.level, bg='lightgray')  
        self.for_entries.place(x=125, y=100, width=300, height=120)  # Adjust position and size of the frame
            
        Label(self.level, text=f"level {self.current_level}", font=("arial", 16, "bold")).place(x=10, y=10)

        self.dd = Label(self.level, text="", bg="gray", font=("arial", 16, "bold"))
        self.dd.place(x=150, y=30)

        self.score_label = Label(self.level, text=f"score: {self.score}", bg="gray", font=("arial", 16, "bold"))
        self.score_label.place(x=10, y=80)

        # The above code is creating buttons in a GUI interface using the Tkinter library in Python.
        # Each button has a specific text label and a command associated with it that will be executed
        # when the button is clicked. The commands are defined using lambda functions to call specific
        # methods of the class instance (`self.next_level()`, `self.shuffle()`, `self.reset()`,
        # `self.check()`, `self.delete_letter()`). The buttons are being placed at different
        # coordinates on the GUI window using the `place()` method.
        Button(self.level, text="next level", command=lambda: self.next_level()).place(x=300, y=10)
        Button(self.level, text="shuffle", command=lambda: self.suffle()).place(x=100, y=300)
        Button(self.level, text="reset", command=lambda: self.reset()).place(x=150, y=300)
        self.submit = Button(self.level, text="submit", command=lambda: self.check()).place(x=200, y=300)
        self.delete = Button(self.level, text="delete", command=lambda: self.delete_letter()).place(x=250, y=300)

        self.entries = []  # List to hold text entry fields
        self.entry_vars = []  # List to hold StringVar instances for entries

        # The above code is a snippet written in Python. It checks the value of `self.current_level`
        # and based on its value, it calls the `create_Entry` method with different parameters to
        # create entries in rows.
        if 1 <= self.current_level <= 4:
            self.create_Entry(3, 1)  # Creates 3 entries in row 1
            self.create_Entry(3, 2)  # Creates 3 entries in row 2
            self.create_Entry(3, 3)  # Creates 3 entries in row 3
        elif 5 <= self.current_level <= 10:
            self.create_Entry(3, 1)  # Creates 3 entries in row 1
            self.create_Entry(3, 2)  # Creates 3 entries in row 2
            self.create_Entry(4, 3)  # Creates 4 entries in row 3
            self.create_Entry(4, 4)  # Creates 4 entries in row 4

        
        self.level.mainloop()  

    def create_Entry(self, count, row_start):
        """
        This function creates text entry fields in a grid layout based on the specified count and row
        start position.
        
        :param count: The `count` parameter in the `create_Entry` function represents the number of text
        entry fields that will be created in the grid layout. It determines how many Entry widgets will
        be generated and displayed horizontally in the grid
        :param row_start: The `row_start` parameter in the `create_Entry` function is used to specify
        the starting row in the grid layout where the text entry fields will be placed. Each text entry
        field will be placed in a separate row starting from the row specified by `row_start`
        """
        """Function to create text entry fields in a grid layout based on the level"""
        
        for i in range(count):
            entry_var = StringVar()
            entry = Entry(self.for_entries, textvariable=entry_var, width=5)  # Placing entries inside the frame
            entry.grid(row=row_start, column=i, padx=5, pady=5, sticky="nsew")  # Use grid layout within the frame
            self.entries.append(entry)
            self.entry_vars.append(entry_var)
  
   
    def next_level(self):
        """
        The function `next_level` moves to the next level if the current word is correct based on the
        current level and score conditions.
        """
        """Function to move to the next level if the current word is correct"""
        
        if self.current_level<=4:
            if self.score >= 3:  
                self.level.destroy()  
                self.current_level += 1  
                self.current_word=''
                self.score=0
                self.levels()
            else:
                    messagebox.showerror("Warning", "Please solve the current level first")
                    
        elif 5<=self.current_level<=10:
            if self.score>= 4:
                self.level.destroy()  
                self.current_level += 1  
                self.current_word=''
                self.score=0
                self.levels()
            else:
                    messagebox.showerror("Warning", "Please solve the current level first")
                    
      
                
            
        
            
    def create_letters_button(self):
        """
        The function `create_letters_button` generates buttons with random letters for word selection
        based on the current level.
        :return: The function `create_letters_button` will return `None` as there is no explicit return
        value specified within the function.
        """
        """Function to create buttons with random letters for word selection"""
        if  self.current_level>10:
            self.level.destroy()
            return 

        self.buttons = []  
        self.letters = []  

        test = {
            1: WordList.level1_words,
            2: WordList.level2_words,
            3: WordList.level3_words,
            4: WordList.level4_words,
            5: WordList.level5_words,
            6: WordList.level6_words,
            7: WordList.level7_words,
            8: WordList.level8_words,
            9: WordList.level9_words,
            10: WordList.level10_words,
        }
        
        for word in self.words_list[self.current_level]:
            for letter in word:
                if letter not in self.letters:
                    self.letters.append(letter)

        random.shuffle(self.letters)  
        self.count = len(self.letters)  

        for i in range(self.count):
            letter = self.letters.pop()  
            button = Button(
                self.level, text=letter, width=2, height=2, command=lambda x=letter: self.add_letter(x)
            )
            button.place(x=100 + (i * 40), y=250)  
            self.buttons.append(button)  

        
    

    def add_letter(self, letter):
        """
        The function `add_letter` adds a given letter to the current word and updates the display with
        the new word.
        
        :param letter: The `letter` parameter in the `add_letter` function represents the letter that is
        being added to the current word when a button is pressed. This function is part of a class, and
        it appends the `letter` to the `current_word` attribute of the class instance. Additionally, it
        """
        """Function to handle adding letters to the current word when a button is pressed"""
        self.current_word += letter  
        self.dd.config(text=self.current_word)  

    def suffle(self):
        """
        The `shuffle` function shuffles the letter buttons by destroying the existing buttons and
        creating new ones.
        """
        """Function to shuffle the letter buttons"""
        for i in self.buttons:
            i.destroy()  
        self.create_letters_button()  

    def reset(self):
        """
        The `reset` function clears the current word and display, and updates the background colors of
        certain widgets.
        """
        """Function to reset the current word and clear the display"""
        self.current_word = ""  
        self.dd.config(text="")  
        if self.dd["text"] == "":  
            self.dd.config(bg="gray")  
            self.level.config(bg='lightgray')
            self.for_entries.config(bg='lightgray')

    def calculate_Score(self):
        """
        The function calculates the score based on the number of correct words entered in a text field.
        :return: If the `self.dd["text"]` is an empty string, the function will return 0. Otherwise, it
        will increment the `self.score` by 1 and update the text of the `self.score_label` to display
        the updated score.
        """
        """Function to calculate the score based on the number of correct words"""
        if self.dd["text"] == "":  
            return 0
        else:
            self.score += 1  
            self.score_label.config(text=f"Score: {self.score}")  
    def filled_entry(self):
        """
        The function `filled_entry` populates entry fields with a given word, handling both 3-letter and
        4-letter words by filling rows with empty entries.
        """
        """Populate the entries with the correct word, handling both 3-letter and 4-letter words."""
        
        if len(self.current_word) == 3:  # Handle 3-letter word
            row_entries = 3
            max_rows = (len(self.entries) + row_entries - 1) // row_entries  # Total number of rows for 3-letter words

           

            # Find the first row that isn't filled
            for row_ in range(max_rows):
                start_index = row_ * row_entries  # Starting index of the row
                
                # Check if the row has at least one empty entry
                row_filled = any(not self.entries[start_index + i].get() for i in range(row_entries))  # Check for empty entries


                if row_filled:  # If there is at least one empty entry, insert the word
                    for i in range(3):  # Loop over 3 letters of the word
                        self.entries[start_index + i].delete(0, END)  # Clear the entry field
                        self.entries[start_index + i].insert(0, self.current_word[i])  # Insert the letter
                        self.entries[start_index + i].config(state='readonly')  # Make entry readonly
                    break  # Exit after filling the first available row

        elif len(self.current_word) == 4:  # Handle 4-letter word
            row_entries = 2 # Set row size for 4-letter words
            max_rows = (len (self.entries) // row_entries)  # Total number of rows for 4-letter words

       

            # Find the first row that isn't filled
            for row_ in range(max_rows):
                start_index = (row_ * row_entries)+6  # Starting index of the row
                
                # Check if the row has at least one empty entry
                row_filled = any(not self.entries[start_index + i].get() for i in range(row_entries))  # Check for empty entries

            

                if row_filled:  # If there is at least one empty entry, insert the word
                    for i in range(4):  # Loop over 4 letters of the word
                        self.entries[start_index + i].delete(0, END)  # Clear the entry field
                        self.entries[start_index + i].insert(0, self.current_word[i])  # Insert the letter
                        self.entries[start_index + i].config(state='readonly')  # Make entry readonly
                    break  # Exit after filling the first available row

                
    def check(self):
        """
        The function `check` checks if the current word is valid based on the current level and updates
        the interface accordingly.
        :return: The function `check` is returning a boolean value. It returns `True` if the current
        word is valid (i.e., if `self.current_word` is in the word list corresponding to the current
        level), and `False` otherwise.
        """
        """Function to check if the current word is valid"""
        level_word = {
            1: WordList.level1_words,
            2: WordList.level2_words,
            3: WordList.level3_words,
            4: WordList.level4_words,
            5: WordList.level5_words,
            6: WordList.level6_words,
            7: WordList.level7_words,
            8: WordList.level8_words,
            9: WordList.level9_words,
            10: WordList.level10_words,
        }
        
        if self.current_word in level_word[self.current_level]:
            self.level.config(bg="green")  
            self.for_entries.config(bg="green")  
            self.correct_words += 1
            self.isit()  
            self.calculate_Score()  
            self.filled_entry()  # Call the method to fill entries
            
            return True
        else:
            self.level.config(bg="red")  
            self.for_entries.config(bg="red")  
            return False
        
    def isit(self):
        """
        The function checks if the current word has been found before and updates the correct words list
        accordingly.
        """
        """Function to check if the current word has been found before"""
        level_words = {
            1: WordList.level1_words,
            2: WordList.level2_words,
            3: WordList.level3_words,
            4: WordList.level4_words,
            5: WordList.level5_words,
            6: WordList.level6_words,
            7: WordList.level7_words,
            8: WordList.level8_words,
            9: WordList.level9_words,
            10: WordList.level10_words,
        }

        current_level_words = level_words[self.current_level]

        if self.current_word in current_level_words:
            self.correct_words_list.append(self.current_word)
            current_level_words.remove(self.current_word)  
        
    def delete_letter(self):
        """
        The `delete_letter` function deletes the last letter added to the current word and updates the
        display accordingly.
        """
        """Function to delete the last letter added to the current word"""
        self.current_word = self.current_word[:-1]  # Remove last character
        self.dd.config(text=self.current_word)  # Update the display

  
        
        
        
# The above code is a Python script that checks if the current module is being run as the main
# program. If it is, it creates an instance of the `Game` class and calls its `mainloop()` method.
# This typically indicates that the `Game` class contains the main logic for a game or application,
# and `mainloop()` is the method responsible for running the main game loop or application loop.
if __name__ == "__main__":  
    game = Game()  
    game.mainloop()

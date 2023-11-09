# french-flashcards
A flashcard app (similar to Quizlet) but each word is timed

Note: In my experience, the Tkinter module may not be successfully installed on macOS, so I recommend downloading and running on a Windows/Linux device if unsure.

As I continued to learn French, I was searching for a way to practice my conjugations. I created this app so I would be able to customize the process in which the flashcards functioned (and looked!). Once the app is open, an infinitive verb is displayed as well as a subject. 6 seconds later, the correctly conjugated form of the word is displayed. The task is to figure out the conjugation before the 6 seconds. Don't worry, it's longer than you think! Clicking the (check) or (x) buttons generates a new flashcard.

As a new flashcard is generated, a random verb is chosen from /src/words.py as well as a random subject (je, tu, nous, etc.). The verb and the correct conjugation (grabbed from /src/words.py) are saved and displayed.


Please enjoy! Happy learning!

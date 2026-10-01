# Text-analyzing-
Analyzing the text readability and other features 
# TEXT INSIGHT: yes
#### Video Demo: https://youtu.be/OCk-3h-siTQ?si=gtiJ-2TjUstKx49m
#### Description:
The project analyzes a certain text to determine its readability, time a person needs to read it and the most frequent word that is out the linking or common words such as (a, in, to, the)
It helps the teachers and students to analyze the hardness of the text without needing to read it, which saves a significant amount of time, and helps teachers determine the appropriate texts for their students.

### Main function:
The primary driver inside the project calls the functions and prints the result in  a clear and neat way.
It contains an error check and handles these errors in a professional way. First, it asks the user to enter the text, then it ensures that the text is not empty, if it is empty the program will end after printing “invalid text” on the screen.
Then it asks the user to enter their reading speed (it also can be the average speed of their students if the user was a teacher). Using try and except the program checks the validity of the user input; if it is not valid, the wpm speed will be considered the average reading speed in the world, which is 183.
Then the main will call the functions one after another and print the results.

This project contains 3 main functions and 2 helping functions.
### First function (reading_time):
It counts the time needed for a reader with a specific speed to read the entered text.
It takes two parameters the text and wpm with default value equals to 183. The function raises a value error if the wpm is zero or less.
Its working mechanism, the first step is dividing the text to words by the spaces between the words, then it checks if the word contain a letter or number or just made of symbols, the words that just made of symbols will not be counted in the text overall length.
It then will divide the total word count by wpm and using timedelta to return much understandable and readable result rather than returning a float to represent the time it returns an object that shows the needed hours: minutes : seconds. Timedelta is a class from the standard library module datetime.
### Second function (reading_ease):
It determines the text complexity according to Coleman-Liau Index, which calculates the hardness of a specific text according to the length of the words and the length of the sentence. Because complex texts contain longer words and sentences with less punctuation marks.
The resulting grade depends on two factors:
1.	** L **
The number of letters on the number of words, all multiplied by 100.
multiplied by 100 to find how many letters the text will contain if the text only contains 100 words.

2.	**S**
The number of sentences on the number of words, all multiplied by 100.
This ratio is multiplied by 100 to find how many sentences the text will contain if the text only contains 100 words.
The number of sentences will be determined by the number of end-of-sentence punctuation marks which are the full stop, question mark and exclamation mark. Re library has been used for this job. Sometimes two exclamation marks or two question marks are written one after the other; in this case, it is not considered that this text contains two sentences, but only one sentence will be added to the counter.
If the text contains a word and letters but does not contain end-of-sentence punctuation marks the program will consider that the text contains 1 sentence and not zero sentences.
Finally, the grade will be calculated by Coleman-Liau formula, which is grade =0.0588 * L - 0.296 * S - 15.8.
And the function will return the result round by 2.

### The first helping function (explaing_the_reading_ease_grade)
It is a very simple function that takes one parameter which is grade and uses if else statements to explain the meaning of the grade result. And return the explanation.

### The third function (‘most_frequent_word’):
Its  job is to determine the most frequent word in the text that is not from the common linking word.
First a list variable has been defined this list contain the most frequent words like “in”, “it”, “the” etc.…
Then the function will pass on each word delete the punctuation marks (using string.punctuation constant) and convert all characters to lowercase and then ensures the word is not in the previous list and contains a letter, not just made of symbols or numbers (a special function has been built for this task and it will be explained later)
If the word is passed the previous check the program will check if it is a new word and have not been added to the_words dictionary before, the program will added it the key will be the word itself and the value will be 1 (how many times this word exists in the text until now). If the word have already been in the dictionary the program will add one to its value in the dictionary.

The function will pass in all the dictionary items to find the most frequent to be returned.

### The second helping function (is_digits_or_symbols):
It is a function takes one parameter which is word and return true if the word made from numbers and symbols only and return false if it contain a letter.


### The explanation behind some of design choices:
1.Using:
re.findall(r"[.!?]+" , text)
rather than split (“.”)
sentences in the real world also ends with question marks and exclamation mark and may end with multiple punctuation marks like (… or ?!, !! or ??) ect…
using split (“.”) will consider that there are 3 sentences if the sentence ends with (…) which will affect the accuracy of the results.

2.Using:
Timedelta rather than float
Using timedelta increases the readability of the results and determine the needed time in an accurate and clean way.
3.Excluding repeated and linking words like “the” and “and” to prevent returning  grammatical words with no real meaning.








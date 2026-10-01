from datetime import datetime , timedelta
import re
import string
def main():
    text = input ("Enter the text:\n")
    if not text.strip():
        print ("invalid text")
        return

    try :
        wpm = int (input ("Enter your reading speed: (the default value will be 183): "))

    except :
        print ("unvalid input, your reading speed wil be considered as 183")
        wpm = 183
    grade = reading_ease(text)
    print ("*************THE RESULTS*************")
    print(f"Reading Time: {reading_time(text ,wpm)}")
    print(f"Grade Level: {grade} , means : {explaing_the_reading_ease_grade(grade)}")

    print(f"Most Frequent Word: {most_frequent_word(text)}")




def reading_time(text , wpm = 183):
    if wpm <=0 :
        raise ValueError("WPM must be greater than 0")
    words = text.split()
    lenght = 0
    for word in words :

        if any(char.isalnum() for char in word ):
            lenght+=1



    return timedelta(minutes= lenght/float (wpm ))




def reading_ease(text):
    words = text.split()
    words_c= 0

    for word in words :

        if any(char.isalnum() for char in word ):
            words_c+=1
    if words_c <=0 :
        return 0.0

    letters_c = sum (1 for char in text if char.isalnum())

    L = (letters_c / words_c) *100

    Sentences = re.findall(r"[.!?]+" , text)
    Sentences_c = len (Sentences)
    if Sentences_c ==0 :
        Sentences_c = 1

    S = (Sentences_c / words_c) *100

    """ Coleman-Liau operation"""
    grade =0.0588 * L - 0.296 * S - 15.8
    return round (grade , 2)




def explaing_the_reading_ease_grade(grade):
    explain ="the grade is not valid"
    if grade < 5 :
        explain = "The text level is very simple "
    elif 5 <= grade < 8:
         explain = "The text level is  simple "
    elif  8 <= grade < 12:
        explain = "The text level is  medium "
    elif 12 <= grade < 16:
         explain = "The text level is  complex "
    elif  grade >= 16:
         explain = "The text level is  very complex "

    return explain




def most_frequent_word(text):
    the_words = {}
    link_words = ['is', 'are', 'to', 'and' , 'also',
            'a', 'for' , 'in' , 'an' ,'the' , 'that' , 'this'
             , 'with' , 'at' , 'as' , 'by' , 'on' , 'which' ]

    words = text.split()

    for word in words :
        word= word.strip(string.punctuation).lower()
        if word not in link_words and not is_digits_or_symbols(word):
            if word not in the_words  :
                the_words[word] = 1
            else:
                the_words[word] = the_words[word] +1

    maxx = 0
    the_w = "there are no words"
    for word , conut in the_words.items() :
        if conut > maxx :
            maxx = conut
            the_w = word
    return the_w




def is_digits_or_symbols(word):
    return not any(char.isalpha() for char in word)




if __name__ == "__main__":
    main()



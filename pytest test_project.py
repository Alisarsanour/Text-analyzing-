from project import reading_time , reading_ease ,most_frequent_word
from datetime import timedelta
import pytest
def test_reading_time():
    text =  "word "*100
    assert reading_time(text , 100) == timedelta (minutes =1 )
    assert reading_time(text , 200 ) == timedelta (seconds =30 )
    assert reading_time("" ) == timedelta (seconds =0 )

    with pytest.raises(ValueError):
        reading_time("any thing", 0)

    with pytest.raises(ValueError):
        reading_time("blah blah blah", -93)



def test_reading_ease():
    text1 = "hey, how are you? "
    assert reading_ease(text1 ) == -5.56

    text2 = "Notwithstanding the ubiquitous integration of" \
    " artificial intelligence into our daily cognitive " \
    "architectures, a paradoxical apprehension persists; " \
    "wherein the more seamlessly these algorithmic constructs " \
    "emulate human sapience, the more acutely we discern the " \
    "irretrievable chasm separating computational simulation " \
    "from genuine phenomenological sentience."

    assert  reading_ease(text2 ) == 28.22

    assert reading_ease("")== 0.0
    assert reading_ease("***")== 0.0


def test_most_frequent_word():
    text1 = "hey hey hey u u la la la la "
    assert most_frequent_word(text1) == "la"
    text2 = "***"
    assert most_frequent_word(text2) == "there are no words"

    text3 = "ss) ss. kk kk ss? kk ss."
    assert most_frequent_word(text3) == "ss"
 



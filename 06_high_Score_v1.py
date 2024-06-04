"""
High Score v1 also known as the final verison,
this wont be included in the final as a quiz with a high score is not needed.
espically in the sense on a quiz which has set questions and answers and isn't endless.
"""


def high_score():
    """
    Add high score to the quiz application.
    """
    save_name = input('Enter your name. ').title()
    save_score = quiz.score

    text_file = open("highscores.txt", "a")
    text_file.write("\n" + save_name + ' has a score of ' + save_score + "\n")
    text_file.close()

    print("\n")
    text_file = open("highscores.txt", "r")
    whole_thing = text_file.read()
    print(whole_thing)
    text_file.close()

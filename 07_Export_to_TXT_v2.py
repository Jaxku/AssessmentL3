""" This script exports the final score along with the user's name to a text file."""


def export_score_basic(score, user_name):

    file_path = f"{user_name}_score.txt"
    with open(file_path, "w") as file:
        file.write(f"User: {user_name}\n")
        file.write(f"Score: {score}\n")

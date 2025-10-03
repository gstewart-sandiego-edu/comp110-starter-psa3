"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
Parker Brown - parkerbrown@sandiego.edu
Gabe Stewart - gstewart@sandiego.edu
"""

def calculate_average_review(target_word, review_filename):
    """
    FIXME: Add function synopsis here.

    Parameters:
    target_word (type: string): The word to look for in the reviews.
    FIXME: add info about second parameter

    Returns:
    (type: float) FIXME by describing what is returned here.
    """

    review_file = open(review_filename, 'r')

    for review in review_file:
        # make lower case to avoid case sensitivity
        review_lower = review.lower()  

        # FIXME: finish implementing this loop body


    # done reading file, so close it
    review_file.close()

    # FIXME: calculate the average review score

    return None     # replace this with returning the calculated average


def calculate_estimated_score(review_text, review_filename):
    """
    FIXME: Fill in this docstring comment, using the exact format given for the
    average_review docstring comment.
    """

    return None     # replace this with returning the estimated review



def get_review_and_estimate():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    pass # replace this line of code with your function implementation


# Do not modify anything after this point.
if __name__ == "__main__":
    get_review_and_estimate()

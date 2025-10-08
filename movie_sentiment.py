"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
Parker Brown - parkerbrown@sandiego.edu
Gabriel Stewart - gstewart@sandiego.edu
"""

def calculate_average_review(target_word, review_filename):
    """
    Calculates and returns the average score of movie reviews which contain a given word.

    Parameters:
        target_word (type: string): The word to look for in the reviews.
        review_filename (type: string): The path to the file containing the movie reviews.

    Returns:
        (type: float) The average score of all of the reviews which contain the given word. Returns None if none of the reviews contain the word.
    """

    review_file = open(review_filename, 'r')

    num_reviews = 0
    total_score = 0
    for review in review_file:
        # make lower case to avoid case sensitivity
        review_lower = review.lower()  
        review_split = review_lower.split(" ")
        if target_word in review_split[1:]:
            total_score += int(review_split[0])
            num_reviews += 1

    # done reading file, so close it
    review_file.close()

    # calculate the average review score
    if num_reviews == 0:
        return None
    else:
        return total_score / num_reviews


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

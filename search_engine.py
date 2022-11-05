"""
*You are given few sentences as a list (Python list of sentences).
*Take a query string as an input from the user.
*You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance
after converting every word in the query and the sentence to lowercase.
*The most relevant sentence is the one with the maximum number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:
    python is not python snake
    python is good
    Python is cool
"""


def matching_words(sentence1, sentence2):
    user_words = sentence1.strip().split(" ")
    base_words = sentence2.strip().split(" ")
    match_score = 0
    for user_word in user_words:
        for base_word in base_words:
            if user_word.lower() == base_word.lower():
                match_score = match_score + 1
    return match_score


if __name__ == "__main__":
    base_sentences = ['Python is good', 'this is snake', 'Priyanshu is a good boy', 'Subscribe to coding']
    user_query = input("What do you are looking for!\n")
    result = [matching_words(user_query, base_sentence) for base_sentence in base_sentences]
    sorted_score_matching = [MatchScore for MatchScore in sorted(zip(result,base_sentences),reverse=True) if
                             MatchScore[0] != 0]
    print(f'{len(sorted_score_matching)} match found!\n')
    for score, matching in sorted_score_matching:
        print(f'\"{matching}\": with score of {score}')

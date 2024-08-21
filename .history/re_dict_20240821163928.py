import re

text = '''

{
    "(Part 3) Advanced Topics and Capstone": [
        {
            "Module 18:Natural Language Processing (NLP)": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 19:Recommendation Systems": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 20:Capstone - Part 1": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 21:Ensemble Techniques": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 22:Deep Neural Networks 1": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 23:Deep Neural Networks 2": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 24:Capstone - Part 2": {
                "Learning Outcomes": [
                    "Identify the similarities and differences between text and numerical data",
                    "Convert text data to numerical data using NLTK",
                    "Tokenize blocks of text",
                    "Decide what features to extract from a text for a particular classification purpose",
                    "Perform feature extraction using NLTK",
                    "Apply the Naive Bayes classifier",
                    "Evaluate text similarity",
                    "Perform text clustering",
                    "Compare the results of classification on text data using several models"
                ],
                "Key Activities": [
                    "Videos",
                    "Knowledge Checks",
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        }
    ]
}




'''








# Regular expression to find all strings in double quotes
pattern = r'"([^"]*?)"'

# Function to replace spaces inside quoted strings with underscores
def replace_spaces_with_underscore(match):
    return '"' + match.group(1).replace(' ', '_') + '"'

# Apply the regex substitution
result = re.sub(pattern, replace_spaces_with_underscore, text)

# Print the modified text
print(result)
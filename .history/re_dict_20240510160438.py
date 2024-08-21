import re

text = '''

{
    "Part 1 Foundations of Machine Learning and AI": [
        {
            "Module 1:Introduction to Machine Learning": {
                "Learning Outcomes": [
                    "Utilize industry-standard notation and concepts",
                    "Recognize discrete and continuous probability functions and their expected values",
                    "Distinguish between measures of central tendency",
                    "Load data into a dataframe using pandas",
                    "Analyze data using selection and statistical techniques",
                    "Create histograms and data visualizations",
                    "Draw business conclusions from datasets and visualizations"
                ],
                "Key Activities": [
                    "Try-It Activity",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 2:Fundamentals of Machine Learning": {
                "Learning Outcomes": [
                    "Analyze measures of central tendency for univariate and multivariate distributions",
                    "Create and interpret visual plots, including probability density functions, histograms, scatter plots, pair plots, and correlation matrices",
                    "Apply the Law of Large Numbers to a given population",
                    "Discuss applications of the Central Limit Theorem",
                    "Interpret a sample covariance matrix using Python",
                    "Approximate correlation from scatterplots",
                    "Identify conditional probabilities"
                ],
                "Key Activities": [
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 3:Introduction to Data Analysis": {
                "Learning Outcomes": [
                    "Discuss real-world contexts for the data science lifecycle",
                    "Manipulate data given a dataset",
                    "Generate visualizations using pandas, Seaborn, and Plotly",
                    "Customize plots using externally sourced documentation",
                    "Use pandas.groupby to manipulate data",
                    "Perform computations between dataframes using set index and reset index"
                ],
                "Key Activities": [
                    "Try-It Activity",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 4:Fundamentals of Data Analysis": {
                "Learning Outcomes": [
                    "Use pandas.merge to join datasets",
                    "Create a variety of plot types in pandas, Seaborn, and Plotly",
                    "Discuss the advantages and disadvantages of each plotting library",
                    "Perform string manipulation in pandas",
                    "Import and clean messy data from real-world datasets"
                ],
                "Key Activities": [
                    "Try-It Activities",
                    "Codio Activities",
                    "Module Quiz"
                ]
            }
        },
        {
            "Module 5:Practical Application 1": {
                "Learning Outcomes": [
                    "Navigate files and directories using your terminal",
                    "Create, alter, and delete files using your terminal",
                    "Create .git repositories locally in your terminal",
                    "Create GitHub repositories online",
                    "Connect local .git repositories to GitHub",
                    "Use the add, commit, and push commands to update work in a remote repository",
                    "Apply exploratory data analysis, plotting, statistical summarization, and data visualization skills and techniques to a machine learning problem"
                ],
                "Key Activities": [
                    "Practical Application Problem"
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
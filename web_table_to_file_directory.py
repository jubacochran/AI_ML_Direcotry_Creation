# %%

import os
import json

# Define the base directory where the folders will be created
base_directory = 'Directory for ML course content'

# Ensure base directory exists
if not os.path.exists(base_directory):
    os.makedirs(base_directory, exist_ok=True)

def create_directory_structure(base_path, structure):
    for part, modules in structure.items():
        part_path = os.path.join(base_path, part)
        if not os.path.exists(part_path):
            os.makedirs(part_path)
            print(f"Created part directory: {part_path}")

        for module_dict in modules:
            for module_name, contents in module_dict.items():
                module_path = os.path.join(part_path, module_name)
                if not os.path.exists(module_path):
                    os.makedirs(module_path)
                    print(f"Created module directory: {module_path}")

                # Process each type of content
                for content_type in ['Learning_Outcomes', 'Key_Activities']:
                    if content_type in contents:
                        content_type_path = os.path.join(module_path, content_type)
                        if not os.path.exists(content_type_path):
                            os.makedirs(content_type_path)
                            print(f"Created {content_type} directory: {content_type_path}")

                        # Create directories for each item under the content type
                        for item in contents[content_type]:
                            item_path = os.path.join(content_type_path, item.replace(" ", "_"))
                            if not os.path.exists(item_path):
                                os.makedirs(item_path)
                                print(f"Created item directory: {item_path}")
# Dictionary with structure
course_structure ={
    "Part_3_Advanced_Topics_and_Capstone": [
        {
            "Module_18:Natural_Language_Processing_(NLP)": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_19:Recommendation_Systems": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_20:Capstone_-_Part_1": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_21:Ensemble_Techniques": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_22:Deep_Neural_Networks_1": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_23:Deep_Neural_Networks_2": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_24:Capstone_-_Part_2": {
                "Learning_Outcomes": [
                    "Identify_the_similarities_and_differences_between_text_and_numerical_data",
                    "Convert_text_data_to_numerical_data_using_NLTK",
                    "Tokenize_blocks_of_text",
                    "Decide_what_features_to_extract_from_a_text_for_a_particular_classification_purpose",
                    "Perform_feature_extraction_using_NLTK",
                    "Apply_the_Naive_Bayes_classifier",
                    "Evaluate_text_similarity",
                    "Perform_text_clustering",
                    "Compare_the_results_of_classification_on_text_data_using_several_models"
                ],
                "Key_Activities": [
                    "Videos",
                    "Knowledge_Checks",
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        }
    ]
}
# Call the function to create the directory structure
create_directory_structure(base_directory, course_structure)

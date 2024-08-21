import os
import json

# Define the base directory where the folders will be created
base_directory = '/Users/jubacochran/Downloads/AI_ML_UC_Berkeley'

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
# Example dictionary with structure
course_structure ={
    "Part_1_Foundations_of_Machine_Learning_and_AI": [
        {
            "Module_1:Introduction_to_Machine_Learning": {
                "Learning_Outcomes": [
                    "Utilize_industry-standard_notation_and_concepts",
                    "Recognize_discrete_and_continuous_probability_functions_and_their_expected_values",
                    "Distinguish_between_measures_of_central_tendency",
                    "Load_data_into_a_dataframe_using_pandas",
                    "Analyze_data_using_selection_and_statistical_techniques",
                    "Create_histograms_and_data_visualizations",
                    "Draw_business_conclusions_from_datasets_and_visualizations"
                ],
                "Key_Activities": [
                    "Try-It_Activity",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_2:Fundamentals_of_Machine_Learning": {
                "Learning_Outcomes": [
                    "Analyze_measures_of_central_tendency_for_univariate_and_multivariate_distributions",
                    "Create_and_interpret_visual_plots,_including_probability_density_functions,_histograms,_scatter_plots,_pair_plots,_and_correlation_matrices",
                    "Apply_the_Law_of_Large_Numbers_to_a_given_population",
                    "Discuss_applications_of_the_Central_Limit_Theorem",
                    "Interpret_a_sample_covariance_matrix_using_Python",
                    "Approximate_correlation_from_scatterplots",
                    "Identify_conditional_probabilities"
                ],
                "Key_Activities": [
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_3:Introduction_to_Data_Analysis": {
                "Learning_Outcomes": [
                    "Discuss_real-world_contexts_for_the_data_science_lifecycle",
                    "Manipulate_data_given_a_dataset",
                    "Generate_visualizations_using_pandas,_Seaborn,_and_Plotly",
                    "Customize_plots_using_externally_sourced_documentation",
                    "Use_pandas.groupby_to_manipulate_data",
                    "Perform_computations_between_dataframes_using_set_index_and_reset_index"
                ],
                "Key_Activities": [
                    "Try-It_Activity",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_4:Fundamentals_of_Data_Analysis": {
                "Learning_Outcomes": [
                    "Use_pandas.merge_to_join_datasets",
                    "Create_a_variety_of_plot_types_in_pandas,_Seaborn,_and_Plotly",
                    "Discuss_the_advantages_and_disadvantages_of_each_plotting_library",
                    "Perform_string_manipulation_in_pandas",
                    "Import_and_clean_messy_data_from_real-world_datasets"
                ],
                "Key_Activities": [
                    "Try-It_Activities",
                    "Codio_Activities",
                    "Module_Quiz"
                ]
            }
        },
        {
            "Module_5:Practical_Application_1": {
                "Learning_Outcomes": [
                    "Navigate_files_and_directories_using_your_terminal",
                    "Create,_alter,_and_delete_files_using_your_terminal",
                    "Create_.git_repositories_locally_in_your_terminal",
                    "Create_GitHub_repositories_online",
                    "Connect_local_.git_repositories_to_GitHub",
                    "Use_the_add,_commit,_and_push_commands_to_update_work_in_a_remote_repository",
                    "Apply_exploratory_data_analysis,_plotting,_statistical_summarization,_and_data_visualization_skills_and_techniques_to_a_machine_learning_problem"
                ],
                "Key_Activities": [
                    "Practical_Application_Problem"
                ]
            }
        }
    ]
}
# Call the function to create the directory structure
create_directory_structure(base_directory, course_structure)

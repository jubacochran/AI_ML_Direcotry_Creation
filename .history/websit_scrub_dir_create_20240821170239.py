# %%

from bs4 import BeautifulSoup
import json
#You must inspect the website and locate the table of your directory structure
# Replace with the actual file path to the HTML file
html_file_path = 'AI_ML_Objectives_table'

# Read the HTML content from the file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize the output structure
course_structure = {}

# Identify all "Part" headers
parts = soup.find_all('strong', text=lambda x: x and x.startswith('(Part'))
for part in parts:
    part_name = part.text
    modules = []
    
    # Identify the next sibling which is a container for modules
    part_container = part.find_next('div', {'class': 'kl_panels_wrapper'})
    if part_container:
        # Find all modules within this part container
        module_headers = part_container.find_all('h3', {'class': 'kl_panel_heading'})
        for module_header in module_headers:
            module_name = module_header.get_text(strip=True)
            module_content_id = module_header.get('aria-controls')
            module_content = part_container.find('div', {'id': module_content_id})
            
            # Extract learning outcomes and key activities
            module_info = {}
            
            # Learning outcomes
            learning_outcomes = module_content.find('p', text='Learning Outcomes')
            if learning_outcomes:
                ul = learning_outcomes.find_next('ul')
                module_info['Learning Outcomes'] = [li.get_text(strip=True) for li in ul.find_all('li')]
            
            # Key activities
            key_activities = module_content.find('p', text='Key Activities')
            if key_activities:
                ul = key_activities.find_next('ul')
                module_info['Key Activities'] = [li.get_text(strip=True) for li in ul.find_all('li')]
            
            # Add to module list
            modules.append({module_name: module_info})
    
    # Add modules to the part structure
    course_structure[part_name] = modules

# Output the structure as a JSON object
print(json.dumps(course_structure, indent=4))

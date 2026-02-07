import yaml
from jinja2 import Environment, FileSystemLoader
import os

def generate_lesson(data_file, template_file, output_file):
    # 1. Load Data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 2. Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('Project-SCOPE/templates'))
    template = env.get_template(os.path.basename(template_file))

    # 3. Render Template
    output_content = template.render(data)

    # 4. Write Output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"✅ Generated {output_file} from {data_file}")

if __name__ == "__main__":
    # Example usage for Fertilization unit
    generate_lesson(
        'Project-SCOPE/data/02_fertilization.yaml', 
        'lesson_template.j2', 
        'Project-SCOPE/units/02_reproduction.md'
    )

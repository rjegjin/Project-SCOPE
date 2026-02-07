import yaml
import json
from jinja2 import Environment, FileSystemLoader
import os

def generate_exam_html(data_file, template_file, output_file):
    # 1. Load Unit Data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 2. Get Quizzes (From data or from a global bank if preferred)
    # Here we take the quiz defined in the YAML for this unit
    quizzes = []
    if 'quiz' in data:
        # Wrap in a list if it's a single quiz
        quiz_data = data['quiz']
        if isinstance(quiz_data, dict):
            # We need to format it slightly for the template
            # (Finding answer text from the is_correct flag)
            answer_text = ""
            for choice in quiz_data.get('choices', []):
                if choice.get('is_correct'):
                    answer_text = choice['text']
            
            quizzes.append({
                "question": quiz_data['question'],
                "choices": quiz_data['choices'],
                "answer": answer_text
            })

    # 3. Setup Jinja2
    env = Environment(loader=FileSystemLoader('Project-SCOPE/templates'))
    template = env.get_template(os.path.basename(template_file))

    # 4. Render
    output_content = template.render(
        title=data['title'],
        subtitle=data['subtitle'],
        quizzes=quizzes
    )

    # 5. Save
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"✅ Exam sheet generated: {output_file}")

if __name__ == "__main__":
    generate_exam_html(
        'Project-SCOPE/data/02_fertilization.yaml',
        'exam_template.j2',
        'Project-SCOPE/output/02_fertilization_exam.html'
    )

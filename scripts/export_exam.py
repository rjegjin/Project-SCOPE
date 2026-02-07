import yaml
from jinja2 import Environment, FileSystemLoader
import os

def generate_exam_html(data_file, template_file, output_file):
    """
    YAML 데이터를 읽어 HTML 형식의 시험지를 생성합니다.
    """
    # 1. Load Unit Data
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading YAML {data_file}: {e}")
        return

    # 2. Get Quizzes
    quizzes = []
    if 'quiz' in data:
        quiz_data = data['quiz']
        # 단일 퀴즈도 리스트로 처리 (추후 확장 대비)
        if isinstance(quiz_data, dict):
            # 정답 텍스트 찾기
            answer_text = ""
            for choice in quiz_data.get('choices', []):
                if choice.get('is_correct'):
                    answer_text = choice['text']
            
            quizzes.append({
                "question": quiz_data.get('question', ''),
                "choices": quiz_data.get('choices', []),
                "answer": answer_text
            })
        elif isinstance(quiz_data, list):
             # 리스트 형태라면 그대로 처리 가능하도록 확장 (미래 대비)
             pass 

    # 3. Setup Jinja2
    template_dir = os.path.dirname(template_file)
    template_name = os.path.basename(template_file)
    
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    # 4. Render
    output_content = template.render(
        title=data.get('title', '제목 없음'),
        subtitle=data.get('subtitle', ''),
        quizzes=quizzes
    )

    # 5. Save
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"✅ Generated Exam: {os.path.basename(output_file)}")

if __name__ == "__main__":
    pass

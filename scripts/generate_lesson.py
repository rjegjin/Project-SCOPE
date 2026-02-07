import yaml
from jinja2 import Environment, FileSystemLoader
import os

def generate_lesson(data_file, template_file, output_file):
    """
    YAML 데이터를 읽어 Jinja2 템플릿을 통해 마크다운 슬라이드를 생성합니다.
    """
    # 1. Load Data
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading YAML {data_file}: {e}")
        return

    # 2. Setup Jinja2 Environment
    # template_file의 디렉토리를 템플릿 폴더로 설정
    template_dir = os.path.dirname(template_file)
    template_name = os.path.basename(template_file)
    
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    # 3. Render Template
    try:
        output_content = template.render(data)
    except Exception as e:
        print(f"❌ Error rendering template: {e}")
        return

    # 4. Write Output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"✅ Generated Slide: {os.path.basename(output_file)}")

if __name__ == "__main__":
    # 테스트용 (직접 실행 시)
    # 현재 스크립트 위치 기준으로 상위 폴더(프로젝트 루트) 추적
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    sample_data = os.path.join(project_root, 'data', '02_fertilization.yaml')
    sample_tpl = os.path.join(project_root, 'templates', 'lesson_template.j2')
    sample_out = os.path.join(project_root, 'units', '02_fertilization_test.md')
    
    if os.path.exists(sample_data):
        generate_lesson(sample_data, sample_tpl, sample_out)

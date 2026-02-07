import os
import glob
from generate_lesson import generate_lesson
from export_exam import generate_exam_html
from export_ppt import create_ppt_from_yaml

def build_all():
    data_dir = 'Project-SCOPE/data'
    output_dir = 'Project-SCOPE/output'
    units_dir = 'Project-SCOPE/units'
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(units_dir, exist_ok=True)
    
    yaml_files = glob.glob(os.path.join(data_dir, "*.yaml"))
    
    print(f"🚀 총 {len(yaml_files)}개의 단원 데이터를 발견했습니다. 빌드를 시작합니다.\n")
    
    for yaml_path in yaml_files:
        base_name = os.path.splitext(os.path.basename(yaml_path))[0]
        print(f"📦 [ {base_name} ] 처리 중...")
        
        # 1. Sli.dev Slide Generation
        md_output = os.path.join(units_dir, f"{base_name}.md")
        generate_lesson(yaml_path, 'lesson_template.j2', md_output)
        
        # 2. Exam Sheet (HTML/PDF) Generation
        exam_output = os.path.join(output_dir, f"{base_name}_exam.html")
        generate_exam_html(yaml_path, 'exam_template.j2', exam_output)
        
        # 3. PowerPoint (.pptx) Generation
        ppt_output = os.path.join(output_dir, f"{base_name}.pptx")
        create_ppt_from_yaml(yaml_path, ppt_output)
        
        print(f"   -> 완주 성공!\n")

    print("✨ 모든 빌드 작업이 완료되었습니다! 'output' 폴더와 'units' 폴더를 확인하세요.")

if __name__ == "__main__":
    build_all()

import os
import glob
import sys

# Add script directory to sys.path to allow imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from generate_lesson import generate_lesson
from export_exam import generate_exam_html
from export_ppt import create_ppt_from_yaml
# quiz_extractor는 필요 시 import

def build_all():
    # 1. Define Paths relative to Project Root
    project_root = os.path.dirname(current_dir)
    
    data_dir = os.path.join(project_root, 'data')
    output_dir = os.path.join(project_root, 'output')
    units_dir = os.path.join(project_root, 'units')
    templates_dir = os.path.join(project_root, 'templates')
    
    # Ensure directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(units_dir, exist_ok=True)
    
    # Template Paths
    slide_template = os.path.join(templates_dir, 'lesson_template.j2')
    exam_template = os.path.join(templates_dir, 'exam_template.j2')
    
    yaml_files = glob.glob(os.path.join(data_dir, "*.yaml"))
    
    print(f"🚀 S.C.O.P.E. Engine Started")
    print(f"📂 Project Root: {project_root}")
    print(f"📂 Found {len(yaml_files)} YAML data files.\n")
    
    for yaml_path in yaml_files:
        base_name = os.path.splitext(os.path.basename(yaml_path))[0]
        print(f"📦 Building Unit: [ {base_name} ]")
        
        # 1. Slide Generation (Markdown)
        md_output = os.path.join(units_dir, f"{base_name}.md")
        generate_lesson(yaml_path, slide_template, md_output)
        
        # 2. Exam Generation (HTML)
        exam_output = os.path.join(output_dir, f"{base_name}_exam.html")
        generate_exam_html(yaml_path, exam_template, exam_output)
        
        # 3. PPT Generation (PPTX)
        ppt_output = os.path.join(output_dir, f"{base_name}.pptx")
        create_ppt_from_yaml(yaml_path, ppt_output)
        
        print("-" * 40)

    print("\n✨ All builds completed successfully!")

if __name__ == "__main__":
    build_all()

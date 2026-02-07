import re
import json
import glob
import os

def extract_quizzes(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find quiz blocks: ::: quiz {metadata} ... :::
    quiz_pattern = re.compile(r':::\s*quiz\s*\{(.*?)\}\s*\n(.*?)\n:::', re.DOTALL)
    
    quizzes = []
    matches = quiz_pattern.findall(content)

    for metadata_str, body in matches:
        metadata = {}
        # Simple extraction for id, type, difficulty
        meta_parts = metadata_str.split(',')
        for part in meta_parts:
            if ':' in part:
                k, v = part.split(':', 1)
                metadata[k.strip()] = v.strip().strip('"').strip("'")

        lines = body.strip().split('\n')
        question = ""
        choices = []
        answer = None

        for line in lines:
            line = line.strip()
            if line.startswith('- ['): # Choice
                is_correct = 'x' in line[3:4].lower()
                choice_text = line[5:].strip()
                choices.append({
                    "text": choice_text,
                    "is_correct": is_correct
                })
                if is_correct:
                    answer = choice_text
            elif line: # Question
                question += line + " "

        quizzes.append({
            "id": metadata.get('id', 'unknown'),
            "type": metadata.get('type', 'unknown'),
            "difficulty": metadata.get('difficulty', 'unknown'),
            "question": question.strip(),
            "choices": choices,
            "answer": answer
        })

    return quizzes

def run_extraction(units_dir, output_file=None):
    if not os.path.exists(units_dir):
        print(f"❌ Units directory not found: {units_dir}")
        return

    md_files = glob.glob(os.path.join(units_dir, "*.md"))
    all_quizzes = []

    print(f"📂 Scanning '{os.path.basename(units_dir)}' directory... ({len(md_files)} files)")

    for md_path in md_files:
        try:
            quizzes = extract_quizzes(md_path)
            filename = os.path.basename(md_path)
            
            for q in quizzes:
                q['source_file'] = filename
                
            all_quizzes.extend(quizzes)
            # print(f"   - {filename}: {len(quizzes)} quizzes")
            
        except Exception as e:
            print(f"❌ Error in {filename}: {e}")

    print(f"✅ Total Quizzes Extracted: {len(all_quizzes)}")
    
    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_quizzes, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved to {os.path.basename(output_file)}")

if __name__ == "__main__":
    # Standalone execution relative to script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    units_path = os.path.join(project_root, "units")
    output_path = os.path.join(project_root, "output", "extracted_quiz_bank.json")
    
    run_extraction(units_path, output_path)

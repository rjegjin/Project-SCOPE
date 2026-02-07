import re
import json

def extract_quizzes(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find quiz blocks
    # ::: quiz {metadata} ... :::
    quiz_pattern = re.compile(r':::\s*quiz\s*\{(.*?)\}\s*\n(.*?)\n:::', re.DOTALL)
    
    quizzes = []
    matches = quiz_pattern.findall(content)

    for metadata_str, body in matches:
        # Parse metadata (simple key: value extraction)
        metadata = {}
        # Simple extraction for id, type, difficulty inside the curly braces
        meta_parts = metadata_str.split(',')
        for part in meta_parts:
            if ':' in part:
                k, v = part.split(':', 1)
                metadata[k.strip()] = v.strip().strip('"').strip("'")

        # Parse Question and Choices from body
        lines = body.strip().split('\n')
        question = ""
        choices = []
        answer = None

        for line in lines:
            line = line.strip()
            if line.startswith('- ['): # It's a choice
                is_correct = 'x' in line[3:4].lower()
                choice_text = line[5:].strip()
                choices.append({
                    "text": choice_text,
                    "is_correct": is_correct
                })
                if is_correct:
                    answer = choice_text
            elif line: # It's part of the question
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

if __name__ == "__main__":
    import glob
    import os

    units_dir = "Project-SCOPE/units"
    md_files = glob.glob(os.path.join(units_dir, "*.md"))
    
    all_quizzes = []

    print(f"📂 '{units_dir}' 폴더에서 {len(md_files)}개의 단원 파일을 찾았습니다.\n")

    for md_path in md_files:
        try:
            filename = os.path.basename(md_path)
            print(f"📄 처리 중: {filename}...")
            quizzes = extract_quizzes(md_path)
            
            # Add file source info to each quiz
            for q in quizzes:
                q['source_file'] = filename
                
            all_quizzes.extend(quizzes)
            print(f"   -> {len(quizzes)}개 문제 추출 완료.")
            
        except Exception as e:
            print(f"❌ 오류 발생 ({md_path}): {e}")

    print(f"\n✅ 총 {len(all_quizzes)}개의 문제를 추출했습니다.\n")
    
    for idx, q in enumerate(all_quizzes, 1):
        print(f"[문제 {idx}] (출처: {q['source_file']} / ID: {q['id']})")
        print(f"Q: {q['question']}")
        print(f"정답: {q['answer']}")
        print("-" * 30)
        
    # Save to JSON
    with open("Project-SCOPE/extracted_quiz_bank.json", "w", encoding="utf-8") as f:
        json.dump(all_quizzes, f, ensure_ascii=False, indent=2)

import os
import glob
import yaml
from bs4 import BeautifulSoup
import re

# 기존 레거시 프로젝트 경로
LEGACY_DIR = "2025-mid3-reproduction-heredity"
# YAML 저장 경로
DATA_DIR = "Project-SCOPE/data"

def clean_text(text):
    if not text: return ""
    return re.sub(r'\s+', ' ', text).strip()

def parse_html_to_yaml(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # 1. Title & Subtitle
    title_section = soup.find(id='title')
    title = "V. 생식과 유전" # Default
    subtitle = "단원명"
    
    if title_section:
        h2 = title_section.find('h2')
        p = title_section.find('p')
        if h2: 
            full_title = clean_text(h2.text)
            if ":" in full_title:
                title, subtitle = full_title.split(":", 1)
                title = title.strip()
                subtitle = subtitle.strip()
            else:
                subtitle = full_title
        if p:
            subtitle += f" - {clean_text(p.text)}"

    # 2. Objectives
    objectives = []
    obj_section = soup.find(id='objectives')
    if obj_section:
        for li in obj_section.find_all('li'):
            objectives.append(clean_text(li.text))

    # 3. Sections
    sections = []
    # Skip these structural/special sections in generic parsing
    skip_ids = ['title', 'objectives', 'intro-q', 'intro-activity', 'quiz', 'summary', 'next', 'modal-overlay']
    
    for section in soup.find_all('section'):
        sec_id = section.get('id')
        if not sec_id or sec_id in skip_ids:
            continue

        sec_data = {}
        
        # Section Title
        h2 = section.find('h2')
        if h2: sec_data['title'] = clean_text(h2.text)
        
        # Try to find content
        # Strategy: Look for grid columns first
        grid = section.find(class_='grid')
        if grid:
            columns = []
            cols = grid.find_all('div', recursive=False) # Direct children only usually
            if not cols: # maybe inside?
                cols = grid.find_all('div', class_=lambda x: x and ('bg-white' in x or 'p-4' in x))
            
            for col in cols:
                col_data = {}
                col_h3 = col.find('h3') or col.find('h4')
                if col_h3: col_data['title'] = clean_text(col_h3.text)
                
                col_img = col.find('img')
                if col_img: 
                    # Fix Image Path: images/foo.jpg -> /images/foo.jpg
                    src = col_img.get('src')
                    if src and not src.startswith('/'):
                        src = '/' + src
                    col_data['image'] = src
                
                col_p = col.find('p')
                if col_p: col_data['text'] = clean_text(col_p.text)
                
                col_ul = col.find('ul')
                if col_ul:
                    col_data['list'] = [clean_text(li.text) for li in col_ul.find_all('li')]
                
                if col_data:
                    columns.append(col_data)
            
            if columns:
                sec_data['columns'] = columns
        
        # If no columns, look for direct content
        if 'columns' not in sec_data:
            # Just grab text content and images
            content_html = ""
            for child in section.children:
                if child.name in ['div', 'p', 'ul', 'img']:
                    # Simple cleaning of src
                    if child.name == 'img':
                        src = child.get('src')
                        if src and not src.startswith('/'):
                            child['src'] = '/' + src
                    content_html += str(child)
            
            if content_html:
                sec_data['content'] = clean_text(BeautifulSoup(content_html, 'html.parser').text[:300]) # Fallback summary
                # Real implementation: We might want to keep some HTML or structured text
                # For this MVP, let's keep it simple.
        
        sections.append(sec_data)

    # 4. Summary
    summary = []
    sum_section = soup.find(id='summary')
    if sum_section:
        for li in sum_section.find_all('li'):
            summary.append(clean_text(li.text))

    # 5. Quiz (Simple extraction of first quiz found)
    quiz_data = None
    quiz_section = soup.find(id='quiz')
    if quiz_section:
        # Try to find question text
        q_text_el = quiz_section.find(class_=lambda x: x and ('text-xl' in x or 'font-bold' in x))
        q_text = clean_text(q_text_el.text) if q_text_el else "퀴즈 문제"
        
        choices = []
        # Find buttons or list items
        options = quiz_section.find_all('button', class_='quiz-option')
        correct_answer = "알 수 없음" # Logic often hidden in JS, difficult to parse without executing JS
        
        # Heuristic: Try to find data-answer attribute
        for opt in options:
            choices.append({
                "text": clean_text(opt.text),
                "is_correct": False # Default
            })
            
        quiz_data = {
            "id": f"{os.path.splitext(os.path.basename(html_path))[0]}-q1",
            "type": "multiple-choice",
            "difficulty": "mid",
            "question": q_text,
            "choices": choices
        }

    # Construct YAML structure
    yaml_structure = {
        "title": title,
        "subtitle": subtitle,
        "theme_color": "emerald", # Default
        "objectives": objectives,
        "sections": sections,
        "summary": summary
    }
    
    if quiz_data:
        yaml_structure['quiz'] = quiz_data

    return yaml_structure

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    html_files = glob.glob(os.path.join(LEGACY_DIR, "*.html"))
    print(f"🚀 Found {len(html_files)} legacy HTML files.")
    
    for html_file in html_files:
        filename = os.path.basename(html_file)
        if filename in ['index.html', 'hidden_further_study.html']: continue # Skip hubs
        
        print(f"📦 Converting {filename}...")
        try:
            data = parse_html_to_yaml(html_file)
            
            yaml_filename = filename.replace('.html', '.yaml')
            # Add prefix to sort them nicely if needed, or keep original name
            output_path = os.path.join(DATA_DIR, yaml_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, allow_unicode=True, sort_keys=False, indent=2)
                
            print(f"   -> Saved to {output_path}")
            
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")

if __name__ == "__main__":
    main()

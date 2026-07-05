import os, hashlib, re, glob

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wiki_dir = os.path.join(repo_root, 'wiki', 'sources')

count = 0
for f in glob.glob(os.path.join(wiki_dir, '*.md')):
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    match = re.search(r'raw_sha256:\s*["\']?([a-f0-9]{64})["\']?', content)
    file_match = re.search(r'raw_file:\s*["\']?(.+?)["\']?(?:\n|$)', content)
    
    if not match or not file_match:
        continue
    
    old_hash = match.group(1)
    raw_path = os.path.normpath(file_match.group(1).strip())
    raw_full = os.path.join(repo_root, raw_path)
    
    if not os.path.exists(raw_full):
        print(f"Missing: {raw_path}")
        continue
    
    with open(raw_full, 'rb') as rf:
        actual_hash = hashlib.sha256(rf.read()).hexdigest()
    
    if actual_hash != old_hash:
        new_content = content.replace(old_hash, actual_hash)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        count += 1
        print(f"Fixed: {os.path.basename(f)}")

print(f"Done. Fixed {count} files.")

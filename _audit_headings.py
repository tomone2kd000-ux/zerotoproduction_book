import glob
import os
import re

root = r'E:\sach\zerotoproduction'
raw_dir = os.path.join(root, 'extracted_epub')
docs_dir = os.path.join(root, 'content', 'docs')
folders = {
    1: 'mo-dau', 2: 'mo-dau', 3: 'mo-dau',
    4: 'chuong-01-getting-started', 5: 'chuong-02-building-an-email-newsletter',
    6: 'chuong-03-sign-up-a-new-subscriber', 7: 'chuong-04-telemetry',
    8: 'chuong-05-going-live', 9: 'chuong-06-reject-invalid-subscribers-1',
    10: 'chuong-07-reject-invalid-subscribers-2', 11: 'chuong-08-error-handling',
    12: 'chuong-09-naive-newsletter-delivery', 13: 'chuong-10-securing-our-api',
    14: 'chuong-11-fault-tolerant-workflows',
}

for number, folder in folders.items():
    source_path = os.path.join(raw_dir, f'ch{number:03}.md')
    if not os.path.isfile(source_path):
        continue
    source = open(source_path, encoding='utf-8').read()
    target_files = glob.glob(os.path.join(docs_dir, folder, '*.mdx'))
    target = '\n'.join(open(path, encoding='utf-8').read() for path in target_files)
    sections = []
    for match in re.finditer(r'^#{2,4}\s+<span class="header-section-number">([\d.]+)</span>', source, re.M):
        section = match.group(1).rstrip('.')
        if section not in sections:
            sections.append(section)
    missing = [section for section in sections if not re.search(r'(?<![\d.])' + re.escape(section) + r'(?![\d.])', target)]
    print(f'ch{number:03} {folder}: source numbered sections={len(sections)}, missing number mentions={missing}')

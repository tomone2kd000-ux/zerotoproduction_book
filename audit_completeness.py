import os
import glob

raw_dir = r'E:\sach\zerotoproduction\extracted_epub'
docs_dir = r'E:\sach\zerotoproduction\content\docs'

mapping = [
    ('ch001-003', ['ch001.md', 'ch002.md', 'ch003.md'], 'mo-dau'),
    ('ch004', ['ch004.md'], 'chuong-01-getting-started'),
    ('ch005', ['ch005.md'], 'chuong-02-building-an-email-newsletter'),
    ('ch006', ['ch006.md'], 'chuong-03-sign-up-a-new-subscriber'),
    ('ch007', ['ch007.md'], 'chuong-04-telemetry'),
    ('ch008', ['ch008.md'], 'chuong-05-going-live'),
    ('ch009', ['ch009.md'], 'chuong-06-reject-invalid-subscribers-1'),
    ('ch010', ['ch010.md'], 'chuong-07-reject-invalid-subscribers-2'),
    ('ch011', ['ch011.md'], 'chuong-08-error-handling'),
    ('ch012', ['ch012.md'], 'chuong-09-naive-newsletter-delivery'),
    ('ch013', ['ch013.md'], 'chuong-10-securing-our-api'),
    ('ch014', ['ch014.md'], 'chuong-11-fault-tolerant-workflows'),
]

header = f"{'Folder':<42} | {'Raw Words':<10} | {'Trans Words':<12} | {'Files':<6} | {'Ratio':<8}"
print(header)
print('-' * len(header))

total_raw = 0
total_trans = 0

for label, raw_files, folder in mapping:
    raw_words = 0
    for rf in raw_files:
        fpath = os.path.join(raw_dir, rf)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                raw_words += len(f.read().split())
                
    folder_path = os.path.join(docs_dir, folder)
    trans_words = 0
    mdx_count = 0
    if os.path.exists(folder_path):
        mfiles = glob.glob(os.path.join(folder_path, '*.mdx'))
        mdx_count = len(mfiles)
        for mf in mfiles:
            with open(mf, 'r', encoding='utf-8') as f:
                trans_words += len(f.read().split())
                
    total_raw += raw_words
    total_trans += trans_words
    ratio = (trans_words / raw_words * 100) if raw_words > 0 else 0
    print(f"{folder:<42} | {raw_words:<10} | {trans_words:<12} | {mdx_count:<6} | {ratio:.1f}%")

print('-' * len(header))
overall_ratio = (total_trans / total_raw * 100) if total_raw > 0 else 0
print(f"{'TOTAL':<42} | {total_raw:<10} | {total_trans:<12} | {55:<6} | {overall_ratio:.1f}%")

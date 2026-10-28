import os
import glob

docs_dir = r'E:\sach\zerotoproduction\content\docs'
folders = sorted([d for d in os.listdir(docs_dir) if os.path.isdir(os.path.join(docs_dir, d))])

print(f"Total Chapter Folders: {len(folders)}")
total_files = 0

for f in folders:
    fpath = os.path.join(docs_dir, f)
    mdxs = sorted(glob.glob(os.path.join(fpath, '*.mdx')))
    total_files += len(mdxs)
    print(f"\n📁 {f} ({len(mdxs)} files):")
    for m in mdxs:
        title = "No Title"
        with open(m, 'r', encoding='utf-8') as fp:
            for line in fp:
                if line.startswith('title:'):
                    title = line.replace('title:', '').strip().strip('"').strip("'")
                    break
        print(f"   - {os.path.basename(m)}: {title}")

print(f"\nTotal MDX Files: {total_files}")

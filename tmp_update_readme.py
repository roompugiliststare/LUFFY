import re
from pathlib import Path

p = Path('README.md')
lines = p.read_text(encoding='utf-8').splitlines()
title_idx = next(i for i, x in enumerate(lines) if 'Complete TODO List' in x)
contrib_idx = next(i for i, x in enumerate(lines) if i > title_idx and x.startswith('## ') and 'Contributing' in x)

TARGETS = {'luffy/deepscaler/utils.py', 'luffy/verl/verl/protocol.py'}
NEW = [
('luffy/deepscaler/utils.py',45,'Add logging for API calls and errors'),
('luffy/deepscaler/utils.py',46,'Support batch processing for multiple prompts'),
('luffy/deepscaler/utils.py',47,'Add timeout configuration for API calls'),
('luffy/deepscaler/utils.py',107,'Implement Vertex AI initialization and authentication'),
('luffy/deepscaler/utils.py',108,'Configure safety settings for content generation'),
('luffy/deepscaler/utils.py',109,'Set up GenerativeModel with proper system instructions'),
('luffy/deepscaler/utils.py',110,'Implement retry logic with exponential backoff'),
('luffy/deepscaler/utils.py',111,'Add comprehensive error handling for API access issues'),
('luffy/deepscaler/utils.py',112,'Handle rate limiting and quota management'),
('luffy/deepscaler/utils.py',113,'Implement response validation and text extraction'),
('luffy/deepscaler/utils.py',114,'Add support for different generation configurations'),
('luffy/verl/verl/protocol.py',114,'Optimize memory usage during tensor reshaping'),
('luffy/verl/verl/protocol.py',115,'Add support for different tensor types and shapes'),
('luffy/verl/verl/protocol.py',136,'Optimize tensor view operations for performance'),
('luffy/verl/verl/protocol.py',137,'Add error handling for invalid batch dimensions'),
('luffy/verl/verl/protocol.py',169,'(zhangchi.usc1992) add consistency check'),
('luffy/verl/verl/protocol.py',265,'we can actually lift this restriction if needed'),
('luffy/verl/verl/protocol.py',351,'(zhangchi.usc1992) whether to copy'),
]
rx = re.compile(r'^- \[ \] \*\*(.+?):(\d+)\*\* - (.*)$')
entries=[]
for line in lines[title_idx+1:contrib_idx]:
    m=rx.match(line)
    if not m: continue
    path, no, msg = m.group(1), int(m.group(2)), m.group(3)
    if path not in TARGETS:
        entries.append((path,no,msg))
entries.extend(NEW)
entries.sort(key=lambda x:(x[0],x[1]))
assert len(entries)>100, len(entries)
out = ['### 📝 Complete TODO List','']
for path,no,msg in entries:
    out.append(f'- [ ] **{path}:{no}** - {msg}')
out.extend(['',''])
before='\n'.join(lines[:title_idx]).rstrip()+'\n\n'
tail='\n'.join(lines[contrib_idx:]).rstrip()+'\n'
p.write_text(before+'\n'.join(out)+'\n'+tail, encoding='utf-8')
print(len(entries))

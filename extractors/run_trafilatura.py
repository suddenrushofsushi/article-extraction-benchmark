#!/usr/bin/env python3
import gzip
import json
from pathlib import Path

import trafilatura


def main():
    output = {}
    for path in Path('html').glob('*.html.gz'):
        with gzip.open(path, 'rt', encoding='utf8') as f:
            html = f.read()
        item_id = path.stem.split('.')[0]
        content = trafilatura.extract(html,
            no_fallback=True,
            include_comments=False,
            include_tables=True,
            favor_recall=True,
            include_formatting=False
        )
        output[item_id] = {'articleBody': trafilatura.extract(html, include_comments=False)}
    (Path('output') / 'trafilatura.json').write_text(
        json.dumps(output, sort_keys=True, ensure_ascii=False, indent=4),
        encoding='utf8')


if __name__ == '__main__':
    main()

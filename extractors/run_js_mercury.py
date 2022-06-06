#!/usr/bin/env python3
import gzip
import json
import os
import subprocess
import time
from pathlib import Path
from tempfile import mkstemp


# built executable file
CLI_PATH = Path('node extractors/js_mercury/index.js')


def main():
    gt = json.load(open('ground-truth.json'))
    output = {}
    for path in Path('html').glob('*.html.gz'):
        with gzip.open(path, 'rt', encoding='utf8') as f:
            html = f.read()
        item_id = path.stem.split('.')[0]
        url = gt[item_id]["url"]

        # save html to temp file
        temp_filepath = f"/tmp/{item_id}_html"
        with open(temp_filepath, 'wt') as fw:
            fw.write(html)

        time.sleep(0.25)
        command_str = f"{CLI_PATH} {url} {temp_filepath}"
        print(command_str)

        # get extracted content from mercury-parser
        result = subprocess.run(command_str, stdout=subprocess.PIPE, shell=True)

        # destroy temp file
        # os.remove(temp_filepath)

        # parse result
        decoded = str(result.stdout)

        output[item_id] = {'articleBody': decoded}
        (Path('output') / 'js_mercury.json').write_text(
            json.dumps(output, sort_keys=True, ensure_ascii=False, indent=4),
            encoding='utf8')


if __name__ == '__main__':
    main()

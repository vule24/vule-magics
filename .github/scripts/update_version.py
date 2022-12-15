import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='UPDATE VERSION')
parser.add_argument('--version', type=str, default='0.0.1')
args = parser.parse_args()
args.version = str(args.version.split('/')[-1])
print('__VERSION__: {}'.format(args.version))

(Path(__file__).parent / "__VERSION__").write_text(str(args.version))

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PATH = {
	'output' : BASE_DIR/'frontend'/'static'/'output',
	'src_data' : BASE_DIR/'backend'/'data'
} 
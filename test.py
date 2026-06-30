from backend.config.config import PATH
from backend.src.backtest import backtest

path = PATH['gold']

def main():
	backtest(path)
	
main()
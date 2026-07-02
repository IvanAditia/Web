from dataclasses import dataclass

@dataclass
class backtest_param:
	lot : float
	risk_percent : float
	contract_size : int
	initial_balance : float
	leverage : int
	fee_perlot : int
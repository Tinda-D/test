import pyupbit

access = "8Rd0urwoJbsLGfoVy8Rie6x3NLJznitB2TKSDifG"          # 본인 값으로 변경
secret = "luhb6LykVI1W56QV7LhdUM7X0cEPUwEUeHIR5QwC"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

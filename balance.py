import pyupbit

access = "CH1zcN42WbxIgtEs1kPPPLcAAHR64WCl1J9cjGwr"          # 본인 값으로 변경
secret = "xROzT6fwijueKLyLMfx66mclDj7Vl30sZUWjF3Yp"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

import time
import pyupbit
import datetime
import telegram
import asyncio

access = "8Rd0urwoJbsLGfoVy8Rie6x3NLJznitB2TKSDifG"
secret = "luhb6LykVI1W56QV7LhdUM7X0cEPUwEUeHIR5QwC"
#secret = "xROzT6fwijueKLyLMfx66mclDj7Vl30sZUWjF3Yp" 23년도 시크릿

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("Autotrade start")
# Telegram 메세지 코드 시작
async def startmsg(): #실행시킬 함수명 임의지정==매수 메세지
    token = '5300696373:AAHeDrkyBmg1F15XmfhJnTHSeSVgwPWd6qo'
    bot = telegram.Bot(token = token)
    await bot.send_message(5015949114,'Autotrade start')
    
asyncio.run(startmsg())   
# Telegram 메세지 코드 끝

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC") #9:00
        end_time = start_time + datetime.timedelta(days=1) #9:00 +1일
        
        # 9:00 < 현재 < # 8:59:50

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 1.3)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    # Telegram 메세지 코드 시작
                    async def bmsg(): #실행시킬 함수명 임의지정==매수 메세지
                        token = '5300696373:AAHeDrkyBmg1F15XmfhJnTHSeSVgwPWd6qo'
                        bot = telegram.Bot(token = token)
                        await bot.send_message(5015949114,'자동매수 시작')
    
                    asyncio.run(bmsg())   
                    # Telegram 메세지 코드 끝
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
                # Telegram 메세지 코드 시작
                async def smsg(): #실행시킬 함수명 임의지정==매도 메세지
                    token = '5300696373:AAHeDrkyBmg1F15XmfhJnTHSeSVgwPWd6qo'
                    bot = telegram.Bot(token = token)
                    await bot.send_message(5015949114,'자동매도 종료')
                
                asyncio.run(smsg())   
                # Telegram 메세지 코드 끝 
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

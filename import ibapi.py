import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time


#Class for interactive brokers connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        # Listen For Realtime bars
    def realtimeBar(self, reqId, time, open_, high, low, close, volume, wap, count):
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e :
            print(e)
    def error(self, id, errorCode, errorString):
        print(errorCode, errorString)


# Bot Logic
class Bot:
    ib = None
    id = 1

    def __init__(self):
        # Connect TO IB on Init
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7497,1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()            
        time.sleep(1)
        # Get Symbol Info
        symbol = input("enter the symbol you want to trade : ")
        # Create our IB Contract Objective
        contract = Contract()
        # Contract= Aktien hier gemeint als Vertrag
        # --> hier wird definiert was bei Der Aktie angezeigt werden soll
        contract.symbol = symbol.upper()
        contract.secType = "STK"
        contract.exchange = "Smart"
        contract.currency = "USD"
        # Request Market Data
        self.ib.reqRealTimeBars(0, contract, 5, "Trades", True, [])
        # To Do Submit Order --> hier wird defineirt welcher ordertyp
        # und ob kauf verkauf
        # Create Order Object
        order = Order()
        order.ordertype = "MKT" # or LMT ETC...
        order.action = "BUY" # or SELL ETC...
        quantity = 100
        order.totalQuantity = quantity
        # Create Contract Object
        # contract = Contract()
        # contract.symbol = symbol
        # contract.secType = "STK" # or FUT ETC
        contract.primaryExchange = "ISLAND"
        # contract.currency = "USD"
        # Place the Order
        self.ib.placeOrder(self.id, contract, order)
        self.id += 1

    # Listen to socket in seperate thread kp ?
    def run_loop(self):
        self.ib.run()

    # Pass realtime bar data back to our bot object
    def on_bar_update(self, reqID, time, open_, high, low, close, volume,
                      wap, count):
        print(close)


# Start Bot
bot = Bot()







#     def check_momentum(self, reqId):
#         if len(self.data[reqId]) >= self.momentum_window:
#             momentum = (self.last_price[reqId] - self.data[reqId][-self.momentum_window])/self.momentum_window
#             if momentum > 0 and not self.order_placed:
#                 self.place_order()

#     def place_order(self):
#         contract = Contract()
#         contract.symbol = self.symbol
#         contract.secType = "STK"
#         contract.currency = "USD"
#         contract.exchange = "SMART"
#         self.buy_price = self.last_price[reqId]
#         self.order_id = self.nextOrderId
#         self.placeOrder(self.order_id, contract, OrderSamples.LimitOrder("BUY", 100, self.buy_price))
#         self.order_placed = True

#     def run(self):
#         self.connect("127.0.0.1", 7497, 1)
#         contract = Contract()
#         contract.symbol = self.symbol
#         contract.secType = "STK"
#         contract.currency = "USD"
#         contract.exchange = "SMART"
#         self.data[reqId] = []
#         self.reqMarketDataType(MarketDataTypeEnum.DELAYED)
#         self.reqMktData(reqId, contract, "", False, False, [])
#         self.run()
        


# if __name__ == "__main__":
#     app = IBApp()
#     app.run()

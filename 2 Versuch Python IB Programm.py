#Imports
import ibapi 
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from ibapi.order import *
#Vars

#Class for Interactive Brokers Connection
class IBapi(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)

#Bot # Logic
class Bot:
    ib = None
    def __init__(self):
        #Conncect to IB on init
        ib = IBapi()
        ib.connect("127.0.0.1", 7496,1)   #7496 für Paperaccount 7497 für echte account
        ib.run()
        self.data = {}
        self.last_price = {}
        self.order_id = None
        self.symbol = "AAPL"
        self.momentum_window = 20
        self.buy_price = None
        self.order_placed = False


    # def tickPrice(self, reqId, tickType, price, attrib):
    #     if tickType == TickTypeEnum.LAST:
    #         self.last_price[reqId] = price
    #         self.check_momentum(reqId)

    # def check_momentum(self, reqId):
    #     if len(self.data[reqId]) >= self.momentum_window:
    #         momentum = (self.last_price[reqId] - self.data[reqId][-self.momentum_window])/self.momentum_window
    #         if momentum > 0 and not self.order_placed:
    #             self.place_order(reqId)
                
    # def place_order(self, reqId):
    #     contract = Contract()
    #     contract.symbol = self.symbol
    #     contract.secType = "STK"
    #     contract.currency = "USD"
    #     contract.exchange = "SMART"
    #     self.buy_price = self.last_price[reqId]
    #     self.order_id = self.nextOrderId
    #     self.placeOrder(self.order_id, contract, OrderSamples.LimitOrder("BUY", 100, self.buy_price))
    #     self.order_placed = True

    # def run(self):
    #     self.connect("127.0.0.1", 7497, 0)
    #     contract = Contract()
    #     contract.symbol = self.symbol
    #     contract.secType = "STK"
    #     contract.currency = "USD"
    #     contract.exchange = "SMART"
    #     self.data[reqId] = []
    #     self.reqMarketDataType(MarketDataTypeEnum.DELAYED)
    #     self.reqMktData(reqId, contract, "", False, False, [])
    #     self.run()

#Start Bot
bot = Bot()
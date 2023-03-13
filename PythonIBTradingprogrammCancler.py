###############################################################################
# IMPORTS

import ibapi
from ibapi.order import Order
from ibapi.ticktype import TickType
from ibapi.common import TickerId, TickAttrib
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

###############################################################################


class IBapi(EClient, EWrapper):

    # ----------------------------------------------------

    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
        self.last_price = {}
        self.order_id = None
        self.symbol = "AAPL"
        self.momentum_window = 20
        self.buy_price = None
        self.order_placed = False

    # ----------------------------------------------------

    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float,
                  attrib: TickAttrib):
        if tickType == TickTypeEnum.LAST:
            self.last_price[reqId] = price
            self.data[reqId] = []
            self.check_momentum(reqId)

    # ----------------------------------------------------

    def check_momentum(self, req_id: int):
        
        if len(self.data[req_id]) >= self.momentum_window:
            momentum = (self.last_price[req_id]
                        - self.data[req_id][-self.momentum_window]) \
                       / self.momentum_window

            if momentum > 0 and not self.order_placed:
                self.place_order(req_id)

    # ----------------------------------------------------

    def place_order(self, req_id: int):
        contract = Contract()
        contract.symbol = "STK"
        contract.currency = "USD"
        contract.exchange = "SMART"
        
        print(req_id)
        
        # self.buy_price = self.last_price[req_id]
        # self.order_id = self.nextOrderId
        # self.placeOrder(
        #     self.order_id, 
        #     contract, 
        #     OrderSamples.Limitorder("BUY", 100, self.buy_price)
        # )
        # self.order_placed = True

    # ----------------------------------------------------

    def run(self):
        print("test")
        self.connect("127.0.0.1", 7497, 1)
        self.place_order(1)
###############################################################################


if __name__ == '__main__':
    app = IBapi()
    app.run()

###############################################################################
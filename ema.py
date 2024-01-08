import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display
import pandas as pd

mt5.initialize("...") #your terminal address like C:\\Program Files\\Alpari MT5\\terminal64.exe
mt5.initialize(login=..., server="...",password="...")  #enter your login information
symbols=mt5.symbols_get()

def ema(symbolnumber,timef,candlenumber,movingnumber) :
    symboldigit = symbols[symbolnumber].digits
    rates2 = mt5.copy_rates_from_pos(symbols[symbolnumber].name, timef, candlenumber, movingnumber*5)
    rates_frame = pd.DataFrame(rates2)
    EMA = round(rates_frame['close'][0:movingnumber*5+1].ewm(span = movingnumber ,adjust=False ).mean(),symboldigit+1)[5*movingnumber-1]
    return EMA


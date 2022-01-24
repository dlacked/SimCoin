import time
import os
import random

os.system("title Codename_Warren")
DASHMoney = 150000
LTCMoney = 94000
ETCMoney = 13000
BTCMoney = 12000000
ETHMoney = 300000
QTUMMoney = 3300
XRPMoney = 300
XMRMoney = 100000
BCHMoney = 560000
i = 0
RDASH = RLTC = RETC = RBCH = RQTUM = RXMR = RXRP = RBTC = RETH = 3
while (True):
    os.system("cls")
    print("Codename_Warren [v 0.0.0]")
    print("This program just simulate virtual currency virtually.")
    print("======================================================")

    #StockMoney = format(StockMoney, ',')
    #DASHMoney = format(DASHMoney, ',')
    #LTCMoney = format(LTCMoney, ',')
    #ETCMoney = format(ETCMoney, ',')
    #BTCMoney = format(BTCMoney, ',')
    #ETHMoney = format(ETHMoney, ',')
    #QTUMMoney = format(QTUMMoney, ',')
    #XRPMoney = format(XRPMoney, ',')
    #XMRMoney = format(XMRMoney, ',')
    #BCHMoney = format(BCHMoney, ',')

    #print("Your holding assets are " + str(StockMoney) + "(KRW).")
    print(str(i+1) + " Refreshed")
    print("Refresh after 10s\n")
    
    print("Dash(DASH) : " + str(DASHMoney) + "(KRW)", end="    ")
    if RDASH == 0:
        print("▲")
    elif RDASH == 1:
        print("▼")
    else:
        print("")
        
    print("Litecoin(LTC) : " + str(LTCMoney) + "(KRW)", end="    ")
    if RLTC == 0:
        print("▲")
    elif RLTC == 1:
        print("▼")
    else:
        print("")
    print("Ethereum Classic(ETC) : " + str(ETCMoney) + "(KRW)", end="    ")
    if RETC == 0:
        print("▲")
    elif RETC == 1:
        print("▼")
    else:
        print("")
    print("Bitcoin Cash(BCH) : " + str(BCHMoney) + "(KRW)", end="    ")
    if RBCH == 0:
        print("▲")
    elif RBCH == 1:
        print("▼")
    else:
        print("")
    print("Quantum (QTUM) : " + str(QTUMMoney) + "(KRW)", end="    ")
    if RQTUM == 0:
        print("▲")
    elif RQTUM == 1:
        print("▼")
    else:
        print("")
    print("Monero (XMR) : " + str(XMRMoney) + "(KRW)", end="    ")
    if RXMR == 0:
        print("▲")
    elif RXMR == 1:
        print("▼")
    else:
        print("")
    print("Ripple (XRP) : " + str(XRPMoney) + "(KRW)", end="    ")
    if RXRP == 0:
        print("▲")
    elif RXRP == 1:
        print("▼")
    else:
        print("")
    print("Bitcoin (BTC) : " + str(BTCMoney) + "(KRW)", end="    ")
    if RBTC == 0:
        print("▲")
    elif RBTC == 1:
        print("▼")
    else:
        print("")
    print("Etherium (ETH) : " + str(ETHMoney) + "(KRW)", end="    ")
    if RETH == 0:
        print("▲")
    elif RETH == 1:
        print("▼")
    else:
        print("")
    time.sleep(10)
    

    RDASH = random.randrange(0,2)
    RLTC = random.randrange(0,2)
    RETC = random.randrange(0,2)
    RBTC = random.randrange(0,2)
    RETH = random.randrange(0,2)
    RQTUM = random.randrange(0,2)
    RXRP = random.randrange(0,2)
    RXMR = random.randrange(0,2)
    RBCH = random.randrange(0,2)
    
    #기존 시세에 랜덤 값을 더하거나 뺌
    if RDASH == 0:
        DASHMoney += random.randrange(1, DASHMoney)
    else:
        DASHMoney -= random.randrange(1, DASHMoney)

    if RLTC == 0:
        LTCMoney += random.randrange(1, LTCMoney)
    else:
        LTCMoney -= random.randrange(1, LTCMoney)

    if RETC == 0:
        ETCMoney += random.randrange(1, ETCMoney)
    else:
        ETCMoney -= random.randrange(1, ETCMoney)

    if RBCH == 0:
        BCHMoney += random.randrange(1, BCHMoney)
    else:
        BCHMoney -= random.randrange(1, BCHMoney)

    if RQTUM == 0:
        QTUMMoney += random.randrange(1, QTUMMoney)
    else:
        QTUMMoney -= random.randrange(1, QTUMMoney)

    if RXMR == 0:
        XMRMoney += random.randrange(1, XMRMoney)
    else:
        XMRMoney -= random.randrange(1, XMRMoney)

    if RXRP == 0:
        XRPMoney += random.randrange(1, XRPMoney)
    else:
        XRPMoney -= random.randrange(1, XRPMoney)

    if RBTC == 0:
        BTCMoney += random.randrange(1, BTCMoney)
    else:
        BTCMoney -= random.randrange(1, BTCMoney)

    if RETH == 0:
        ETHMoney += random.randrange(1, ETHMoney)
    else:
        ETHMoney -= random.randrange(1, ETHMoney)
    i += 1

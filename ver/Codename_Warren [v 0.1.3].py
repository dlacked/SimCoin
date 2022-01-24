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
FEMIMoney = 5

i = 0
RDASH = RLTC = RETC = RBCH = RQTUM = RXMR = RXRP = RBTC = RETH = RFEMI = 2
while (True):
    os.system("cls")
    print("Codename_Warren [v 0.1.3]")
    print("This program just simulate virtual currency virtually.")
    print("======================================================")

    #StockMoney = format(StockMoney, ',')
    StrDASHMoney = format(DASHMoney, ',')
    StrLTCMoney = format(LTCMoney, ',')
    StrETCMoney = format(ETCMoney, ',')
    StrBTCMoney = format(BTCMoney, ',')
    StrETHMoney = format(ETHMoney, ',')
    StrQTUMMoney = format(QTUMMoney, ',')
    StrXRPMoney = format(XRPMoney, ',')
    StrXMRMoney = format(XMRMoney, ',')
    StrBCHMoney = format(BCHMoney, ',')
    StrFEMIMoney = format(FEMIMoney, ',')

    #print("Your holding assets are " + str(StockMoney) + "(KRW).")
    print(str(i) + " Refreshed")
    print("Refresh after 10s\n")
    
    print("  Dash(DASH)             |  " + StrDASHMoney + "(KRW)", end="  ")
    if RDASH == 0:
        print("▲")
    elif RDASH == 1:
        print("▼")
    else:
        print("")
        
    print("  Litecoin(LTC)          |  " + StrLTCMoney + "(KRW)", end="  ")
    if RLTC == 0:
        print("▲")
    elif RLTC == 1:
        print("▼")
    else:
        print("")
    print("  Ethereum Classic(ETC)  |  " + StrETCMoney + "(KRW)", end="  ")
    if RETC == 0:
        print("▲")
    elif RETC == 1:
        print("▼")
    else:
        print("")
    print("  Bitcoin Cash(BCH)      |  " + StrBCHMoney + "(KRW)", end="  ")
    if RBCH == 0:
        print("▲")
    elif RBCH == 1:
        print("▼")
    else:
        print("")
    print("  Quantum (QTUM)         |  " + StrQTUMMoney + "(KRW)", end="  ")
    if RQTUM == 0:
        print("▲")
    elif RQTUM == 1:
        print("▼")
    else:
        print("")
    print("  Monero (XMR)           |  " + StrXMRMoney + "(KRW)", end="  ")
    if RXMR == 0:
        print("▲")
    elif RXMR == 1:
        print("▼")
    else:
        print("")
    print("  Ripple (XRP)           |  " + StrXRPMoney + "(KRW)", end="  ")
    if RXRP == 0:
        print("▲")
    elif RXRP == 1:
        print("▼")
    else:
        print("")
    print("  Bitcoin (BTC)          |  " + StrBTCMoney + "(KRW)", end="  ")
    if RBTC == 0:
        print("▲")
    elif RBTC == 1:
        print("▼")
    else:
        print("")
    print("  Etherium (ETH)         |  " + StrETHMoney + "(KRW)", end="  ")
    if RETH == 0:
        print("▲")
    elif RETH == 1:
        print("▼")
    else:
        print("")
    print("  Femicoin (FEMI)        |  " + StrFEMIMoney + "(KRW)", end="  ")
    if RFEMI == 0:
        print("▲")
    elif RFEMI == 1:
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
    RFEMI = random.randrange(0,2)
    
    #기존 시세에 랜덤 값을 더하거나 뺌
    if RDASH == 0:
        if DASHMoney < 150000/20:
            DASHMoney += random.randrange(1, (150000/20)*4)
        else:
            DASHMoney += random.randrange(0, DASHMoney*2)
    else:
        DASHMoney -= random.randrange(0, int(DASHMoney/2))

    if RLTC == 0:
        if LTCMoney < 94000/20:
            LTCMoney += random.randrange(0, (94000/20)*4) 
        else:
            LTCMoney += random.randrange(0, LTCMoney*2)
    else:
        LTCMoney -= random.randrange(0, int(LTCMoney/2))

    if RETC == 0:
        if ETCMoney < 13000/20:
            ETCMoney += random.randrange(0, (13000/20)*4)
        else:
            ETCMoney += random.randrange(0, ETCMoney*2)
    else:
        ETCMoney -= random.randrange(0, int(ETCMoney/2))

    if RBCH == 0:
        if BCHMoney < 560000/20:
            ETCMoney += random.randrange(0, (560000/20)*4)
        else:
            BCHMoney += random.randrange(0, BCHMoney*2)
    else:
        BCHMoney -= random.randrange(0, int(BCHMoney/2))

    if RQTUM == 0:
        if QTUMMoney < 3300/20:
            QTUMMoney += random.randrange(0, (3300/20)*4)
        else:
            QTUMMoney += random.randrange(0, QTUMMoney*2)
    else:
        QTUMMoney -= random.randrange(0, int(QTUMMoney/2))

    if RXMR == 0:
        if XMRMoney < 100000/20:
            XMRMoney += random.randrange(0, (100000/20)*4)
        else:
            XMRMoney += random.randrange(0, XMRMoney*2)
    else:
        XMRMoney -= random.randrange(0, int(XMRMoney/2))

    if RXRP == 0:
        if XRPMoney < 300/20:
            XRPMoney += random.randrange(0, (300/20)*4)
        else:
            XRPMoney += random.randrange(0, XRPMoney*2)
    else:
        XRPMoney -= random.randrange(0, int(XRPMoney/2))

    if RBTC == 0:
        if BTCMoney < 120000000/20:
            BTCMoney += random.randrange(0, (120000000/20)*4)
        else:
            BTCMoney += random.randrange(0, BTCMoney*2)
    else:
        BTCMoney -= random.randrange(0, int(BTCMoney/2))

    if RETH == 0:
        if ETHMoney < 300000/20:
            ETHMoney += random.randrange(0, (300000/20)*4)
        ETHMoney += random.randrange(0, ETHMoney*2)
    else:
        ETHMoney -= random.randrange(0, int(ETHMoney/2))
        
    if RFEMI == 0:
        if FEMIMoney < 5/20:
            FEMIMoney += random.randrange(0, (5/20)*4)
        FEMIMoney += random.randrange(0, FEMIMoney*2)
    else:
        FEMIMoney -= random.randrange(0, int(FEMIMoney/2))
    i += 1

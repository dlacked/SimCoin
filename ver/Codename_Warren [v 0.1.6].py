import time
import os
import random

os.system("title Codename_Warren")

#시작 자산/시세 설정
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

#프로그램 메인 (Part 2)
while (True):
    os.system("cls")
    print("Codename_Warren [v 0.1.6]")
    print("이 프로그램은 가상 화폐의 시스템을 모방한 프로그램입니다.")
    print("=========================================================")

    #천 단위 ',' 구분 위한 문자열 변경
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

    #현재 자산/시세 표시
    print(str(i) + " Refreshed")
    print("5s 후 새로고침합니다.\n")
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
    time.sleep(5)

    #증감을 표시하기 위한 랜덤 값
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
    
    if RDASH == 0:
        if DASHMoney < 150000/20:
            DASHMoney += random.randrange(1, DASHMoney*10)
        else:
            DASHMoney += random.randrange(0, DASHMoney)
    else:
        DASHMoney -= random.randrange(0, int(DASHMoney))

    if RLTC == 0:
        if LTCMoney < 94000/20:
            LTCMoney += random.randrange(0, LTCMoney*10) 
        else:
            LTCMoney += random.randrange(0, LTCMoney)
    else:
        LTCMoney -= random.randrange(0, int(LTCMoney))

    if RETC == 0:
        if ETCMoney < 13000/20:
            ETCMoney += random.randrange(0, ETCMoney*10)
        else:
            ETCMoney += random.randrange(0, ETCMoney)
    else:
        ETCMoney -= random.randrange(0, int(ETCMoney))

    if RBCH == 0:
        if BCHMoney < 560000/20:
            BCHMoney += random.randrange(0, BCHMoney*10)
        else:
            BCHMoney += random.randrange(0, BCHMoney)
    else:
        BCHMoney -= random.randrange(0, int(BCHMoney))

    if RQTUM == 0:
        if QTUMMoney < 3300/20:
            QTUMMoney += random.randrange(0, QTUMMoney*10)
        else:
            QTUMMoney += random.randrange(0, QTUMMoney)
    else:
        QTUMMoney -= random.randrange(0, int(QTUMMoney))

    if RXMR == 0:
        if XMRMoney < 100000/20:
            XMRMoney += random.randrange(0, XMRMoney*10)
        else:
            XMRMoney += random.randrange(0, XMRMoney)
    else:
        XMRMoney -= random.randrange(0, int(XMRMoney))

    if RXRP == 0:
        if XRPMoney < 300/20:
            XRPMoney += random.randrange(0, XRPMoney*10)
        else:
            XRPMoney += random.randrange(0, XRPMoney)
    else:
        XRPMoney -= random.randrange(0, int(XRPMoney))

    if RBTC == 0:
        if BTCMoney < 120000000/20:
            BTCMoney += random.randrange(0, BTCMoney*10)
        else:
            BTCMoney += random.randrange(0, BTCMoney)
    else:
        BTCMoney -= random.randrange(0, int(BTCMoney))

    if RETH == 0:
        if ETHMoney < 300000/20:
            ETHMoney += random.randrange(0, ETHMoney*10)
        ETHMoney += random.randrange(0, ETHMoney)
    else:
        ETHMoney -= random.randrange(0, int(ETHMoney))
        
    if RFEMI == 0:
        if FEMIMoney <= 1:
            FEMIMoney += random.randrange(0, 10)
        FEMIMoney += random.randrange(0, FEMIMoney)
    else:
        FEMIMoney -= random.randrange(0, int(FEMIMoney))
    i += 1

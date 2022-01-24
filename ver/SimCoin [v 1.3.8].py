import time
import os
import random

#화면 셋팅
os.system("title SimCoin")
#os.system("mode con cols=65 lines=60")
os.system("cls")

#시작 자산/시세 설정
MyMoney = 10000000
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

DASHData = [0]
LTCData = [0]
ETCData = [0]
BTCData = [0]
ETHData = [0]
QTUMData = [0]
XRPData = [0]
XMRData = [0]
BCHData = [0]
FEMIData = [0]

i = 0
j = 0

RTime = 0
RDASH = RLTC = RETC = RBCH = RQTUM = RXMR = RXRP = RBTC = RETH = RFEMI = 2

#프로그램 설명(Part 1)
print("SimCoin [v 1.3.8]")
print("이 프로그램은 가상 화폐의 시스템을 모방한 프로그램입니다.")
print("=========================================================")
print("[프로그램 설명]")
print("● 먼저 기본 자산 10,000,000(KRW)가 주어지며, 가상 화폐를")
print("   구매/판매하면서 자산을 불려나가는 것을 목표로 하는 프로그램입니다.")
print("   가상 화폐로 억만장자가 되어보세요!")
print("\n[주의 사항]")
print("● 이 프로그램은 실제 가상 화폐를 거래하는 프로그램이 아닙니다.")
print("● 가상 화폐 거래를 원할 시, 원하시는 거래 수량을 입력해주시고,")
print("   띄어쓰기 한 칸을 하신 후 거래를 원하시는 코인을 입력해주십시오.")
print("   ex)2 BTC")
print("\n본문을 다 읽으셨으면, 아무 키를 눌러 실행하십시오.")
os.system("pause >nul")

#프로그램 메인 (Part 2)
while (True):
    os.system("cls")

    print("SimCoin [v 1.3.8]")
    print("이 프로그램은 가상 화폐의 시스템을 모방한 프로그램입니다.")
    print("=========================================================")

    #천 단위 ',' 구분 위한 문자열 변경
    StrMyMoney = format(MyMoney, ',')
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

    #시세 갱신 시간 랜덤 설정
    RTime = random.randrange(3, 5)

    #현재 자산/시세 표시
    print("보유 자산 : " + StrMyMoney + " (KRW)")
    print(str(i) + " Refreshed\n")   
    print("  Dash (DASH)             |  " + StrDASHMoney + " (KRW)   ", DASHData[0], end="    ")
    if RDASH == 0:
        print("▲\n")
    elif RDASH == 1:
        print("▼\n")
    else:
        print("\n")
        
    print("  Litecoin (LTC)          |  " + StrLTCMoney + " (KRW)   ", LTCData[0], end="    ")
    if RLTC == 0:
        print("▲\n")
    elif RLTC == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Ethereum Classic (ETC)  |  " + StrETCMoney + " (KRW)   ", ETCData[0], end="    ")
    if RETC == 0:
        print("▲\n")
    elif RETC == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Bitcoin Cash (BCH)      |  " + StrBCHMoney + " (KRW)   ", BCHData[0], end="    ")
    if RBCH == 0:
        print("▲\n")
    elif RBCH == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Quantum (QTUM)          |  " + StrQTUMMoney + " (KRW)   ", QTUMData[0], end="    ") 
    if RQTUM == 0:
        print("▲\n")
    elif RQTUM == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Monero (XMR)            |  " + StrXMRMoney + " (KRW)   ", XMRData[0], end="    ")
    if RXMR == 0:
        print("▲\n")
    elif RXMR == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Ripple (XRP)            |  " + StrXRPMoney + " (KRW)   ", XRPData[0], end="    ") 
    if RXRP == 0:
        print("▲\n")
    elif RXRP == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Bitcoin (BTC)           |  " + StrBTCMoney + " (KRW)   ", BTCData[0], end="    ") 
    if RBTC == 0:
        print("▲\n")
    elif RBTC == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Etherium (ETH)          |  " + StrETHMoney + " (KRW)   ", ETHData[0], end="    ") 
    if RETH == 0:
        print("▲\n")
    elif RETH == 1:
        print("▼\n")
    else:
        print("\n")
    print("  Femicoin (FEMI)         |  " + StrFEMIMoney + " (KRW)   ", FEMIData[0], end="    ") 
    if RFEMI == 0:
        print("▲\n")
    elif RFEMI == 1:
        print("▼\n")
    else:
        print("\n")

    #선택
    while (True):
        print("1) 구매")
        print("2) 판매")
        print("Any Key) 다음 턴")
        Num = input(">>> ")
        
        #구매
        if Num == "1":
            while (True):
                Amount, Initial = input("\n구매할 수량과 구매할 화폐를 입력하십시오.\n>>> ").split()
                if Initial == "DASH":
                    if MyMoney < DASHMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (DASHMoney * int(Amount))
                        DASHData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                elif Initial == "LTC":
                    if MyMoney < LTCMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (LTCMoney * int(Amount))
                        LTCData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "ETC":
                    if MyMoney < ETCMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (ETCMoney * int(Amount))
                        ETCData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "BTC":
                    if MyMoney < BTCMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (BTCMoney * int(Amount))
                        BTCData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "ETH":
                    if MyMoney < ETHMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (ETHMoney * int(Amount))
                        ETHData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "QTUM":
                    if MyMoney < QTUMMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (QTUMMoney * int(Amount))
                        QTUMData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "XRP":
                    if MyMoney < XRPMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (XRPMoney * int(Amount))
                        XRPData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                elif Initial == "XMR":
                    if MyMoney < XMRMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (XMRMoney * int(Amount))
                        XMRData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break

                elif Initial == "BCH":
                    if MyMoney < BCHMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (BCHMoney * int(Amount))
                        BCHData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break

                elif Initial == "FEMI":
                    if MyMoney < FEMIMoney * int(Amount):
                        print("\n자산이 부족합니다.\n")
                    else:
                        MyMoney -= (FEMIMoney * int(Amount))
                        FEMIData[0] += int(Amount)
                        StrMyMoney = format(MyMoney, ',')
                        print("\n구매 완료.")
                        print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                        break
                    
                else:
                    print("\n잘 못 입력하셨습니다.\n")
                    
        #판매
        elif Num == "2":
            if i == 0:
                print("\n 0 턴에서는 판매할 수 없습니다.\n")
            else:
                while (True):
                    Amount, Initial = input("\n판매할 수량과 판매할 화폐를 입력하십시오.\n>>> ").split()
                    if Initial == "DASH":
                        if DASHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            DASHData[0] -= int(Amount)
                            MyMoney += DASHMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "LTC":
                        if LTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            LTCData[0] -= int(Amount)
                            MyMoney += LTCMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "ETC":
                        if ETCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            ETCData[0] -= int(Amount)
                            MyMoney += ETCMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "BTC":
                        if BTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            BTCData[0] -= int(Amount)
                            MyMoney += BTCMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "BTC":
                        if BTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            BTCData[0] -= int(Amount)
                            MyMoney += BTCMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "ETH":
                        if ETHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            ETHData[0] -= int(Amount)
                            MyMoney += ETHMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "QTUM":
                        if QTUMData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            QTUMData[0] -= int(Amount)
                            MyMoney += QTUMMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break

                    elif Initial == "XRP":
                        if XRPData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            XRPData[0] -= int(Amount)
                            MyMoney += XRPMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break
                        
                    elif Initial == "XMR":
                        if XMRData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            XMRData[0] -= int(Amount)
                            MyMoney += XMRMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break
                        
                    elif Initial == "BCH":
                        if BCHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            BCHData[0] -= int(Amount)
                            MyMoney += BCHMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break
                        
                    elif Initial == "FEMI":
                        if FEMIData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않으셨습니다.\n")
                        else:
                            FEMIData[0] -= int(Amount)
                            MyMoney += FEMIMoney * int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n판매 완료."); print("변경된 보유 자산 :", StrMyMoney, "(KRW)\n")
                            break
                        
                    else:
                        print("\n잘 못 입력하셨습니다.\n")
                        
        #다음 턴
        else:
            print("\n시세 갱신 대기 중...")
            time.sleep(RTime)
            break

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

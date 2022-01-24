import time
import os
import random

#버전 설정
Ver = "1.11.20"
SC = "SimCoin"

#화면 셋팅
os.system("title " + SC)
os.system("mode con cols=85 lines=1000")
os.system("cls")

#기본 설정
DASHData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LTCData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ETCData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BTCData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ETHData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
QTUMData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XRPData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XMRData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BCHData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
FEMIData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

MyMoney = 10000000
DASHMoney = DASHData[1] = 150000
LTCMoney = LTCData[1] = 94000
ETCMoney = ETCData[1] = 13000
BTCMoney = BTCData[1] = 12000000
ETHMoney = ETHData[1] = 300000
QTUMMoney = QTUMData[1] = 3300
XRPMoney = XRPData[1] = 300
XMRMoney = XMRData[1] = 100000
BCHMoney = BCHData[1] = 560000
FEMIMoney = FEMIData[1] = 5

i = 0
j = 0
k = 0

RTime = 0
RDASH = RLTC = RETC = RBCH = RQTUM = RXMR = RXRP = RBTC = RETH = RFEMI = 2

#글꼴 설정

class text:
    Green = '\033[92m'
    Red = '\033[91m'
    Bold = '\033[1m'
    End = '\033[0m'
    Yellow = '\033[93m'
    Gray = '\033[37m'
    DarkCyan = '\033[36m'
    DarkGray = '\033[90m'
    
#프로그램 설명(Part 1)
print(SC, "[v " + Ver + "]")
print("이 프로그램은 실제 가상 화폐를 거래하는 프로그램이 아닙니다.")
print("============================================================")
print("[게임 설명]\n")
print("● 천만원으로 가상 화폐를 구매/판매하면서 자산을 불려나가는 게임입니다.")
print("   10턴 안에 만수르를 뛰어넘는 억만장자가 되어보십시오.")
print("\n\n[입력법]\n")
print("● 가상 화폐를 구매/판매하고 싶다면, 수량과 화폐를")
print("   다음과 같은 형식으로 명령어를 입력하십시오.")
print(text.Green + "   [수량] [화폐 이니셜]" + text.End)
print("   ex) 1 BTC\n")
print("● 최종 보유 자산은 마지막 턴 시세를 기준으로 마지막 턴까지")
print("   판매하지 않은 화폐들을 포함하여 합산합니다.\n")
print("● 가상 화폐 구매/판매를 중지하고 싶다면 다음 명령어를 입력하십시오.")
print(text.Green + "   0 /esc\n\n" + text.End)
print("※ 다음 본문은 게임 최초 실행시에만 보여집니다.\n")
print("※ 입력법을 어길 시 치명적 오류로 강제종료 될 수 있습니다.\n\n")
print("본문을 다 읽었다면, 아무 키를 눌러 실행하십시오.")
os.system("pause >nul")

#프로그램 메인 (Part 2)
for i in range(0, 11):
    os.system("cls")

    print(SC, "[v " + Ver + "]")
    print("이 프로그램은 실제 가상 화폐를 거래하는 프로그램이 아닙니다.")
    print("============================================================")

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
    StrDASHData = format(DASHData[0], ',')
    StrLTCData = format(LTCData[0], ',')
    StrETCData = format(ETCData[0], ',')
    StrBTCData = format(BTCData[0], ',')
    StrETHData = format(ETHData[0], ',')
    StrQTUMData = format(QTUMData[0], ',')
    StrXRPData = format(XRPData[0], ',')
    StrXMRData = format(XMRData[0], ',')
    StrBCHData = format(BCHData[0], ',')
    StrFEMIData = format(FEMIData[0], ',')

    #시세 갱신 시간 랜덤 설정
    RTime = random.randrange(1, 3)

    #현재 자산 표시
    print("보유 자산 : " + StrMyMoney + "\\", end=" ")
    if i == 10:
        print("(마지막 턴)\n")
    else:
        print("(" + str(i) + "턴)\n")

    #현재 턴의 화폐 시세, 증감율, 보유 수 표시
    print("  Dash (DASH)             |  " + StrDASHMoney + "\\    ", end="")
    if RDASH == 0:
        if ((DASHData[i+1]-DASHData[i])/DASHData[i])*100 == 0:
            print("(-)    " + StrDASHData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((DASHData[i+1]-DASHData[i])/DASHData[i])*100) + "% ▲)    " + text.End + StrDASHData + "\n")
    elif RDASH == 1:
        if ((DASHData[i+1]-DASHData[i])/DASHData[i])*100 == 0:
            print("(-)    " + StrDASHData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((DASHData[i+1]-DASHData[i])/DASHData[i])*-100) + "% ▼)    " + text.End + StrDASHData + "\n")
    else:
        print(StrDASHData + "\n")
        
    print("  Litecoin (LTC)          |  " + StrLTCMoney + "\\    ", end="")
    if RLTC == 0:
        if ((LTCData[i+1]-LTCData[i])/LTCData[i])*100 == 0:
            print("(-)    " + StrLTCData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((LTCData[i+1]-LTCData[i])/LTCData[i])*100) + "% ▲)    " + text.End + StrLTCData + "\n")
    elif RLTC == 1:
        if ((LTCData[i+1]-LTCData[i])/LTCData[i])*100 == 0:
            print("(-)    " + StrLTCData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((LTCData[i+1]-LTCData[i])/LTCData[i])*-100) + "% ▼)    " + text.End + StrLTCData + "\n")
    else:
        print(StrLTCData + "\n")
        
    print("  Ethereum Classic (ETC)  |  " + StrETCMoney + "\\    ", end="")
    if RETC == 0:
        if ((ETCData[i+1]-ETCData[i])/ETCData[i])*100 == 0:
            print("(-)    " + StrETCData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((ETCData[i+1]-ETCData[i])/ETCData[i])*100) + "% ▲)    " + text.End + StrETCData + "\n")
    elif RETC == 1:
        if ((ETCData[i+1]-ETCData[i])/ETCData[i])*100 == 0:
            print("(-)    " + StrETCData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((ETCData[i+1]-ETCData[i])/ETCData[i])*-100) + "% ▼)    " + text.End + StrETCData + "\n")
    else:
        print(StrETCData + "\n")
        
    print("  Bitcoin Cash (BCH)      |  " + StrBCHMoney + "\\    ", end="")
    if RBCH == 0:
        if ((BCHData[i+1]-BCHData[i])/BCHData[i])*100 == 0:
            print("(-)    " + StrBCHData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((BCHData[i+1]-BCHData[i])/BCHData[i])*100) + "% ▲)    " + text.End + StrBCHData + "\n")
    elif RBCH == 1:
        if ((BCHData[i+1]-BCHData[i])/BCHData[i])*100 == 0:
            print("(-)    " + StrBCHData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((BCHData[i+1]-BCHData[i])/BCHData[i])*-100) + "% ▼)    " + text.End + StrBCHData + "\n")
    else:
        print(StrBCHData + "\n")
        
    print("  Quantum (QTUM)          |  " + StrQTUMMoney + "\\    ", end="") 
    if RQTUM == 0:
        if ((QTUMData[i+1]-QTUMData[i])/QTUMData[i])*100 == 0:
            print("(-)    " + StrQTUMData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((QTUMData[i+1]-QTUMData[i])/QTUMData[i])*100) + "% ▲)    " + text.End + StrQTUMData + "\n")
    elif RQTUM == 1:
        if ((QTUMData[i+1]-QTUMData[i])/QTUMData[i])*100 == 0:
            print("(-)    " + StrQTUMData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((QTUMData[i+1]-QTUMData[i])/QTUMData[i])*-100) + "% ▼)    " + text.End + StrQTUMData + "\n")
    else:
        print(StrQTUMData + "\n")
        
    print("  Monero (XMR)            |  " + StrXMRMoney + "\\    ", end="")
    if RXMR == 0:
        if ((XMRData[i+1]-XMRData[i])/XMRData[i])*100 == 0:
            print("(-)    " + StrXMRData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((XMRData[i+1]-XMRData[i])/XMRData[i])*100) + "% ▲)    " + text.End + StrXMRData + "\n")
    elif RXMR == 1:
        if ((XMRData[i+1]-XMRData[i])/XMRData[i])*100 == 0:
            print("(-)    " + StrXMRData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((XMRData[i+1]-XMRData[i])/XMRData[i])*-100) + "% ▼)    " + text.End + StrXMRData + "\n")
    else:
        print(StrXMRData + "\n")
        
    print("  Ripple (XRP)            |  " + StrXRPMoney + "\\    ", end="") 
    if RXRP == 0:
        if ((XRPData[i+1]-XRPData[i])/XRPData[i])*100 == 0:
            print("(-)    " + StrXRPData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((XRPData[i+1]-XRPData[i])/XRPData[i])*100) + "% ▲)    " + text.End + StrXRPData + "\n")
    elif RXRP == 1:
        if ((XRPData[i+1]-XRPData[i])/XRPData[i])*100 == 0:
            print("(-)    " + StrXRPData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((XRPData[i+1]-XRPData[i])/XRPData[i])*-100) + "% ▼)    " + text.End + StrXRPData + "\n")
    else:
        print(StrXRPData + "\n")
        
    print("  Bitcoin (BTC)           |  " + StrBTCMoney + "\\    ", end="") 
    if RBTC == 0:
        if ((BTCData[i+1]-BTCData[i])/BTCData[i])*100 == 0:
            print("(-)    " + StrBTCData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((BTCData[i+1]-BTCData[i])/BTCData[i])*100) + "% ▲)    " + text.End + StrBTCData + "\n")
    elif RBTC == 1:
        if ((BTCData[i+1]-BTCData[i])/BTCData[i])*100 == 0:
            print("(-)    " + StrBTCData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((BTCData[i+1]-BTCData[i])/BTCData[i])*-100) + "% ▼)    " + text.End + StrBTCData + "\n")
    else:
        print(StrBTCData + "\n")
        
    print("  Etherium (ETH)          |  " + StrETHMoney + "\\    ", end="") 
    if RETH == 0:
        if ((ETHData[i+1]-ETHData[i])/ETHData[i])*100 == 0:
            print("(-)    " + StrETHData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((ETHData[i+1]-ETHData[i])/ETHData[i])*100) + "% ▲)    " + text.End + StrETHData + "\n")
    elif RETH == 1:
        if ((ETHData[i+1]-ETHData[i])/ETHData[i])*100 == 0:
            print("(-)    " + StrETHData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((ETHData[i+1]-ETHData[i])/ETHData[i])*-100) + "% ▼)    " + text.End + StrETHData + "\n")
    else:
        print(StrETHData + "\n")
        
    print("  Femicoin (FEMI)         |  " + StrFEMIMoney + "\\    ", end="") 
    if RFEMI == 0:
        if ((FEMIData[i+1]-FEMIData[i])/FEMIData[i])*100 == 0:
            print("(-)    " + StrFEMIData)
        else:
            print(text.Green + "(" + '%.2f' % float(((FEMIData[i+1]-FEMIData[i])/FEMIData[i])*100) + "% ▲)    " + text.End + StrFEMIData + "\n")
    elif RFEMI == 1:
        if ((FEMIData[i+1]-FEMIData[i])/FEMIData[i])*100 == 0:
            print("(-)    " + StrFEMIData)
        else:
            print(text.Red + "(" + '%.2f' % float(((FEMIData[i+1]-FEMIData[i])/FEMIData[i])*-100) + "% ▼)    " + text.End + StrFEMIData + "\n")
    else:
        print(StrFEMIData)

    #선택
    while (True):
        print("\n1) 구매")
        print("2) 판매")
        print("Any Key) 다음 턴")
        Num = input(">>> ")
        
        #구매
        if Num == "1":
            while (True):
                Amount, Initial = input("\n구매할 수량과 화폐를 입력법에 따라 입력하십시오.\n>>> ").split()

                if Initial == "DASH":
                    if MyMoney < DASHMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / DASHData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (DASHMoney * int(Amount))
                                DASHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (DASHMoney * int(Amount))
                            DASHData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                        
                elif Initial == "LTC":
                    if MyMoney < LTCMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / LTCData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (LTCMoney * int(Amount))
                                LTCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (LTCMoney * int(Amount))
                            LTCData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                
                elif Initial == "ETC":
                    if MyMoney < ETCMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / ETCData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (ETCMoney * int(Amount))
                                ETCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (ETCMoney * int(Amount))
                            ETCData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                        
                elif Initial == "BTC":
                    if MyMoney < BTCMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / BTCData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (BTCMoney * int(Amount))
                                BTCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (BTCMoney * int(Amount))
                            BTCData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                    
                elif Initial == "ETH":
                    if MyMoney < ETHMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / ETHData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (ETHMoney * int(Amount))
                                ETHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (ETHMoney * int(Amount))
                            ETHData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                        
                elif Initial == "QTUM":
                    if MyMoney < QTUMMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / QTUMData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (QTUMMoney * int(Amount))
                                QTUMData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (QTUMMoney * int(Amount))
                            QTUMData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                    
                elif Initial == "XRP":
                    if MyMoney < XRPMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / XRPData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (XRPMoney * int(Amount))
                                XRPData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                        else:
                            MyMoney -= (XRPMoney * int(Amount))
                            XRPData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                    
                elif Initial == "XMR":
                    if MyMoney < XMRMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / BTCData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (XMRMoney * int(Amount))
                                XMRData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (XMRMoney * int(Amount))
                            XMRData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break

                elif Initial == "BCH":
                    if MyMoney < BCHMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / BCHData[i+1]
                            if Amount < 1:
                                ("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (BCHMoney * int(Amount))
                                BCHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (BCHMoney * int(Amount))
                            BCHData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break

                elif Initial == "FEMI":
                    if MyMoney < FEMIMoney * int(Amount):
                        print("\n자산이 부족합니다.")
                    else:
                        if int(Amount) < 0:
                            print("\n음수는 입력할 수 없습니다.")
                        elif int(Amount) == 0:
                            Amount = MyMoney / FEMIData[i+1]
                            if Amount < 1:
                                print("\n자산이 부족합니다.")
                            else:
                                MyMoney -= (FEMIMoney * int(Amount))
                                FEMIData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        else:
                            MyMoney -= (FEMIMoney * int(Amount))
                            FEMIData[0] += int(Amount)
                            StrMyMoney = format(MyMoney, ',')
                            print("\n" + str(int(Amount)), str(Initial) + " 구매 완료.")
                            print("변경된 보유 자산 :", StrMyMoney + "\\")
                            break
                elif Initial == "/esc" and Amount == "0":
                    break
                else:
                    print("\n없는 화폐입니다.")
            else:
                print("\n자산이 부족합니다.")
                    
        #판매
        elif Num == "2":
            if i == 0:
                print("\n0턴에서는 판매할 수 없습니다.")
            else:
                while (True):
                    Amount, Initial = input("\n판매할 수량과 화폐를 입력법에 따라 입력하십시오.\n>>> ").split()

                    if Initial == "DASH":
                        if DASHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if DASHData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = DASHData[0]
                                    DASHData[0] = 0
                                    MyMoney += (DASHMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                DASHData[0] -= int(Amount)
                                MyMoney += DASHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "LTC":
                        if LTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                if LTCData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = LTCData[0]
                                    LTCData[0] = 0
                                    MyMoney += (LTCMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                LTCData[0] -= int(Amount)
                                MyMoney += LTCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ETC":
                        if ETCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if ETCData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = ETCData[0]
                                    ETCData[0] = 0
                                    MyMoney += (ETCMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                ETCData[0] -= int(Amount)
                                MyMoney += ETCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "BTC":
                        if BTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if BTCData[0] - 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = BTCData[0]
                                    BTCData[0] = 0
                                    MyMoney += (BTCMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BTCData[0] -= int(Amount)
                                MyMoney += BTCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ETH":
                        if ETHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if ETHData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = ETHData[0]
                                    ETHData[0] = 0
                                    MyMoney += (ETHMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                ETHData[0] -= int(Amount)
                                MyMoney += ETHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "QTUM":
                        if QTUMData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if QTUMData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = QTUMData[0]
                                    QTUMData[0] = 0
                                    MyMoney += (QTUMMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                QTUMData[0] -= int(Amount)
                                MyMoney += QTUMMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
    
                    elif Initial == "XRP":
                        if XRPData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if DASHData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = XRPData[0]
                                    XRPData[0] = 0
                                    MyMoney += (XRPMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                XRPData[0] -= int(Amount)
                                MyMoney += XRPMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "XMR":
                        if XMRData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = XMRData[0]
                                XMRData[0] = 0
                                MyMoney += (XMRMoney * int(Amount))
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            else:
                                XMRData[0] -= int(Amount)
                                MyMoney += XMRMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "BCH":
                        if BCHData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if BCHData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = BCHData[0]
                                    BCHData[0] = 0
                                    MyMoney += (BCHMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BCHData[0] -= int(Amount)
                                MyMoney += BCHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "FEMI":
                        if FEMIData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if FEMIData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = FEMIData[0]
                                    FEMIData[0] = 0
                                    MyMoney += (FEMIMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                FEMIData[0] -= int(Amount)
                                MyMoney += FEMIMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                print("\n" + str(int(Amount)), str(Initial) + " 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                    elif Initial == "/esc" and Amount == "0":
                        break    
                    else:
                        print("\n없는 화폐입니다.")
                        
        #다음 턴 / 종료
        else:
            if i < 10:
                os.system("cls")
                print(SC, "[v " + Ver + "]")
                print("이 프로그램은 실제 가상 화폐를 거래하는 프로그램이 아닙니다.")
                print("============================================================")
                print("보유 자산 : " + StrMyMoney + "\\", end=" ")
                if i+1 == 10:
                    print("(마지막 턴)\n")
                else:
                    print("(" + str(i+1) + "턴)\n")
                print("시세 갱신 중...")
                time.sleep(RTime)
                break
            else:
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
            DASHMoney += random.randrange(0, DASHMoney*10)
            DASHData[i+2] = DASHMoney
        else:
            DASHMoney += random.randrange(0, DASHMoney)
            DASHData[i+2] = DASHMoney
    else:
        DASHMoney -= random.randrange(0, DASHMoney)
        DASHData[i+2] = DASHMoney

    if RLTC == 0:
        if LTCMoney < 94000/20:
            LTCMoney += random.randrange(0, LTCMoney*10)
            LTCData[i+2] = LTCMoney
        else:
            LTCMoney += random.randrange(0, LTCMoney)
            LTCData[i+2] = LTCMoney
    else:
        LTCMoney -= random.randrange(0, LTCMoney)
        LTCData[i+2] = LTCMoney

    if RETC == 0:
        if ETCMoney < 13000/20:
            ETCMoney += random.randrange(0, ETCMoney*10)
            ETCData[i+2] = ETCMoney
        else:
            ETCMoney += random.randrange(0, ETCMoney)
            ETCData[i+2] = ETCMoney
    else:
        ETCMoney -= random.randrange(0, ETCMoney)
        ETCData[i+2] = ETCMoney

    if RBCH == 0:
        if BCHMoney < 560000/20:
            BCHMoney += random.randrange(0, BCHMoney*10)
            BCHData[i+2] = BCHMoney
        else:
            BCHMoney += random.randrange(0, BCHMoney)
            BCHData[i+2] = BCHMoney
    else:
        BCHMoney -= random.randrange(0, BCHMoney)
        BCHData[i+2] = BCHMoney

    if RQTUM == 0:
        if QTUMMoney < 3300/20:
            QTUMMoney += random.randrange(0, QTUMMoney*10)
            QTUMData[i+2] = QTUMMoney
        else:
            QTUMMoney += random.randrange(0, QTUMMoney)
            QTUMData[i+2] = QTUMMoney
    else:
        QTUMMoney -= random.randrange(0, QTUMMoney)
        QTUMData[i+2] = QTUMMoney

    if RXMR == 0:
        if XMRMoney < 100000/20:
            XMRMoney += random.randrange(0, XMRMoney*10)
            XMRData[i+2] = XMRMoney
        else:
            XMRMoney += random.randrange(0, XMRMoney)
            XMRData[i+2] = XMRMoney
    else:
        XMRMoney -= random.randrange(0, XMRMoney)
        XMRData[i+2] = XMRMoney

    if RXRP == 0:
        if XRPMoney < 300/20:
            XRPMoney += random.randrange(0, XRPMoney*10)
            XRPData[i+2] = XRPMoney
        else:
            XRPMoney += random.randrange(0, XRPMoney)
            XRPData[i+2] = XRPMoney
    else:
        XRPMoney -= random.randrange(0, XRPMoney)
        XRPData[i+2] = XRPMoney

    if RBTC == 0:
        if BTCMoney < 120000000/20:
            BTCMoney += random.randrange(0, BTCMoney*10)
            BTCData[i+2] = BTCMoney
        else:
            BTCMoney += random.randrange(0, BTCMoney)
            BTCData[i+2] = BTCMoney
    else:
        BTCMoney -= random.randrange(0, BTCMoney)
        BTCData[i+2] = BTCMoney

    if RETH == 0:
        if ETHMoney < 300000/20:
            ETHMoney += random.randrange(0, ETHMoney*10)
            ETHData[i+2] = ETHMoney
        else:
            ETHMoney += random.randrange(0, ETHMoney)
            ETHData[i+2] = ETHMoney
    else:
        ETHMoney -= random.randrange(0, ETHMoney)
        ETHData[i+2] = ETHMoney
        
    if RFEMI == 0:
        if FEMIMoney <= 1:
            FEMIMoney += random.randrange(0, 10)
            FEMIData[i+2] = FEMIMoney
        else:
            FEMIMoney += random.randrange(0, FEMIMoney)
            FEMIData[i+2] = FEMIMoney
    else:
        FEMIMoney -= random.randrange(0, FEMIMoney)
        FEMIData[i+2] = FEMIMoney

#게임 결과 (Part 3)
os.system("cls")
MyMoney += (FEMIData[11] * FEMIData[0]) + (QTUMData[11] * QTUMData[0]) + (DASHData[11] * DASHData[0]) + (LTCData[11] * LTCData[0]) + (ETCData[11] * ETCData[0]) + (BCHData[11] * BCHData[0]) + (XMRData[11] * XMRData[0]) + (XRPData[11] * XRPData[0]) + (BTCData[11] * BTCData[0]) + (ETHData[11] * ETHData[0])
StrMyMoney = format(MyMoney, ',')
print(SC, "[v " + Ver + "]")
print("이 프로그램은 실제 가상 화폐를 거래하는 프로그램이 아닙니다.")
print("============================================================")
print("게임 종료.\n")
print("최종 보유 자산 :", StrMyMoney + "\\", end=" ")

if (MyMoney-10000000)/100000 < 0:
    print("(기존 금액보다 " + text.Red + '%.2f' % float((MyMoney-10000000)/-100000) + "% ▼" + text.End + ")")
elif (MyMoney-10000000)/100000 > 0:
    print("(기존 금액보다 " + text.Green + '%.2f' % float((MyMoney-10000000)/100000) + "% ▲" + text.End + ")")
else:
    print("")

if (MyMoney < 500000):
    print(text.DarkCyan + "9등급" + text.End)
elif (MyMoney < 1000000):
    print(text.DarkCyan + "8등급" + text.End)
elif (MyMoney < 5000000):
    print(text.DarkCyan + "7등급" + text.End)
elif (MyMoney < 10000000):
    print(text.DarkCyan + "6등급" + text.End)
elif (MyMoney == 10000000):
    print(text.DarkCyan + "5등급" + text.End)
elif (MyMoney < 50000000):
    print(text.DarkCyan + "4등급" + text.End)
elif (MyMoney < 100000000):
    print(text.DarkGray + "3등급" + text.End)
elif (MyMoney < 1000000000):
    print(text.Gray + "2등급" + text.End)
else:
    print(text.Yellow + "1등급" + text.End)

print("\n아무 키를 눌러 끝내십시오.")
os.system("pause >nul")

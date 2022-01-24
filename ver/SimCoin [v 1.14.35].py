import time
import os
import random

#버전 설정
Ver = "1.14.35"
SC = "SimCoin BETA"

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
NEOData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XRPData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XMRData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BCHData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BSVData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
USDTData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
EOSData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BNBData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XTZData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ADAData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LINKData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
XLMData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TRXData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
HTData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
CROData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

MyMoney = 10000000
DASHMoney = DASHData[1] = 120000
LTCMoney = LTCData[1] = 81000
ETCMoney = ETCData[1] = 10000
BTCMoney = BTCData[1] = 11000000
ETHMoney = ETHData[1] = 290000
NEOMoney = NEOData[1] = 16000
XRPMoney = XRPData[1] = 320
XMRMoney = XMRData[1] = 95000
BCHMoney = BCHData[1] = 440000
BSVMoney = BSVData[1] = 310000
USDTMoney = USDTData[1] = 1100
EOSMoney = EOSData[1] = 4800
BNBMoney = BNBData[1] = 25000
XTZMoney = XTZData[1] = 3200
ADAMoney = ADAData[1] = 68
XLMMoney = XLMData[1] = 80
LINKMoney = LINKData[1] = 4600
TRXMoney = TRXData[1] = 24
HTMoney = HTData[1] = 5300
CROMoney = CROData[1] = 70

RTime = 0
RDASH = RLTC = RETC = RBTC = RETH = RNEO = RXRP = RXMR = RBCH = RBSV = RUSDT = REOS = RBNB = RXTZ = RADA = RXLM = RLINK = RTRX = RHT = RCRO = 2

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
print("● 가상 화폐를 구매/판매하고 싶다면, 수량과 통화를")
print("   다음과 같은 형식으로 입력하십시오.")
print(text.Green + "   [수량] [통화]" + text.End + "\n")
print("    └  [수량]에 0 입력 시, [통화]에 해당하는 화폐를 구매/판매할 수 있는")
print("       최대한으로 구매/판매할 수 있습니다.")
print(text.Green + "       0 [통화]" + text.End + "\n")
print("    └  [통화]를 입력할 때 대소문자 구분하지 않습니다.")
print("       하지만, 대소문자를 섞어 입력하면 인식하지 못하므로\n       통일하여 입력하시기 바랍니다.\n")
print("● 취소하고 싶다면 다음 명령어를 입력하십시오.")
print(text.Green + "   0 /esc\n" + text.End)
print("● 도움이 필요하다면 다음 명령어를 입력하십시오.")
print(text.Green + "   0 /helpme\n" + text.End)
print("● 0턴에서는 구매/판매가 불가능합니다.\n")
print("● 최종 보유 자산은 보유 자산과 마지막 턴 시세를 기준으로 마지막 턴까지")
print("   판매되지 않은 화폐들을 합산한 값으로 나타냅니다.")
print("\n\n[주의 사항]\n")
print("● 다음 본문은 게임 최초 실행시에만 보여집니다.\n")
print("● 입력법을 어길 시 치명적 오류를 야기할 수 있으니 주의하십시오.\n\n")
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
    StrNEOMoney = format(NEOMoney, ',')
    StrXRPMoney = format(XRPMoney, ',')
    StrXMRMoney = format(XMRMoney, ',')
    StrBCHMoney = format(BCHMoney, ',')
    StrBSVMoney = format(BSVMoney, ',')
    StrUSDTMoney = format(USDTMoney, ',')
    StrEOSMoney = format(EOSMoney, ',')
    StrBNBMoney = format(BNBMoney, ',')
    StrXTZMoney = format(XTZMoney, ',')
    StrADAMoney = format(ADAMoney, ',')
    StrXLMMoney = format(XLMMoney, ',')
    StrLINKMoney = format(LINKMoney, ',')
    StrTRXMoney = format(TRXMoney, ',')
    StrHTMoney = format(HTMoney, ',')
    StrCROMoney = format(CROMoney, ',')

    
    StrDASHData = format(DASHData[0], ',')
    StrLTCData = format(LTCData[0], ',')
    StrETCData = format(ETCData[0], ',')
    StrBTCData = format(BTCData[0], ',')
    StrETHData = format(ETHData[0], ',')
    StrNEOData = format(NEOData[0], ',')
    StrXRPData = format(XRPData[0], ',')
    StrXMRData = format(XMRData[0], ',')
    StrBCHData = format(BCHData[0], ',')
    StrBSVData = format(BSVData[0], ',')
    StrUSDTData = format(USDTData[0], ',')
    StrEOSData = format(EOSData[0], ',')
    StrBNBData = format(BNBData[0], ',')
    StrXTZData = format(XTZData[0], ',')
    StrADAData = format(ADAData[0], ',')
    StrXLMData = format(XLMData[0], ',')
    StrLINKData = format(LINKData[0], ',')
    StrTRXData = format(TRXData[0], ',')
    StrHTData = format(HTData[0], ',')
    StrCROData = format(CROData[0], ',')

    #시세 갱신 시간 랜덤 설정
    RTime = random.randrange(1, 3)

    #현재 자산 표시
    print("보유 자산 : " + StrMyMoney + "\\", end=" ")
    if i == 10:
        print("(마지막 턴)\n")
    else:
        print("(" + str(i) + "턴)\n")

    #현재 턴의 화폐 시세, 증감율, 보유 수 표시
    print("  Binance Coin (BNB)\t\t|\t" + StrBNBMoney + "\\    ", end="")
    if RBNB == 0:
        if ((BNBData[i+1]-BNBData[i])/BNBData[i])*100 == 0:
            print("(-)    " + StrBNBData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((BNBData[i+1]-BNBData[i])/BNBData[i])*100) + "% ▲)    " + text.End + StrBNBData + "\n")
    elif RBNB == 1:
        if ((BNBData[i+1]-BNBData[i])/BNBData[i])*100 == 0:
            print("(-)    " + StrBNBData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((BNBData[i+1]-BNBData[i])/BNBData[i])*-100) + "% ▼)    " + text.End + StrBNBData + "\n")
    else:
        print(StrBNBData + "\n")

    print("  Bitcoin (BTC)\t\t\t|\t" + StrBTCMoney + "\\    ", end="") 
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

    print("  Bitcoin Cash (BCH)\t\t|\t" + StrBCHMoney + "\\    ", end="")
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

    print("  Bitcoin SV(BSV)\t\t|\t" + StrBSVMoney + "\\    ", end="")
    if RBSV == 0:
        if ((BSVData[i+1]-BSVData[i])/BSVData[i])*100 == 0:
            print("(-)    " + StrBSVData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((BSVData[i+1]-BSVData[i])/BSVData[i])*100) + "% ▲)    " + text.End + StrBSVData + "\n")
    elif RBSV == 1:
        if ((BSVData[i+1]-BSVData[i])/BSVData[i])*100 == 0:
            print("(-)    " + StrBSVData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((BSVData[i+1]-BSVData[i])/BSVData[i])*-100) + "% ▼)    " + text.End + StrBSVData + "\n")
    else:
        print(StrBSVData + "\n")

    print("  Cardano (ADA)\t\t\t|\t" + StrADAMoney + "\\    ", end="")
    if RADA == 0:
        if ((ADAData[i+1]-ADAData[i])/ADAData[i])*100 == 0:
            print("(-)    " + StrADAData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((ADAData[i+1]-ADAData[i])/ADAData[i])*100) + "% ▲)    " + text.End + StrADAData + "\n")
    elif RADA == 1:
        if ((ADAData[i+1]-ADAData[i])/ADAData[i])*100 == 0:
            print("(-)    " + StrADAData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((ADAData[i+1]-ADAData[i])/ADAData[i])*-100) + "% ▼)    " + text.End + StrADAData + "\n")
    else:
        print(StrADAData + "\n")

    print("  Chainlink (LINK)\t\t|\t" + StrLINKMoney + "\\    ", end="")
    if RLINK == 0:
        if ((LINKData[i+1]-LINKData[i])/LINKData[i])*100 == 0:
            print("(-)    " + StrLINKData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((LINKData[i+1]-LINKData[i])/LINKData[i])*100) + "% ▲)    " + text.End + StrLINKData + "\n")
    elif RLINK == 1:
        if ((LINKData[i+1]-LINKData[i])/LINKData[i])*100 == 0:
            print("(-)    " + StrLINKData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((LINKData[i+1]-LINKData[i])/LINKData[i])*-100) + "% ▼)    " + text.End + StrLINKData + "\n")
    else:
        print(StrLINKData + "\n")

    print("  Crypto.com Coin (CRO)\t\t|\t" + StrCROMoney + "\\    ", end="")
    if RCRO == 0:
        if ((CROData[i+1]-CROData[i])/CROData[i])*100 == 0:
            print("(-)    " + StrCROData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((CROData[i+1]-CROData[i])/CROData[i])*100) + "% ▲)    " + text.End + StrCROData + "\n")
    elif RCRO == 1:
        if ((CROData[i+1]-CROData[i])/CROData[i])*100 == 0:
            print("(-)    " + StrCROData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((CROData[i+1]-CROData[i])/CROData[i])*-100) + "% ▼)    " + text.End + StrCROData + "\n")
    else:
        print(StrCROData + "\n")
        
    print("  Dash (DASH)\t\t\t|\t" + StrDASHMoney + "\\    ", end="")
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

    print("  EOS (EOS)\t\t\t|\t" + StrEOSMoney + "\\    ", end="")
    if REOS == 0:
        if ((EOSData[i+1]-EOSData[i])/EOSData[i])*100 == 0:
            print("(-)    " + StrEOSData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((EOSData[i+1]-EOSData[i])/EOSData[i])*100) + "% ▲)    " + text.End + StrEOSData + "\n")
    elif REOS == 1:
        if ((EOSData[i+1]-EOSData[i])/EOSData[i])*100 == 0:
            print("(-)    " + StrEOSData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((EOSData[i+1]-EOSData[i])/EOSData[i])*-100) + "% ▼)    " + text.End + StrEOSData + "\n")
    else:
        print(StrEOSData + "\n")

    print("  Ethereum (ETH)\t\t|\t" + StrETHMoney + "\\    ", end="") 
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

    print("  Ethereum Classic (ETC)\t|\t" + StrETCMoney + "\\    ", end="")
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

    print("  Huobi Token (HT)\t\t|\t" + StrHTMoney + "\\    ", end="") 
    if RHT == 0:
        if ((HTData[i+1]-HTData[i])/HTData[i])*100 == 0:
            print("(-)    " + StrHTData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((HTData[i+1]-HTData[i])/HTData[i])*100) + "% ▲)    " + text.End + StrHTData + "\n")
    elif RHT == 1:
        if ((HTData[i+1]-HTData[i])/HTData[i])*100 == 0:
            print("(-)    " + StrHTData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((HTData[i+1]-HTData[i])/HTData[i])*-100) + "% ▼)    " + text.End + StrHTData + "\n")
    else:
        print(StrHTData + "\n")
        
    print("  Litecoin (LTC)\t\t|\t" + StrLTCMoney + "\\    ", end="")
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
        
    print("  Monero (XMR)\t\t\t|\t" + StrXMRMoney + "\\    ", end="")
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

    print("  Neo (NEO)\t\t\t|\t" + StrNEOMoney + "\\    ", end="") 
    if RNEO == 0:
        if ((NEOData[i+1]-NEOData[i])/NEOData[i])*100 == 0:
            print("(-)    " + StrNEOData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((NEOData[i+1]-NEOData[i])/NEOData[i])*100) + "% ▲)    " + text.End + StrNEOData + "\n")
    elif RNEO == 1:
        if ((NEOData[i+1]-NEOData[i])/NEOData[i])*100 == 0:
            print("(-)    " + StrNEOData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((NEOData[i+1]-NEOData[i])/NEOData[i])*-100) + "% ▼)    " + text.End + StrNEOData + "\n")
    else:
        print(StrNEOData + "\n")
        
    print("  Ripple (XRP)\t\t\t|\t" + StrXRPMoney + "\\    ", end="") 
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

    print("  Stellar (XLM)\t\t\t|\t" + StrXLMMoney + "\\    ", end="") 
    if RXLM == 0:
        if ((XLMData[i+1]-XLMData[i])/XLMData[i])*100 == 0:
            print("(-)    " + StrXLMData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((XLMData[i+1]-XLMData[i])/XLMData[i])*100) + "% ▲)    " + text.End + StrXLMData + "\n")
    elif RXLM == 1:
        if ((XLMData[i+1]-XLMData[i])/XLMData[i])*100 == 0:
            print("(-)    " + StrXLMData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((XLMData[i+1]-XLMData[i])/XLMData[i])*-100) + "% ▼)    " + text.End + StrXLMData + "\n")
    else:
        print(StrXLMData + "\n")
        
    print("  Tether (USDT)\t\t\t|\t" + StrUSDTMoney + "\\    ", end="") 
    if RUSDT == 0:
        if ((USDTData[i+1]-USDTData[i])/USDTData[i])*100 == 0:
            print("(-)    " + StrUSDTData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((USDTData[i+1]-USDTData[i])/USDTData[i])*100) + "% ▲)    " + text.End + StrUSDTData + "\n")
    elif RUSDT == 1:
        if ((USDTData[i+1]-USDTData[i])/USDTData[i])*100 == 0:
            print("(-)    " + StrUSDTData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((USDTData[i+1]-USDTData[i])/USDTData[i])*-100) + "% ▼)    " + text.End + StrUSDTData + "\n")
    else:
        print(StrUSDTData + "\n")

    print("  Tezos (XTZ)\t\t\t|\t" + StrXTZMoney + "\\    ", end="") 
    if RXTZ == 0:
        if ((XTZData[i+1]-XTZData[i])/XTZData[i])*100 == 0:
            print("(-)    " + StrXTZData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((XTZData[i+1]-XTZData[i])/XTZData[i])*100) + "% ▲)    " + text.End + StrXTZData + "\n")
    elif RXTZ == 1:
        if ((XTZData[i+1]-XTZData[i])/XTZData[i])*100 == 0:
            print("(-)    " + StrXTZData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((XTZData[i+1]-XTZData[i])/XTZData[i])*-100) + "% ▼)    " + text.End + StrXTZData + "\n")
    else:
        print(StrXTZData + "\n")
        
    print("  TRON (TRX)\t\t\t|\t" + StrTRXMoney + "\\    ", end="") 
    if RTRX == 0:
        if ((TRXData[i+1]-TRXData[i])/TRXData[i])*100 == 0:
            print("(-)    " + StrTRXData + "\n")
        else:
            print(text.Green + "(" + '%.2f' % float(((TRXData[i+1]-TRXData[i])/TRXData[i])*100) + "% ▲)    " + text.End + StrTRXData + "\n")
    elif RTRX == 1:
        if ((TRXData[i+1]-TRXData[i])/TRXData[i])*100 == 0:
            print("(-)    " + StrTRXData + "\n")
        else:
            print(text.Red + "(" + '%.2f' % float(((TRXData[i+1]-TRXData[i])/TRXData[i])*-100) + "% ▼)    " + text.End + StrTRXData + "\n")
    else:
        print(StrTRXData + "\n")    
        
    

    #선택
    while (True):
        print("\n1) 구매")
        print("2) 판매")
        print("Any Key) 다음 턴")
        Num = input(">>> ")
        
        #구매
        if Num == "1":
            if i == 10:
                print("\n10턴에서는 구매할 수 없습니다.")
            else:
                while (True):
                    Amount, Initial = input("\n명령어를 입력하십시오.\n>>> ").split()
    
                    if Initial == "DASH" or Initial == "dash": 
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "DASH 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (DASHMoney * int(Amount))
                                DASHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "DASH 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            
                    elif Initial == "LTC" or Initial == "ltc":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "LTC 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (LTCMoney * int(Amount))
                                LTCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "LTC 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                    
                    elif Initial == "ETC" or Initial == "etc":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ETC 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (ETCMoney * int(Amount))
                                ETCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ETC 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "BTC" or Initial == "btc":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BTC 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (BTCMoney * int(Amount))
                                BTCData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BTC 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                    
                    elif Initial == "ETH" or Initial == "eth":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ETH 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (ETHMoney * int(Amount))
                                ETHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ETH 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "NEO" or Initial == "neo":
                        if MyMoney < NEOMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / NEOData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (NEOMoney * int(Amount))
                                    NEOData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "NEO 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (NEOMoney * int(Amount))
                                NEOData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "NEO 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "XRP" or Initial == "xrp":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XRP 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (XRPMoney * int(Amount))
                                XRPData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XRP 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                    
                    elif Initial == "XMR" or Initial == "xmr":
                        if MyMoney < XMRMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / XMRData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (XMRMoney * int(Amount))
                                    XMRData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XMR 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (XMRMoney * int(Amount))
                                XMRData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XMR 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "BCH" or Initial == "bch":
                        if MyMoney < BCHMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / BCHData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (BCHMoney * int(Amount))
                                    BCHData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BCH 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (BCHMoney * int(Amount))
                                BCHData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BCH 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "BSV" or Initial == "bsv":
                        if MyMoney < BSVMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / BSVData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (BSVMoney * int(Amount))
                                    BSVData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BSV 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (BSVMoney * int(Amount))
                                BSVData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BSV 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "USDT" or Initial == "usdt":
                        if MyMoney < USDTMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / USDTData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (USDTMoney * int(Amount))
                                    USDTData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "USDT 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (USDTMoney * int(Amount))
                                USDTData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "USDT 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "EOS" or Initial == "eos":
                        if MyMoney < EOSMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / EOSData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (EOSMoney * int(Amount))
                                    EOSData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "EOS 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (EOSMoney * int(Amount))
                                EOSData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "EOS 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "BNB" or Initial == "bnb":
                        if MyMoney < BNBMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / BNBData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (BNBMoney * int(Amount))
                                    BNBData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BNB 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (BNBMoney * int(Amount))
                                BNBData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BNB 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "XTZ" or Initial == "xtz":
                        if MyMoney < XTZMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / XTZData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (XTZMoney * int(Amount))
                                    XTZData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XTZ 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (XTZMoney * int(Amount))
                                XTZData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XTZ 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ADA" or Initial == "ada":
                        if MyMoney < ADAMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / ADAData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (ADAMoney * int(Amount))
                                    ADAData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ADA 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (ADAMoney * int(Amount))
                                ADAData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ADA 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "XLM" or Initial == "xlm":
                        if MyMoney < XLMMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / XLMData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (XLMMoney * int(Amount))
                                    XLMData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XLM 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (XLMMoney * int(Amount))
                                XLMData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XLM 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "LINK" or Initial == "link":
                        if MyMoney < LINKMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / LINKData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (LINKMoney * int(Amount))
                                    LINKData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "LINK 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (LINKMoney * int(Amount))
                                LINKData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "LINK 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "TRX" or Initial == "trx":
                        if MyMoney < TRXMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / TRXData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (TRXMoney * int(Amount))
                                    TRXData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "TRX 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (TRXMoney * int(Amount))
                                TRXData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "TRX 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "HT" or Initial == "ht":
                        if MyMoney < HTMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / HTData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (HTMoney * int(Amount))
                                    HTData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "HT 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (HTMoney * int(Amount))
                                HTData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "HT 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "CRO" or Initial == "cro":
                        if MyMoney < CROMoney * int(Amount):
                            print("\n자산이 부족합니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력할 수 없습니다.")
                            elif int(Amount) == 0:
                                Amount = MyMoney / CROData[i+1]
                                if Amount < 1:
                                    print("\n자산이 부족합니다.")
                                else:
                                    MyMoney -= (CROMoney * int(Amount))
                                    CROData[0] += int(Amount)
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "CRO 구매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                MyMoney -= (CROMoney * int(Amount))
                                CROData[0] += int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "CRO 구매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            
                    elif Initial == "/esc" and Amount == "0":
                        break
                    elif Initial == "/helpme" and Amount == "0":
                        print("\n구매/판매 : " + text.Green + "[수량] [화폐 이니셜]" + text.End)
                        print("최대한 구매/판매 : " + text.Green + "0 [화폐 이니셜]" + text.End)
                        print("취소 : " + text.Green + "0 /esc" + text.End)
                        print("도움 : " + text.Green + "0 /helpme" + text.End)
                        break
                    else:
                        print("\n존재하지 않는 화폐이거나 명령어입니다.")
                else:
                    print("\n자산이 부족합니다.")
                    
        #판매
        elif Num == "2":
            if i == 0:
                print("\n0턴에서는 판매할 수 없습니다.")
            else:
                while (True):
                    Amount, Initial = input("\n명령어를 입력하십시오.\n>>> ").split()

                    if Initial == "DASH" or Initial == "dash":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "DASH 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                DASHData[0] -= int(Amount)
                                MyMoney += DASHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "DASH 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "LTC" or Initial == "ltc":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "LTC 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                LTCData[0] -= int(Amount)
                                MyMoney += LTCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "LTC 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ETC" or Initial == "etc":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ETC 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                ETCData[0] -= int(Amount)
                                MyMoney += ETCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ETC 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "BTC" or Initial == "btc":
                        if BTCData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if BTCData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = BTCData[0]
                                    BTCData[0] = 0
                                    MyMoney += (BTCMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BTC 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BTCData[0] -= int(Amount)
                                MyMoney += BTCMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BTC 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ETH" or Initial == "eth":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ETH 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                ETHData[0] -= int(Amount)
                                MyMoney += ETHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ETH 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "NEO" or Initial == "neo":
                        if NEOData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if NEOData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = NEOData[0]
                                    NEOData[0] = 0
                                    MyMoney += (NEOMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "NEO 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                NEOData[0] -= int(Amount)
                                MyMoney += NEOMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "NEO 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
    
                    elif Initial == "XRP" or Initial == "xrp":
                        if XRPData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if XRPData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = XRPData[0]
                                    XRPData[0] = 0
                                    MyMoney += (XRPMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XRP 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                XRPData[0] -= int(Amount)
                                MyMoney += XRPMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XRP 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "XMR" or Initial == "xmr":
                        if XMRData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if XMRData[0] - 0 == 0:
                                    print("\n해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = XMRData[0]
                                    XMRData[0] = 0
                                    MyMoney += (XMRMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XMR 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                XMRData[0] -= int(Amount)
                                MyMoney += XMRMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XMR 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "BCH" or Initial == "bch":
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
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BCH 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BCHData[0] -= int(Amount)
                                MyMoney += BCHMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BCH 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                        
                    elif Initial == "BSV" or Initial == "bsv":
                        if BSVData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if BSVData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = BSVData[0]
                                    BSVData[0] = 0
                                    MyMoney += (BSVMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BSV 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BSVData[0] -= int(Amount)
                                MyMoney += BSVMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BSV 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            
                    elif Initial == "USDT" or Initial == "usdt":
                        if USDTData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if USDTData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = USDTData[0]
                                    USDTData[0] = 0
                                    MyMoney += (USDTMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "USDT 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                USDTData[0] -= int(Amount)
                                MyMoney += USDTMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "USDT 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            
                    elif Initial == "EOS" or Initial == "eos":
                        if EOSData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if EOSData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = EOSData[0]
                                    EOSData[0] = 0
                                    MyMoney += (EOSMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "EOS 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                EOSData[0] -= int(Amount)
                                MyMoney += EOSMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "EOS 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                            
                    elif Initial == "BNB" or Initial == "bnb":
                        if BNBData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if BNBData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = BNBData[0]
                                    BNBData[0] = 0
                                    MyMoney += (BNBMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "BNB 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                BNBData[0] -= int(Amount)
                                MyMoney += BNBMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "BNB 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "XTZ" or Initial == "xtz":
                        if XTZData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if XTZData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = XTZData[0]
                                    XTZData[0] = 0
                                    MyMoney += (XTZMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XTZ 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                XTZData[0] -= int(Amount)
                                MyMoney += XTZMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XTZ 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "ADA" or Initial == "ada":
                        if ADAData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if ADAData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = ADAData[0]
                                    ADAData[0] = 0
                                    MyMoney += (ADAMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "ADA 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                ADAData[0] -= int(Amount)
                                MyMoney += ADAMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "ADA 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break


                    elif Initial == "XLM" or Initial == "xlm":
                        if XLMData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if XLMData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = XLMData[0]
                                    XLMData[0] = 0
                                    MyMoney += (XLMMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "XLM 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                XLMData[0] -= int(Amount)
                                MyMoney += XLMMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "XLM 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "LINK" or Initial == "link":
                        if LINKData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if LINKData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = LINKData[0]
                                    LINKData[0] = 0
                                    MyMoney += (LINKMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "LINK 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                LINKData[0] -= int(Amount)
                                MyMoney += LINKMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "LINK 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "TRX" or Initial == "trx":
                        if TRXData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if TRXData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = TRXData[0]
                                    TRXData[0] = 0
                                    MyMoney += (TRXMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "TRX 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                TRXData[0] -= int(Amount)
                                MyMoney += TRXMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "TRX 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "HT" or Initial == "ht":
                        if HTData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if HTData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = HTData[0]
                                    HTData[0] = 0
                                    MyMoney += (HTMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "HT 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                HTData[0] -= int(Amount)
                                MyMoney += HTMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "HT 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break

                    elif Initial == "CRO" or Initial == "cro":
                        if CROData[0] < int(Amount):
                            print("\n해당 화폐를 구입하지 않았거나 해당 수량만큼 구입하지 않았습니다.")
                        else:
                            if int(Amount) < 0:
                                print("\n음수는 입력하실 수 없습니다.")
                            elif int(Amount) == 0:
                                if CROData[0] - 0 == 0:
                                    print("\n 해당 화폐를 구입하지 않았습니다.")
                                else:
                                    Amount = CROData[0]
                                    CROData[0] = 0
                                    MyMoney += (CROMoney * int(Amount))
                                    StrMyMoney = format(MyMoney, ',')
                                    StrAmount = format(int(Amount), ',')
                                    print("\n" + StrAmount, "CRO 판매 완료.")
                                    print("변경된 보유 자산 :", StrMyMoney + "\\")
                                    break
                            else:
                                CROData[0] -= int(Amount)
                                MyMoney += CROMoney * int(Amount)
                                StrMyMoney = format(MyMoney, ',')
                                StrAmount = format(int(Amount), ',')
                                print("\n" + StrAmount, "CRO 판매 완료.")
                                print("변경된 보유 자산 :", StrMyMoney + "\\")
                                break
                    elif Initial == "/esc" and Amount == "0":
                        break
                    
                    elif Initial == "/helpme" and Amount == "0":
                        print("\n구매/판매 : " + text.Green + "[수량] [화폐 이니셜]" + text.End)
                        print("최대한 구매/판매 : " + text.Green + "0 [화폐 이니셜]" + text.End)
                        print("취소 : " + text.Green + "0 /esc" + text.End)
                        print("도움 : " + text.Green + "0 /helpme" + text.End)
                        break
                    else:
                        print("\n존재하지 않는 화폐이거나 명령어입니다.")
                        
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
    RNEO = random.randrange(0,2)
    RXRP = random.randrange(0,2)
    RXMR = random.randrange(0,2)
    RBCH = random.randrange(0,2)
    RBSV = random.randrange(0,2)
    RUSDT = random.randrange(0,2)
    REOS = random.randrange(0,2)
    RBNB = random.randrange(0,2)
    RXTZ = random.randrange(0,2)
    RADA = random.randrange(0,2)
    RXLM = random.randrange(0,2)
    RLINK = random.randrange(0,2)
    RTRX = random.randrange(0,2)
    RHT = random.randrange(0,2)
    RCRO = random.randrange(0,2)
    
    if RDASH == 0:
        if DASHMoney < DASHData[1]/20:
            DASHMoney += random.randrange(0, DASHMoney*10)
            DASHData[i+2] = DASHMoney
        else:
            DASHMoney += random.randrange(0, DASHMoney)
            DASHData[i+2] = DASHMoney
    else:
        DASHMoney -= random.randrange(0, DASHMoney)
        DASHData[i+2] = DASHMoney

    if RLTC == 0:
        if LTCMoney < LTCData[1]/20:
            LTCMoney += random.randrange(0, LTCMoney*10)
            LTCData[i+2] = LTCMoney
        else:
            LTCMoney += random.randrange(0, LTCMoney)
            LTCData[i+2] = LTCMoney
    else:
        LTCMoney -= random.randrange(0, LTCMoney)
        LTCData[i+2] = LTCMoney

    if RETC == 0:
        if ETCMoney < ETCData[1]/20:
            ETCMoney += random.randrange(0, ETCMoney*10)
            ETCData[i+2] = ETCMoney
        else:
            ETCMoney += random.randrange(0, ETCMoney)
            ETCData[i+2] = ETCMoney
    else:
        ETCMoney -= random.randrange(0, ETCMoney)
        ETCData[i+2] = ETCMoney

    if RBCH == 0:
        if BCHMoney < BCHData[1]/20:
            BCHMoney += random.randrange(0, BCHMoney*10)
            BCHData[i+2] = BCHMoney
        else:
            BCHMoney += random.randrange(0, BCHMoney)
            BCHData[i+2] = BCHMoney
    else:
        BCHMoney -= random.randrange(0, BCHMoney)
        BCHData[i+2] = BCHMoney

    if RNEO == 0:
        if NEOMoney < NEOData[1]/20:
            NEOMoney += random.randrange(0, NEOMoney*10)
            NEOData[i+2] = NEOMoney
        else:
            NEOMoney += random.randrange(0, NEOMoney)
            NEOData[i+2] = NEOMoney
    else:
        NEOMoney -= random.randrange(0, NEOMoney)
        NEOData[i+2] = NEOMoney

    if RXMR == 0:
        if XMRMoney < XMRData[1]/20:
            XMRMoney += random.randrange(0, XMRMoney*10)
            XMRData[i+2] = XMRMoney
        else:
            XMRMoney += random.randrange(0, XMRMoney)
            XMRData[i+2] = XMRMoney
    else:
        XMRMoney -= random.randrange(0, XMRMoney)
        XMRData[i+2] = XMRMoney

    if RXRP == 0:
        if XRPMoney < XRPData[1]/20:
            XRPMoney += random.randrange(0, XRPMoney*10)
            XRPData[i+2] = XRPMoney
        else:
            XRPMoney += random.randrange(0, XRPMoney)
            XRPData[i+2] = XRPMoney
    else:
        XRPMoney -= random.randrange(0, XRPMoney)
        XRPData[i+2] = XRPMoney

    if RBTC == 0:
        if BTCMoney < BTCData[1]/20:
            BTCMoney += random.randrange(0, BTCMoney*10)
            BTCData[i+2] = BTCMoney
        else:
            BTCMoney += random.randrange(0, BTCMoney)
            BTCData[i+2] = BTCMoney
    else:
        BTCMoney -= random.randrange(0, BTCMoney)
        BTCData[i+2] = BTCMoney

    if RETH == 0:
        if ETHMoney < ETHData[1]/20:
            ETHMoney += random.randrange(0, ETHMoney*10)
            ETHData[i+2] = ETHMoney
        else:
            ETHMoney += random.randrange(0, ETHMoney)
            ETHData[i+2] = ETHMoney
    else:
        ETHMoney -= random.randrange(0, ETHMoney)
        ETHData[i+2] = ETHMoney
        
    if RBSV == 0:
        if BSVMoney < BSVData[1]/20:
            BSVMoney += random.randrange(0, BSVMoney*10)
            BSVData[i+2] = BSVMoney
        else:
            BSVMoney += random.randrange(0, BSVMoney)
            BSVData[i+2] = BSVMoney
    else:
        BSVMoney -= random.randrange(0, BSVMoney)
        BSVData[i+2] = BSVMoney

    if RUSDT == 0:
        if USDTMoney < USDTData[1]/20:
            USDTMoney += random.randrange(0, USDTMoney*10)
            USDTData[i+2] = USDTMoney
        else:
            USDTMoney += random.randrange(0, USDTMoney)
            USDTData[i+2] = USDTMoney
    else:
        USDTMoney -= random.randrange(0, USDTMoney)
        USDTData[i+2] = USDTMoney

    if REOS == 0:
        if EOSMoney < EOSData[1]/20:
            EOSMoney += random.randrange(0, EOSMoney*10)
            EOSData[i+2] = EOSMoney
        else:
            EOSMoney += random.randrange(0, EOSMoney)
            EOSData[i+2] = EOSMoney
    else:
        EOSMoney -= random.randrange(0, EOSMoney)
        EOSData[i+2] = EOSMoney

    if RBNB == 0:
        if BNBMoney < BNBData[1]/20:
            BNBMoney += random.randrange(0, BNBMoney*10)
            BNBData[i+2] = BNBMoney
        else:
            BNBMoney += random.randrange(0, BNBMoney)
            BNBData[i+2] = BNBMoney
    else:
        BNBMoney -= random.randrange(0, BNBMoney)
        BNBData[i+2] = BNBMoney

    if RXTZ == 0:
        if XTZMoney < XTZData[1]/20:
            XTZMoney += random.randrange(0, XTZMoney*10)
            XTZData[i+2] = XTZMoney
        else:
            XTZMoney += random.randrange(0, XTZMoney)
            XTZData[i+2] = XTZMoney
    else:
        XTZMoney -= random.randrange(0, XTZMoney)
        XTZData[i+2] = XTZMoney

    if RADA == 0:
        if ADAMoney < ADAData[1]/20:
            ADAMoney += random.randrange(0, ADAMoney*10)
            ADAData[i+2] = ADAMoney
        else:
            ADAMoney += random.randrange(0, ADAMoney)
            ADAData[i+2] = ADAMoney
    else:
        ADAMoney -= random.randrange(0, ADAMoney)
        ADAData[i+2] = ADAMoney

    if RXLM == 0:
        if XLMMoney < XLMData[1]/20:
            XLMMoney += random.randrange(0, XLMMoney*10)
            XLMData[i+2] = XLMMoney
        else:
            XLMMoney += random.randrange(0, XLMMoney)
            XLMData[i+2] = XLMMoney
    else:
        XLMMoney -= random.randrange(0, XLMMoney)
        XLMData[i+2] = XLMMoney

    if RLINK == 0:
        if LINKMoney < LINKData[1]/20:
            LINKMoney += random.randrange(0, LINKMoney*10)
            LINKData[i+2] = LINKMoney
        else:
            LINKMoney += random.randrange(0, LINKMoney)
            LINKData[i+2] = LINKMoney
    else:
        LINKMoney -= random.randrange(0, LINKMoney)
        LINKData[i+2] = LINKMoney

    if RTRX == 0:
        if TRXMoney < TRXData[1]/20:
            TRXMoney += random.randrange(0, TRXMoney*10)
            TRXData[i+2] = TRXMoney
        else:
            TRXMoney += random.randrange(0, TRXMoney)
            TRXData[i+2] = TRXMoney
    else:
        TRXMoney -= random.randrange(0, TRXMoney)
        TRXData[i+2] = TRXMoney

    if RHT == 0:
        if HTMoney < HTData[1]/20:
            HTMoney += random.randrange(0, HTMoney*10)
            HTData[i+2] = HTMoney
        else:
            HTMoney += random.randrange(0, HTMoney)
            HTData[i+2] = HTMoney
    else:
        HTMoney -= random.randrange(0, HTMoney)
        HTData[i+2] = HTMoney

    if RCRO == 0:
        if CROMoney < CROData[1]/20:
            CROMoney += random.randrange(0, CROMoney*10)
            CROData[i+2] = CROMoney
        else:
            CROMoney += random.randrange(0, CROMoney)
            CROData[i+2] = CROMoney
    else:
        CROMoney -= random.randrange(0, CROMoney)
        CROData[i+2] = CROMoney

#게임 결과 (Part 3)
os.system("cls")
MyMoney += (BSVData[11] * BSVData[0]) + (NEOData[11] * NEOData[0]) + (DASHData[11] * DASHData[0]) + (LTCData[11] * LTCData[0]) + (ETCData[11] * ETCData[0]) + (BCHData[11] * BCHData[0]) + (XMRData[11] * XMRData[0]) + (XRPData[11] * XRPData[0]) + (BTCData[11] * BTCData[0]) + (ETHData[11] * ETHData[0]) + (USDTData[11] * USDTData[0]) + (EOSData[11] * EOSData[0]) + (BNBData[11] * BNBData[0]) + (XTZData[11] * XTZData[0]) + (ADAData[11] * ADAData[0]) + (XLMData[11] * XLMData[0]) + (LINKData[11] * LINKData[0]) + (TRXData[11] * TRXData[0]) + (HTData[11] * HTData[0]) + (CROData[11] * CROData[0])
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
elif (MyMoney < 50000000):
    print(text.DarkCyan + "5등급" + text.End)
elif (MyMoney < 100000000):
    print(text.DarkCyan + "4등급" + text.End)
elif (MyMoney < 5000000000):
    print(text.DarkGray + "3등급" + text.End)
elif (MyMoney < 10000000000):
    print(text.Gray + "2등급" + text.End)
else:
    print(text.Yellow + "1등급" + text.End)

while(True):
    print("\n기록을 변경하시겠습니까? [Y/N]")
    f = open("Record.txt", "r")
    print ("저장된 기록 : " + f.readline())
    YorN = input(">>> ")

    if YorN == "Y" or YorN == "y":
        Name = input("\n이름을 입력하십시오.\n>>> ")
        if Name == "0 /esc":
            None
            
        else:
            f = open("Record.txt", "w")
            f.write(Name)
            f.write("  |  ")
            f.write(StrMyMoney)
            f.write("\\")
            f.close()
            print("\n저장되었습니다.")
            print("\n\n아무 키를 눌러 끝내십시오.")
            os.system("pause >nul")
            break
    elif YorN == "N" or YorN == "n":
        print("\n\n아무 키를 눌러 끝내십시오.")
        os.system("pause >nul")
        break
    else:
        print("\n잘 못 입력하셨습니다.\n")

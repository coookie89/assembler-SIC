mnemonic = {"ADD": "24", "ADDF": "88", "ADDR": "144", "AND": "64", "CLEAR": "180", "COMP": "40", "COMPF": "136", "COPMR": "160",
            "DIV": "36", "DIVF": "100", "DIVR": "156", "FIX": "196", "FLOAT": "192", "HIO": "244", "J": "60", "JEQ": "48", "JGT": "52", "JLT": "56",
            "JSUB": "72", "LDA": "0", "LDB": "104", "LDCH": "80", "LDF": "112", "LDL": "8", "LDS": "108", "LDT": "116", "LDX": "4", "LPS": "224",
            "UML": "32", "MULF": "96", "MULR": "152", "NORM": "200", "OR": "68", "RD": "216", "RMO": "172", "RSUB": "76", "SHIFTL": "164",
            "SHIFTR": "168", "SIO": "240", "SSK": "236", "STA": "12", "STB": "120", "STCH": "84", "STF": "128", "STI": "212", "STL": "20",
            "STS": "124", "STSW": "232", "STT": "132", "STX": "16", "SUB": "28", "SUBF": "92", "SUBR": "148", "SVC": "176", "TD": "224",
            "TIO": "248", "TIX": "44", "TIXR": "184", "WD": "220"}

ASCII = {"NULL": "0", "SOH": "1", "STX": "2", "ETX": "3", "EOT": "4", "ENQ": "5", "ACK": "6", "BEL": "7", "BS": "8", "HT": "9",
         "LF": "10", "VT": "11", "FF": "12", "CR": "13", "SO": "14", "SI": "15", "DLE": "16", "DC1": "17", "DC2": "18", "DC3": "19",
         "DC4": "20", "NAK": "21", "SYN": "22", "ETB": "23", "CAN": "24", "EM": "25", "SUB": "26", "ESC": "27", "FS": "28", "GS": "29",
         "RS": "30", "US": "31", "SP": "32", "!": "33", "''": "34", "#": "35", "$": "36", "%": "37", "&": "38", "'": "39",
         "(": "40", ")": "41", "*": "42", "+": "43", ",": "44", "-": "45", ".": "46", "/": "47", "0": "48", "1": "49",
         "2": "50", "3": "51", "4": "52", "5": "53", "6": "54", "7": "55", "8": "56", "9": "57", ":": "58", ";": "59",
         "<": "60", "=": "61", ">": "62", "?": "63", "@": "64", "A": "65", "B": "66", "C": "67", "D": "68", "E": "69",
         "F": "70", "G": "71", "H": "72", "I": "73", "J": "74", "K": "75", "L": "76", "M": "77", "N": "78", "O": "79",
         "P": "80", "Q": "81", "R": "82", "S": "83", "T": "84", "U": "85", "V": "86", "W": "87", "X": "88", "Y": "89",
         "Z": "90", "[": "91", "\\": "92", "]": "93", "^": "94", "_": "95", "`": "96", "a": "97", "b": "98", "c": "99",
         "d": "100", "e": "101", "f": "102", "g": "103", "h": "104", "i": "105", "j": "106", "k": "107", "l": "108", "m": "109",
         "n": "110", "o": "111", "p": "112", "q": "113", "r": "114", "s": "115", "t": "116", "u": "117", "v": "118", "w": "119",
         "x": "120", "y": "121", "z": "122", "{": "123", "|": "124", "}": "125", "~": "126", "DEL": "127"}


language = []  #存輸入的組合語言
label = []  # 紀錄每一行的label
opcode = []  # 紀錄每一行的opcode
oprand = []  # 紀錄每一行的oprand
PC = []  #程式計數器,紀錄下個記憶體位址
MC=[]   #紀錄每一行的機器碼

print("開始打你的組合語言吧!!")


while True:
    code = input("here: ")
    st = code.split()

    if len(st) == 3:

        if st[1] == "START":
            s = 1
            i = 0
            language.append(st)
            label.append(st[0])
            opcode.append(st[1])
            oprand.append(st[2])
            PC.append(int(st[2],16)) 
            i = i+1

        elif s == 1:
            if st[1] == "BYTE" or st[1] == "WORD" or st[1] == "RESB" or st[1] == "RESW":
                language.append(st)
                label.append(st[0])
                opcode.append(st[1])
                oprand.append(st[2])
                if st[1] == "BYTE":
                    if i==1:
                        PC.append(PC[0])
                        i = i+1
                    else:
                        PC.append(PC[i-1]-3)
                        i = i+1
                elif st[1] == "WORD":
                    if i==1:
                        PC.append(PC[0])
                        i = i+1
                    else:
                        PC.append(PC[i-1]+3)
                        i = i+1
                elif st[1] == "RESB":
                    if i==1:
                        PC.append(PC[0])
                        i = i+1
                    else:
                        PC.append(PC[i-1]+int(st[2]))
                        i = i+1
                elif st[1] == "RESW":
                    if i==1:
                        PC.append(PC[0])
                        i = i+1
                    else:
                        PC.append(PC[i-1]+int(st[2])*3)
                        i = i+1
            else:
                language.append(st)
                label.append(st[0])
                opcode.append(st[1])
                oprand.append(st[2])
                if i==1:
                    PC.append(PC[0])
                    i = i+1
                else:
                    PC.append(PC[i-1]+3)
                    i = i+1

    elif len(st) == 2:
        if s == 1:
            if st[0] == "END":
                language.append(st)
                label.append(" ")
                opcode.append(st[0])
                oprand.append(st[1])
                break

            else:
                language.append(st)
                label.append(" ")
                opcode.append(st[0])
                oprand.append(st[1])
                if i==1:
                    PC.append(PC[0])
                    i = i+1
                else:
                    PC.append(PC[i-1]+3)
                    i = i+1

    elif len(st) == 1:
        if s == 1:
            language.append(st)
            label.append(" ")
            opcode.append(st[0])
            oprand.append(" ")
            if i==1:
                PC.append(PC[0])
                i=i+1
            else:
                PC.append(PC[i-1]+3)
                i = i+1

for j in range(0,i):
    opop=hex(PC[j]).replace('0x','')
    if len(opop)==1:
        opop='000'+opop
        PC[j]=opop
    elif len(opop)==2:
        opop='00'+opop
        PC[j]=opop
    elif len(opop)==3:
        opop='0'+opop
        PC[j]=opop
    else:
        PC[j]=opop                                                                  #將位置全部改成16進位 字串 沒有0x

for j in range(1,i):
    if opcode[j]=="WORD":
        opop=opcode[j]                                                          #直接放入目的碼
        for a in range(0,6-len(oprand[j])):
            opop="0"+opop                                                       #不足6補0
    elif opcode[j]=="BYTE":
        opop=oprand[j]
        temp=""
        if opop[0]=='C':                                                        #如果是字串
            for a in range(2,len(opop)-1):                                      #把一個個字元拿出來 扣掉C''三個位置
                temp=temp+ASCII[opop[a]]                                        #尋找ASCII
            MC.append(temp)
        elif opop[0]=='X':                                                      #如果是16進位
            for a in range(2,len(opop)-1):                                      #扣掉X''三個位置
                temp=temp+opop[a]
            MC.append(temp)
    elif opcode[j]=="RSUB":
        MC.append("4C0000")
    elif opcode[j]=="RESW" or opcode[j]=="RESB":                                #沒有目的碼
        MC.append(" ")
    else:                                                                       #其他狀況
        opop=hex(int(mnemonic[opcode[j]])).replace('0x','')                     #將opcode轉成16進位
        if len(opop)==1:
            opop='0'+opop
        for l in range(0,i+1):
            if oprand[j]==label[l]:                                             #找到對應lable位置
                MC.append(opop+PC[l])                                           #兩個串在一起
                break
                
for j in range(0,i-1):
    print(MC[j])

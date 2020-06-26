mnemonic = {"ADD": "18", "ADDF": "58", "ADDR": "90", "AND": "40", "CLEAR": "B4", "COMP": "28", "COMPF": "88", "COPMR": "A0",
            "DIV": "24", "DIVF": "64", "DIVR": "9C", "FIX": "C4", "FLOAT": "C0", "HIO": "F4", "J": "3C", "JEQ": "30", "JGT": "34", "JLT": "38",
            "JSUB": "48", "LDA": "00", "LDB": "68", "LDCH": "50", "LDF": "70", "LDL": "08", "LDS": "6C", "LDT": "74", "LDX": "04", "LPS": "E0",
            "UML": "20", "MULF": "60", "MULR": "98", "NORM": "C8", "OR": "44", "RD": "D8", "RMO": "AC", "RSUB": "4C", "SHIFTL": "A4",
            "SHIFTR": "A8", "SIO": "F0", "SSK": "EC", "STA": "0C", "STB": "78", "STCH": "54", "STF": "80", "STI": "D4", "STL": "14",
            "STS": "7C", "STSW": "E8", "STT": "84", "STX": "10", "SUB": "1C", "SUBF": "5C", "SUBR": "94", "SVC": "B0", "TD": "E0",
            "TIO": "F8", "TIX": "2C", "TIXR": "B8", "WD": "DC"}

ASCII = {"NULL": "00", "SOH": "01", "STX": "02", "ETX": "03", "EOT": "04", "ENQ": "05", "ACK": "06", "BEL": "07", "BS": "08", "HT": "09",
         "LF": "0A", "VT": "0B", "FF": "0C", "CR": "0D", "SO": "0E", "SI": "0F", "DLE": "10", "DC1": "11", "DC2": "12", "DC3": "13",
         "DC4": "14", "NAK": "15", "SYN": "16", "ETB": "17", "CAN": "18", "EM": "19", "SUB": "1A", "ESC": "1B", "FS": "1C", "GS": "1D",
         "RS": "1E", "US": "1F", "SP": "20", "!": "21", "''": "22", "#": "23", "$": "24", "%": "25", "&": "26", "'": "27",
         "(": "28", ")": "29", "*": "2A", "+": "2B", ",": "2C", "-": "2D", ".": "2E", "/": "2F", "0": "30", "1": "31",
         "2": "32", "3": "33", "4": "34", "5": "35", "6": "36", "7": "37", "8": "38", "9": "39", ":": "3A", ";": "3B",
         "<": "3C", "=": "3D", ">": "3E", "?": "3F", "@": "40", "A": "41", "B": "42", "C": "43", "D": "44", "E": "45",
         "F": "46", "G": "47", "H": "48", "I": "49", "J": "4A", "K": "4B", "L": "4C", "M": "4D", "N": "4E", "O": "4F",
         "P": "50", "Q": "51", "R": "52", "S": "53", "T": "54", "U": "55", "V": "56", "W": "57", "X": "58", "Y": "59",
         "Z": "5A", "[": "5B", "\\": "5C", "]": "5D", "^": "5E", "_": "5F", "`": "60", "a": "61", "b": "62", "c": "63",
         "d": "64", "e": "65", "f": "66", "g": "67", "h": "68", "i": "69", "j": "6A", "k": "6B", "l": "6C", "m": "6D",
         "n": "6E", "o": "6F", "p": "70", "q": "71", "r": "72", "s": "73", "t": "74", "u": "75", "v": "76", "w": "77",
         "x": "78", "y": "79", "z": "7A", "{": "7B", "|": "7C", "}": "7D", "~": "7E", "DEL": "7F"}


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
        opop=oprand[j]                                                          #直接放入目的碼
        for a in range(0,6-len(oprand[j])):
            opop="0"+opop                                                       #不足6補0
        MC.append(opop)
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
        opop=mnemonic[opcode[j]]                                                
        for l in range(0,i+1):
            if oprand[j]==label[l]:                                             #找到對應lable位置
                MC.append(opop+PC[l])                                           #兩個串在一起
                break
                
for j in range(0,i-1):
    print(MC[j])

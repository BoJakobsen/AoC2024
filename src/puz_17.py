with open('data/17.dat') as f:
    lines = [(x.strip()) for x in f]



CPU = {}
CPU['A'] = int(lines[0].split(':')[1])
CPU['B'] = int(lines[1].split(':')[1])
CPU['C'] = int(lines[2].split(':')[1])
CPU['PC'] = 0
CPU['OUT'] = []

Prog = list(map(int,lines[4].split(':')[1].split(',')))


def combo(operand):
    if operand <= 3 :
        return operand
    elif operand == 4 :
        return CPU['A']
    elif operand == 5 :
        return CPU['B']
    elif operand == 6 :
        return CPU['C']
    elif operand == 7 :
        print("ERROR: combo 7")


        

def RunProg(prog = Prog):
    while CPU['PC'] < len(prog):
        jnz = False 
        op = prog[CPU['PC']]
        operand = prog[CPU['PC']+1]


        match op:
            case 0:  # adv
                #  print('adv:', operand)
                CPU['A'] = CPU['A'] // 2**combo(operand)
            case 1:  # blx
                CPU['B'] = CPU['B'] ^ operand
            case 2:  # bst
                CPU['B'] = combo(operand) % 8
            case 3:  # jnz
                if CPU['A'] != 0 :
                    jnz = True
                    CPU['PC'] = operand
            case 4:  # bxc
                CPU['B'] = CPU['B'] ^ CPU['C']
            case 5:  # out
                CPU['OUT'].append(str(combo(operand) % 8))
            case 6:  # bdv
                CPU['B'] = CPU['A'] // 2**combo(operand)
            case 7:  # cdv
                CPU['C'] = CPU['A'] // 2**combo(operand)

#        print(op, operand)
        if not jnz:
            CPU['PC'] += 2 # Advance PC if not jnz command

RunProg()
print(','.join(CPU['OUT']))

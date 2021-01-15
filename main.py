import portent, oracle, util

print("Welcome to Enigma")
running = True

while(running):
    cmd = input('> ')
    cmd = cmd.lower().split(' ')
    if cmd[0] == 'ask':
        if len(cmd) > 1:
            if util.isdigit(cmd[-1]):
                print(oracle.ask(int(cmd[-1])))
                continue
        print(oracle.ask())
    elif cmd[0] == 'portent' or cmd[0] == 'p':
        if len(cmd) > 1:
            if util.isdigit(cmd[1]):
                print('\n'.join(portent.gen(abs(int(cmd[1])))))
                continue
        print(portent.gen()[0])
    elif cmd[0] == 'roll':
        if len(cmd) < 3:
            print("Invalid arguments, format: roll [num] [sides]")
            continue
        if not util.isdigit(cmd[1]) or not util.isdigit(cmd[2]):
            print("Invalid arguments, format: roll [num] [sides]")
            continue
        roll = util.roll(abs(int(cmd[1])), abs(int(cmd[2])))
        if(len(roll) == 1):
            print(roll[0])
        else:
            print(' + '.join(str(v) for v in roll) + ' = {}'.format(sum(roll)))
                
    elif cmd[0] == 'exit':
        running = False



data = input()
data = data.split("\n")

mem1 = dict()
mem2 = dict()
for line in data:
    var, val = line.split(" = ")
    
    if var == "mask":
        mask1 = int(val.replace("X", "1"), 2) # Replace X for 0
        mask2 = int(val.replace("X", "0"), 2) # Replace X for 1
        
        # Position of every bit with an X from less significant bit to most significant
        X_pos = [ len(val) - i for i, x in enumerate(val, start=1) if x == "X" ]
        
        # 1 where there is a X, 0 in any other case
        X_pos_bin = int(val.replace("1", "0").replace("X", "1"), 2) 
    else:
        mem1[var[4:-1]] = (int(val) & mask1) | mask2
        
        address = (int(var[4:-1]) | mask2)
        
        # Every position with a X in the mask is set to 0 in the address
        address = (address | X_pos_bin) ^ X_pos_bin
        
        # 2^count(X) combinations
        for c in range(2 ** len(X_pos)):
            
            c = bin(c)[2:].zfill(len(X_pos))
            
            new_address = address
            # Activate bits
            for b, pos in zip(c, X_pos):
                new_address |= (int(b) << pos)
                
            mem2[new_address] = int(val)
                
        
print("Part 1: %d" % sum(mem1.values()))
print("Part 2: %d" % sum(mem2.values()))
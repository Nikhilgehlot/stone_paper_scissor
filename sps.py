import random
c1 = 0
c2 = 0
i = 0
while i <=5:
    choosed=input("enter ur chjoice ""\n""1.stone\n2.paper\n3.scissor")
    lst = ["stone", "paper", "scissor"]
    comp = random.choice(lst)
    if choosed == "stone":
        if comp==choosed:
            print(f"match draw:{choosed} vs {comp}")
        elif comp=="paper":
            print(f"u won:{choosed} vs {comp}")
            c1+=1
        elif comp == "scissor":
            print(f"u won:{choosed} vs {comp}")
            c1 += 1
    if choosed == "paper":
       if comp==choosed:
           print(f"match draw:{choosed} vs {comp}")
       elif comp=="stone":
           print(f"u loose:{choosed} vs {comp}")
           c2+=1
       elif comp == "scissor":
           print(f"u loose:{choosed} vs {comp}")
           c2 += 1
    if choosed == "scissor":
        if comp == choosed:
            print(f"match draw:{choosed} vs {comp}")
        elif comp == "stone":
            print(f"u loose:{choosed} vs {comp}")
            c2 += 1
        elif comp == "paper":
            print(f"u won:{choosed} vs {comp}")
            c1 += 1
    i+=1

if c1>c2:
    print("u won")
else:
    print("u loose")


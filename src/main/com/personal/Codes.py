with open("Codes.txt", "w") as f:
    for a in range(1, 51):
        for b in range(1, 11):
            for c in range(1, 11):
                S = "JM_A" + str(a) + "_B" + str(b) + "_" + str(c)
                f.write(S)
                f.write("\n")

f.close()

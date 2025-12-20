from sys import stdin

def solve(lines):
    for line in lines:
        stack = []
        matched_flag = True

        for ch in line:
            if (ch == "("):
                stack.append("(")
            
            if (ch == "["):
                stack.append("[")

            if (ch == ")"):
                if not (len(stack) != 0 and stack.pop() == "("):
                    matched_flag = False
                    break

            if (ch == "]"):
                if not (len(stack) != 0 and stack.pop() == "["):
                    matched_flag = False
                    break
                
        if (len(stack) != 0):
            matched_flag = False

        if matched_flag:
            print("yes")
        else:
            print("no")

if __name__=="__main__":
    lines = []
    while True:
        line = stdin.readline().rstrip("\n")
        if (line == "."):
            break
        lines.append(line)

    solve(lines)



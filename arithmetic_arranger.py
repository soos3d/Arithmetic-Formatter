
err_size = "Error: Too many problems."
err_op = "Error: Operator must be '+' or '-'."
err_digits = "Error: Numbers must only contain digits."
err_len = "Error: Numbers cannot be more than four digits."

#arranger function
def arithmetic_arranger(problems, solve = False):
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = None
    #check if the problems are in the correct format
    if len(problems) > 5:
            print(err_size)
    else:
    #this loop splits the problems in each element
        for p in problems:
            [a, op, b] = p.split()
    #check lenght of each operand
            if len(a) > 4 or len(b) > 4:
                print(err_len)
                quit()
    #check for + or -
            if op != "+" and op != "-":
                 print(err_op)
                 quit()

    #check for digits only
            try:
                 n1 = int(a)
                 n2 = int(b)
            except:
                 print(err_digits)
                 quit()

    #This makes calculation based on the operator sign
            sum = None
            if op == "+":
                sum = str(int(a) + int(b))
            else:
                sum = str(int(a) - int(b))

    #this formats the lines to create the table effect
            lenght = max(len(a), len(b)) + 2
            top = str(a).rjust(lenght)
            bottom = op + str(b).rjust(lenght - 1)
            line = ""
            res = str(sum).rjust(lenght)
            for s in range(lenght):
                line += "-"

            if problems != problems[-1]:
                first += top + '    '
                second += bottom + '    '
                lines += line + '    '
                sumx += res + '    '
            else:
                first += top
                second += bottom
                lines += line
                sumx += res

        #prints on the screen with or without result depending on solve
        if solve:
            string = first +"\n" + second + "\n" + lines +"\n" + sumx
        else:
            string = first +"\n" + second + "\n" + lines
        print(string)


#lits of problems
problems = list(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "54 + 67"])
#calls the function
arithmetic_arranger(problems, solve = True)

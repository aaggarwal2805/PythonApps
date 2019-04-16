#INCOME = 183148
import sys
import csv
TAX_RANGE = [9700, 39475, 84200, 160725, 204100, 510300]
FINAL_VALUE = [TAX_RANGE[0]+1, TAX_RANGE[0]+1, TAX_RANGE[0]+1, TAX_RANGE[0]+1, TAX_RANGE[0]+1, TAX_RANGE[0]+1]
TAX_PER = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]




def read_income(file_path):
    with open(file_path) as income_text:
        income = float(income_text.read())
        return(income)

def tax_b1(income):    #(0 - 9700)
    tax_b1 = income * TAX_PER[0]
    return(tax_b1)

def tax_b2(r1, r2): #(9700-39475)
    tax_b2 = (r2 -r1) * TAX_PER[1]
    return(tax_b2)

def tax_b3(r1, r2): #(39475-84200)
    tax_b3 = (r2 -r1) * TAX_PER[2]
    return(tax_b3)

def tax_b4(r1, r2): #(84200-160725)
    tax_b4 = (r2 -r1) * TAX_PER[3]
    return(tax_b4)

def tax_b5(r1, r2): #(160725-204100)
    tax_b5 = (r2 -r1) * TAX_PER[4]
    return(tax_b5)

def tax_b6(r1, r2): #(204100-510300)
    tax_b6 = (r2 -r1) * TAX_PER[5]
    return(tax_b6)

def tax_b7(income):
    tax_b7 = income * TAX_PER[6]
    return(tax_b7)


def main(input_file):
    ti = read_income(input_file)
#181376
    if ti > 0 and ti < TAX_RANGE[0]:
        tax = tax_b1(ti)
    elif ti > TAX_RANGE[0] and ti < TAX_RANGE[1]:
        tax = tax_b1(TAX_RANGE[0]) + tax_b2(ti, TAX_RANGE[1])
    elif ti > TAX_RANGE[1] and ti < TAX_RANGE[2]:
        tax = tax_b1(TAX_RANGE[0]) + tax_b2(TAX_RANGE[0], TAX_RANGE[1]) + tax_b3(ti, TAX_RANGE[2])
    elif ti > TAX_RANGE[2] and ti < TAX_RANGE[3]:
        tax = tax_b1(TAX_RANGE[0]) + tax_b2(TAX_RANGE[0], TAX_RANGE[1]) + tax_b3(TAX_RANGE[1], TAX_RANGE[2]) + tax_b4(ti, TAX_RANGE[3])
    elif ti > TAX_RANGE[3] and ti < TAX_RANGE[4]:
        tax = tax_b1(TAX_RANGE[0]) + tax_b2(TAX_RANGE[0], TAX_RANGE[1]) + tax_b3(TAX_RANGE[1], TAX_RANGE[2]) + tax_b4(TAX_RANGE[2],TAX_RANGE[3]) + tax_b5(ti, TAX_RANGE[4])
    elif ti > TAX_RANGE[4] and ti < TAX_RANGE[5]:
        tax = tax_b1(TAX_RANGE[0]) + tax_b2(TAX_RANGE[0], TAX_RANGE[1]) + tax_b3(TAX_RANGE[1], TAX_RANGE[2]) + tax_b4(TAX_RANGE[2],TAX_RANGE[3]) + tax_b5(TAX_RANGE[3], TAX_RANGE[4]) + tax_b6(ti, TAX_RANGE[5])
    elif ti > TAX_RANGE[5]:
        tax = tax_b7(ti)
    else: print("no tax")
    print(tax)





if __name__ == '__main__':
    input_file_path = sys.argv[1]
    main(input_file_path)

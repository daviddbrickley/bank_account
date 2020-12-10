"""
p = principle (present value)
r = interest rate
n = how many payments per period
t = how many periods 
fv =  future value
"""




def compound_interest():
    p = float(input("What's the princible? "))
    r = float(input("What's the rate? "))
    n = float(input("How many periods per year? "))
    t = int(input("how many years? "))
    
    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    roi = ci/balance * 100
    
    print('\n Balance at the end of the period $',round(balance,2))
    print("You earned $", round(ci,2),"during this ",t,"year period")
    print ("this is a ",round(roi,2),"% return on investment")
compound_interest()

"""
roi = x * ci
roi/ci = x * ci/ci
_ = x

"""

# Python3 programa para encontrar composto
# interesse por valores fornecidos.
  
def compound_interest(principle, rate, time): 
  
    # Calcula juros compostos  
    CI = principle * (pow((1 + rate / 100), time)) 
    print("O interesse composto é", CI) 
  
# Driver Code  
compound_interest(10000, 10.25, 5) 
  
# Este código é contribuído por Dorgival Fernando.
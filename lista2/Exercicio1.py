def conta_vogais(string): 
    string = string.lower() 
    vogais = 'aeiou' 
    return {i: string.count(i) for i in vogais if i in string} 
 
print(conta_vogais('olaaa')) 
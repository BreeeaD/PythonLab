#itemul 3
print("Salut, pentru inceput introduti numele tau: ")
nume = input()
print("Bine salut " + nume)

#itemul 4
nr_int = 3456
nr_float = 343.231
txt_scurt = "CEVA"
txt_randuri = """CEVA 
ce va aparea cu inca CEVA
din rand nou acum"""

#itemul 5
print(type(nr_float))
print(type(txt_randuri))

#itemul 6 
print(len(txt_scurt))

#itemul 7
print(txt_randuri.upper())

#itemul 8
print(txt_scurt[2:])

#itemul 10
ceva = 1223
ceva_ceva = "akal"

txt_Ceva = "CEva info nr {}, ceva info txt {}"
format_ceva = txt_Ceva.format(ceva, ceva_ceva)
print(format_ceva)

form_ceva = f"CEva info nr {ceva}, ceva info txt {ceva_ceva}"
print(form_ceva)
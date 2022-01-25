lista_a={
'piekarnia':['bulki','chlebek','paczek'],
'warzywniak':['buraki','fasola','ziemniaki']
}

lista_dict=dict(lista_a)
print('Lista zakupow') 
for sklep,rzeczy in lista_dict.items(): 
    print('Kiedy ide do' ,(sklep.upper()),',kupuje tam takie produkty jak:',(rzeczy))
print('Idac do sklepu ,kupilem razem',len(rzeczy)*2,'rzeczy')

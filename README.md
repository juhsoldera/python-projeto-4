# python-projeto-4
Sistemas Especialistas com Python - Controlar corrosão em torre de destilação de Petróleo.

# Especificação:

Entradas: pH no topo da torre, vazão de produto, vazão de água de lavagem, injeção de neutralizante,  
- pH no topo da torre: 5,2 >= pH <= 6,2
- vazão de produto: > 0
- vazão de água de lavagem:  130 +- 10%
- injeção de neutralizante:  20
 
 
Se vazão de produto > 0
Então “torre em operação”
 
Se “Torre em operação”
E ‘pH no topo da torre’ = 5,9
E vazão de água de lavagem < 130 * 1,1
E vazão de água de lavagem > 130 * 0,9
Então “Corrosão sob controle na torre”
 
Se “Torre em operação”
E ‘pH no topo da torre’ = 5,0
E vazão de água de lavagem < 130 * 1,1
E vazão de água de lavagem > 115
Então “Risco elevado de corrosão na torre”
E “Ajustar a vazão de água de lavagem para > 130 * 0,9”
 
Se “Torre em operação”
E ‘pH no topo da torre’ = 5,0
E vazão de água de lavagem < 130 * 1,1
E vazão de água de lavagem > 130 * 0,9
Então “Risco elevado de corrosão na torre”
E “Aumentar a injeção de neutralizante em 10%”

"""### **Q10)** Detectar duas ou mais palavras consecutivas com todas as letras maiúsculas. Cada palavra pode possuir qualquer quantidade de letras.."""


import re

teste=['Durante o “Dia do Fico”, DOM PEDRO declarou que permaneceria no Brasil.', 'O Magazine Luiza(MGLU) é uma empresa de varejo', 'LUIZA HELENA TRAJANO é uma empresária brasileira.', 'RELATÓRIO de TENDÊNCIAS', 'O RELATÓRIO DE DESEMPENHO foi publicado']


for item in teste:
    print(re.findall(r'([A-ZÀ-Ú]{2,}\s[A-ZÀ-Ú]+\s?[A-ZÀ-Ú]+)', item))


    

 






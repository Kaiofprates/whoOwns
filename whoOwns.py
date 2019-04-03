#coding: utf-8
from busca import whois
print('         ===================================================================\t\n\t           dP                MMP"""""YMM                              \n\t           88                M\' .mmm. `M                              \n\tdP  dP  dP 88d888b. .d8888b. M  MMMMM  M dP  dP  dP 88d888b. .d8888b. \n\t88  88  88 88\'  `88 88\'  `88 M  MMMMM  M 88  88  88 88\'  `88 Y8ooooo. \n\t88.88b.88\' 88    88 88.  .88 M. `MMM\' .M 88.88b.88\' 88    88       88 \n\t8888P Y8P  dP    dP `88888P\' MMb     dMM 8888P Y8P  dP    dP `88888P\' \n\t                             MMMMMMMMMMM                                     \n\t=====================================================================\n        [*] Lembre-se que essa consulta é válida somente para domínios br\n'
)
query  = input('Informe o site: ')
whois(query).obtem_identificacao()
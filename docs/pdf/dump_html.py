# Projeto: Desenvolvimento Front-end — Rede Raízes do Nordeste
# Autora: Aliny Reis Ramos — RU 5071671
# Curso: CST em Análise e Desenvolvimento de Sistemas — UNINTER
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pdf as b
body, toc = b.number_headings(b.build_body())
body = body.replace('file://', '')
open(sys.argv[1], 'w', encoding='utf-8').write('<html><body>' + body + '</body></html>')
print('ok', len(toc))

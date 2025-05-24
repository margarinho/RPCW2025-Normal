import json
import re
import unicodedata
conceitos_json = "conceitos.json"
disciplinas_json = "disciplinas.json"
mestres_json = "mestres.json"
obras_json = "obras.json"
aprendizes_json = "pg55921.json"



with open(conceitos_json, 'r', encoding='utf-8') as jsonfile:
    conceitos = json.load(jsonfile)

string_conceitos = []
c = set()
for dic in conceitos['conceitos']:
    conceitos_r = [f":{v.replace(' ','_')}" for v in dic['conceitosRelacionados']]
    s_conceitos_r = ', '.join(conceitos_r)
    conceito = (
        f":{dic['nome'].replace(' ','_')} a :Conceito ;\n"
        f"    :estaRelacionado {s_conceitos_r} ;\n"
        f"    :surgeEm :{dic['períodoHistórico'].replace(' ','_').replace('/','_')} ."
    )
    string_conceitos.append(conceito)
      
with open(disciplinas_json, 'r', encoding='utf-8') as jsonfile:
    disciplinas = json.load(jsonfile)

string_disciplinas = []
string_c = []
for dic in disciplinas['disciplinas']:
    tipos = [f":{v.replace(' ','_')}" for v in dic['tiposDeConhecimento']]
    if dic.get('conceitos'):
        conceitos_d = [f":{v.replace(' ','_')}" for v in dic['conceitos']]
    s_tipos = ', '.join(tipos)
    diciplina = (
        f":{dic['nome'].replace(' ','_')} rdf:type owl:NamedIndividual , :Disciplina ;\n"
        f"    :pertenceA {s_tipos} ."
    )
    nome = dic['nome'].replace(' ', '_').replace('\n', '')
    for c in conceitos_d:
        
        t = f"{c} :eEstudadoEm :{nome} . "
        string_c.append(t)
    
with open(mestres_json, 'r', encoding='utf-8') as jsonfile:
    mestres = json.load(jsonfile)
    
string_mestres = []
for dic in mestres['mestres']:
    disciplinas_m = [f":{v.replace(' ','_')}" for v in dic['disciplinas']]
    s_disciplinas_m = ', '.join(disciplinas_m)
    mestre = (
        f":{dic['nome'].replace(' ','_')} a :Mestre ;\n"
        f"    :ensina {s_disciplinas_m} ;\n"
        f"    :nascidoEm :{dic['períodoHistórico'].replace(' ','_').replace('/','_')} ."
    )
    
    string_mestres.append(mestre)

with open(obras_json, 'r', encoding='utf-8') as jsonfile:
    obras = json.load(jsonfile)
    
string_obras = []
for dic in obras['obras']:
    obras_c = [f":{v.replace(' ','_')}" for v in dic['conceitos']]
    s_obras_c = ', '.join(obras_c)
    obra = (
        f":{dic['titulo'].replace(' ','_')} a :Obra ;\n"
        f"    :foiEscritoPor :{dic['autor'].replace(' ','_')} ;\n"
        f"    :explica {s_obras_c} ."
    )
    
    string_mestres.append(mestre)
   

with open(aprendizes_json, 'r', encoding='utf-8') as jsonfile:
    aprendizes = json.load(jsonfile)
    
string_aprendizes = []

for a in aprendizes:
    discilinas_a = [f":{v.replace(' ','_')}" for v in a['disciplinas']]
    s_discilinas_a = ', '.join(discilinas_a)
    nome = unicodedata.normalize('NFKD', a['nome']).encode('ASCII', 'ignore').decode('utf-8')
    nome = nome.replace(" ", "_")
    nome = re.sub(r'\W+', '', nome)
    aprendiz = (
        f":{nome} a :Aprendiz ;\n"
        f"    :aprende {s_discilinas_a} ;\n"
        f"    :idade {a['idade']} ."
    )
    string_aprendizes.append(aprendiz)
    
with open('sapientia_base.ttl', 'r') as f:
    conteudo_original = f.read()

with open('sapientia_ind.ttl', 'w', encoding='utf-8') as f:
    f.write(conteudo_original)
    f.write('\n\n')
    f.write('\n'.join(string_conceitos) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_disciplinas) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_c) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_mestres) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_obras) +'\n')
    f.write('\n\n')
    f.write('\n'.join(string_aprendizes) +'\n')
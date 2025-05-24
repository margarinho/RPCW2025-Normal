from rdflib import OWL, RDF, Graph, Namespace

g = Graph()
g.parse('sapientia_ind.ttl')

n = Namespace("http://www.semanticweb.org/magui/ontologies/2025/academia#")

# Define a propriedade no grafo
if (n.estudaCom, None, None) not in g:
    g.add((n.estudaCom, RDF.type, OWL.ObjectProperty))

# SPARQL UPDATE para inserir as novas relações
update_query = """
PREFIX : <http://www.semanticweb.org/magui/ontologies/2025/academia#>

INSERT {
  ?aprendiz :estudaCom ?disciplina .
}
WHERE {
  ?aprendiz a :Aprendiz ;
            :aprende ?disciplina .

  ?mestre a :Mestre ;
          :ensina ?disciplina .
}
"""

g.update(update_query)

q2 = """
PREFIX : <http://www.semanticweb.org/magui/ontologies/2025/academia#>

SELECT ?aprendiz ?mestre WHERE {
    ?aprendiz :estudaCom ?mestre .
} LIMIT 10
"""

for row in g.query(q2):
    print(row)

with open("sapientia_ind_updated_estudaCom.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
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
  ?aprendiz :estudaCom ?mestre .
}
WHERE {
  ?aprendiz a :Aprendiz ;
            :aprende ?disciplina .

  ?mestre a :Mestre ;
          :ensina ?disciplina .
}
"""

g.update(update_query)

print(g.serialize(format='turtle').decode("utf-8") if isinstance(g.serialize(), bytes) else g.serialize(format='turtle'))

with open("sapientia_ind_updated.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
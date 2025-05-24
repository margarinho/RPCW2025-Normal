from rdflib import OWL, RDF, Graph, Namespace

g = Graph()
g.parse('sapientia_ind.ttl')

n = Namespace("http://www.semanticweb.org/magui/ontologies/2025/academia#")

if (n.daBasesPara, None, None) not in g:
    g.add((n.daBasesPara, RDF.type, OWL.ObjectProperty))

update_query = """
PREFIX : <http://www.semanticweb.org/magui/ontologies/2025/academia#>

INSERT {
  ?disciplina :daBasesPara ?aplicacao .
}
WHERE {
  ?disciplina a :Disciplina ;
              :temAplicacao ?aplicacao .
}
"""

g.update(update_query)

print(len(g.serialize(format='turtle').decode("utf-8") if isinstance(g.serialize(), bytes) else g.serialize(format='turtle')))

with open("sapientia_ind_updated.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
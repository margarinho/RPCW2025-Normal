from rdflib import OWL, RDF, Graph, Namespace

g = Graph()
g.parse('sapientia_ind.ttl')

n = Namespace("http://www.semanticweb.org/magui/ontologies/2025/academia#")

if (n.daBasesPara, None, None) not in g:
    g.add((n.daBasesPara, RDF.type, OWL.ObjectProperty))

update_query = """

INSERT {
  ?disciplina :daBasesPara ?aplicacao .
}
WHERE {
  ?conceito :eEstudadoPor ?disciplina ;
          :temAplicacao ?aplicacao .
}
"""

g.update(update_query)

with open("sapientia_ind_updated_daBasesPara.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))
import subprocess

from rdflib import Graph

MERGED_ONTOLOGY_FILE = 'merged_ontology.rdf'

graph = Graph()
# TODO: all the files to merge come from command line argument
graph.parse('ontology.ttl', format='turtle')
graph.parse('module-individual.ttl', format='turtle')

subprocess.call(["python", "pyLODE/pylode/cli.py", "-i", MERGED_ONTOLOGY_FILE])

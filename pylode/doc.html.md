# Test Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test`
* **Version Information**
  * 
* **Imports**
  * <a href="http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test">http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test</a>
* **Ontology RDF**
  * <a href="merged_ontology.ttl">RDF (turtle)</a>
### Description
<p>This is just a test ontology</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Namespaces](#namespaces)  


## Overview

**Figure 1:** Ontology overview  
## Classes
[Album](#Album),
[Artist](#Artist),
[Canción](#Cancin),
[Individual](#Individual),
[Singer](#Singer),
### Individual <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test#Individual`
Sub-classes |<a href="http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Artist">Artist</a><sup class="sup-c" title="class">c</sup><br />
### Album <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Album`
### Artist <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Artist`
Super-classes |<a href="#Individual">default1:Individual</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Singer">Singer</a><sup class="sup-c" title="class">c</sup><br />
### Singer <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Singer`
Super-classes |<a href="http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Artist">Artist</a><sup class="sup-c" title="class">c</sup><br />
### Canción <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#Song`
Description | musical composition for voice(s)

## Object Properties
[part of](partof),
[played by](playedby),
[](partof)
### part of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#part_of`
Domain(s) |()<br />
[](playedby)
### played by <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#played_by`
Domain(s) |()<br />

## Namespaces
* **default (:)**
  * `http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test#`
* **:**
  * `http://www.semanticweb.org/alejandro/ontologies/2020/3/onto-publ-test#`
* **default1**
  * `http://www.semanticweb.org/alejandro/ontologies/2020/3/imported-onto-test#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Classes: c
* Object Properties :op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni
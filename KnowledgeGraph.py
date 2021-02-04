'''
Information Extraction is a process of extracting information in a more structured way i.e., 
the information which is machine-understandable. It consists of sub fields which cannot be easily solved. 
Therefore, an approach to store data in a structured manner is Knowledge Graph 
which is a set of three-item sets called Triple where the set combines a subject, a predicate and an object.'''


# Import our dependencies
import spacy
from spacy.lang.en import English
import networkx as nx
import matplotlib.pyplot as plt

# Use spaCy to split the text in sentences


def textToSentences(text):
    nlp = English()
    nlp.add_pipe('sentencizer')
    doc = nlp(text)
    return [str(sent).strip() for sent in doc.sents]


def printToken(token):
    print(token.text, '->', token.dep_)


def isRelationCandidate(token):
    deps = ['ROOT', 'adj', 'attr', 'agent', 'amod']
    return any(subs in token.dep_ for subs in deps)


def isConstructionCandidate(token):
    deps = ["compound", "prep", "conj", "mod"]
    return any(subs in token.dep_ for subs in deps)


def appendChunk(original, chunk):
    return original + ' ' + chunk


def processSubjectObjectPairs(tokens):
    subject = ''
    object = ''
    relation = ''
    subjectConstruction = ''
    objectConstruction = ''
    for token in tokens:
        printToken(token)
        if "punct" in token.dep_:
            continue
        if isRelationCandidate(token):
            relation = appendChunk(relation, token.lemma_)
        if isConstructionCandidate(token):
            if subjectConstruction:
                subjectConstruction = appendChunk(
                    subjectConstruction, token.text)
            if objectConstruction:
                objectConstruction = appendChunk(
                    objectConstruction, token.text)
        if "subj" in token.dep_:
            subject = appendChunk(subject, token.text)
            subject = appendChunk(subjectConstruction, subject)
            subjectConstruction = ''
        if 'obj' in token.dep_:
            object = appendChunk(object, token.text)
            object = appendChunk(objectConstruction, object)
            objectConstruction = ''
    print(subject.strip(), ",", relation.strip(), ",", object.strip())
    return (subject.strip(), relation.strip(), object.strip())


def processSentence(sentence):
    tokens = nlp_model(sentence)
    return processSubjectObjectPairs(tokens)


def printGraph(triples):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[1])
        G.add_edge(triple[1], triple[2])
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=700, node_color='skyblue', alpha=0.9,
            labels={node: node for node in G.nodes()})
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    text = "London is the capital and largest city of England and the United Kingdom. Standing on the River " \
        "Thames in the south-east of England, at the head of its 50-mile (80 km) estuary leading to " \
        "the North Sea, London has been a major settlement for two millennia. " \
        "Londinium was founded by the Romans. The City of London, " \
        "London's ancient core − an area of just 1.12 square miles (2.9 km2) and colloquially known as " \
        "the Square Mile − retains boundaries that follow closely its medieval limits." \
        "The City of Westminster is also an Inner London borough holding city status. " \
        "Greater London is governed by the Mayor of London and the London Assembly." \
        "London is located in the southeast of England." \
        "Westminster is located in London." \
        "London is the biggest city in Britain. London has a population of 7,172,036."

    sentences = textToSentences(text)
    nlp_model = spacy.load('en_core_web_sm')
    triple = []
    print(text)
    for sentence in sentences:
        triple.append(processSentence(sentence))
    printGraph(triple)

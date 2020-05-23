"""
Knowledge Graph library for use with ipycytoscape.

"""
import json

class Node(object):
    """
    Creates a node object.
    """
    def __init__(self, name, node_id, taxonomy_id="", href="", verbose=0):
        """
        :param name: Name of node object.
        :param node_id: ID tag of node object.
        :param taxonomy_id: Taxonomy ID (human or viral), optional.
        :param href: Node url, optional.
        """
        assert type(name) == str, "Name of node must be a string."
        assert type(node_id) == str, "Node ID must be a string."
        assert type(taxonomy_id) == str, "Taxonomy ID must be a string."
        assert type(href) == str, "Node url must be a string."
       
        self.name = name
        self.node_id = node_id
        self.taxonomy_id = taxonomy_id
        self.href = href
        
        if verbose == 1:
            print("Created Node: {name: " + name + ", id: " + node_id + ", taxonomy_id: " + taxonomy_id + ", href: " + href + "}.")
        
class Edge(object):
    """
    Creates an edge object.
    """
    def __init__(self, source, target, verbose=0):
        """
        :param source: Origin node.
        :param target: Target node.
        """
        self.source = source
        self.target = target
        
        if verbose == 1:
            print("Created Edge: {Source: " + source.node_id + ", Target: " + target.node_id + "}.")
        
    
class KnowledgeGraph(object):
    """
    Creates a base JSON object for storing nodes and edges.
    """   
    def __init__(self):
        self.num_nodes = 0
        self.data = {"nodes": [], "edges": []}           
       
    def add_node(self, Node):
        """
        :param Node: Node object to add.
        """
        new_node = {"data": {"id": Node.node_id, "name": Node.name, "taxonomy" : Node.taxonomy_id, "href": Node.href}}
        self.data["nodes"].append(new_node)
        
    def add_edge(self, Edge):
        """
        :param Edge: Edge object to add.
        """
        new_edge = {"data": {"source": Edge.source.node_id, "target": Edge.target.node_id}}
        self.data["edges"].append(new_edge)
        
    def save_to_JSON(self, filename, filepath):
        """
        :param filepath: File location and name to save JSON.
        """
        assert type(filename) == str, "Name must be a string."
        assert type(filepath) == str, "Path must be a string."
        
        with open(filename + ".json", "w") as json_file:
            json.dump(self.data, json_file)       
        
        
        
        
        
        
        
        
        
        
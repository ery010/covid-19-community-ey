"""
Knowledge Graph library for use with ipycytoscape.

"""
import ipycytoscape
import json

class Node(object):
    """
    Creates a node object.
    """
    def __init__(self, name, node_id, taxonomy_id="", href="", color="red", description="", verbose=0):
        """
        :param name: Name of node object.
        :param node_id: ID tag of node object.
        :param taxonomy_id: Taxonomy ID (human or viral), optional.
        :param href: Node url, optional.
        :param color: Color of node, default is red.
        """
        assert type(name) == str, "Name of node must be a string."
        assert type(node_id) == str, "Node ID must be a string."
        assert type(taxonomy_id) == str, "Taxonomy ID must be a string."
        assert type(href) == str, "Node url must be a string."
        assert type(color) == str, "Node color must be a string."
        assert type(description) == str, "Description must be a string."
        
        self.name = name
        self.node_id = node_id
        self.taxonomy_id = taxonomy_id
        self.href = href
        self.color = color
        
        if description != "":
            self.description = "<br>" + description
        else:
            self.description = description
            
        self.children = []
        self.num_children = 0
        
        if verbose == 1:
            print("Created Node: {name: " + name + ", id: " + node_id + ", taxonomy_id: " + taxonomy_id + ", href: " + href + "}.")
            print("Color: " + color)
        
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
        source.children.append(target.name)
        source.num_children += 1
        
        if verbose == 1:
            print("Created Edge: {Source: " + source.node_id + ", Target: " + target.node_id + "}.")
        
    
class KnowledgeGraph(object):
    """
    Creates a base JSON object for storing nodes and edges.
    """   
    def __init__(self):
        self.num_nodes = 0
        self.data = {"nodes": [], "edges": []}
        self.stats = {}
        self.style = [{
                        'selector': 'node',
                        'css': {
                            'content': 'data(protein_name)',
                            'text-valign': 'center',
                            'color': 'white',
                            'text-outline-width': 2,
                            'text-outline-color': 'data(color)',
                            'background-color': 'data(color)'
                        }
                        },
                        {
                        'selector': ':selected',
                        'css': {
                            'background-color': 'black',
                            'line-color': 'black',
                            'target-arrow-color': 'black',
                            'source-arrow-color': 'black',
                            'text-outline-color': 'black'
                        }}
                        ]
       
    def add_node(self, Node):
        """
        :param Node: Node object to add.
        """
        new_node = {"data": {"id": Node.node_id,
                             "protein_name": Node.name,
                             "name": "UniProt: <a href=" + Node.href + ">" + Node.name + "</a>" + Node.description, 
                             "taxonomy" : Node.taxonomy_id, 
                             "href": Node.href, 
                             "color": Node.color}}
        self.data["nodes"].append(new_node)
        
    def add_edge(self, Edge):
        """
        :param Edge: Edge object to add.
        """
        new_edge = {"data": {"source": Edge.source.node_id, "target": Edge.target.node_id}}
        self.data["edges"].append(new_edge)
        
        if Edge.source.name not in self.stats.keys():
            self.stats[Edge.source.name] = 1
        else:
            self.stats[Edge.source.name] +=1
        
    def save_to_JSON(self, filename, filepath):
        """
        :param filename: File name to save JSON as.
        :param filepath: File location and name to save JSON.
        """
        assert type(filename) == str, "Filename must be a string."
        assert type(filepath) == str, "Path must be a string."
        
        with open(filepath + filename + ".json", "w") as json_file:
            json.dump(self.data, json_file)       
            
    def data_from_JSON(self, filename, filepath):
        """
        :param filename: File name to import JSON data from.
        :param filepath: File location to import JSON file from.
        """
        assert type(filename) == str, "Filename must be a string."
        assert type(filepath) == str, "Path must be a string."
        
        with open(filepath + filename) as new_file:
            json_file = json.load(new_file)
        
        self.data = json_file
        
    def load_graph(self, spacing=30):
        """
        :param spacing: Amount of spacing between nodes, default is 30.
        """
        cytoscapeobj = ipycytoscape.CytoscapeWidget()
        cytoscapeobj.graph.add_graph_from_json(self.data)
        cytoscapeobj.set_style(self.style)
        cytoscapeobj.set_layout(nodeSpacing=spacing)
        
        return cytoscapeobj      
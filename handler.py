from info import info
import graphviz
import networkx


def handle(pb2_request, repo_path):

  # Create empty graph
  graph = networkx.Graph()

  # Read the input text
  input_text = """c This file describes a tree decomposition with 3 bags, width 1, for a graph with 5 vertices
s tree_decomposition 3 1 5
b 1 2 3
b 2 1
b 3 1
1 2
1 3"""

  # Split the input text into lines
  lines = input_text.strip().split('\n')

  # Parse the tree decomposition
  for line in lines:
      if line.startswith('b'):
          bag_nodes = list(map(int, line.split()[1:]))
          bag_id = 'b{}'.format(bag_nodes[0])
          graph.add_node(bag_id, label=','.join(map(str, bag_nodes[1:])), fillcolor='#ff8c00b2')
      elif not line.startswith('s') and not line.startswith('c'):
          u, v = map(int, line.split())
          graph.add_edge('b{}'.format(u), 'b{}'.format(v), color='#ff8c00b2')

  # Create the DOT source code
  dot_source = 'graph {\nbgcolor=transparent\n'
  for node, data in graph.nodes(data=True):
      dot_source += '{} [label="{}", fillcolor="{}"]\n'.format(node, data['label'], data['fillcolor'])
  for u, v, data in graph.edges(data=True):
      dot_source += '{} -- {} [color="{}"]\n'.format(u, v, data['color'])
  dot_source += '}'

  # Render the DOT source code as an SVG image
  pygraphviz_graph = networkx.drawing.nx_agraph.to_agraph(graph)
  svg_code = graphviz.Source(pygraphviz_graph.to_string()).pipe(format='svg').decode('utf-8')

  # Output the SVG image
  print(svg_code)

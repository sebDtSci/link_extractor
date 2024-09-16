from ocr import ocr
import networkx as nx
import matplotlib.pyplot as plt


def extract_info_from_images(image_paths):
    image_info = {}
    for img_path in image_paths:
        text = ocr(img_path)
        image_info[img_path] = text
    return image_info

def create_graph(image_info):
    G = nx.Graph()
    for image, text in image_info.items():
        words = text.split()
        for word in words:
            G.add_edge(image, word)
    return G

def plot_graph(G):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
    plt.show(block=True)  # Ensure the graph is shown

# Exemple d'utilisation
image_paths = ['sms-1.jpg', 'image-2.jpg']  # Liste des chemins vers les images
image_info = extract_info_from_images(image_paths)
graph = create_graph(image_info)
plot_graph(graph)
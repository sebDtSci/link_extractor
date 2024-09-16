import re
import networkx as nx

def process_doc(filepath: str) -> str:
    doc = {}
    with open(filepath, "r") as f:
        text = get

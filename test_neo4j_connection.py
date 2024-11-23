from dotenv import load_dotenv
import os
from langchain_community.graphs import Neo4jGraph

import warnings
warnings.filterwarnings("ignore")

load_dotenv(".env")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

def load_knowledge_graph(kg):
    cypher = """
        CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
        """
    kg.query(cypher)

def match_movie(kg):
    cypher = """
        MATCH (matrix:Movie {title: "The Matrix"})
        RETURN matrix
    """

    result = kg.query(query=cypher)
    return result

if __name__ == "__main__":
    kg = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE)
    load_knowledge_graph(kg)
    print(match_movie(kg))
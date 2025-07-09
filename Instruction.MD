# Instructions for MCP, A2A, and LangGraph

This document provides a guide on how to use the Model Context Protocol (MCP), Agent2Agent (A2A) Protocol, and LangGraph for building multi-agent systems. It also includes links to the official documentation and relevant resources.

## Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard that enables a two-way connection between AI models and external data sources or tools. It allows developers to securely provide context to Large Language Models (LLMs). Think of it as a standardized way to connect AI models to different data sources and tools.

### Key Concepts

*   **Server**: An MCP server exposes resources, tools, and prompts to an AI model.
*   **Resources**: Read-only data sources that provide structured information to an LLM.
*   **Tools**: Functions that allow an LLM to perform actions or interact with external APIs.
*   **Prompts**: Reusable instruction templates to guide the LLM's behavior.

### Using the Python SDK

The official Python SDK for MCP simplifies the process of creating servers and clients.

#### Installation

It is recommended to use a virtual environment for your project.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]"
```

#### Creating a Simple MCP Server

Here's an example of a server that exposes a simple "add" tool:

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("CalculatorServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b
```

### Useful Links
*   **Official MCP Documentation:** [https://docs.modelcontext.dev/](https://docs.modelcontext.dev/)
*   **Python SDK on GitHub:** [https://github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
*   **MCP Introduction:** [https://docs.modelcontext.dev/introduction](https://docs.modelcontext.dev/introduction)

## Agent2Agent (A2A) Protocol

The Agent2Agent (A2A) protocol is an open standard designed for communication and collaboration between AI agents. It allows different agent frameworks to work together without needing custom integration code.

### Key Concepts

*   **AgentCard**: A JSON document that describes an agent's capabilities, skills, and how to interact with it.
*   **Agent Executor**: The core logic that processes requests and generates responses for an agent.
*   **Messages**: The units of communication within the A2A protocol, representing a single turn in a conversation.

### Using the Python SDK

The official A2A Python SDK provides the tools to build A2A-compliant agents.

#### Installation
```bash
pip install a2a-python
```

#### Building an A2A Agent

An A2A agent consists of an AgentCard and an Agent Executor. The server is typically run using Uvicorn.

1.  **Define the AgentCard**: Create a JSON file that describes your agent.
2.  **Implement the Agent Executor**: Create a class that inherits from `AgentExecutor` and implements the agent's logic.
3.  **Run the Server**: Use the `a2a-sdk` to run a Uvicorn server that hosts your agent.

### Useful Links
*   **Official A2A Protocol Site:** [https://a2a.dev/](https://a2a.dev/)
*   **A2A Python SDK on GitHub:** [https://github.com/a2aproject/a2a-python](https://github.com/a2aproject/a2a-python)
*   **A2A Introduction and Key Concepts:** [https://a2a.dev/docs/key-concepts](https://a2a.dev/docs/key-concepts)

## LangGraph

LangGraph is a library for building stateful, multi-agent applications with LLMs. It is part of the LangChain ecosystem and allows you to represent agent workflows as graphs. Nodes represent actions and edges represent the transitions between them.

### Key Concepts

*   **State**: A central object that holds the current state of the application and is passed between nodes.
*   **Nodes**: Python functions that perform a unit of work, such as calling an LLM, processing data, or interacting with a tool.
*   **Edges**: Connections between nodes that define the flow of the application. Edges can be conditional, allowing for dynamic branching.

### Using LangGraph

#### Installation
```bash
pip install langgraph
```

#### Building a Simple Graph
Here is a conceptual overview of building a graph:

1.  **Define the State**: Create a `TypedDict` to represent the state of your graph.
2.  **Create Nodes**: Write Python functions that take the state as input and return an updated state.
3.  **Build the Graph**: Use `StateGraph` to add nodes and edges, defining the workflow.
4.  **Compile and Run**: Compile the graph into a runnable object and execute it.

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# 1. Define the State
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

# 2. Define Nodes
def node_a(state):
    print("Executing Node A")
    return {"messages": ["Message from Node A"]}

def node_b(state):
    print("Executing Node B")
    return {"messages": ["Message from Node B"]}

# 3. Build the Graph
workflow = StateGraph(AgentState)
workflow.add_node("a", node_a)
workflow.add_node("b", node_b)
workflow.set_entry_point("a")
workflow.add_edge("a", "b")
workflow.add_edge("b", END)

# 4. Compile and Run
app = workflow.compile()
app.invoke({"messages": []})
```

### Useful Links
*   **LangGraph Documentation:** [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
*   **LangChain Python on GitHub:** [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
*   **Introductory Blog Post:** [https://blog.langchain.dev/langgraph/](https://blog.langchain.dev/langgraph/)

## Gemini API

The Gemini API gives you access to Google's latest generative models. You can use it for a variety of use cases, including content generation, dialogue agents, and summarization.

### Useful Links
*   **Official Gemini API Documentation:** [https://ai.google.dev/docs](https://ai.google.dev/docs)
*   **Gemini API Quickstart (Python):** [https://ai.google.dev/tutorials/python_quickstart](https://ai.google.dev/tutorials/python_quickstart)
import pandas as pd
import re

# Input Markdown table as a string
markdown_table = """
|Index | Time | Title                                                        |  Publication  |                            Paper                             |
| :--: | :--: | ------------------------------------------------------------ | :-----------: | :----------------------------------------------------------: |
| 1 | 2023.09 | **PlanBench An Extensible Benchmark for Evaluating** | NIPS 2023 | [link](https://openreview.net/pdf?id=YXogl4uQUO) |
| 2 | 2024.09 | **LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench** | NIPS 2024 | [link](https://openreview.net/forum?id=Gcr1Lx4Koz) |
| 3 | 2024.11 | **An automatic end-to-end chemical synthesis development platform powered by large language models** | Nature Communications| [link](https://www.nature.com/articles/s41467-024-54457-x) |
| 4 | 2023.12 | **Autonomous chemical research with large language models** | NIPS 2024 | [link](https://www.nature.com/articles/s41586-023-06792-0) |
| 5 | 2018.05 | **Planning chemical syntheses with deep neural networks and symbolic AI** | Nature | [link](https://www.nature.com/articles/nature25978) |
| 6 | 2020.10 | **Computational planning of the synthesis of complex natural products** | Nature | [link](https://www.nature.com/articles/s41586-020-2855-y) |
| 7 | 2024.05 | **Augmenting large language models with chemistry tools** | Nature | [link](https://www.nature.com/articles/s42256-024-00832-8) |
| 8 | 2024.07 | **Retrosynthesis prediction with an iterative string editing model** | Nature Communications| [link](https://www.nature.com/articles/s41467-024-50617-1) |
| 9 | 2024.02 | **Leveraging large language models for predictive chemistry** | Nature Machine Intelligence| [link](https://www.nature.com/articles/s42256-023-00788-1?fromPaywallRec=false) |
| 10 | 2024.03 | **Efficient retrosynthetic planning with MCTS exploration enhanced A* search** | Nature Communications Chemistry| [link](https://www.nature.com/articles/s42004-024-01133-2) |
| 11 | 2013.12 | **Towards a Planning-Based Approach to the Automated Design of Chemical Processes** | AIBP@AI* IA 2013| [link](https://ceur-ws.org/Vol-1101/paper3.pdf) |
| 12 | 2015.12 | **Exploring Organic Synthesis with State-of-the-Art Planning Techniques** | GCAI 2015| [link](https://www.cs.ryerson.ca/~mes/publications/MatloobSoutchanskiExploringOrganicSynthesisWithState-of-the-ArtPlanning_SPARK2016.pdf) |
| 13 | 2015.12 | **Computer-aided key step generation in alkaloid total synthesis** | Science| [link](https://www.science.org/doi/10.1126/science.ade8459) |
| 14 | 2024.01 | **Retro-fallback: retrosynthetic planning in an uncertain world** | ICLR 2024| [link](https://openreview.net/forum?id=dl0u4ODCuW) |
| 15 | 2023.10 | **Re-evaluating Retrosynthesis Algorithms with Syntheseus** | NIPS 2023| [link](https://openreview.net/forum?id=W5U18rgtpg) |
| 16 | 2022.01 | **Chemformer: a pre-trained transformer for computational chemistry** |  Machine Learning| [link](https://iopscience.iop.org/article/10.1088/2632-2153/ac3ffb) |
"""

# Step 1: Parse the markdown table into a pandas DataFrame
# Use regex to capture the rows and columns from the markdown table
data = []
md_table = markdown_table.strip().split("\n")

header = md_table[:2]
rows = md_table[2:]  # Skip the header and separator

for row in rows:
    cols = re.split(r"\s*\|\s*", row.strip("|"))
    data.append(cols)  # Exclude the first empty column (for the index)

columns = ['Index', 'Time', 'Title', 'Publication', 'Paper']
df = pd.DataFrame(data, columns=columns)

# Step 2: Sort the DataFrame by the "Time" column
df['Time'] = pd.to_datetime(df['Time'], format='%Y.%m')  # Convert Time to datetime format
df = df.sort_values(by='Time', ascending=True)

# Step 3: Convert the sorted DataFrame back into a Markdown table format
sorted_markdown = '\n'.join(header)+'\n'

for i, (index, row) in enumerate(df.iterrows()):
    sorted_markdown += f"| {i+1} | {row['Time'].strftime('%Y.%m')} | {row['Title']} | {row['Publication']} | {row['Paper']} |\n"

# Print the sorted Markdown table
print(sorted_markdown)

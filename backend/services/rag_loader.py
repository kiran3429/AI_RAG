import json
from pathlib import Path

RAG_DIRECTORY = Path("rag_types")


def get_available_rags():

    rag_list = []

    if not RAG_DIRECTORY.exists():
        return rag_list

    for rag_folder in RAG_DIRECTORY.iterdir():

        if not rag_folder.is_dir():
            continue

        config_file = rag_folder / "config.json"

        if config_file.exists():

            with open(config_file, "r") as file:

                rag_list.append(json.load(file))

    return rag_list
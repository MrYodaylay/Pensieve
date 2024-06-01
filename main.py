import argparse
import pathlib

import strictyaml

from pensieve import ModelProvider
from pensieve import Document, DocumentIndex


def main():

    # Parse command line arguments
    cli = argparse.ArgumentParser()
    cli.add_argument("input", type=pathlib.Path)
    cli.add_argument("-c", "--config", type=pathlib.Path)
    cli.add_argument("-o", "--output", type=pathlib.Path)
    args = cli.parse_args()

    # FUTURE Check command line arguments

    # Parse configuration file
    with open(args.config, "r") as config_file:
        config = strictyaml.load(config_file.read(), None).data

    # Iterate input directory / files
    document_index = DocumentIndex(args.input)

    # Authenticate with provider
    model_provider = ModelProvider(config["completions"]["provider"])
    model_provider.auth(config["completions"]["auth"])

    # Get model class
    model = model_provider.get_model(config["completions"]["model"])
    model.system_prompt(config["completions"]["system_prompt"])


    model.get_completion(document_index.get_document(0))


if __name__ == "__main__":
    main()


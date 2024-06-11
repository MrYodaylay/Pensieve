import argparse
import pathlib

import strictyaml

from pensieve import ModelProvider, Processor
from pensieve import Document, Index


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
    submission_index = Index(args.input)

    # Authenticate with provider
    model_provider = ModelProvider(config["completions"]["provider"], auth=config["completions"]["auth"])

    # Get model class
    model = model_provider.get_model(config["completions"]["model"])

    # Generate completions
    processor = Processor(
        model, prompt=config["completions"]["system_prompt"]
    )
    processor.run(submission_index)

    submission_index.write_csv()


if __name__ == "__main__":
    main()

import csv
from pathlib import Path

from pensieve.document import Document
from pensieve.submission import Submission


class Index:

    def __init__(self, path: Path):

        path = path.resolve()
        if not path.exists():
            raise FileNotFoundError(f"Path \"{path}\" cannot be found.")

        self._submissions = list()

        if path.is_dir():
            self._import_directory(path)
            self.base_path = path

        elif path.is_file():
            self._import_file(path)
            self.base_path = path.parent

        else:
            raise FileNotFoundError(f"Path \"{path}\" is neither a file nor directory.")

    def __iter__(self):
        return self._submissions.__iter__()

    def _import_directory(self, directory: Path):

        for file in directory.iterdir():
            self._import_file(file)

    def _import_file(self, file: Path):

        if file.is_file():
            self._submissions.append(Submission(file))

    def get_submission(self, i: int):
        return self._submissions[i]

    def write_csv(self):
        with open(self.base_path.joinpath("output.csv"), "wt", encoding="utf-8", errors="replace", newline="") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, doublequote=False, quotechar="\"", escapechar="\\")

            for submission in self._submissions:

                if submission is None or submission.document is None:
                    continue

                try:
                    row = [submission.name]
                    for line in submission.response.lines:
                        row.append(line.replace("\"", "\'"))

                    writer.writerow(row)
                except Exception as e:
                    writer.writerow([submission.name, str(e)])

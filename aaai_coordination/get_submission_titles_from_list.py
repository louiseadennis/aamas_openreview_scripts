import openreview
import os
import argparse
import json
import logging
import client_object

from pathlib import Path

LOG = logging.getLogger()

# Modify this function to support loading submission IDs from different file formats
def read_submissions_file(submissions_file: Path) -> list[str]:
    with submissions_file.open('r') as fd:
        submissions_ids = [line.strip() for line in fd.readlines() if line.strip()]
    return submissions_ids


def get_openreview_credentials():
    credentials_file = Path(".openreview_credentials")
    if credentials_file.exists():
        with open(credentials_file, "r") as fh:
            lines = fh.readlines()
            if len(lines) >= 2:
                return lines[0].strip(), lines[1].strip()

    username = os.getenv("OPENREVIEW_USER")
    password = os.getenv("OPENREVIEW_PASS")
    if username and password:
        return username, password

    username = input("Enter your OpenReview username: ")
    password = input("Enter your OpenReview password: ")
    return username, password




def make_parser():
    parser = argparse.ArgumentParser(
            description="Downloads PDF of each openreview submission listed in the input file")
    parser.add_argument("submissions_file", type=Path, help="Text file with one submission ID per line")
    return parser


def main(submissions_file):
    submissions_ids = read_submissions_file(submissions_file)
    client = client_object.client
    venue_id = client_object.venue_id

    submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
    
    for note in submissions:
        if note.id in submissions_ids:
            print(note.content['title'])


if __name__ == "__main__":
    args = make_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main(args.submissions_file)

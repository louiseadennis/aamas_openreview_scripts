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


def download_submission_pdfs(submission_ids, pdf_dir):
    # username, password = get_openreview_credentials()
    client = client_object.client

    LOG.info(f"Downloading PDFs to {pdf_dir}...")
    pdf_dir.mkdir(exist_ok=True)

    submissions_no_pdf = []
    for submission_id in submission_ids:
        pdf_path = pdf_dir / f"{submission_id}.pdf"
        try:
            pdf_data = client.get_pdf(submission_id)
        except Exception as e:
            LOG.error(f"Error downloading PDF for {submission_id}: {e}")
            submissions_no_pdf.append(submission_id)
            continue
        with open(pdf_path, 'wb') as f:
            f.write(pdf_data)
    if len(submissions_no_pdf) > 0:
        LOG.error(f"Number of submissions with no PDF={len(submissions_no_pdf)}")


def make_parser():
    parser = argparse.ArgumentParser(
            description="Downloads PDF of each openreview submission listed in the input file")
    parser.add_argument("submissions_file", type=Path, help="Text file with one submission ID per line")
    parser.add_argument("pdf_dir", type=Path, help="Output directory")
    return parser


def main(submissions_file, pdf_dir):
    submissions_ids = read_submissions_file(submissions_file)
    download_submission_pdfs(submissions_ids, pdf_dir)


if __name__ == "__main__":
    args = make_parser().parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main(args.submissions_file, args.pdf_dir)

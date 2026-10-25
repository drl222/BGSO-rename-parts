# encoding: utf-8
# see https://github.com/jontingvold/pyrankvote
import pyrankvote
from pyrankvote import Candidate, Ballot
import csv
import sys

ordering_text_to_number = {
    'First Choice': 1,
    'Second Choice': 2,
    'Third Choice': 3,
    'Fourth Choice': 4,
    'Fifth Choice': 5,
}

def run_stv(filename):
    with open(filename, newline='') as f:
        csvreader = csv.reader(f)
        
        # read candidates from the header
        candidates_raw = next(csvreader)
        candidates = [Candidate(candidate) for candidate in candidates_raw]

        # raw ballots have fixed columns being the candidates, and the entries in the columns being the personal ranking
        # enumerate and sort to get the reverse: columns are the personal rankings, and entries in the columns are candidate names
        ordered_votes = [sorted([(ordering_text_to_number[order_i], candidates[choice_i]) for choice_i, order_i in enumerate(row)]) for row in csvreader]
        ballots = [Ballot([candidate for order, candidate in vote]) for vote in ordered_votes]

    election_result = pyrankvote.single_transferable_vote(candidates, ballots, 2)
    winners = election_result.get_winners()

    print(f"TOTAL NUMBER OF BALLOTS: {len(ballots)}")
    print(election_result)
    print(winners)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the name of the raw results file")
        exit()
    source = sys.argv[1]
    run_stv(source)
# -*- coding: UTF-8 -*-
"""
rvt_journal_parser
find specific messages in a given journal file
to detect model corruption, missing links and the like.
"""
import os.path as op

model_corrupt = 'orrupt'
missing_links = 'TaskDialog "Revit could not find or read'
circular_link_conflict = 'TaskDialog_Circular_Link_Conflict'
key_phrases = {missing_links: "missing_links",
               model_corrupt: "corrupt",
               circular_link_conflict: "circular links",
               }


def read_journal(journal_path):
    """
    reads journal file to detect key phrases
    :param journal_path: journal file path
    :return:dict
    """
    detected = {}
    with open(journal_path, 'rb') as journal:
        journal_name = op.basename(journal_path)
        for line in journal:
            decoded_line = line.decode("latin1", "ignore")
            if model_corrupt in decoded_line:
                print("!!_Corrupt_Model_!!")
                print(journal_path)
                print(decoded_line)
                detected[journal_name] = key_phrases[model_corrupt]
            if missing_links in decoded_line:
                print("!!_Missing_Links_!!")
                print(journal_path)
                print(decoded_line)
                detected[journal_name] = key_phrases[missing_links]
    return detected

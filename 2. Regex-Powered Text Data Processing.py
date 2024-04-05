# Task 1: Email Extractor:

import re

def extract_emails(filename):
    email_list = set()
        
    with open(filename, "r") as file:
        email_list = []
        for line in file:
            strip_line = line.strip()
            print(strip_line)
            emails = re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", strip_line)
            if emails:
                email_list.append(emails)

    print(email_list)


extract_emails("contacts.txt")
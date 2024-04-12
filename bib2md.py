import bibtexparser

def convert_bib_to_md(bib_filename, md_filename):
    with open(bib_filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Sort the entries by year in descending order
    sorted_entries = sorted(bib_database.entries, key=lambda entry: entry.get('year', ''), reverse=True)

    md_bibliography = ""
    for i, entry in enumerate(sorted_entries):
        authors = entry['author'].replace(' and ', ', ')
        title = entry['title']
        journal = entry['journal']
        volume = entry.get('volume', '')
        pages = entry.get('pages', '')
        year = entry.get('year', '')
        doi = entry.get('doi', '')
        url = entry.get('url', '')

        doi_link = f'[{doi}]({url})' if doi else ''
        md_entry = f'{i+1}. {authors}. **{title}.** *{journal}*, {volume}, {pages} ({year}). {doi_link}\n\n'
        md_bibliography += md_entry

    with open(md_filename, 'w') as md_file:
        md_file.write(md_bibliography)

# Usage
bib_filename = 'your_bib_file.bib'  # replace with your .bib file
md_filename = 'your_md_file.md'  # replace with your desired .md file
convert_bib_to_md(bib_filename, md_filename)

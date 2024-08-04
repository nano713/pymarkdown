import bibtexparser

def convert_bib_to_md(bib_filename, md_filename):
    with open(bib_filename, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Sort the entries by year in descending order
    sorted_entries = sorted(bib_database.entries, key=lambda entry: entry.get('year', ''), reverse=True)

    year_min = '3000'  # future years
    md_bibliography = ""
    for i, entry in enumerate(sorted_entries):
        authors = entry['author'].replace(' and ', ', ')
        title = entry['title']
        if entry.get('journal'):
            journal = entry['journal']
        elif entry.get('publisher'):
            journal = entry['publisher']
        volume = entry.get('volume', '')
        pages = entry.get('pages', '')
        year = entry.get('year', '')
        doi = entry.get('doi', '')
        url = entry.get('url', '')
        pdf = entry.get('pdf', '')
        if pdf:
            pdf_link = '[{{< icon "download" >}}]('+f'{pdf})'
        else:
            pdf_link = ''

        md_entry = f'{i+1}. **{title}**.\n{authors}. [*{journal}*, {volume}, {pages} ({year}).]({url}) {pdf_link}\n\n'
        
        # Convert Daichi Kozawa into **Daichi Kozawa**
        md_entry = md_entry.replace('Daichi Kozawa', '<u>Daichi Kozawa</u>')
        
        if int(year) < int(year_min):
            md_entry = f'## {year}\n'+md_entry
        
        md_bibliography += md_entry
        year_min = min(year, year_min)

    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_bibliography)

# Usage
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QFileDialog

    app = QApplication([])
    bib_filename, _ = QFileDialog.getOpenFileName(None, "Select a .bib file", "", "BibTex Files (*.bib)")

    md_filename = bib_filename[:-4] + '.md'
    convert_bib_to_md(bib_filename, md_filename)

# pymarkdown

# bib2md.py
BibTeX to Markdown Converter for Hugo

This Python script is originally intended to be used with Hugo, a popular static site generator. It converts a BibTeX bibliography file into a Markdown file that can be used to create a bibliography page on a Hugo website. The entries in the Markdown file are sorted by year in descending order and formatted in a specific style.

## Dependencies

This script requires the `bibtexparser` library. You can install it using pip:

```bash
pip install bibtexparser
```

## Usage
To use this script, you need to specify the paths to your input .bib file and your desired output .md file in the bib_filename and md_filename variables, respectively:

```Python
bib_filename = 'your_bib_file.bib'  # replace with your .bib file
md_filename = 'your_md_file.md'  # replace with your desired .md file
convert_bib_to_md(bib_filename, md_filename)
```

Then, run the script. It will read the .bib file, convert each entry into a Markdown formatted string, and write the strings to the .md file.

## Output Format
Each entry in the .bib file is converted into the following format in the .md file:

```Markdown
1. Author1, Author2, ..., AuthorN. **Title.** *Journal*, Volume, Pages (Year). DOI
```

If the volume, pages, year, doi, or url field is not present in an entry in the .bib file, it will be omitted in the corresponding Markdown entry.

## Note
This script assumes that each entry in your .bib file contains the fields author, title, and journal. If some entries do not contain these fields, you may need to modify the script accordingly.

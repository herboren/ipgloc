import csv, os, path, keyterms

# Get column headers
columns = keyterms.KeyTerms().report_columns

# threat_Template Path
template = f'{os.getcwd()}\\template\Threat_Template.csv'

# Check for output, touch if no exist.
if not os.path.exists(template):
    f = open(template, 'a')
    f.write('')

# Lets load the threat_template
with open(template, 'w', encoding='utf-8', newline='') as tt:
    tt_write = csv.writer(tt, dialect='excel')
    tt_write.writerow(columns)

f.close()


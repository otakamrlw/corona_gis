from tabula import read_pdf
import tabula
import pandas as pd

# paths
pdf_path = "/Users/takayuki/Document/career/nagoyaU/corona/報道発表_pdf/4月/20200401.pdf"
directory_path = "/Users/takayuki/Document/career/nagoyaU/corona/報道発表_pdf/4月"
template_path = "/Users/takayuki/Document/career/nagoyaU/corona/tabula-template.json"

# Read pdf into DataFrame
# df = tabula.io.read_pdf(pdf_path, output_format="dataframe", pages=1, lattice=True, encoding="utf-8")
# df = tabula.io.read_pdf_with_template(pdf_path, template_path, output_format="dataframe", pages=1, lattice=True, encoding="utf-8")
# print(df)

# df.to_csv("output.csv", encoding='utf-8')

# convert PDF into CSV
# tabula.convert_into(pdf_path, "output2.csv", output_format="csv", lattice=True, pages=1)
# tabula.convert_into(pdf_path, "test.csv", output_format="csv", pages=1, lattice=True)
# # convert all PDFs in a directory
tabula.convert_into_by_batch(directory_path, output_format='csv', lattice=True, pages=1, java_options="-Dfile.encoding=utf-8")
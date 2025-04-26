import functionsNakada

# how to use "getTableFromPDF"
# you need to set two parameters getTableFromPDF(file, pages)
# file: "1" for CAMS report
# pages: [80,81,82] => pages you want to extract

pages = [80,81,82]
res = functionsNakada.getTableFromPDF(1, pages)

for item in res:
    print('--------------------------------------------')
    print('table page number is', item)
    print(res[item])


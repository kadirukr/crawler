import webcrawler
import pandas as pd

def main():
    
    docArray = webcrawler.xyz().getPages()
    print(docArray)
    #print(webcrawler.WebScrapper().lessorNamesArray(docArray))
    #print(webcrawler.WebScrapper().lessorPLZArray(docArray))
    #print(webcrawler.WebScrapper().lessorOrtArray(docArray))

    #array1=webcrawler.WebScrapper().lessorNamesArray(docArray)
    #array2=webcrawler.WebScrapper().lessorPLZArray(docArray)
    #array3=webcrawler.WebScrapper().lessorOrtArray(docArray)

    #dic = {"Lessor Name":array1, "PLZ":array2, "Ort":array3}
    #df = pd.DataFrame(data=dic)
    
    #df.to_csv('/Users/kadiruelker/Desktop/webcrawler/data.csv', encoding='utf-8')


if __name__ == '__main__':
    main()

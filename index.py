import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import xlrd
 
loc = ("c://ecp/test.xls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
 

# stop = stopwords.words('english')
# text = "my package from amazon never arrived fix this asap"
# text = " ".join([word for word in text.split() if word not in (stop)])
# print(text)
 
def jaccard_similarity(x,y):
  """ returns the jaccard similarity between two lists """
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)
sentences =  []

for i in range(sheet.nrows):
    if i != 0:
        print(sheet.cell_value(i, 2))
        sentences.append(sheet.cell_value(i, 2))
sentences = [sent.lower().split(" ") for sent in sentences]


 
 
for i in range(len(sentences)):
  for j in range(i+1 ,len(sentences)):
    #  print(sentences[i])
    #  print(sentences[j])
     print(jaccard_similarity(sentences[i],sentences[j]))
     score = jaccard_similarity(sentences[i],sentences[j])
     if score == 1.0:
       print(score)
       sentences.remove(sentences[i])
       break
print(sentences)
 
 
  
   
 

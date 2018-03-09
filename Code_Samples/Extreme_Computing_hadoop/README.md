
# Task 1 Inverted index with MapReduce

Use the files in the folder /data/assignments/ex2/task1/large/ as input and produce an inverted
index using MapReduce. For instance, given the following documents: 

  d1.txt: cat dog cat fox
  d2.txt: cat bear cat cat fox
  d3.txt: fox wolf dog

you should build the following full inverted index.

bear : 1 : {(d2.txt,1)}
cat : 2 : {(d1.txt, 2), (d2.txt, 3)}
dog : 2 : {(d1.txt, 1), (d3.txt, 1)}
fox : 3 : {(d1.txt, 1), (d2.txt, 1), (d3.txt, 1)}
wolf : 1 : {(d3.txt,1)}

For each term (anything separated by spaces), there is a single record consisting of a number and
a list of what are termed postings; the colon character (‘:’) is used to delimit the fields of each record.
There are also colons in the document, but just leave them as-is. The first field is a number that represents
the number of documents that contain the term. Then a list of postings follows where each posting
is a pair consisting of the document name and the frequency of the word in that specific document. Note
that terms are sorted alphabetically and also that the items inside lists are also sorted alphabetically by
document identifier. For example, the following line:

cat : 2 : {(d1.txt, 2), (d2.txt, 3)}

indicates that the word cat appears in two documents, two times in document d1.txt and three times
in document d2.txt. Instead of hdfs://scutter01.inf.ed.ac.uk:8020/data/incredibly/long/path/d1.txt,
just use d1.txt.
To get the full path to the input file in Hadoop streaming, read the mapreduce_map_input_file environment
variable. In Python, that’s os.environ["mapreduce_map_input_file"]. Use a single space
between elements in your inverted index (not a tab, and not double-spaces)

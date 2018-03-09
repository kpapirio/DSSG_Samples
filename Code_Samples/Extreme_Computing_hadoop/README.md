# 1.1 Inverted index with MapReduce
## Task 1 Inverted index with MapReduce

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
document identifier.


# 1.2 Parsing StackOverflow
For tasks 2-4, you will use a dataset from StackOverflow (stackLarge.txt) and extract specific
pieces of information. Initially, you should understand the format of the dataset, next you will need to
parse each post, and finally you will need to implement your MapReduce workflows. Use MapReduce
for tasks 2-4.

The dataset contains a number of post records, one record per line. Each record consists of commaseparated
key-value pairs, which are then pointlessly wrapped in an XML element. That is, a record
looks like:

    <row attribute1=value1, attribute2=value2, ..., attributeN=valueN />

Each record has its own identifier stored in a field named Id and a type, indicated by the value of a field
PostTypeId. If the value of PostTypeId is 1, than the post refers to a question, otherwise is the value of
PostTypeId is 2 the post refers to an answer.

An example of a question post is:

    <row Id="2155" PostTypeId="1" AcceptedAnswerId="2928"
    CreationDate="2008-08-05T12:13:40.640" Score="25" ViewCount="17551"
    Body="The question content" OwnerUserId="371" LastEditorUserId="2134"
    LastEditorDisplayName="stackoverflowGuy"
    LastEditDate="2008-08-23T18:09:09.777"
    LastActivityDate="2013-09-19T15:39:43.160" Title="How do I?"
    Tags="&lt;asp.net&gt;" AnswerCount="6" CommentCount="0"
    FavoriteCount="12" />
    
You will need to parse the record into a structure that will allow access to the value of each attribute
by name. In this example, Id="2155" represents the unique identifier given to the post; PostTypeId="1"
means that this post is a question; AcceptedAnswerId="2928" means that the accepted answer from the
user for this query is the answer with Id="2928"; and so on.

An example of a post that corresponds to an answer is:

    <row Id="659891" PostTypeId="2" ParentId="659089"
    CreationDate="2009-03-18T20:07:44.843" Score="1"
    Body="Description of the problem"
    OwnerUserId="45756" OwnerDisplayName="terminator"
    LastActivityDate="2009-03-18T20:07:44.843" CommentCount="0" />
    
The attribute-value pair Id="659891" represents the unique identifier given to this post. The value
for ParentId represents the identifier of the question this answer applies to, and the value for OwnerUserId
represents the user who wrote the answer for this question.

You do not need to know exactly what each attribute means, but you will need to be able to access
the value of each attribute, given a record. You will need to write a parser for each record and then
answer the following questions. For each question, we give the expected output
format; lines beginning with ‘#’ are only descriptive comments and you are not required to print them;
you only need to print the actual output values.

## Task 2
Which are the 10 most popular questions according to their view counts (attribute ViewCount in a question
post)? Output Format: 

    #Count Id
    17551 659891
    2131 659892
    1782 314159
    . . .
    
The columns are count and question id. Ties may be broken arbitrarily. Sort in decreasing order of
count. Use a single space between count and id.

## Task 3
Who was the user that answered the most questions and what were the Ids of these questions? A user
has answered a question only if their answer was selected as the accepted answer. Output Format:

     #OwnerUserId -> PostId, PostId, PostId, . . .
     1342 -> 23, 26, 531
     
Use a single space in your actual output: “1342 -> 23, 26, 531”

# 1.3 Sifting Web Data

## Task 5
In lectures, you saw how to sample uniformly a single line from a stream of lines efficiently on a single
machine. For large data, running reservoir sampling on a single machine would take too long. Implement
a MapReduce version of reservoir sampling which uniformly samples only a single line and uses
MapReduce to do so. Use your implementation to sample a single line from the file webLarge.txt.
Your output should contain only a single line. Do not implement the method that generates a random
number for each line then takes the largest one.

## Task 6
Extend the basic version of reservoir sampling such that it can sample multiple lines uniformly without
replacement and run on a single machine (i.e. no MapReduce). This means that if we want to sample
k lines from a file with n lines in total, then each of the (nCk) possible outcomes has equal probability.
Implement a program that will sample 100 lines from the file webLarge.txt. Run your program locally
(not as a MapReduce job).

## Task 7
Make your own implementation of a Bloom filter. We leave the choice of a hashing function up to you.
Write a program that uses your implementation of Bloom filter to approximately de-duplicate the lines
in the file webLarge.txt. The output of an approximate de-duplication contains no duplicate lines, but
some lines from the input might not appear at all in the output. You should think carefully about the
number of hashing functions and the size of the Bloom filter you use. The probability that a line (and its
duplicates) from the input does not appear at all in the output should be less than 1%. You can assume
that your hashing functions produce every value equally likely. When choosing the size of your Bloom
filter and number of hashing functions, you should assume the worst case in which all lines are unique.
The number of lines should be a command-line parameter to your program. 


## Task 8
Imagine you are Google and you want to know which search queries (if any) form at least 1% of all
queries in total. In the file queriesLarge.txt each line is a hash of a query and queries occurred in the
order as listed in the file. Implement the lossy counting algorithm and run it on the file queriesLarge.txt.
Your output should contain all queries that form at least 1% of all queries and no query that formed less
than 0.9% of all queries.

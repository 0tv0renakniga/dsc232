according to recent poll, data scientists spend most time
a) cleaning moving data (CORRECT ANSWER)
b) pickling features/models
c) deploying models in production
d) analyzing/presenting data


you are waiting in line at costco. what is costco's main concern
a) thoughput (CORRECT ANSWER)
b) latency

you are waiting in line at costco. what is your main concern
a) thoughput
b) latency (CORRECT ANSWER)

doing linear algebra in python is much slow than doing the same in matlab
a) not if you use numpy (CORRECT ANSWER)
b) yes it is slower
c) no python is faster than matlab
d) python is slower than matlab if memory is limited

why is SQL called a declaritive lanuage
a) because an SQL query defines what the answer should be not the squence of steps for reaching the answer (CORRECT ANSWER)
b) because it is easier to understand than procedural lanuages
c) because it can not be executed
d) because it specifies the excution path

what is the main technological change that enabled data science
a) digital storage (CORRECT ANSWER)
b) faster more powerful computer
c) multicore cpus
d) 10 Gb/s internet connections

table elements can have
a) differnt types of differnt columns (CORRECT ANSWER)
b) elements of different types
c) different types for different rows

types of table elements
a) have to support multiplication and addition
b) have to support addition
c) don't have to support either multiplication or addition (CORRECT ANSWER)

missing rows in a table
a) consume no storage (CORRECT ANSWER)
b) represented as rows of nulls

what does it mean when the conclusion from statistic analysis are said to be reproduciable
a) data collected from the same similar source yields the same conclusions (CORRECT ANSWER)
b) given the same input, you get the same output
c)it means that the notebook and data are put in a zip file and the same results are generated when run by someone else
d) running the same notebook many times, on random subsets of the data produces similar results

"The distribution of memory access latencies is oftern heavily tailed"
-explain this statement and why it is justified

as dicussed in class the latency of memory access has a heavy tail
suppose instead of considering single latencies we consider the sums of the latencies of disjoint sequences of 100 memory accesses each
suppose further the latencies of differnt accesses are independent
what can you say about the tails of the distribution of the sums?
a) has lighter tails than the individual latencies (CORRECT ANSWER)
b) has heavier tails than the individual latencies
c) both tails are equally heavy

EXPLAINIATION: 
- this is a direct consequence of the central limit theorem.
- the sum of independent random variables converges to the normal distribution which has exponential or light tails

caches sometimes have a dirty flag assicoiated with each page. the flag indicates wheather the page was changed since it was loaded in the cache. explain the reason for the flag and the effect it has on servicing cache misses
-explain

suppose a disk drive has seek latency of 10ms and a base throughput of 100MB/s
the term base throughput here means the rate at which the disk can read data once the reading head is in place
suppose your program reads block of data from random location on disk, give the effective throughput and the effective atency corresponding to the block sizes below
the term effective latency means the time from CPU issuing the read command to the disk to the time the disk block is avaiable in memory
the term efficive throughput means the number of MB that the CPU can read in a second

answering 
latency:ms
thoughput: MB/sec

10MB thoughput in MB/sec
1KB thoughput in MB/sec
10MB latency in ms

matrix elements
must have all the same type
can have different types for differnt columns (CORRECT ANSER)
can have differnt types for differnt rows

types of table elements don't have to support either multiplication or addition
a) must have different rows
b) don't have to support either multiplicaation or addition (CORRECT ANSWER)

if A and B are matrcies, A-B is well defined if
A and B have the same shapes (CORRECT ANSWER)
A and B are symmetric
the number of columns in A is equal to the number of rows in B

matrix A (n_rows,m_columns) and matrix B (j_rows,k_columns). what has to be equal for AxB and what is result of shape.
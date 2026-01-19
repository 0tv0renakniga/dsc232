
# Question 1

- which requires the most communicatio

a) shuffles #ANSWER

b) transformations

c) actions

d) no answer in text provided


---

# Question 2

- you are given RDD of string( each string contains words seprated by space) `IN`. your goal is to write a spark comand that will generate triplets(`first`,`second`,`third`) where `count` is the number of words `IN` that has the `length` and start with the letter`first`

```python
# start here
OUT = (IN
       .flatMap(lambda line: line.split())
       .map(lambda w: ((w[0], len(w)), 1))
       .reduceByKey(lambda a,b: a+b)
       .map(lambda kv: (kv[0][0], kv[0][1], kv[1])))
```

---

# Question 3

- you are given an RDD of key-value pairs `IN`. Both key and value are integers. write a command that outputs a key-value RDD `OUT` wher keys are the same as the keys `IN and the values is the average of the values associated with the key

```python
# start here
OUT = (IN
       .mapValues(lambda v: (v, 1))
       .reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1]))
       .mapValues(lambda sc: sc[0]/sc[1]))
```

---

# Question 4

- the following question ask that you write code that computes a desired result.
- - the code should be real. it should produce the correct answer when run in a pyspark environment
- your answer must keep the information in an RDD form and translate the result into a pthon object only at the end 
- we recomend try your command in a pyspark notebook to make sure it works as intended, before writing the anser in the space

**You are given an RDD `R` of strings. write a single line command to cound the number of strings whose length is 2**

```python
# start here
ans = R.filter(lambda s: len(s) == 2).count()
```

# Question 5

- the following question ask that you write code that computes a desired result.
- - the code should be real. it should produce the correct answer when run in a pyspark environment
- your answer must keep the information in an RDD form and translate the result into a pthon object only at the end 
- we recomend try your command in a pyspark notebook to make sure it works as intended, before writing the anser in the space

**You are given an RDD `R` of word. Your task is to count the number of appearance of the first two letter(symbols) of the word. For example te first two letter of "The" are "Th" and the first two letters of "!" are "!". List the pairs (letter, count that appear from the most common one to the least common one. Don't list pairs that do not appear. For full points perform collect only at the end of computation**

```python
# start here
OUT = (R
       .map(lambda w: (w[:2], 1))
       .reduceByKey(lambda a,b: a+b)
       .sortBy(lambda kv: kv[1], ascending=False))
```

# Question 6

- Similar to the previous question, but now you count word pairs, not letter pairs
- More precisely: you are given an RDD `R` in which each elemnt is a sentence, where the words are seprated by sentences
- Youa re to transform each line into a list of pairs
- Example
  - "This ice cream is the best!"
  - (This,ice),(ice,cream),(cream,is),(is,the),(the,best)
- Your task is to count the number of pairs each type(same two words)
- As the previous question list the pair that appear from the most common to the least common one. Don't list pairs that do not exist.
- For full points perform collect only at the end 

```python
esult = (

R.

map(lambda line: line.split()).

flatMap(lambda words: [((u, v), 1) for u, v in zip(words, words[1:])]).

reduceByKey(lambda a, b: a + b).

sortBy(lambda x: x[1], ascending=False).
collect()

)
```
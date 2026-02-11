# Question 1
- spark uses caching to reduce memory

a) True
b) False


# Question 2
- we can reduce execution time if we cache an RDD and that RDD is used to compute more than one result

a) True
b) False



# Question 3
- Suppse A and B are RDDs
- Issuing the command `A=B.cache()`(note: using juypter notebook) results in B being materialized immediately

a) True
b) False



# Question 4
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
A1 = T.map(lambda x:x^2)
```

# Question 5
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
B1 = A1.filter(lambda x:x<1000)
```

# Question 6
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
C1 = B1.count()
```

# Question 7
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
B2 = A1.filter(lambda x: x>10)
```

# Question 8
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
C2 = B2.count()
```

# Question 9
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
A1 = T.map(lambda x:x^2).cache()
```

# Question 10
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
B1 = A1.filter(lambda x<1000)
```

# Question 11
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
C1 = B1.count()
```

# Question 12
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
B2 = A1.filter(lambda x: x>10)
```

# Question 13
- What is the ammount of time it takes to complete each of the following commands
- Assume the following:
  - computing the square of each element takes 100 seconds
  - prfiltering based on inequality taked 10 seconds
  - performaing a count on an RDD takes 5 seconds
  - Adding a command to the executiion plan takes 0 seconds
  - T is an RDD
  - All commands above the question you are answering) have been executed 


```python
C2 = B2.count()
```

# Question 14
- 
a) 
b) 
c) 
d) 

```python

```

# Question 15
- 
a) 
b) 
c) 
d) 

```python

```

# Question 16
- 
a) 
b) 
c) 
d) 
```python

```

# Question 17
- 
a) 
b) 
c) 
d) 

```python

```
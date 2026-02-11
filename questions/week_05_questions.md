# Question 1
- 

a)
b)
c)
d)

# Question 1
- **
```python

```
---



# Question 1
- Suppose $V$ is a vector space of dimension $d$, that $\vec{u_1}$,$\vec{u_2}$...,$\vec{u_d}$ is a basis for $V$ and $\vec{x} \in V$ express $\vec{x}$ as a linear combination of the bias vectors

a)$\vec{u_1} +\vec{u_2}+...+\vec{u_d}$
b)$\sum_{i=1}^{d} a_i \vec{u_i}$ where a_i are constants
c)$\vec{u_1} -\vec{u_2}+\vec{u_3}...(-1)^{d-1}\vec{u_d}$
d)$\frac{1}{d} \sum_{i=1}^{d} \vec{u_i}$

# Question 2
- Suppose $M$ is a  symmetric real value $dxd$ matrix that ((\vec{u_1},\lambda_1),(\vec{u_2}\lambda_2),...,(\vec{u_d},\lambda_d))are eigen-vector, eigen value pairs which are true

a)for any $i: M\vec{u_i}=\lambda_i\vec{u_i}$
b)for any $i: \vec{u_i}\cdot\vec{u_i}=1$
c)for any $i \neq j : \vec{u_i}\cdot\vec{u_i}=0$
d)$the set $\vec{u_1,...,}\vec{u_i} $for the basis $R^{d}$


# Question 3
- Suppose $N$ vectors in $$R^{d}: \vec{x_1},...,\vec{x_N}$ each $\vec{x_i}$ is a column vector Choose the expecter vector $\vec{\mu}$

a)$\frac{1}{N} \sum_{i=1}^{N} \vec{x_i}$
b)$\sum_{i=1}^{N} \vec{x_i}$
c)$\frac{1}{d} \sum_{i=1}^{N} \vec{x_i}$
d)$$\frac{1}{N} \sum_{i=1}^{N} \vec{x_i}^T$

# Question 4
- Suppose $N$ vectors in $$R^{d}: \vec{x_1},...,\vec{x_N}$ each $\vec{x_i}$ is a column vector Choose the covariance matrix $C$

a)$\frac{1}{N} \sum_{i=1}^{N} (\vec{x_i}-\mu)(\vec{x_i}-\mu)^T$
b)$\frac{1}{N} \sum_{i=1}^{N} (\vec{x_i}-\mu)^T(\vec{x_i}-\mu)$
c)$\frac{1}{d} \sum_{i=1}^{N} (\vec{x_i}-\mu)(\vec{x_i}-\mu)^T$
d)$\frac{1}{d} \sum_{i=1}^{N} (\vec{x_i}-\mu)^T(\vec{x_i}-\mu)$


# Question 5
-Suppose C is a covariance matrix computed for the dataset  \vec{x_1},...,\vec{x_N}$. suppose non of the eigenvalues of C is zero. usppose $U$ is the orthonormal matrix that contains the eigenvectors of $C$. $U$ can be seen as the change of bias. define the transformed dataset ti be $\vec{y_i}=U\vec{x_i}$. what can you say about the covariance matrix C^{\prime} of the dataset \vec{y_1},...,\vec{y_N}$.C^{\prime} =

a) $I$
b) $UCU^T$
c) $C$
d) $C^{-1}$
e) $c^{\prime}$ is the sum of the eigenvalues of $C$

# Question 6 
- suppose $\vec{x}$ is drawn from a distribution $D$ over $R^{d}$. $C$ is the covariance matrix for the distribution. The PCA of $C$ yields the eigen-vectors \vec{u_1},...,\vec{u_d}$ with unequal eigen values $\sigma_{1}^{2}$>$\sigma_{2}^{2}$ >... > $\sigma_{d}^{2}$. let $\vec{v} \in R^{d}$ be an arbitrary vector. write an expression for the best approximation of $\vec{v}$  using the top $k$ eigen-vectors

a) $\sum_{i=1}^{k} (\vec{v}\cdot\vec{u_i})\vec{u_i}$
b) $\sum_{i=1}^{k} (\vec{v}\cdot\vec{u_i})$
c) $\sum_{i=1}^{d} (\vec{v}\cdot\vec{u_i})\vec{u_i}$
d) $(\vec{v}\cdot\vec{u_i})$
e) $\sum_{i=1}^{k} (\vec{v}\cdot\vec{u_i})\sigma_{i}^{2}$
f) e) $\sum_{i=1}^{d} (\vec{v}\cdot\sigma_{i}^{2})\vec{u_i}$

# question 7 
-suppose $\vec{x}$ is drawn from distribution D over $R^{d}$. let C be the covariancr matrix foa distribution $D$ and suppose the spectral decomposition of C is $C = A^TDA$ where A is orthonormal matrix and $D$ is the Diagonal matrix I\sigma_{i}^2 where  $\sigma_{1}^{2}$>=$\sigma_{2}^{2}$ >=... >= $\sigma_{d}^{2}$ are the variances of the principle components. Equivalently $\sigma_{i}^{2}$ is the eigen value associated with the ith eigen vector of $C$. write an expression for the fraction of the total vvariance that is explained by the compnents 1 to $k\leq d

a) $\frac{\sum_{i=1}^{k} \sigma_{i}^{2}}{\sum_{i=1}^{d} \sigma_{i}^{2}}$
b) $\frac{\sigma_{1}^{2}}{\sum_{i=1}^{d} \sigma_{i}^{2}}$
c) $\frac{\sigma_{k}^{2}}{\sum_{i=1}^{d} \sigma_{i}^{2}}$
d) $\frac{\sigma_{1}^{2}}{\sum_{i=1}^{d}}$
d) $\sigma_{1}^{2}+\sigma_{1}^{2}+...+\sigma_{k}^{2}$

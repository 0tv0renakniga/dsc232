# Week 5: Mathematical Modeling, PCA, and High-Dimensional Geometry

**Focus:** Mathematical Modeling, PCA, and High-Dimensional Geometry using the Weather dataset.

---

## Battle-Ready Summary: "The Physics of Data"

Week 5 moves beyond "how to use Spark" and into "how to model reality." The professor argues that all major machine learning methods (PCA, K-Means, Regression) are just variations of minimizing Root Mean Square Error (RMSE).

**The Central Workflow:**
$\text{Data} \to \text{Model} \to \text{Compressed Representation} \to \text{Reconstruction} \to \text{Residual (Error)}$

---

## Detailed Concept Breakdown

### 1. Functions as Vectors (Lecture 9.1)
* **Concept:** You can treat a function (like a year of daily temperatures) as a single vector in high-dimensional space ($d=365$).
* **The Math:** To approximate these functions, we use an Orthonormal Basis (like Fourier/Sinusoids).
* **Key Formula:** A function $f$ is approximated by:
    $$g(i) = \sum_{j=0}^{i} (f \cdot u_j) u_j$$
    Where $u_j$ are basis vectors and $(f \cdot u_j)$ are the coefficients.
> **The Trap:** You must normalize basis vectors to have unit length (norm = 1) and be orthogonal (dot product = 0) for this formula to work.

### 2. PCA for Dimensionality Reduction (Lecture 9.2)
* **Application:** Applied to Massachusetts Snow Depth.
* **The Mechanism:** Decomposing the signal into Eigenvectors that capture specific physical properties.
    1.  **Coefficient 1 (Volume):** Correlates with the mean. Captures "Heavy vs. Light" snow years.
    2.  **Coefficient 2 (Phase/Timing):** Negative in Jan, Positive in March. Captures "Early vs. Late" season starts.
    3.  **Coefficient 3 (Duration):** Positive in Feb, Negative in Jan/March. Captures "Short vs. Long" seasons.
* **Metric:** "Percentage of Variance Explained." Top 6 eigenvectors explain ~80% of the variance.

### 3. The "Unified RMS Theory" (Lecture 10.1)
**The Claim:** PCA, Regression, and K-Means are mathematically identical in goal: they minimize the reconstruction error $\|x - \text{model}(x)\|^2$.

* **PCA:** Approximates $x$ with a subspace (line/plane).
* **K-Means:** Approximates $x$ with a prototype point (centroid).
* **Regression:** Approximates $y$ given $x$.

**Physics Terminology:**
* **Extensive Properties:** Scale with data size $N$ (e.g., total error, specific coefficients for a year).
* **Intensive Properties:** Do not scale with $N$ (e.g., the Eigenvectors themselves, the Model parameters).

### 4. Alternating Minimization (Lecture 9.5)
* **The Problem:** How to separate the effect of Year (Time) vs. Station (Location) on snow depth?
* **The Algorithm:**
    1.  Calculate row means (Station effects).
    2.  Subtract them from the data.
    3.  Calculate column means (Year effects) on the residuals.
    4.  Repeat until convergence.
* **Result:** Time (Year) has a 4x stronger effect on snow depth than Location.

### 5. High-Dimensional Geometry (Lecture 10.2)
* **The "Curse":** Our intuition from 2D/3D fails in high dimensions ($d > 100$).
* **The Reality:**
    * **Concentration of Measure:** The length of a random vector concentrates tightly around $\sqrt{d}$ (or $\sqrt{cd}$).
    * **Equidistance:** The distance between any two random vectors approaches a constant.
    * **Orthogonality:** Two random vectors in high dimensions are almost always orthogonal (dot product $\approx 0$).
* **Consequence:** Algorithms based on distance (like K-Nearest Neighbors) fail in high dimensions because "nearest" and "farthest" become indistinguishable.

---

## The "Exam Ready" Checklist

### 1. Can you calculate RMSE?
**Concept:** Root Mean Square Error (RMSE) is the "unified theory" for this week. It is the metric used to judge how good your model (PCA, Regression, or K-Means) is at reconstructing the original data.

**The Formula:**
$$RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (Actual_i - Predicted_i)^2}$$

**How to do it by hand (The Step-by-Step):**
1.  **Difference:** Subtract the prediction from the actual value for every data point.
2.  **Square:** Square each difference (this makes all errors positive and penalizes big errors more heavily).
3.  **Mean:** Sum all the squared values and divide by $N$ (the number of points).
4.  **Root:** Take the square root of that average.

> **The Exam Trap:**
> * They might ask for **MSE** (Mean Squared Error), which is just the value before the square root. Don't take the root if they ask for MSE.
> * They might ask for the **Residual Norm**. This usually implies the sum of squared errors without the division by $N$, or sometimes the Euclidean length ($\|\vec{r}\|_2$) of the difference vector. Read the units carefully.

### 2. Can you check for Orthonormality?
**Concept:** PCA relies on changing your coordinate system to a new "Basis." For the math to work (specifically the reconstruction formula), this basis must be Orthonormal.

**The Definition:** A set of vectors $\{u_1, u_2, ...\}$ is Orthonormal if it passes two tests:
1.  **Unit Length (Normal):** The dot product of a vector with itself is 1. ($\vec{u}_1 \cdot \vec{u}_1 = 1$)
2.  **Orthogonal:** The dot product of any two different vectors is 0. ($\vec{u}_1 \cdot \vec{u}_2 = 0$)

> **The Exam Trap:**
> * They will give you a matrix $U$. You must check if $U \times U^T = I$ (Identity Matrix).
> * **Question:** "Is the vector $[1, 1]$ a valid basis vector for PCA?"
> * **Answer:** No. Its length is $\sqrt{1^2 + 1^2} = \sqrt{2}$. You must normalize it to $[1/\sqrt{2}, 1/\sqrt{2}]$ for it to be part of an orthonormal set.

### 3. Do you know the "Curse"? (High-Dimensional Geometry)
**Concept:** In high dimensions (e.g., $d=1000$), geometry behaves counter-intuitively. Our 2D/3D intuitions are wrong.

**The Three Rules of the Curse:**
1.  **Concentration of Length:** Random vectors don't have random lengths anymore. They all have a length very close to $\sqrt{d}$.
2.  **Orthogonality:** If you pick two random vectors in high dimensions, they are almost certainly orthogonal (their dot product is $\approx 0$).
3.  **Equidistance:** The distance between any two points tends to be the same.

> **The Exam Trap:**
> * **Question:** "Why does K-Nearest Neighbors (KNN) fail on 2000-dimensional data?"
> * **Answer:** Because the concept of "Nearest" vanishes. The distance to the nearest neighbor and the farthest neighbor is almost identical, so the algorithm cannot distinguish "close" from "far".

### 4. Can you interpret Eigenvectors?
**Concept:** In PCA, Eigenvectors are not just math abstractions; they are shapes that represent real-world physical properties (like weather patterns).

**How to read the "Shapes" (Weather Data Context):**
* **Eigenvector 1 (The Mean/Volume):** Look for a line that is mostly positive (or same sign) everywhere.
    * *Meaning:* "This year had more snow overall" or "less snow overall." It scales the volume.
* **Eigenvector 2 (The Tilt/Phase):** Look for a line that crosses zero once (e.g., goes from Negative $\to$ Positive).
    * *Meaning:* It shifts the season. "Snow started late" vs. "Snow started early."
* **Eigenvector 3 (The Duration):** Look for a line that crosses zero twice (e.g., Positive $\to$ Negative $\to$ Positive).
    * *Meaning:* It changes the shape width. "Short intense season" vs. "Long mild season."

> **The Exam Trap:**
> They will show you a graph of a wiggly line and ask: "This eigenvector corresponds to which physical phenomenon?"
>
> **Strategy: Count the zero crossings.**
> * 0 crossings $\approx$ Magnitude (Heavy/Light).
> * 1 crossing $\approx$ Shift (Early/Late).
> * 2 crossings $\approx$ Duration (Short/Long).

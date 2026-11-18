$$H_1(A) = M\big[I(a_i)\big] \tag{3.12}$$

Trong đó $a_i$ là các dấu của nguồn A (Ta hiểu dấu là các con chữ, hoặc các ký hiệu ... của nguồn). Còn nguồn A là một tập rời rạc các dấu $a_i$ với các xác suất xuất hiện của chúng. Ta quy ước viết A như sau:

$$A = \{a_i\} = \begin{pmatrix} a_1 & a_2 & \dots & a_s \\ p(a_1) & p(a_2) & \dots & p(a_s) \end{pmatrix} \tag{3.13}$$

$$\text{Với } 0 \le p(a_i) \le 1 \text{ và } \sum_{i=1}^s p(a_i) = 1 \tag{3.14}$$

A được cho bởi (3.13) và (3.14) còn gọi là trường tin (hay trường biến cố). Từ (3.12) và (3.13), ta có:

$$H_1(A) = M\big[I(a_i)\big] = \sum_{i=1}^s p(a_i)I(a_i)$$

$$\Rightarrow H_1(A) = -\sum_{i=1}^s p(a_i)\log p(a_i) \tag{3.15}$$

$H_1(A)$ còn gọi là entropy một chiều của nguồn rời rạc:

<u>Ví dụ:</u> $\text{H}_1(\text{Việt}) = 4,5167\text{ bit} \qquad \text{H}_1(\text{Nga}) = 4,35\text{ bit}$

$\text{H}_1(\text{Anh}) = 4,19\text{ bit}$

### 3.2.3. Các tính chất của entropy một chiều của nguồn rời rạc

#### 3.2.3.1. Tính chất 1

Khi $p(a_k) = 1$ và $p(a_r) = 0$ với $\forall r \ne k$ thì:

$$H_1(A) = H_1(A_{\min}) = 0 \tag{3.16}$$

<u>Chứng minh:</u>

Ta đã có: $0 \le p(a_i) \le 1 \Rightarrow \log p(a_i) \le 0 \Rightarrow -\log p(a_i) \ge 0$

$$\Rightarrow H_1(A) \ge 0 \Rightarrow H_1(A_{\min}) = 0$$

Bây giờ ta chỉ còn phải chứng tỏ $H_1(A_{\min}) = 0$ khi $p(a_k) = 1$ và $p(a_r) = 0$ ($\forall r \ne k$).

Thật vậy, $p(a_r) = 0 \Rightarrow p(a_r)\log p(a_r) = 0$ ($\forall r \ne k$)

$p(a_k) = 1 \Rightarrow p(a_k)\log p(a_k) = 0$ ($\forall r \ne k$)

$$\Rightarrow H_1(A) = -\sum_{i=1}^s p(a_i)\log p(a_i)$$

$$= -p(a_k)\log p(a_k) - \sum_{i=1, i \ne k}^s p(a_i)\log p(a_i) = 0$$

<u>Ý nghĩa:</u>
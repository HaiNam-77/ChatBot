[Hình: Đồ thị tín hiệu $x(t)$ theo thời gian $t$ với các xung vuông có biên độ bằng 1 xuất hiện ngẫu nhiên.]

Hình 2.20.

Phân bố xác suất các giá trị (0 hoặc 1) của $x(t)$ tuân theo luật Poisson:
$$P_n(t) = \frac{(\lambda t)^n}{n!} e^{-\lambda t}, \quad t > 0$$
Trong đó $\lambda$ là số các bước nhảy của hàm $x(t)$ trong một đơn vị thời gian, còn $P_n$ là xác suất để xảy ra $n$ bước nhảy của hàm $x(t)$ trong thời gian $t$.
Hãy tìm hàm tự tương quan, hàm tương quan chuẩn hoá và thời gian tương quan của quá trình ngẫu nhiên, biết rằng $P(1) = P(0) = 0,5$.

**2.3.** Tìm hàm tự tương quan của quá trình ngẫu nhiên dừng sau:
$$x(t) = A \cos(2\pi f_0 t + \varphi)$$
Trong đó $A = \text{const}$, $f_0 = \text{const}$, $\varphi$ là đại lượng ngẫu nhiên có phân bố đều trong khoảng $(-\pi, \pi)$.

**2.4.** Tìm hàm tự tương quan và mật độ phổ của tín hiệu điện báo ngẫu nhiên $x(t)$ cho bởi hình dưới đây. Biết rằng nó nhận các giá trị $+a; -a$ với xác suất như nhau và bằng $1/2$. Còn xác suất để trong khoảng $\tau$ có $N$ bước nhảy là:
$$P(N, \tau) = \frac{(\lambda \tau)^N}{N!} e^{-\lambda \tau}, \quad \tau > 0$$
(theo phân bố Poisson).

**2.5.** Hãy chứng tỏ rằng đường bao của tín hiệu giải tích có thể biểu diễn bằng công thức sau:
$$f \ A(t) = \sqrt{S_a(t) S_a^*(t)}$$
Trong đó: $S_a^*(t)$ là hàm liên hợp phức của $S_a(t)$:
$S_a(t) = x(t) + j\hat{x}(t)$ là tín hiệu giải tích.

**2.6.** Một quá trình ngẫu nhiên dừng có hàm tự tương quan:
a) $R_{x_1}(\tau) = \sigma^2 e^{-\alpha |\tau|}$
b) $R_{x_2}(\tau) = \sigma^2 e^{-\alpha |\tau|} \cos \omega_0 \tau$
Hãy tính toán và vẽ đồ thị mật độ phổ của các quá trình ngẫu nhiên trên.
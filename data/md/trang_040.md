- Tần số góc tức thời của tín hiệu giải tích $\omega(t)$:

$$\omega(t) = \frac{d\theta(t)}{dt} = \left[ arctg \frac{\hat{x}(t)}{x(t)} \right]' = \frac{[\hat{x}(t)/x(t)]'}{1 + \frac{\hat{x}^2(t)}{x^2(t)}} = \frac{x(t)\hat{x}'(t) - \hat{x}(t)x'(t)}{x^2(t) + \hat{x}^2(t)} \quad (2.58)$$

[Hình 2.13: Đồ thị biểu diễn tín hiệu dao động $x(t)$ và đường bao $A(t)$ theo thời gian $t$.]

- Tính chất của $A(t)$:
    + $A(t) \ge |x(t)|$
    + Khi $\hat{x}(t) = 0 \Rightarrow A(t) = |x(t)|$
    + Xét: $A'(t) = \frac{x(t)x'(t) + \hat{x}(t)\hat{x}'(t)}{\sqrt{x^2(t) + \hat{x}^2(t)}}$
    Khi $\hat{x}(t) = 0 \Rightarrow A'(t) = x'(t)$
    Vậy khi $\hat{x}(t) = 0$ thì độ nghiêng của $A(t)$ và $x(t)$ là như nhau.

- Kết luận:
    Đối với các tín hiệu ngẫu nhiên thì các yếu tố của tín hiệu là ngẫu nhiên. Nhờ có khái niệm tín hiệu giải tích nên ta mới nghiên cứu các tính chất thống kê của các yếu tố của nó được thuận lợi, đặc biệt là trong tính toán.

### 2.6.2. Tín hiệu dải rộng và giải hẹp
#### 2.6.2.1. Tín hiệu dải rộng
Người ta gọi một tín hiệu là tín hiệu dải rộng nếu bề rộng phổ của nó thoả mãn bất đẳng thức sau:
$$\frac{\Delta\omega}{\omega_0} \ge 1 \quad (2.59)$$
Nhìn chung tín hiệu dải rộng là tín hiệu mà bề rộng phổ của nó có thể so sánh được với $\omega_0$.

Trong đó: $\Delta\omega = \omega_2 - \omega_1$ và $\omega_0 = \frac{\omega_2 + \omega_1}{2}$ gọi là tần số trung tâm (xem Hình 2.14).
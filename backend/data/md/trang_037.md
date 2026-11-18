Với $a$ càng lớn thì có thể bỏ qua ảnh hưởng xấu của nhiễu. Do đó đường bao (biên độ tín hiệu) không có gia số (không thăng giáng) và cũng không có sai pha. Khi đó $\varphi_y$ nhận giá trị “0” trong khoảng $(-\pi, \pi)$ với xác suất lớn.

### 2.6. BIỂU DIỄN PHỨC CHO THỂ HIỆN CỦA TÍN HIỆU NGẪU NHIÊN – TÍN HIỆU GIẢI HẸP

#### 2.6.1. Cặp biến đổi Hilbert và tín hiệu giải tích

##### 2.6.1.1. Nhắc lại cách biểu diễn một dao động điều hoà dưới dạng phức

Cho:
$$x(t) = A_0 \cos(\omega_0 t + \varphi_0) = A(t) \cos \theta(t) \tag{2.46}$$

Trong đó: $\omega_0$ là tần số trung tâm; $\theta(t)$ : pha đầy đủ;
$\varphi_0$ : pha đầu.

Trong “Lý thuyết mạch”, người ta rất hay dùng cách biểu diễn $x(t)$ dưới dạng phức sau:
$$\dot{x}(t) = x(t) + j\hat{x}(t) = A(t)e^{j\theta(t)} \tag{2.47}$$

Trong đó: $x(t) = \text{Re}[\dot{x}(t)]$;
$$\hat{x}(t) = \text{Im}[\dot{x}(t)] = A_0 \sin \theta(t)$$

Ta có thể biểu diễn $\dot{x}(t)$ dưới dạng một vector trên mặt phẳng phức.

Khi $A(t) = const$ thì quỹ tích của điểm M sẽ là một vòng tròn tâm O, bán kính OM.

$\omega(t) = d\theta/dt$ là tần số của dao động (Hình 2.12)

[Hình: Biểu diễn vector $\dot{x}(t)$ trên mặt phẳng phức. Trục hoành là phần thực $\text{Re}[\dot{x}(t)]$, trục tung là phần ảo $\text{Im}[\dot{x}(t)]$. Vector $A$ kết thúc tại điểm M, tạo với trục hoành một góc $\theta(t)$. Hình chiếu của M xuống trục hoành là $x(t)$ và xuống trục tung là $\hat{x}(t)$.]

Hình 2.12.

##### 2.6.1.2. Cặp biến đổi Hilbert – Tín hiệu giải tích

**a. Cặp biến đổi Hilbert và tín hiệu giải tích:**

Để dễ dàng biểu diễn dưới dạng phức những thể hiện phức tạp của các quá trình ngẫu nhiên, người ta dùng cặp biến đổi Hilbert. Nó cho phép ta tìm $\hat{x}(t)$ khi biết $x(t)$ và ngược lại.
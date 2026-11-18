[Hình: Sơ đồ Venn biểu diễn mối quan hệ giữa các tập hợp quá trình ngẫu nhiên (QTNN): QTNN dừng rộng, QTNN dừng hẹp và QTNN chuẩn.]

Hình 2.1.

Trong những đặc trưng thống kê của các quá trình ngẫu nhiên, hàm tự tương quan và hàm tương quan là những đặc trưng quan trọng nhất. Theo định nghĩa, hàm tự tương quan sẽ bằng:
$$
\begin{aligned}
R_x\left(t_1, t_2\right) &= M\left\{\left[X\left(t_1\right)-m_x\left(t_1\right)\right] \cdot\left[X\left(t_2\right)-m_x\left(t_2\right)\right]\right\} \\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left[x_1-m_x\left(t_1\right)\right] \cdot\left[x_2-m_x\left(t_2\right)\right] W_2\left(x_1, x_2, t_1, t_2\right) d x_1 d x_2
\end{aligned} \tag{2.8}
$$

$R_x\left(t_1, t_2\right)$ đặc trưng cho sự phụ thuộc thống kê giữa hai giá trị ở hai thời điểm thuộc cùng một thể hiện của quá trình ngẫu nhiên.

$W_2\left(x_1, x_2, t_1, t_2\right)$ là hàm mật độ phân bố xác suất hai chiều của hai giá trị của quá trình ngẫu nhiên ở hai thời điểm $t_1$ và $t_2$.

Khi $t_1 = t_2$ thì (2.8) trở thành:
$$R_x\left(t_1, t_2\right)=M\left\{\left[X(t)-m_x(t)\right]^2\right\}=D_x(t) \tag{2.9}$$

Như vậy, phương sai là trường hợp riêng của hàm tự tương quan khi hai thời điểm xét trùng nhau.

Đôi khi để tiện tính toán và so sánh, người ta dùng hàm tự tương quan chuẩn hoá được định nghĩa bởi công thức:
$$
\begin{aligned}
\tau_x\left(t_1, t_2\right) &= \frac{R_x\left(t_1, t_2\right)}{\sqrt{R_x\left(t_1, t_1\right) R_x\left(t_2, t_2\right)}}=\frac{R_x\left(t_1, t_2\right)}{\sqrt{D_x\left(t_1\right) D_x\left(t_2\right)}} \\
&= \frac{R_x\left(t_1, t_2\right)}{\sigma_x\left(t_1\right) \sigma_x\left(t_2\right)}
\end{aligned} \tag{2.10}
$$

Dễ dàng thấy rằng: $\left|\tau_x\left(t_1, t_2\right)\right| \leq 1$.

### 2.3.2. Khoảng tương quan

Khoảng tương quan cũng là một đặc trưng khá quan trọng. Ta thấy rằng hai giá trị của một quá trình ngẫu nhiên $\xi(t)$ chỉ tương quan với nhau khi khoảng cách $\tau$ giữa hai thời điểm
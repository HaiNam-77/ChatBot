$$W_1(\varphi) = \int_0^\infty W_2(A, \varphi) dA = \int_0^\infty \frac{1}{2\pi} \frac{A}{\delta^2} \exp \left\{ -\frac{A^2}{2\delta^2} \right\} dA$$
$$W_1(\varphi) = \frac{1}{2\pi} \int_0^\infty W_1(A) dA \tag{2.39}$$

Vậy mật độ phân bố xác suất pha đầu của nhiễu dải hẹp, chuẩn là phân bố đều trong khoảng $(0, 2\pi)$. (Hình 2.10).

[Hình: Đồ thị hàm mật độ phân bố xác suất $W_1(\varphi)$ là một đường nằm ngang có giá trị $1/2\pi$ trong khoảng từ $0$ đến $2\pi$ trên trục hoành $\varphi$.]
Hình 2.10. Phân bố đều

**2.5.2.3. Ví dụ 3:**

Ở đầu vào bộ tách sóng tuyến tính đặt hỗn hợp tín hiệu và nhiễu:
$$y(t) = x(t) + n(t)$$
Với: $x(t) = U_0 \cos \omega_0 t$ là tín hiệu xác định.
$n(t) = A_n(t) \cos [\omega_0 t - \varphi(t)]$ là nhiễu giải hẹp, chuẩn.

Tìm mật độ phân bố xác suất đường bao và pha của điện áp đầu ra bộ tách sóng tuyến tính.

Ta có:
$$y(t) = U_0 \cos \omega_0 t + c(t) \cos \omega_0 t + s(t) \sin \omega_0 t$$
$$= [U_0 + c(t)] \cos \omega_0 t + s(t) \sin \omega_0 t = A_y \cos [\omega_0 t - \varphi_y(t)]$$

Trong đó: $A_y(t) = \sqrt{[U_0 + c(t)]^2 + s^2(t)}$ là bao của hỗn hợp tín hiệu và nhiễu.
$\varphi_y(t) = \arctan \frac{s(t)}{U_0 + c(t)}$ là pha của hỗn hợp tín hiệu và nhiễu.

Làm tương tự như ví dụ 2, ta có:
$$W_1(A_y) = \frac{A_y(t)}{\delta^2} \exp \left\{ -\frac{A_y^2(t) + U_0^2}{\delta^2} \right\} I_0 \cdot \left\{ \frac{A_y(t) \cdot U_0}{\delta^2} \right\} \tag{2.44}$$

Biểu thức (2.44) gọi là phân bố Rice (Hình 2.11a).
$I_0$ là hàm Bessel biến dạng loại 1 cấp 0.
$$I_0(z) = \frac{1}{2\pi} \int_0^{2\pi} e^{z \cos \theta} d\theta$$
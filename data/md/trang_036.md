$I_0(z)$ có thể viết dưới dạng chuỗi vô hạn sau:

$$I_0(z) = \sum_{n=0}^{\infty} \frac{1}{(n!)^2} \left( \frac{z}{2} \right)^{2n}$$

Khi $z \ll 1: I_0(z) = 1 + \frac{z^2}{4} + ... \approx e^{z^2/4}$

Nhận xét:
- Khi $a = 0$ sẽ không có tín hiệu, chỉ có nhiễu giải hẹp, chuẩn do đó phân bố Rice trở về phân bố Reyleigh.
- $a$ càng lớn, phân bố Rice càng tiến tới phân bố Gausse.

Giải thích:
Khi $a \gg 1$ thì tín hiệu mạnh, nhiễu yếu. Tín hiệu tác dụng với thành phần không trực giao với nó của nhiễu (khi tín hiệu càng mạnh thì hỗn hợp này càng ít khác tín hiệu), còn thành phần của nhiễu trực giao với tín hiệu thì không chịu sự “chèn ép” của tín hiệu. Do đó mật độ phân bố xác suất bao của hỗn hợp sẽ mang đặc điểm của thành phần nhiễu trực giao với tín hiệu.

$$W_1(\varphi_y) = \frac{1}{2\pi} \exp \left( -\frac{U_0^2}{\delta^2} \right) + \frac{U_0 \cos \varphi_y}{2\sqrt{2\pi\delta^2}} \left[ 1 + \phi \left( \frac{U_0 \cos \varphi_y}{\sqrt{2\delta^2}} \right) \right] \exp \left\{ -\frac{U_0^2 \sin \varphi_y}{2\delta^2} \right\} \quad (2.45)$$

Trong đó: $\phi(z) = \frac{2}{\sqrt{2\pi}} \int_0^z e^{-\theta^2/2} d\theta$ là tích phân xác suất.

Đồ thị của biểu thức (2.45) biểu diễn trên hình Hình 2.11b.

[Hình: Hình 2.11. Phân bố Rice. Gồm hai đồ thị: đồ thị a biểu diễn mật độ xác suất $W(A_y/\sigma)$ theo $A_y/\sigma$ cho các giá trị $a = U_0/\sigma = 0, 2, 4$; đồ thị b biểu diễn mật độ xác suất $W_1(\varphi_y)$ theo $\varphi_y$ cho các giá trị $a = 0, 2, 5$.]

Hình 2.11. Phân bố Rice

Nhận xét:
+ $a = 0$: chỉ có nhiễu $W_1(\varphi_y)$ chính là $W_1(\varphi)$ đã xét ở ví dụ 2.
+ $a \gg 1$: đường cong $W_1(\varphi_y)$ càng nhọn, hẹp.

Giải thích:
### 2.7.3. Khái niệm về máy thu tối ưu

#### 2.7.3.1. Máy thu tối ưu

Một cách tổng quát, ta coi một máy thu đặc trưng bởi một toán tử thu $\overline{\psi}$ (Hình 2.18). Yêu cầu của toán tử thu $\overline{\psi}$ là tác dụng vào $y(t)$ (là tín hiệu vào) phải cho ra tín hiệu đã phát $x(t)$.

Nếu ta phát đi một thể hiện nào đó của một quá trình ngẫu nhiên $x(t)$:

$$x(t) = \{x_i(t)\}, (i = \overline{1, m})$$

Ta coi những thể hiện này có cùng công suất $P_x$, có cùng thời hạn T và có cùng bề rộng phổ $F_c$.

[Hình: Sơ đồ khối mô tả toán tử thu với đầu vào $y(t)$, khối xử lý $\overline{\psi}$ và đầu ra $x(t)$]

Hình 2.18. Toán tử thu

Giả thiết: trong quá trình truyền từ nơi phát đến nơi thu chỉ có tạp âm trắng Gausse $n(t)$, các tín hiệu phát là đồng xác suất.

Vector tín hiệu ta nhận được: $\vec{y}_0 = \frac{\vec{y}}{\sqrt{n}}$

Nếu $\vec{y}_0$ này gần với vector tín hiệu $\vec{x}_{j0}$ nhất so với các vector tín hiệu khác, tức là:

$$\left\| \frac{\vec{y}}{\sqrt{n}} - \frac{\vec{x}_j}{\sqrt{n}} \right\| \le \left\| \frac{\vec{y}}{\sqrt{n}} - \frac{\vec{x}_i}{\sqrt{n}} \right\|, \forall i : i = \overline{1, m}; i \neq j$$

Khi đó máy thu có $\overline{\psi}$ tác dụng lên $\vec{y}$ cho ra $\vec{x}_j : \overline{\psi}[\vec{y}] = \vec{x}_k$, sẽ được gọi là máy thu tối ưu (theo nghĩa Kachennhicov trong trường hợp các tín hiệu $x_i(t)$ là đồng xác suất).

#### 2.7.3.2. Liên hệ giữa máy thu tối ưu K và máy thu theo tiêu chuẩn độ lệch trung bình bình phương nhỏ nhất

Độ lệch trung bình bình phương (tbbp) giữa tín hiệu thu được và tín hiệu phát thứ $j$ là:

$$\overline{[y(t) - x_j(t)]^2} = \frac{1}{T} \int_0^T [y(t) - x_j(t)]^2 dt$$

Máy thu theo tiêu chuẩn độ lệch tbbp nhỏ nhất là máy thu đảm bảo:

$$\min_{\forall j} \overline{[y(t) - x_j(t)]^2}, j = \overline{1, m}$$

Như vậy, máy thu sẽ cho ra tín hiệu $\vec{x}_j(t)$ nếu:

$$\overline{[y(t) - x_j(t)]^2} \le \overline{[y(t) - x_i(t)]^2}, \forall i \neq j, i = \overline{1, m}$$
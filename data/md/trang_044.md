căn bậc hai công suất trung bình của nó. Nếu cho trước công suất trung bình P thì độ dài của vector $\vec{x}$ sẽ tỷ lệ với $\sqrt{n}$ (tức là tỷ lệ với căn bậc hai của đáy tín hiệu $B = F_c T = \frac{n}{2}$)

**Nhận xét:**

Như vậy, với cùng một công suất trung bình tín hiệu nào có đáy càng lớn (tức là tín hiệu càng phức tạp) thì độ dài của vector biểu diễn nó càng lớn. Khi đáy của tín hiệu càng lớn thì độ dài của vector tín hiệu càng lớn $\rightarrow$ vector tổng của tín hiệu và nhiễu dải hẹp càng ít khác vector tín hiệu $\rightarrow$ ta sẽ nhận đúng được tín hiệu với xác suất cao. Để tính chống nhiễu của tín hiệu càng cao thì yêu cầu B càng phải lớn.

Trong trường hợp $x(t)$ không rời rạc hoá: $E_x = \int_0^T x^2(t) dt$. Khi đó chuẩn của vector sẽ là:

$$||\vec{x}|| = \sqrt{(\vec{x}, \vec{x})} = \sqrt{2 F_c E_x} \Rightarrow ||\vec{x}|| = \sqrt{2 F_c \int_0^T x^2(t) dt} \quad (2.69)$$

Người ta còn gọi không gian mà chuẩn của vector cho bởi tích vô hướng (2.69) là không gian Hilbert và ký hiệu là $L^2$. Không gian $L^2$ là sự mở rộng trực tiếp của không gian Euclide hữu hạn chiều lên số chiều vô hạn.

### 2.7.2. Mật độ xác suất của vector ngẫu nhiên - Khoảng cách giữa hai vector tín hiệu

#### 2.7.2.1. Mật độ xác suất của vector ngẫu nhiên

**a. Vector tín hiệu:**

Để tiếp tục những vấn đề sau này được thuận tiện, ta đưa vào khái niệm vector tín hiệu.

**Định nghĩa 2.3.**

Vector tín hiệu $\vec{x}_0$ là vector sau:

$$\vec{x}_0 = \frac{\vec{x}}{\sqrt{n}} \quad (2.63)$$

Trong đó $\vec{x}$ là vector biểu diễn tín hiệu x(t) trong không gian n chiều.

**Tính chất:**

+ $\vec{x}_0$ có phương và chiều trùng với $\vec{x}$

+ Độ lớn (modul): $||\vec{x}_0|| = \left\| \frac{\vec{x}}{\sqrt{n}} \right\| = \sqrt{P}$

**b. Xác suất phân bố của mút vector $\vec{x}_0$ và miền xác định của nó**

Trong không gian tín hiệu, tín hiệu được biểu diễn bởi vector. Do đó xác suất để tồn tại tín hiệu đó ở một miền (nói riêng: tại một điểm) nào đấy của không gian chính là xác suất để mút vector tín hiệu rơi vào miền ấy (nói riêng: điểm ấy) của không gian.
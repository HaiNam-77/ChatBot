[Hình: Đồ thị Hình 2.7 biểu diễn bình phương môđun hàm truyền đạt $|\dot{K}(\omega)|^2$ theo tần số góc $\omega$. Đồ thị có dạng hình chuông đạt cực đại tại $\omega_0$. Một hình chữ nhật nét đứt có chiều cao $|\dot{K}(\omega)|^2_{max}$ và chiều rộng đáy $\Delta\omega_{tâ}$ được vẽ đè lên để minh họa khái niệm dải thông tương đương có cùng diện tích với miền dưới đường cong.]

Hình 2.7.

**Ý nghĩa hình học:**

$\Delta\omega_{tâ}$ chính là đáy của hình chữ nhật có diện tích bằng diện tích của miền giới hạn bởi đường cong $|\dot{K}(\omega)|^2$ và nửa trục hoành $(0, \infty)$; còn chiều cao của hình chữ nhật này là $|\dot{K}(\omega)|^2_{max}$

**Ý nghĩa vật lý:**

$\Delta\omega_{tâ}$ đặc trưng cho khả năng làm suy giảm tạp âm của các bộ lọc tuyến tính. Với cùng $|\dot{K}(\omega_0)|$, bộ lọc nào có $\Delta\omega_{tâ}$ càng hẹp thì công suất tạp âm đầu ra của bộ lọc ấy càng bé.

### 2.5.2. Bài toán tối đa

$G_R(\omega)$ và $B_R(\tau)$ chưa đặc trưng đầy đủ cho quá trình ngẫu nhiên.

Nội dung: Tìm hàm mật độ xác suất của tín hiệu ở đầu ra mạch vô tuyến điện tuyến tính.

#### 2.5.2.1. Mở đầu

Tìm mật độ xác suất n chiều của tín hiệu ngẫu nhiên ở đầu ra mạch tuyến tính là bài toán rất khó, nó không giải được dưới dạng tổng quát. Dưới đây chỉ xét hai trường hợp đơn giản:

- Tìm mật độ xác suất một chiều của tín hiệu ra bộ lọc tuyến tính khi tác động đầu vào là tín hiệu ngẫu nhiên chuẩn (có vô hạn thể hiện). Trong trường hợp này người ta đã chứng minh được tín hiệu ra cũng là một tín hiệu ngẫu nhiên chuẩn.
- Đặt vào bộ lọc tuyến tính một tín hiệu ngẫu nhiên không chuẩn. Nếu $\frac{\Delta\omega_{tâ}}{2\pi F} \ll 1$ ($F$ là bề rộng phổ của tín hiệu vào) thì tín hiệu ngẫu nhiên ở đầu ra sẽ có phân bố tiệm cận chuẩn. Người ta bảo đó là sự chuẩn hoá (Gauss hoá) các quá trình ngẫu nhiên không chuẩn bằng bộ lọc giải hẹp.

#### 2.5.2.2. Ví dụ 2:

Cho tạp âm giải hẹp, chuẩn có dạng:
$$n(t) = c(t) \cos \omega_0 t + s(t) \sin \omega_0 t = A(t) \cos (\omega_0 t - \varphi) \quad (2.37)$$
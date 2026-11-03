Công suất của thể hiện $x_T(t)$ sẽ bằng:

$$P_T = \frac{E_T}{T} = \frac{1}{2\pi T} \int_{-\infty}^{\infty} \left| \dot{S}_T (\omega) \right|^2 d\omega = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{\left| \dot{S}_T (\omega) \right|^2}{T} d\omega \quad (2.16)$$

Ta thấy vế trái của (2.16) là công suất của thể hiện $x_T(t)$ trong khoảng thời gian tồn tại hữu hạn T, còn vế phải là một tổng liên tục của các đại lượng $\{|\dot{S}_T(\omega)|^2/T\}d\omega$. Rõ ràng là để đảm bảo sự bình đẳng về thứ nguyên giữa hai vế của (2.16) thì lượng $\frac{|\dot{S}_T(\omega)|^2}{T}d\omega$ phải biểu thị công suất trong dải tần vô cùng bé $d\omega$. Như vậy, $\frac{|\dot{S}_T(\omega)|^2}{T}$ sẽ biểu thị công suất của thể hiện $x_T(t)$ trong một đơn vị tần số [W/Hz] tức là mật độ phổ công suất của thể hiện $x_T(t)$. Đến đây ta đặt:

$$\frac{\left| \dot{S}_T (\omega) \right|^2}{T} = G_T (\omega) \quad (2.17)$$

và gọi $G_T(\omega)$ là mật độ phổ công suất của thể hiện $x_T(t)$ trong khoảng T hữu hạn. $G_T(\omega)$ đặc trưng cho sự phân bố công suất của một thể hiện $x_T(t)$ trên thang tần số. Khi cho $T \to \infty$ ta sẽ tìm được mật độ phổ công suất của một thể hiện duy nhất $x_T(t)$ của quá trình ngẫu nhiên:

$$G_x (\omega) = \lim_{T \to \infty} G_T (\omega) = \lim_{T \to \infty} \frac{\left| \dot{S}_T (\omega) \right|^2}{T} \quad (2.18)$$

$G_x(\omega)$ cũng có ý nghĩa tương tự như $G_T(\omega)$.

Từ (2.18) ta thấy rằng để xác định mật độ phổ công suất của cả quá trình ngẫu nhiên (tức là tập các thể hiện ngẫu nhiên) thì phải lấy trung bình thống kê đại lượng $G_x(\omega)$, tức là:

$$G_x (\omega) = M \{ G_x (\omega) \} = M \lim_{T \to \infty} \frac{\left| \dot{S}_T (\omega) \right|^2}{T} \quad (2.19)$$

Biểu thức (2.19) là công thức xác định mật độ phổ công suất của các quá trình ngẫu nhiên.

### 2.4.2. Cặp biến đổi Wiener – Khinchin

Để thấy được mối quan hệ giữa các đặc trưng thống kê (nói riêng là hàm tự tương quan) và các đặc trưng vật lý (nói riêng là mật độ phổ công suất) ta viết lại và thực hiện biến đổi (2.19) như sau:
$$P_{ra} = \frac{G_0}{2\pi} \int_0^\infty |\dot{K} (\omega)|^2 d\omega \qquad (2.30)$$

Hàm tự tương quan của quá trình ngẫu nhiên ở đầu ra trong trường hợp này sẽ bằng:

$$R_{ra} (\tau) = \frac{1}{2\pi} \int_{-\infty}^\infty G_v (\omega) |\dot{K} (\omega)|^2 e^{j\omega\tau} d\omega$$
$$= \frac{1}{2\pi} N_0 \int_{-\infty}^\infty |\dot{K} (\omega)|^2 e^{j\omega\tau} d\omega$$
$$= \frac{N_0}{2\pi} \int_{-\infty}^\infty |\dot{K} (\omega)|^2 e^{j\omega\tau} d\omega$$
$$R_{ra} (\tau) = \frac{G_0}{2\pi} \int_0^\infty |\dot{K} (\omega)|^2 \cos \omega\tau d\omega \qquad (2.31)$$

**2.5.1.2. Ví dụ 1:**

Một mạch vô tuyến điện tuyến tính có tham số không đổi và đặc tính truyền đạt dạng chữ nhật (hình 2.4b) chịu tác động của tạp âm trắng dừng. Tìm hàm tự tương quan của tạp âm ra.

[Hình: Hình 2.5. a) Đồ thị mật độ phổ công suất $G_v(\omega)$ của tạp âm trắng là một hằng số $2N_0$. b) Đặc tính truyền đạt $|\dot{K}(\omega)|$ của mạch có dạng xung vuông (lọc dải) trong khoảng tần số từ $\omega_1$ đến $\omega_2$ với độ cao $K_0$.]

Hình 2.5.

Theo giả thiết: $G_v (\omega) = 2N_0$ và $|\dot{K} (\omega)| = \begin{cases} K_0 & \omega_1 < \omega < \omega_2 \\ 0 & \forall \omega \neq (\omega_1, \omega_2) \end{cases}$

Theo (2.31), ta có:

$$R_{ra} (\tau) = \frac{N_0}{\pi} \int_{\omega_1}^{\omega_2} K_0^2 \cos \omega\tau d\omega = \frac{N_0 K_0^2}{\pi\tau} (\sin \omega_2\tau - \sin \omega_1\tau)$$
$$= \frac{N_0 K_0^2}{\pi\tau} \Delta\omega \frac{\sin \dfrac{\Delta\omega\tau}{2}}{\dfrac{\Delta\omega\tau}{2}} \cos \omega_0\tau$$
$$R_{ra} (\tau) = \sigma_{ra}^2 \frac{\sin \dfrac{\Delta\omega\tau}{2}}{\dfrac{\Delta\omega\tau}{2}} \cos \omega_0\tau \qquad (2.32)$$

Đồ thị $R_{ra} (\tau)$ như hình 2.5.

Biểu thức (2.32) có thể viết gọn lại như sau:
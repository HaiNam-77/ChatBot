[Hình: Đồ thị hàm mật độ phổ công suất $G(\omega)$ có dạng hình chuông đối xứng qua $\omega_0$. Một hình chữ nhật bao quanh đỉnh của đồ thị có chiều cao $G(\omega_0)$ và chiều rộng $\Delta \omega$, diện tích hình chữ nhật bằng diện tích dưới đường cong.]

Hình 2.3. Bề rộng phổ công suất

**Ý nghĩa hình học:**

Bề rộng phổ $\Delta \omega$ chính là đáy của hình chữ nhật có chiều cao bằng $G(\omega_0)$ và có diện tích bằng diện tích của miền giới hạn bởi trục $\omega$ và đường cong biểu diễn $G(\omega)$ (Hình 2.3).

**Ý nghĩa vật lý:**

Bề rộng phổ đặc trưng cho sự tập trung công suất (hoặc năng lượng) của tín hiệu ngẫu nhiên ở quanh một tần số trung tâm, ngoài ra nó cũng đặc trưng cho cả sự bằng phẳng của phổ ở quanh tần số trung tâm $\omega_0$.

### 2.4.4. Mở rộng cặp biến đổi Wiener – Khinchin cho trường hợp $R(\tau)$ không khả tích tuyệt đối

Nếu quá trình ngẫu nhiên $x(t)$ chứa các thành phần dao động điều hoà dạng:
$$x_K(t) = A_K \cos(\omega_K t - \varphi_K)$$
trong đó $A_K$ và $\varphi_K$ nói chung có thể là các đại lượng ngẫu nhiên, thì hàm tương quan trung bình:
$$R_{x_K}^*(\tau) = \frac{A_K^2}{2} \cos \omega_K \tau$$ không thoả mãn điều kiện khả tích tuyệt đối.

Nếu sử dụng biểu diễn sau của hàm delta:
$$\int_{-\infty}^{\infty} e^{jxy} dx = \int_{-\infty}^{\infty} \cos(xy) dx = \delta(y)$$
và biểu diễn phổ năng lượng của $x_K(t)$ dưới dạng:
$$G_K^*(\omega) = \frac{A_K^2}{4} [\delta(\omega - \omega_K) + \delta(\omega + \omega_K)]$$
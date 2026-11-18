xét là hữu hạn. Khi $\tau \to \infty$, thì coi như hai giá trị ấy không tương quan với nhau nữa. Tuy vậy, trong thực tế, đối với hầu hết các quá trình ngẫu nhiên chỉ cần $\tau$ đủ lớn thì sự tương quan giữa hai giá trị của quá trình đã mất. Do đó, đối với tính toán thực tế người ta định nghĩa khoảng (thời gian) tương quan như sau:

**Định nghĩa 2.1.**

Khoảng tương quan $\tau_k$ là khoảng thời gian trong đó $\tau_\xi(\tau)$ không nhỏ hơn 0,05. (hình vẽ 2.2). Như vậy, $\forall \tau > \tau_k$ thì xem như hết tương quan.

Nếu cho biểu thức giải tích của $\tau_\xi(\tau)$ thì $\tau_K$ được tính như sau:

$$\tau_k = \frac{1}{2} \int_{-\infty}^{\infty} |\tau_\xi(\tau)| d\tau \tag{2.11}$$

[Hình: Đồ thị hàm tương quan $\tau_\xi(\tau)$ hình chuông đối xứng qua trục tung, xác định khoảng tương quan $\tau_k$ tại giá trị 0,05 và minh họa bằng một hình chữ nhật bao quanh.]

**Hình 2.2. Khoảng tương quan**

**Ý nghĩa hình học:**

$\tau_K$ là nửa cạnh đáy của hình chữ nhật có chiều cao bằng đơn vị K, có diện tích bằng diện tích của miền giới hạn bởi trục hoành và đường biểu diễn $\tau_\xi(\tau)$.

Trong thực tế, ta thường gặp những quá trình ngẫu nhiên ergodic. Ví dụ: tạp âm của các máy thu vô tuyến điện... Đối với các quá trình ngẫu nhiên ergodic, ta có thể xác định các đặc trưng thống kê của chúng bằng thực nghiệm một cách dễ dàng.

Ta đã biết rằng, nếu X(t) – ergodic và với T đủ lớn thì ta có thể viết:

$$R_x(\tau) = M \{ [x(t) - m_x] . [x(t - \tau) - m_x] \}$$
$$\approx \frac{1}{T} \int_{0}^{T} [x(t) - m_x] . [x(t + \tau) - m_x] dt \tag{2.12}$$

Trung bình thống kê = trung bình theo thời gian.
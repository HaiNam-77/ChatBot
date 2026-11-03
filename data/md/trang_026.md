$$R(\tau) = \frac{1}{2\pi} \int_{-\infty}^{\infty} G(\omega) e^{j\omega\tau} d\omega \quad (2.21)$$

Cặp công thức (2.20) và (2.21) gọi là cặp biến đổi Wiener – Khinchin, đó là sự mở rộng cặp biến đổi Fourier sang các tín hiệu ngẫu nhiên dừng (ít nhất là theo nghĩa rộng).

Rõ ràng từ định nghĩa (2.17) của mật độ phổ công suất, ta thấy hàm $G(\omega)$ là hàm chẵn của đối số $\omega$. Do đó sau khi dùng công thức Euler ($e^{\pm j\omega\tau} = \cos \omega\tau \pm j \sin \omega\tau$) để biến đổi thức (2.20) và (2.21), ta được:

$$G(\omega) = 2 \int_{0}^{\infty} R(\tau) \cos \omega\tau d\tau$$
$$R(\tau) = \frac{1}{\pi} \int_{0}^{\infty} G(\omega) \cos \omega\tau d\omega \quad (2.22)$$

**Chú ý 1:**

Từ mật độ phổ công suất của tín hiệu ngẫu nhiên, không thể sao lại bất cứ một thể hiện nào (là hàm của thời gian $t$) của nó, vì $G(\omega)$ không chứa những thông tin (những hiểu biết) về pha của các thành phần phổ riêng lẻ. Đối với tín hiệu xác định thì từ mật độ phổ hoàn toàn có thể sao lại chính tín hiệu đó nhờ tích phân ngược Fourier. Đó là chỗ khác nhau về bản chất giữa biến đổi Fourier và biến đổi Wiener – Khinchin.

**Chú ý 2:**

Nếu phải xét đồng thời hai quá trình ngẫu nhiên thì người ta cũng đưa ra khái niệm mật độ phổ chéo. Mật độ phổ chéo và hàm tương quan chéo của hai quá trình ngẫu nhiên có liên hệ dừng cũng thoả mãn cặp biến đổi Wiener – Khinchin.

### 2.4.3. Bề rộng phổ công suất

Một đặc trưng vật lý quan trọng khác của các tín hiệu ngẫu nhiên là bề rộng phổ công suất, nó được định nghĩa bởi công thức sau:

$$\Delta\omega = \frac{\int_{0}^{\infty} G(\omega) d\omega}{G(\omega_0)} \quad (2.23)$$

Trong đó:

$G(\omega)$ là mật độ phổ công suất của tín hiệu ngẫu nhiên.

$G(\omega_0)$ là giá trị cực đại của $G(\omega)$.

$\Delta\omega$ là bề rộng phổ công suất (còn gọi là bề rộng phổ) của quá trình ngẫu nhiên.
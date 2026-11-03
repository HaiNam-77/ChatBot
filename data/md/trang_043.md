Trong đó $n$ là số các giá trị rời rạc (còn gọi là các giá trị mẫu) của thể hiện tín hiệu $x(t)$ trong khoảng quan sát $T$; còn $x_k$ là giá trị mẫu thứ $k$ của $x(t)$ tại thời điểm rời rạc $k\Delta t$. Để cho gọn, ta đặt $\omega_c(t - k\Delta t) = \lambda$, khi đó (2.65) có dạng:

$$E \approx \frac{1}{\omega_c} \int_{-T/2}^{T/2} \left[ \sum_{k=1}^n x_k \frac{\sin \lambda}{\lambda} \right]^2 d\lambda = \frac{1}{\omega_c} \sum_{k=1}^n x_k^2 \int_{-T/2}^{T/2} \frac{\sin^2 \lambda}{\lambda^2} d\lambda$$

Ta có: $\int_{-T/2}^{T/2} \frac{\sin^2 \lambda}{\lambda^2} d\lambda \approx \pi$ (với $T$ khá lớn)

$$\Rightarrow E = \frac{\pi}{\omega_c} \sum_{k=1}^n x_k^2 = \frac{1}{2F_c} \sum_{k=1}^n x_k^2 \quad (2.66)$$

Biểu thức (2.66) cho ta tính được năng lượng của chuỗi

### 2.7.1.2. Biểu diễn $x(t)$ thành vectơ $\vec{x}$ trong không gian $n$ chiều

Khai triển Kachennhicov (2.65) là một dạng khai triển trực giao. Các hàm $\psi_k(t) = \frac{\sin \omega_c(t - k\Delta t)}{\omega_c(t - k\Delta t)}$ là các hàm trực giao.

$$\left( \int_{-\infty}^{\infty} \frac{\sin \omega_c(t - k\Delta t)}{\omega_c(t - k\Delta t)} \cdot \frac{\sin \omega_c(t - i\Delta t)}{\omega_c(t - i\Delta t)} dt = \begin{cases} \pi/\omega_c, & i = k \\ 0, & i \neq k \end{cases} \right)$$

Vì vậy ta có thể coi mỗi hàm là một vector đơn vị trên hệ trục toạ độ trực giao. Khi $T$ hữu hạn thì $k_{\max} = n$ cũng sẽ hữu hạn. Khi đó ta có thể coi $x(t)$ là một vectơ $\vec{x}$ trong không gian $n$ chiều có các thành phần (hình chiếu) trên các trục toạ độ tương ứng là $x(k\Delta t), (k = \overline{1, n})$.

$$x(t) \Leftrightarrow \{x(t - \Delta t), x(t - 2\Delta t), \dots, x(t - n\Delta t)\}$$
$$x(t) \Leftrightarrow \{x_1, x_2, \dots, x_n\} \Leftrightarrow \vec{x}$$

Theo định nghĩa, độ dài (hay chuẩn) của vector $\vec{x}$ sẽ là:

$$\|\vec{x}\| = \sqrt{\sum_{k=1}^n x_k^2} \left( = \sqrt{(\vec{x}, \vec{x})} \right) \quad (2.67)$$

Để ý đến (2.66), ta có:

$$\|\vec{x}\| = \sqrt{2F_c E} = \sqrt{2F_c T \cdot P} = \sqrt{nP} \quad (2.68)$$
$$\left( n = \frac{T}{\Delta t} = 2F_c T \right)$$

Trong đó $P$ là công suất của thể hiện tín hiệu trong khoảng hữu hạn $T$. Như vậy, với thời hạn quan sát và bề rộng phổ của thể hiện cho trước thì độ dài của vector biểu diễn tỷ lệ với
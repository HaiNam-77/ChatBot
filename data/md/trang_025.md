$$
\begin{aligned}
G(\omega) &= M \lim_{T \to \infty} \frac{|\dot{S}_T(\omega)|^2}{T} = \lim_{T \to \infty} \frac{M|\dot{S}_T(\omega)|^2}{T} = \\
&= \lim_{T \to \infty} \frac{1}{T} M \{\dot{S}_T(\omega) \dot{S}_T^*(\omega)\} \\
&= \lim_{T \to \infty} \frac{1}{T} M \left\{ \int_{-T/2}^{T/2} x_T(t_1) e^{-j\omega t_1} dt_1 \cdot \int_{-T/2}^{T/2} x_T(t_2) e^{-j\omega t_2} dt_2 \right\} \\
&= \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} \int_{-T/2}^{T/2} M \{x_T(t_1) x_T(t_2)\} e^{-j\omega(t_1 - t_2)} dt_1 dt_2
\end{aligned}
$$

Nhưng theo định nghĩa (2.8), ta thấy ngay $M \{x_T(t_1) x_T(t_2)\}$ là hàm tự tương quan của quá trình ngẫu nhiên trung tâm (có $m_x = 0$) nên ta có thể viết:

$$M \{x_T(t_1) x_T(t_2)\} = R_T(t_1, t_2)$$

Nếu $\tau = -t_2 + t_1$ thì đối với những quá trình dừng, ta có:

$$M \{x_T(t_1) x_T(t_2)\} = R_T(\tau)$$

Ta có thể viết lại biểu thức cho $G(\omega)$:

$$
\begin{aligned}
G(\omega) &= \lim_{T \to \infty} \left\{ \frac{1}{T} \int_{-\frac{T}{2}-t_2}^{\frac{T}{2}+t_2} R_T(\tau) e^{-j\omega \tau} d\tau \int_{-T/2}^{T/2} dt_2 \right\} \\
&= \lim_{T \to \infty} \frac{1}{T} \int_{-\frac{T}{2}-t_2}^{\frac{T}{2}+t_2} R_T(\tau) e^{-j\omega \tau} d\tau \cdot \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} dt_2
\end{aligned}
$$

$$G(\omega) = \int_{-\infty}^{\infty} R(\tau) e^{-j\omega \tau} d\tau \tag{2.20}$$

Tất nhiên ở đây phải giả sử tích phân ở vế phải của (2.20) tồn tại. Điều này luôn luôn đúng nếu hàm tự tương quan $R(\tau)$ khả tích tuyệt đối, tức là:

$$\int_{-\infty}^{\infty} R(\tau) d\tau < \infty$$

Biểu thức (2.20) là mật độ phổ công suất của quá trình ngẫu nhiên dừng. Nó biểu diễn một cách trung bình (thống kê) sự phân bố công suất của quá trình ngẫu nhiên theo tần số của các thành phần dao động điều hoà nguyên tố (tức là những thành phần dao động điều hoà vô cùng bé).

Như vậy, từ (2.20) ta có thể kết luận rằng phổ công suất $G(\omega)$ của quá trình ngẫu nhiên dừng là biến đổi thuận Fourier của hàm tự tương quan $R(\tau)$. Hiển nhiên rằng khi đã tồn tại biến đổi thuận Fourier thì cũng tồn tại biến đổi ngược Fourier sau:
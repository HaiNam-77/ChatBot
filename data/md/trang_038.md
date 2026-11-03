Hilbert đã chứng tỏ rằng phần thực và phần ảo của hàm phức (2.47) liên hệ với nhau bởi các biến đổi tích phân đơn trị hai chiều sau:

$$\hat{x}(t) = \text{Im}[\dot{x}(t)] = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{x(\tau)}{t - \tau} d\tau = h[x(t)] \tag{2.48}$$

$$x(t) = -\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\hat{x}(\tau)}{t - \tau} d\tau = \text{Re}[\dot{x}(t)] = h^{-1}[\hat{x}(t)] \tag{2.49}$$

Cặp công thức trên được gọi là cặp biến đổi Hilbert. Trong đó (2.48) gọi là biến đổi thuận Hilbert, còn (2.49) gọi là biến đổi Hilbert ngược.

**Chú ý:**

Cũng giống như tính chất của các tích phân, biến đổi Hilbert là một phép biến đổi tuyến tính.

(Một phép biến đổi f được gọi là tuyến tính nếu có:
$$f(x_1 + x_2) = f(x_1) + f(x_2)$$
$$f(kx) = kf(x), k = const$$

Các hàm $x(t)$ và $\hat{x}(t)$ được gọi là liên hiệp Hilbert đối với nhau. Tín hiệu phức $\dot{x}(t)$ có phần thực và phần ảo thoả mãn cặp biến đổi Hilbert gọi là tín hiệu giải tích (tương ứng với tín hiệu thực $x(t)$).

**b. Biến đổi Hilbert đối với tín hiệu hình sin:**

Trong mục này ta sẽ chứng tỏ $\cos \omega_0 t$ và $\sin \omega_0 t$ thoả mãn cặp biến đổi H. Thật vậy:

$$\hat{x}(t) = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\cos \omega_0 \tau}{t - \tau} d\tau = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\cos[\omega_0(t - \tau) - \omega_0 t]}{t - \tau} d\tau =$$
$$= \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\cos \omega_0(t - \tau) \cos \omega_0 t + \sin \omega_0(t - \tau) \sin \omega_0 t}{t - \tau} d\tau =$$
$$= \frac{\cos \omega_0 t}{\pi} \int_{-\infty}^{\infty} \frac{\cos \omega_0(t - \tau)}{t - \tau} d\tau + \frac{\sin \omega_0 t}{\pi} \int_{-\infty}^{\infty} \frac{\sin \omega_0(t - \tau)}{t - \tau} d\tau$$

Chú ý rằng: $\int_{-\infty}^{\infty} \frac{\cos az}{z} dz = 0$ và $\int_{-\infty}^{\infty} \frac{\sin az}{z} dz = \pi$

$$\Rightarrow \hat{x}(t) = \sin \omega_0 t$$

Vậy $(\sin \omega_0 t)$ là liên hợp H của $(\cos \omega_0 t)$

Tương tự $(-\cos \omega_0 t)$ là liên hợp phức H của $(\sin \omega_0 t)$

**c. Biến đổi H đối với các hàm tổng quát hơn:**

- Đối với các hàm tuần hoàn $x(t)$:

Trong “Lý thuyết mạch” ta đã biết, chuỗi Fourier của hàm tuần hoàn (thoả mãn điều kiện Dirichlet) là:

$$x(t) = \sum_{k=0}^{\infty} (a_k \cos k\omega_0 t + b_k \sin k\omega_0 t) \tag{2.50}$$
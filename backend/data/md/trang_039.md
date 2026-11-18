Vì biến đổi H là biến đổi tuyến tính nên biến đổi H của tổng bằng tổng các biến đổi H của các hàm thành phần, nên:

$$\hat{x}(t)=h[x(t)]=\sum_{k=0}^{\infty}\left(a_{k} \sin k \omega_{0} t-b_{k} \cos k \omega_{0} t\right) \tag{2.51}$$

Các biểu thức (2.50) và (2.51) gọi là chuỗi liên hiệp H.
- khi $x(t)$ không tuần hoàn:
Nếu hàm không tuần hoàn $x(t)$ khả tích tuyệt đối thì khai triển Fourier của nó là:

$$x(t)=\frac{1}{2 \pi} \int_{0}^{\infty}[a(\omega) \cos \omega t+b(\omega) \sin \omega t] d \omega \tag{2.52}$$

Khi đó:

$$\begin{aligned} \hat{x}(t)=h[x(t)] & =\frac{1}{2 \pi} h\left(\int_{0}^{\infty}[a(\omega) \cos \omega t+b(\omega) \sin \omega t] d \omega\right) \\ & =\frac{1}{2 \pi} \int_{0}^{\infty}\{H[a(\omega) \cos \omega t]+H[b(\omega) \sin \omega t]\} d \omega \\ & =\frac{1}{2 \pi} \int_{0}^{\infty}[a(\omega) \sin \omega t-b(\omega) \cos \omega t] d \omega \end{aligned} \tag{2.53}$$

Các biểu thức (2.52) và (2.53) gọi là các tích phân liên hiệp H.

**d. Các yếu tố của tín hiệu giải tích:**

Từ (2.50) và (2.51) (hoặc từ (2.52) và (2.53)) ta xây dựng được tín hiệu giải tích ứng với tín hiệu thực $x(t)$ như sau:

$$\dot{x}(t)=x(t)+j \hat{x}(t)=A(t) e^{j \theta(t)}$$
$$x(t)=\operatorname{Re}[\dot{x}(t)]=A(t) \cos \theta(t) \tag{2.54}$$
$$\hat{x}(t)=\operatorname{Im}[\dot{x}(t)]=A(t) \sin \theta(t) \tag{2.55}$$

- Đường bao của tín hiệu giải tích:
Từ (2.54) và (2.55) ta thấy:

$$A(t)=\sqrt{x^{2}(t)+\hat{x}^{2}(t)} \tag{2.56}$$

$A(t)$ đặc trưng cho sự biến thiên (dạng biến thiên) của biên độ của tín hiệu (Hình 2.13).
$A(t)$ được gọi là đường bao của tín hiệu (còn gọi là biên độ biến thiên hay biên độ tức thời của tín hiệu).
- Pha tức thời của tín hiệu giải tích:
Ký hiệu pha tức thời: $\theta(t)$ bằng:

$$\theta(t)=\operatorname{arctg} \frac{\hat{x}(t)}{x(t)} \tag{2.57}$$
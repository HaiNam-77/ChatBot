Thì (2.61) có thể khai triển như sau:
$$
\begin{aligned}
x(t) &= A(t) \cos \omega_0 t \cdot \cos \varphi(t) + A(t) \sin \omega_0 t \cdot \sin \varphi(t) \\
&= A(t) \cos \varphi(t) \cdot \cos \omega_0 t + A(t) \sin \varphi(t) \cdot \sin \omega_0 t \quad (2.62) \\
&= c(t) \cos \omega_0 t + s(t) \sin \omega_0 t
\end{aligned}
$$
$c(t) \cos \omega_0 t$ là tín hiệu điều biên biến đổi chậm
$s(t) \sin \omega_0 t$ là tín hiệu điều biên biến đổi chậm

Vậy một tín hiệu dải hẹp hình sin bao giờ cũng có thể biểu diễn dưới dạng tổng của hai tín hiệu điều biên biến đổi chậm, với các yếu tố xác định như sau:
$$
\begin{cases}
A(t) = \sqrt{c^2(t) + s^2(t)} \\
\varphi(t) = \text{arctg} \frac{s(t)}{c(t)} \\
\omega(t) = \frac{d\theta(t)}{dt}
\end{cases} \quad (2.63)
$$
Rõ ràng là các số hạng ở vế phải (2.62) thoả mãn cặp biến đổi Hilbert.
Việc biểu diễn một tín hiệu dải hẹp thành tổng của hai tín hiệu điều biên biến thiên chậm sẽ làm cho việc phân tích mạch vô tuyến điện dưới tác động của nó đơn giản đi nhiều. Ta sẽ xét lại bài toán này ở phần sau.

### 2.7. BIỂU DIỄN HÌNH HỌC CHO THỂ HIỆN CỦA TÍN HIỆU NGẪU NHIÊN

#### 2.7.1. Khai triển trực giao và biểu diễn vector của tín hiệu

##### 2.7.1.1. Năng lượng của chuỗi Kachennhicov

Ta đã biết rất rõ khai triển trực giao Fourier cho các hàm $x(t)$ có phổ vô hạn. Ở giáo trình “Lý thuyết mạch”, ta cũng biết rằng một hàm $x(t)$ có phổ không chứa tần số lớn hơn $F_c$ có thể phân tích thành chuỗi trực giao Kachennhicov sau:
$$x(t) = \sum_{k=-\infty}^{\infty} x(k\Delta t) \frac{\sin 2\pi F_c (t - k\Delta t)}{2\pi F_c (t - k\Delta t)} \quad (2.64)$$
Trong đó: $\Delta t = \frac{1}{2 F_c}$

Nếu ta chỉ xét tín hiệu có phổ hữu hạn $x(t)$ trong khoảng thời gian T hữu hạn thì ta có biểu thức gần đúng sau để tính năng lượng của nó:
$$E = \int_{-T/2}^{T/2} x^2(t) dt \approx \int_{-T/2}^{T/2} \left[ \sum_{k=1}^{n} x_k \frac{\sin \omega_c (t - k\Delta t)}{\omega_c (t - k\Delta t)} \right]^2 dt \quad (2.65)$$
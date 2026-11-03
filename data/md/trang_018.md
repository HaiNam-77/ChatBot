# CHƯƠNG 2. TÍN HIỆU VÀ NHIỄU

## 2.1. TÍN HIỆU XÁC ĐỊNH VÀ CÁC ĐẶC TRƯNG VẬT LÝ CỦA CHÚNG

Tín hiệu xác định thường được xem là một hàm xác định của biến thời gian $t$ ($s(t)$). Hàm này có thể được mô tả bằng một biểu thức giải tích hoặc được mô tả bằng đồ thị. Một trong các đặc trưng vật lý quan trọng của tín hiệu là hàm mật độ phổ biên độ phức $\dot{S}(\omega)$. Với tín hiệu $s(t)$ khả tích tuyệt đối, ta có cặp biến đổi Fourier sau:

$$\dot{S}(\omega) = \int_{-\infty}^{\infty} s(t) e^{-j\omega t} dt \tag{2.1}$$

$$s(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \dot{S}(\omega) e^{j\omega t} d\omega \tag{2.2}$$

Sau đây là một số đặc trưng vật lý quen thuộc của tín hiệu:
- Thời hạn của tín hiệu (T): Thời hạn của tín hiệu là khoảng thời gian tồn tại của tín hiệu, trong khoảng này giá trị của tín hiệu không đồng nhất bằng 0.
- Bề rộng phổ của tín hiệu (F): Đây là miền xác định bởi tần số khác không cao nhất của tín hiệu.
- Năng lượng của tín hiệu (E): Năng lượng của tín hiệu có thể tính theo miền thời gian hay miền tần số.

$$E = \int_{-\infty}^{\infty} s^2(t) dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |\dot{S}(\omega)|^2 d\omega \quad [J] \tag{2.3}$$

(Định lý Parseval)
- Công suất của tín hiệu (P):

$$P = \frac{E}{T} \quad [W]$$

## 2.2. TÍN HIỆU VÀ NHIỄU LÀ CÁC QUÁ TRÌNH NGẪU NHIÊN

### 2.2.1. Bản chất ngẫu nhiên của tín hiệu và nhiễu

Như đã xét ở trên, chúng ta coi tín hiệu là biểu hiện vật lý của tin (trong thông tin vô tuyến: dạng vật lý cuối cùng của tin là sóng điện từ). Quá trình vật lý mang tin diễn ra theo thời gian, do đó về mặt toán học thì khi có thể được, cách biểu diễn trực tiếp nhất cho tín hiệu là viết biểu thức của nó theo thời gian hay vẽ đồ thị thời gian của nó.

Trong lý thuyết cổ điển, dù tín hiệu tuần hoàn hoặc không tuần hoàn nhưng ta đều coi là đã biết trước và biểu diễn nó bằng một hàm tiền định của thời gian. Đó là quan niệm xác định về tín hiệu (tín hiệu tiền định). Tuy vậy, quan niệm này không phù hợp với thực tế. Thật vậy, tín hiệu tiền định không thể dùng vào việc truyền tin tức được. Với cách coi tín hiệu là biểu...
### 2.4. CÁC ĐẶC TRƯNG VẬT LÝ CỦA TÍN HIỆU NGẪU NHIÊN VÀ NHIỄU, BIẾN ĐỔI WIENER – KHINCHIN

#### 2.4.1. Những khái niệm xây dựng lý thuyết phổ của quá trình ngẫu nhiên - mật độ phổ công suất

Mục trước ta mới chỉ đưa ra một số đặc trưng thống kê của các quá trình ngẫu nhiên (tín hiệu, nhiễu) mà chưa đưa ra các đặc trưng vật lý của chúng. Về mặt lý thuyết cũng như thực tế, các đặc trưng vật lý của tín hiệu ngẫu nhiên (quá trình ngẫu nhiên) đóng một vai trò rất quan trọng ở những chương sau khi nói đến cơ sở lý thuyết chống nhiễu cũng như xét các biện pháp thực tế và các thiết bị chống nhiễu ta không thể không dùng đến những đặc trưng vật lý của tín hiệu ngẫu nhiên và nhiễu. Khi xét các loại tín hiệu xác định trong giáo trình “Lý thuyết mạch”, chúng ta đã làm quen với các đặc trưng vật lý của chúng như: năng lượng, công suất, thời hạn của tín hiệu, phổ biên độ phức, mật độ phổ, bề rộng phổ, ... Cơ sở để hình thành các đặc trưng vật lý này là chuỗi và tích phân Fourier.

Đối với các tín hiệu ngẫu nhiên và nhiễu, ta không thể dùng trực tiếp các biến đổi Fourier để xây dựng các đặc trưng vật lý của chúng được vì những lý do sau:
- Tập các thể hiện $\{x_i(t)\}, i = 1, 2, ... \infty$ của quá trình ngẫu nhiên $x(t)$ cho trên khoảng T thường là một tập vô hạn (thậm chí nó cũng không phải là một tập đếm được).
- Nếu tín hiệu ngẫu nhiên là dừng chặt thì tập vô hạn các thể hiện theo thời gian của nó thường sẽ không khả tích tuyệt đối. Tức là:
$$\lim_{T \to \infty} \int_{-T/2}^{T/2} |x(t)| dt = \infty$$

Để tránh khỏi những khó khăn trên, ta làm như sau:

Lấy hàm $x_T(t)$ trùng với một thể hiện của quá trình ngẫu nhiên trung tâm $x(t)$ (QTNN trung tâm là QTNN có kỳ vọng không) ở trong đoạn $\left[ -\frac{T}{2}, \frac{T}{2} \right]$ và nó bằng không ở ngoài đoạn đó:

$$x_T(t) = \begin{cases} x(t) & |t| \le T/2 \\ 0 & |t| > T/2 \end{cases} \tag{2.13}$$

Từ (2.13), ta thấy $x_T(t)$ thoả mãn điều kiện khả tích tuyệt đối nên có thể dùng biến đổi Fourier cho nó được. Ta đã biết rằng phổ biên độ phức $\dot{S}_T(\omega)$ của $x_T(t)$ được xác định bởi tích phân thuận Fourier sau:

$$\dot{S}_T(\omega) = \int_{-T/2}^{T/2} x_T(t) e^{-j\omega t} dt \tag{2.14}$$

Theo định lý Parseval, ta có biểu thức tính năng lượng của $x_T(t)$ như sau:

$$E_T = \int_{-\infty}^{\infty} x_T^2(t) dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |\dot{S}_T(\omega)|^2 d\omega \tag{2.15}$$
[Hình: Đồ thị hàm số $y = \ln x$ và tiếp tuyến $y = x - 1$ tiếp xúc tại điểm $(1, 0)$ trên hệ trục tọa độ vuông góc $Oxy$, đường thẳng cắt trục tung tại $-1$.]

Hình 3.1.

$\underline{\text{Ví dụ:}}$ $\text{H}_0(\text{Việt}) = \log_2 36 = 5,1713\,\text{bit}$

$\text{H}_0(\text{Nga}) = \log_2 32 = 5\,\text{bit}$

$\text{H}_0(\text{Anh}) = \log_2 27 = 4,75489\,\text{bit}$

### 3.2.4. Entropy của nguồn rời rạc, nhị phân

Nguồn rời rạc nhị phân là nguồn chỉ có hai dấu:
$$
\begin{cases}
a_1 \Leftrightarrow \text{"0"} & \text{với xác suất } p(a_1) = p \\
a_2 \Leftrightarrow \text{"1"} & \text{với xác suất } p(a_2) = 1-p
\end{cases}
$$

Ta có ngay:
$$H_1(A) = -\sum_{i=1}^2 p(a_i) \log p(a_i) = -p\log p - (1-p)\log(1-p) = f(p) \tag{3.18}$$

Đồ thị $f(p)$ được biểu diễn trên hình 3.2.

[Hình: Đồ thị hàm số $H_1(A) = f(p)$ đối xứng qua đường thẳng $p = 0,5$, đi qua các điểm $(0, 0)$ và $(1, 0)$, đạt giá trị cực đại $H_1(A)_{\max} = 1$ tại $p = 0,5$.]

Hình 3.2.

Ta thấy $H_1(A) = f(p)$ chỉ phụ thuộc vào đặc tính thống kê của các tin.

Nếu đơn vị dùng là bit thì $\max H_1(A) = 1$
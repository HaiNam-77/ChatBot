với $c(t)$ và $s(t)$ có phân bố chuẩn cùng công suất trung bình và với $\varphi = arctg \frac{s(t)}{c(t)}$

$A(t) = \sqrt{c^2(t) + s^2(t)}$ - đường bao của nhiễu.

Công suất trung bình của cả hai thành phần của nhiễu bằng nhau và bằng hằng số: $\sigma_c^2 = \sigma_s^2 = \sigma^2$. Khi $n(t)$ dừng, người ta coi là hai thành phần của nhiễu không tương quan.

Tác động $n(t)$ lên bộ tách sóng tuyến tính. Hãy tìm mật độ xác suất một chiều của điện áp ra bộ tách sóng biết rằng bộ tách sóng không gây méo đường bao và không gây thêm một lượng dịch pha nào. Thực chất của bài toán là phải tìm $W_1(A)$ và $W_1(\varphi)$.

Trong giáo trình “lý thuyết xác suất”, ta đã có công thức tìm mật độ xác suất một chiều của từng đại lượng ngẫu nhiên theo mật độ xác suất đồng thời của chúng, nên ta có:

$$W_1(A) = \int_0^{2\pi} W_2(A, \varphi) d\varphi$$
$$W_1(\varphi) = \int_0^\infty W_2(A, \varphi) dA$$

Do đó, vấn đề ở đây là phải tìm $W_2(A, \varphi)$.

Vì bộ tách sóng không gây méo đường bao và không gây thêm một lượng dịch pha nào nên $W_2(A, \varphi)$ ở đầu ra cũng chính là $W_2(A, \varphi)$ ở đầu vào.

Tìm $W_2(A, \varphi)$: Vì đầu bài chỉ cho $W_1(c)$ và $W_1(s)$ nên ta phải tìm $W_2(A, \varphi)$ theo $W_2(c, s)$.

Theo giả thiết $c(t)$ và $s(t)$ không tương quan nên:

$$W_2(c, s) = W_1(c)W_1(s) \tag{2.38}$$
$$\Rightarrow W_2(c, s) = \frac{1}{\sqrt{2\pi}\sigma} \exp(-c^2 / 2\sigma^2) \frac{1}{\sqrt{2\pi}\sigma} \exp(-s^2 / 2\sigma^2) = \frac{1}{2\pi\sigma^2} \exp \left\{ -\frac{c^2 + s^2}{2\sigma^2} \right\}$$
$$W_2(c, s) = \frac{1}{2\pi\sigma^2} \exp \left\{ -\frac{1}{2\sigma^2} A^2 \right\} \tag{2.39}$$

Ta thấy xác suất để một điểm có toạ độ $(c, s)$ trong hệ toạ độ Đêcac rơi vào một yếu tố diện tích $dcds$ sẽ bằng: $P_{dcds} = W_2(c, s)dcds$. Để ý đến (2.37) ta thấy xác suất này cũng chính là xác suất để một điểm có toạ độ $(A, \varphi)$ trong hệ toạ độ cực rơi vào một yếu tố diện tích $dAd\varphi$. Ta có:

$$P_{dcds} = W_2(c, s)dcds = W_2(A, \varphi)dAd\varphi \tag{2.40}$$

Từ đó:

$$W_2(A, \varphi) = W_2(c, s) \frac{dcds}{dAd\varphi} \tag{2.41}$$
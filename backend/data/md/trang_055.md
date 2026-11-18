$$I(x_k, y_\ell) = I(x_k) - I(x_k / y_\ell)$$
$$= \log \frac{1}{p(x_k)} - \log \frac{1}{p(x_k / y_\ell)}$$
$$\Rightarrow I(x_k, y_\ell) = \log \frac{p(x_k / y_\ell)}{p(x_k)} \quad (3.11)$$

Biểu thức (3.11) gọi là lượng thông tin về $x_k$ khi đã rõ tin $y_\ell$ hay còn gọi là lượng thông tin chéo về $x_k$ do $y_\ell$ mang lại.

Nếu việc truyền tin không bị nhiễu thì $y_\ell = x_k$. Tức là nếu phát $x_k$ thì chắc chắn nhận được chính nó. Khi đó:
$$p(x_k / y_\ell) = p(x_k / x_k) = 1$$
Từ (3.11) ta có:
$$I(x_k, y_\ell) = I(x_k, x_k) = I(x_k) = \log \frac{1}{p(x_k)} \quad (**)$$

Như vậy khi không có nhiễu, lượng thông tin nhận được đúng bằng độ bất định của sự kiện $x_k$, tức là đúng bằng thông tin tiên nghiệm của $x_k$.

Vậy lượng thông tin tổn hao trong kênh sẽ là:
$$I(x_k) - I(x_k, y_\ell) = I(x_k / y_\ell)$$

Đơn vị đo của thông tin (lượng thông tin) cũng chính là đơn vị đo độ bất định.
Nếu cơ số của logarit là 10 thì đơn vị đo thông tin được gọi là Hartley, hay đơn vị thập phân.
Nếu cơ số của logarit là $e = 2,718...$ thì đơn vị đo thông tin được gọi là nat, hay đơn vị đo tự nhiên.
Nếu cơ số của logarit là 2 thì đơn vị đo thông tin được gọi là bit, hay đơn vị nhị phân.
1 Hartley = 3,322 bit
1 nat = 1,443 bit

### 3.2. ENTROPY VÀ CÁC TÍNH CHẤT CỦA ENTROPY

#### 3.2.1. Tính chất thống kê của nguồn rời rạc và sự ra đời của khái niệm entropy

Trong mục trước, ta mới chỉ xét đến lượng thông tin về một biến cố (hay một tin) trong một tập các biến cố (hay tin) xung khắc, đồng xác suất.

Thực tế tồn tại phổ biến loại tập các biến cố (hay nguồn tin, tập tin) xung khắc, không đồng xác suất. Tức là xác suất xuất hiện các biến cố khác nhau trong tập là khác nhau. Ta gọi sự khác nhau giữa các xác suất xuất hiện biến cố của tập (hay tin của nguồn rời rạc) là tính chất thống kê của nó.
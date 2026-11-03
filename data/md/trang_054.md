$$I(x_k) = k \ln[p(x_k)] \tag{3.6}$$

Hệ số tỷ lệ $k$ trong (3.6) có thể chọn tuỳ ý, nó chỉ xác định hệ đơn vị đo của $I(x_k)$. Vì $\ln[p(x_k)] \le 0$ nên để $I(x_k) \ge 0$ thì $k < 0$.

Nếu lấy $k = -1$ thì:
$$I(x_k) = -\ln[p(x_k)] = \ln\left[\frac{1}{p(x_k)}\right] \tag{3.7}$$

Khi đó, đơn vị đo độ bất định sẽ là đơn vị tự nhiên, ký hiệu là nat.

Nếu lấy $k = -\frac{1}{\ln 2}$ thì:
$$I(x_k) = -\frac{\ln p(x_k)}{\ln 2} = -\log_2 p(x_k) \tag{3.8}$$

Khi đó đơn vị đo độ bất định sẽ là đơn vị nhị phân, ký hiệu là bit (1 nat = 1,443 bit)

Một bit chính là độ bất định chứa trong một phần tử (biến cố của tập xác suất chọn (xuất hiện) bằng 1/2. Người ta thường sử dụng đơn vị [bit] do trong kỹ thuật tính và kỹ thuật liên lạc thường dùng các mã nhị phân.

Ngoài ra, người ta còn có thể sử dụng những đơn vị đo khác tuỳ theo cách chọn cơ số của logarit. Vì vậy trong trường hợp tổng quát, ta có thể viết:
$$I(x_k) = -\log p(x_k) \tag{3.9}$$

### 3.1.3. Xác định lượng thông tin

Ở mục 1, ta đã có kết luận sau:

Lượng thông tin bằng độ bất định tiên nghiệm - độ bất định hậu nghiệm. Vì độ bất định sẽ trở thành thông tin khi nó bị thủ tiêu nên ta có thể coi độ bất định cũng chính là thông tin.

Do đó:

Lượng thông tin = thông tin tiên nghiệm – thông tin hậu nghiệm (*)

Thông tin tiên nghiệm (hay còn gọi là lượng thông tin riêng) được xác định theo (3.9). Còn thông tin hậu nghiệm xác định như sau:

Gọi $x_k$ là tin gửi đi, $y_l$ là tin thu được có chứa những dấu hiệu để hiểu biết về $x_k$ (có chứa thông tin về $x_k$). Khi đó xác suất để rõ về $x_k$ khi đã thu được $y_l$ là $p(x_k/y_l)$. Như vậy độ bất định của tin $x_k$ khi đã rõ $y_l$ bằng:
$$I(x_k/y_l) = -\log p(x_k/y_l) \tag{3.10}$$

Biểu thức (3.10) được gọi là thông tin hậu nghiệm về $x_k$ (thông tin riêng về $x_k$ sau khi có $y_l$).

Thay (3.9) và (3.10) vào (*), ta có:

Lượng thông tin về $x_k$ ký hiệu là $I(x_k, y_l)$ tính được:
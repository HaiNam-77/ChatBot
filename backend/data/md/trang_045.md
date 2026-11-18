Nếu $x(t)$ là xác định thì mút của vector $\vec{x}_0$ chỉ chiếm một điểm trong không gian $n$ chiều. Còn nếu $x(t)$ là ngẫu nhiên có một tập các thể hiện $\{x_i(t)\}$ thì mút vector $\vec{x}_0$ của nó sẽ chiếm một miền nào đó trong không gian $n$ chiều với thể tích: $V = \Delta x_1 \Delta x_2 \dots \Delta x_n$. Khi ấy, xác suất để tồn tại tín hiệu ngẫu nhiên trong miền có thể tích $dV$ sẽ là:

$$P \{t/hNN \in dV\} = P \{\text{mút vector t/h đó} \in dV\} =$$
$$= dP = W_n(x_1, x_2, \dots, x_n) dx_1 dx_2 \dots dx_n = W_n(\vec{x}_0) dV \quad (2.70)$$

Sau đây ta sẽ xét miền xác định của một số dạng tín hiệu ngẫu nhiên:
- Các thể hiện của tín hiệu phát có cùng đáy, cùng công suất:
Khi đó miền xác định của vector tín hiệu phát sẽ là mặt cầu có bán kính bằng chuẩn của vector tín hiệu phát $\|\vec{x}_0\| = \sqrt{P}$ và có tâm ở gốc toạ độ của vector ấy. (Sở dĩ như vậy vì $\vec{x}_0$ có chuẩn không đổi nhưng phương và chiều của nó thay đổi ngẫu nhiên).
- Tạp âm trắng:
Ta đã biết rằng các thể hiện $n_i(t)$ của tạp âm trắng $n(t)$ có cùng công suất $P_n$. Như vậy miền xác định của tạp âm trắng là mặt cầu có bán kính bằng $\sqrt{P_n}$, có tâm là gốc của vector tạp âm $\vec{n}_0$.
- Tổng của tín hiệu $x(t)$ và tạp âm $n(t)$:
$$y(t) = x(t) + n(t)$$
$$\Rightarrow \vec{y}_0 = \vec{x}_0 + \vec{n}_0 \Rightarrow \|\vec{y}_0\| = \sqrt{P_y}$$
Nếu $x(t)$ và tạp âm $n(t)$ không tương quan thì:
$$P_y = P_x + P_n \quad (\text{vì } B_y(0) = B_x(0) + B_n(0))$$
$$\Rightarrow \|\vec{y}_0\| = \sqrt{P_x + P_n} \Rightarrow \|\vec{y}_0\|^2 = P_x + P_n$$
$$\Rightarrow \|\vec{y}_0\|^2 = \|\vec{x}_0\|^2 + \|\vec{n}_0\|^2 \quad (2.71)$$
Từ (2.71) ta thấy $\vec{x}_0 \perp \vec{n}_0$ và $\vec{y}_0$ là cạnh huyền của một tam giác vuông có hai cạnh là $\vec{x}_0$ và $\vec{n}_0$.
Nếu $x(t)$ xác định thì miền xác định của mút $\vec{y}_0$ sẽ là đường tròn đáy của hình nón có đỉnh ở gốc tọa độ, chiều cao bằng $\|\vec{x}_0\|$ và bán kính bằng $\|\vec{n}_0\|$. (Hình 2.16).
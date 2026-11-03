Ta có:
$$
\begin{cases}
\frac{1}{(\sqrt{n})^2} \sum_{k=1}^n u_k^2 = \frac{1}{n} \|\vec{u}\|^2 = \|\vec{u}_0\|^2 = \|\vec{u}_0\| \|\vec{u}_0\| \cos(\vec{u}_0, \vec{u}_0) \\
\frac{1}{(\sqrt{n})^2} \sum_{k=1}^n v_k^2 = \frac{1}{n} \|\vec{v}\|^2 = \|\vec{v}_0\|^2 = \|\vec{v}_0\| \|\vec{v}_0\| \cos(\vec{v}_0, \vec{v}_0) \\
\frac{1}{n} \sum_{k=1}^n u_k v_k = (\vec{u}_0, \vec{v}_0) = \|\vec{u}_0\| \|\vec{v}_0\| \cos(\vec{u}_0, \vec{v}_0)
\end{cases}
$$
$\Rightarrow d^2(\vec{u}_0, \vec{v}_0) = \|\vec{u}_0\|^2 + \|\vec{v}_0\|^2 - 2\|\vec{u}_0\| \cdot \|\vec{v}_0\| \cos(\vec{u}_0, \vec{v}_0)$
$d^2(\vec{u}_0, \vec{v}_0) = \|\vec{u}_0\|^2 + \|\vec{v}_0\|^2 - 2\|\vec{u}_0\| \cdot \|\vec{v}_0\| \cos \varphi$

Trong đó $\varphi$ là góc hợp bởi $\vec{u}_0$ và $\vec{v}_0$ trong không gian $n$ chiều.
$$\cos \varphi = \frac{\vec{u}_0 \cdot \vec{v}_0}{\|\vec{u}_0\| \cdot \|\vec{v}_0\|} \tag{2.72}$$
$$d^2(\vec{u}_0, \vec{v}_0) = P_u + P_v - 2\sqrt{P_u P_v} \cos \varphi \tag{2.73}$$

Nếu ta không rời rạc hoá tín hiệu thì:
$$d(\vec{u}_0, \vec{v}_0) = \|\vec{u}_0 - \vec{v}_0\| = \sqrt{\frac{1}{T} \int_0^T [u(t) - v(t)]^2 dt}$$
$$d^2(\vec{u}_0, \vec{v}_0) = \frac{1}{T} \int_0^T u^2(t) dt + \frac{1}{T} \int_0^T v^2(t) dt - \frac{2}{T} \int_0^T u(t) v(t) dt$$
Hay
$$
\begin{aligned}
&= P_u + P_v - 2R_{uv}(t, t) \\
&= P_u + P_v - 2R_{uv}(0)
\end{aligned}
$$

Trong đó $R_{uv}(0)$ là hàm tương quan chéo của tín hiệu $u(t)$ và $v(t)$.
$$R_{uv}(0) = \sqrt{D_u(t) D_v(t)} \cdot \rho_{uv}(0)$$
$$d^2(u_0, v_0) = P_u + P_v - 2\sqrt{P_u P_v} \cdot \rho_{uv}(0) \tag{2.74}$$

So sánh (2.73) và (2.74) ta thấy ngay ý nghĩa hình học của hàm tương quan chéo chuẩn hoá: $\rho_{uv}(0)$ đóng vai trò cosin chỉ phương của hai vector tín hiệu.
$$\cos \varphi = \rho_{uv}(0) \tag{2.75}$$

**Kết luận:**
- Với một mức nhiễu xác định, xác suất thu đúng càng cao khi các thể hiện của tín hiệu càng cách xa nhau.
- Khoảng cách giữa hai mút của hai vector tín hiệu càng lớn khi độ dài hai vector càng lớn.
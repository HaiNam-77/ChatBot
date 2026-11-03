*Chú ý: Bảng này đưa ra với giả sử việc chọn các phần tử là đồng xác suất.*

### 3.1.2.2. Kết luận

+ Bảng này cho thấy: độ bất định gắn liền với bản chất ngẫu nhiên của phép chọn, của biến cố.
+ Độ bất định (ký hiệu I) là hàm của số phần tử thuộc tập $I(x_k) = f(n)$ (a)
+ Độ bất định có liên quan với xác suất chọn phần tử của tập $\Rightarrow I(x_k) = E[p(x_k)]$ (b)

Để tìm mối quan hệ giữa độ bất định I và xác suất chọn một phần tử $x_k (p(x_k))$ trong tập, ta xuất phát từ các tiêu đề sau:

Theo suy nghĩ thông thường, độ bất định I phải thoả mãn:

+ $I(x_k) \ge 0$
+ $p(x_k) = 1 \rightarrow I(x_k) = E[p(x_k)] = E[1] = 0$ (3.1)
+ Tính cộng được:
    Nếu $x_k$ và $x_i$ độc lập, thì:
    $$E[p(x_k \cdot x_i)] = E[p(x_k) p(x_i)] = E[p(x_k)] + E[p(x_i)]$$
    Nếu $x_k$ và $x_i$ phụ thuộc thì:
    $$E[p(x_k x_i)] = E[p(x_k) p(x_i / x_k)] = E[p(x_k)] + E[p(x_i / x_k)]$$

Đặt $p(x_k) = p$ và $p(x_i / x_k) = q$, thì khi đó với mọi $p, q$ ($0 < p \le 1, 0 < q \le 1$), ta có:
$$E[p] + E[q] = E[pq]$$ (3.2)

Từ (3.2) ta có thể tìm được dạng hàm $I(p)$. Lấy vi phân 2 vế của (3.2) theo $p$, ta có:
$$E'(p) = q E'(pq)$$

Nhân cả 2 vế của phương trình này với $p$ và ký hiệu $pq = \tau$, ta có:
$$p E'(p) = \tau E'(\tau)$$ (3.3)

Biểu thức (3.3) đúng $\forall p, \tau \ne 0$. Nhưng điều này chỉ có thể có khi cả hai vế của (3.3) bằng một hằng số k nào đó:
$$p E'(p) = \tau E'(\tau) = k = const$$

Từ đó chúng ta có phương trình vi phân $p I'(p) = const = k$, lấy tích phân phương trình này, ta tìm được:
$$E(p) = k \ln p + C$$ (3.4)

Kể đến điều kiện ban đầu (3.1), chúng ta có:
$$E(p) = k \ln p$$ (3.5)

Như vậy, ta có:
thì định lý Wiener – Khinchin sẽ đúng cả đối với những quá trình ngẫu nhiên có những thành phần tần số rời rạc, kể cả thành phần một chiều ở tần số $\omega_K = 0$.

### 2.5. TRUYỀN CÁC TÍN HIỆU NGẪU NHIÊN QUA CÁC MẠCH VÔ TUYẾN ĐIỆN TUYẾN TÍNH

Đối với các tín hiệu xác định, trong giáo trình “Lý thuyết mạch”, ta đã xét bài toán phân tích sau: Cho một mạch tuyến tính có cấu trúc đã biết (biết hàm truyền đạt $\dot{K}(\omega)$ hoặc biết phản ứng xung $g(t)$). Ta phải xét tác động đầu vào theo hưởng ứng đầu ra và ngược lại. Đối với các tín hiệu ngẫu nhiên nếu số thể hiện là đếm được và hữu hạn thì ta có thể xét hưởng ứng ra đối với từng tác động đầu vào như bài toán trên. Nhưng khi số thể hiện của tín hiệu ngẫu nhiên là vô hạn thì ta không thể áp dụng được những kết quả của bài toán phân tích đối với các tín hiệu xác định. Sau đây ta sẽ xét bài toán này.

#### 2.5.1. Bài toán tối thiểu
##### 2.5.1.1. Bài toán:
Cho một mạch tuyến tính (có tham số không đổi và biết $\dot{K}(\omega)$ của nó. Biết mật độ phổ công suất $G_v(\omega)$ của quá trình ngẫu nhiên tác động ở đầu vào. Ta phải tìm mật độ phổ công suất $G_{ra}(\omega)$ và hàm tự tương quan $R_{ra}(\tau)$ của quá trình ngẫu nhiên ở đầu ra.

[Hình: Sơ đồ khối mô tả hệ thống tuyến tính có hàm truyền đạt $\dot{K}(\omega)$, với tín hiệu vào có mật độ phổ công suất $G_v(\omega)$ và tín hiệu ra có mật độ phổ công suất $G_{ra}(\omega)$.]

Hình 2.4. Hàm truyền đạt $\dot{K}(\omega)$

##### 2.5.1.1. Giải bài toán
Ở giáo trình “Lý thuyết mạch” ta đã biết hàm phổ biên độ phức của tín hiệu ở đầu ra mạch vô tuyến điện tuyến tính bằng:
$$\dot{S}_{ra}(\omega) = \dot{K}(\omega) \dot{S}_v(\omega) \tag{2.24}$$
Trong đó $\dot{K}(\omega)$ là hàm truyền của mạch đã biết.
$\dot{S}_v(\omega)$ là phổ biên độ phức của tín hiệu vào
<u>Chú ý</u>: Đối với các quá trình ngẫu nhiên ta không biết được $\dot{S}_v(\omega)$. Không thể tính được $\dot{S}_v(\omega)$, mặt khác ta đã biết theo (2.19):
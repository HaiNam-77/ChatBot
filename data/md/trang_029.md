$$G_V(\omega) = M \lim_{T \to \infty} \frac{|\dot{S}_{VT}(\omega)|^2}{T} = M \lim_{T \to \infty} \left\{ \frac{1}{T} \left| \frac{\dot{S}_{raT}(\omega)}{\dot{K}(\omega)} \right|^2 \right\} =$$
$$= \frac{1}{|\dot{K}(\omega)|^2} M \lim_{T \to \infty} \frac{|\dot{S}_{raT}(\omega)|^2}{T} = \frac{1}{|\dot{K}(\omega)|^2} G_{ra}(\omega)$$

Hay:
$$G_{ra}(\omega) = |\dot{K}(\omega)|^2 G_V(\omega) \tag{2.25}$$

Người ta đã chứng minh được rằng hưởng ứng ra của hệ thống tuyến tính có tham số không đổi là một quá trình ngẫu nhiên không dừng ngay cả khi tác động đầu vào là một quá trình ngẫu nhiên dừng.

Tuy vậy, trong trường hợp hệ thống tuyến tính thụ động có suy giảm thì ở những thời điểm $t \gg t_0 = 0$ (thời điểm đặt tác động vào) thì quá trình ngẫu nhiên ở đầu ra sẽ được coi là dừng.

Khi đó hàm tự tương quan và mật độ phổ công suất của quá trình ngẫu nhiên ở đầu ra sẽ liên hệ với nhau theo cặp biến đổi Wiener – Khinchin. Ta có:
$$R_{ra}(\tau) = \frac{1}{2\pi} \int_{-\infty}^{\infty} G_{ra}(\omega) e^{j\omega\tau} d\omega \tag{2.26}$$

**Nhận xét:**

Từ (2.25) ta thấy mật độ phổ công suất của hưởng ứng ra được quyết định bởi bình phương môđun hàm truyền của mạch khi đã cho phổ công suất của tác động vào, nó không phụ thuộc gì vào đặc tính pha tần của mạch.

Công suất của quá trình ngẫu nhiên ở đầu ra (khi quá trình ngẫu nhiên vào là dừng):
$$R_{ra}(0) = \sigma^2 = \frac{1}{2\pi} \int_{-\infty}^{\infty} G_{ra}(\omega) d\omega = P_{ra} = \frac{1}{2\pi} \int_{-\infty}^{\infty} |\dot{K}(\omega)|^2 G_V(\omega) d\omega \tag{2.27}$$

Nếu phổ công suất của tác động vào không phụ thuộc tần số, tức là $G(\omega) = N_0$ (quá trình ngẫu nhiên có tính chất này được gọi là tạp âm trắng) thì:
$$P_{ra} = \frac{1}{2\pi} N_0 \int_{-\infty}^{\infty} |\dot{K}(\omega)|^2 d\omega \tag{2.28}$$

Vì môđun hàm truyền luôn là một hàm chẵn nên:
$$P_{ra} = \frac{2}{2\pi} N_0 \int_{0}^{\infty} |\dot{K}(\omega)|^2 d\omega \tag{2.29}$$

Mặt khác, nếu gọi $G_0$ là phổ công suất thực tế (phần phổ công suất trải từ $0 \to \infty$) thì $G_0 = 2N_0$ và (2.29) có thể viết lại như sau:
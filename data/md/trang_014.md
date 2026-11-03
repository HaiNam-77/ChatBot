#### 1.2.2.1. Nguồn tin
Nơi sản sinh ra tin
- Nếu tập tin là hữu hạn thì nguồn sinh ra nó được gọi là nguồn rời rạc.
- Nếu tập tin là vô hạn thì nguồn sinh ra nó được gọi là nguồn liên tục.
Nguồn tin có hai tính chất: Tính thống kê và tính hàm ý.
Với nguồn rời rạc, tính thống kê biểu hiện ở chỗ xác suất xuất hiện các tin là khác nhau.
Tính hàm ý biểu hiện ở chỗ xác suất xuất hiện của một tin nào đó sau một dãy tin khác nhau nào đó là khác nhau.
Ví dụ: $P(y/ta) \neq P(y/ba)$

#### 1.2.2.2. Máy phát
Là thiết bị biến đổi tập tin thành tập tín hiệu tương ứng. Phép biến đổi này phải là đơn trị hai chiều (thì bên thu mới có thể “sao lại” được đúng tin gửi đi). Trong trường hợp tổng quát, máy phát gồm hai khối chính.
- Thiết bị mã hoá: Làm ứng mỗi tin với một tổ hợp các ký hiệu đã chọn nhằm tăng mật độ, tăng khả năng chống nhiễu, tăng tốc độ truyền tin.
- Khối điều chế: Là thiết bị biến tập tin (đã hoặc không mã hoá) thành các tín hiệu để bức xạ vào không gian dưới dạng sóng điện từ cao tần. Về nguyên tắc, bất kỳ một máy phát nào cũng có khối này.

#### 1.2.2.3. Đường truyền tin
Là môi trường vật lý, trong đó tín hiệu truyền đi từ máy phát sang máy thu. Trên đường truyền có những tác động làm mất năng lượng, làm mất thông tin của tín hiệu.

#### 1.2.2.4. Máy thu
Là thiết bị lập lại (sao lại) thông tin từ tín hiệu nhận được. Máy thu thực hiện phép biến đổi ngược lại với phép biến đổi ở máy phát: Biến tập tín hiệu thu được thành tập tin tương ứng.
Máy thu gồm hai khối:
- Giải điều chế: Biến đổi tín hiệu nhận được thành tin đã mã hoá.
- Giải mã: Biến đổi các tin đã mã hoá thành các tin tương ứng ban đầu (các tin của nguồn gửi đi).

#### 1.2.2.5. Nhận tin
Có ba chức năng:
- Ghi giữ tin (ví dụ bộ nhớ của máy tính, băng ghi âm, ghi hình...)
- Biểu thị tin: Làm cho các giác quan của con người hoặc các bộ cảm biến của máy thụ cảm được để xử lý tin (ví dụ băng âm thanh, chữ số, hình ảnh...)
- Xử lý tin: Biến đổi tin để đưa nó về dạng dễ sử dụng. Chức năng này có thể thực hiện bằng con người hoặc bằng máy.
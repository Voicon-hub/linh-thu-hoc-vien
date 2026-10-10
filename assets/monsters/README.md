# Artwork quái vật

Đặt vào thư mục này 104 file PNG theo `asset_filename` trong `monsters_104.json`: `mon_001.png` … `mon_104.png`.

- PNG RGBA 1024×1024, nền trong suốt, một quái vật mỗi file.
- Không đưa chữ, ID, sao, huy hiệu độ hiếm hoặc khung thẻ vào ảnh (game tự vẽ các lớp này).
- Nhân vật chiếm khoảng 75–85% khung hình, không chạm mép ảnh.

Game tự nhận ảnh khi có ít nhất một trong các file mon_001 / mon_053 / mon_104. Con nào chưa có ảnh sẽ dùng artwork vector dự phòng.
Kiểm tra trước khi đẩy lên GitHub:  `python3 tools/check_assets.py --thumbs`
Trong game: Bộ sưu tập → 🎴 Xưởng thẻ mẫu → "Kiểm tra 104 file artwork".
(Các file .svg sẵn có trong thư mục này là 8 quái vật mẫu của Xưởng thẻ.)

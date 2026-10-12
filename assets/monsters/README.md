# Artwork quái vật
Tên file theo mã: `mon_001.png … mon_040.png` (xem `asset_filename` trong `monsters_40.json`).
- PNG RGBA 1024×1024, nền trong suốt, một quái vật mỗi file; nhân vật chiếm khoảng 75–85% khung hình.
- Không đưa chữ, ID, sao, huy hiệu độ hiếm hoặc khung thẻ vào ảnh (game tự dựng các lớp này).
Hiện có ảnh thật cho 25 quái vật: hệ Hỏa (001–005), Thủy (006–010), Lôi (016–020), Phong (021–025), Thổ (026–030).
Hệ Mộc, Ánh Sáng, Bóng Tối chưa có ảnh nên dùng artwork vector dự phòng.
Kiểm tra: `python3 tools/check_assets.py --thumbs` hoặc trong game: Hồ sơ → "Kiểm tra 40 file artwork".
